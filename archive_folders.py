import os.path
import tarfile
import time

def compress_folder_to_tar_gz(src_dir, tar_file_name=None):
    if tar_file_name is None:
        tar_file_name = src_dir.replace(' ', '-')

    tar_file_name += '.tar.gz'

    #creating archive of source directory
    try:
        tarFile = tarfile.open(tar_file_name, mode = 'w:gz')
        tarFile.add(src_dir)
        tarFile.close()

        return True

    except:
        return None
        

def list_dirs(src_dir=None):
    if src_dir is None:
        src_dir = './'

    dirs = []

    for o in os.listdir(src_dir):
        if os.path.isdir('%s%s' % (src_dir, o)):
            dirs.append(o)
            print o
        else:
            print 'not a dir: %s' % o
            
    return dirs


