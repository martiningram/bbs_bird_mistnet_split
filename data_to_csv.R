# Expects the path to mistnet as the first argument.
args = commandArgs(trailingOnly=TRUE)

mistnet_path <- args[1]

bird_data_file <- paste(mistnet_path, 'birds.Rdata', sep='/')
fold_data_file <- paste(mistnet_path, 'fold.ids.Rdata', sep='/')

stopifnot(file.exists(bird_data_file) & file.exists(fold_data_file))

target_folder <- './csv_bird_data'

if (!file.exists(target_folder)) {
  dir.create(target_folder)
}

data_file <- load(bird_data_file)
fold_file <- load(fold_data_file)

for (cur_field in c(data_file, fold_file)) {

  actual_data <- eval(parse(text = cur_field))

  # Write this data to a csv
  write.csv(actual_data, paste0(target_folder, '/', cur_field, '.csv'))
}
