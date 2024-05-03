class ArgsConfig:
    GPU = 1
    EPOCHS = 2
    BATCHSIZE = 32
    HIDDENSIZE = 64
    N_THREADS = 2
    EPOCHS_MDN = 2
    NMIX = 8
    LOGSTEP = 100
    DATASET_KEY = "lfw"

def get_dirpaths():
    if ArgsConfig.DATASET_KEY == "lfw":
        out_dir = "data/output/lfw"
        listdir = "data/imglist/lfw" 
        featslistdir = "data/featslist/lfw"
    else:
        raise NameError("[ERROR] Incorrect key: %s" % (ArgsConfig.DATASET_KEY))
    return out_dir , listdir , featslistdir