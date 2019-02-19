import os
DATA_LINKS_NAME = 'data_links.txt'
NOT_VALID_DATA_LINKS_NAME = 'not_data_links.txt'
CHROME_WEBDRIVER_PATH = 'driver\\chromedriver.exe'

CWD = os.path.abspath(os.pardir)
ERROR_LOG = "error_log.txt"
LOG_PATH = CWD + "\\datasets\\" + ERROR_LOG
descFileName = 'desc.txt'
evalFileName = 'eval.txt'
tagsFileName = 'tags.txt'
overFileName = 'over.txt'
DS_CSV = os.path.join(CWD, "datasets.csv")
CELLS_TSV = os.path.join(os.getcwd(), os.path.join("input", "cells.tsv"))
NB_CSV = os.path.join(os.getcwd(), os.path.join("input", "notebooks.csv"))
LINKS_TSV = os.path.join(CWD, "data_gathering\\links_ds.tsv")
UNKNOWN_ERRORS = os.path.join(CWD, "data_gathering\\unknown_errors.txt")
NOT_VALID_KERNELS = os.path.join(CWD, "data_gathering\\not_valid_kernels.txt")

