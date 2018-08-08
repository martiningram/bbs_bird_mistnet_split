import os
import zipfile
import subprocess
from shutil import copytree
from distutils.dir_util import copy_tree
from glob import glob


def unzip_into_same_folder(zip_file_path):

    folder = os.path.split(zip_file_path)[0]

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(folder)

mistnet_path = './mistnet/'
download_path = '/tmp/'

data_target_path = os.path.join(mistnet_path, 'proprietary.data', 'BBS')

download_folder = os.path.join(download_path, 'ftpext.usgs.gov', 'pub', 'er',
                               'md', 'laurel', 'BBS', 'DataFiles')

if not os.path.isdir(download_folder):

    url = 'ftp://ftpext.usgs.gov/pub/er/md/laurel/BBS/DataFiles/'

    # Fetch the data
    process = subprocess.Popen(['wget', '-r', url], cwd=download_path)
    process.communicate()
    assert(process.return_code == 0)

assert(os.path.isdir(download_folder))

copy_tree(download_folder, data_target_path, update=True)

# Copy the 50 stop data up, too
folder_name = '50-StopData'

# Unzip the required files
data_file_zips = glob(os.path.join(data_target_path, '*.zip'))
survey_zips = glob(os.path.join(data_target_path, folder_name, '*/*.zip'))

for cur_zip in data_file_zips + survey_zips:

    unzip_into_same_folder(cur_zip)

mistnet_script_path = os.path.join('extras', 'BBS-analysis')

scripts_to_run = [os.path.join(mistnet_script_path, 'data_extraction',
                               'data-extraction.R'),
                  os.path.join(mistnet_script_path, 'BBS_evaluation',
                               'define-train-folds.R')]

# Now, run the R scripts required
for cur_script in scripts_to_run:
    print('Running {}'.format(cur_script))
    process = subprocess.Popen(['Rscript', cur_script], cwd=mistnet_path)
    process.communicate()
    assert(process.returncode == 0)

# Finally, run the script to convert this data to csvs
assert(os.path.isfile('data_to_csv.R'))
process = subprocess.Popen(['Rscript', 'data_to_csv.R', mistnet_path])
process.communicate()
assert(process.returncode == 0)
