import os.path
import sys
import tarfile
import time

def compress_folder_to_tar_gz(src_dir, tar_file_name=None):
    '''
    Open a directory and create an archive in the current directory from the src_dir.
    '''
    if tar_file_name is None:
        tar_file_name = src_dir.replace(' ', '-')

    tar_file_name += '.tar.gz'

    try:
        tarFile = tarfile.open(tar_file_name, mode = 'w:gz')
        tarFile.add(src_dir)
        tarFile.close()

        return True

    except:
        return None


def list_dirs(src_dir='./'):
    '''
    List all sub-directories of src_dir.
    '''
    dirs = []

    for o in os.listdir(src_dir):
        if os.path.isdir('%s%s' % (src_dir, o)):
            dirs.append(o)
#            print o
#        else:
#            print 'not a dir: %s' % o
    if len(dirs) > 0:
        return dirs
    else:
        print 'No sub-directories within directory %s' % src_dir
        sys.exit(0)


def archive_dir_sub_dirs(src_dir='./'):
    '''
    Archive all sub-directories for src_dir, defaults to the current directory.
    '''
    dirs = list_dirs(src_dir)
    if len(dirs) == 0:
        print 'No sub-directories within directory %s' % src_dir
        sys.exit(0)

    for cur_dir in dirs:
        if compress_folder_to_tar_gz(cur_dir):
            print 'Archived %s' % cur_dir
        else:
            print '%s not Archived' % cur_dir

def main():
    if (len(sys.argv) > 1):
        src_dir = sys.argv[1]
        if not os.path.isdir(src_dir):
            print '%s is not a valid dir, please try again.' % src_dir
            sys.exit(0)
    else:
        src_dir = './'

    archive_dir_sub_dirs(src_dir)

if __name__ == "__main__":
    main()

