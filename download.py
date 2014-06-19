import os
import urllib
import urllib2


URL_BASE = 'http://dl.bintray.com/androlini/generic/'
ROOT = 'sui/'


def check_folder(folder):
    dir = os.path.dirname(folder)
    if not os.path.exists(dir):
        os.makedirs(dir)


def get_filelist():
    print "Reading file list..."
    list_file = urllib2.urlopen(URL_BASE + '/filelist.txt')
    files = {}
    for line in list_file:
        line = line.strip()
        if line.endswith(':'):
            folder = line[:-1]
            files[folder] = []
        elif len(line) > 0:
            files[folder].append(line)
    print "File list read"
    return files


def download_files(file_dict):
    print "Downloading files"
    for key in file_dict.keys():
        if key == 'root':
            folder = ''
        else:
            folder = key + '/'
        for file in file_dict[key]:
            check_folder(ROOT + folder)
            print "Downloading " + file + " to " + folder + "..."
            urllib.urlretrieve(URL_BASE + folder + file, ROOT + folder + file)

    print "Download complete"


def create_directories():
    print "Creating directories"
    check_folder(ROOT + 'ext/')
    check_folder(ROOT + 'actions/')
    check_folder(ROOT + 'listeners/')
    print "Directories created"


def main():
    print "Started setup"
    download_files(get_filelist())
    create_directories()
    print "Setup complete"


if __name__ == "__main__":
    main()