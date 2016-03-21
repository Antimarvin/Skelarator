__author__ = "Richard L. Sweat Jr."

import os

PROJECT_NAME = os.path.basename(os.getcwd())
REQ_FOLDERS = ['bin', 'docs', 'tools', 'etc', PROJECT_NAME, os.path.join(PROJECT_NAME, 'tests')]
BASE_FILES = ['README.TXT', 'requirements.txt', 'setup.py', 'test-requirements.txt']
DOCS_FILES = ['conf.py', 'index.txt', 'quickstart.txt']
PROJECT_FILES = ['__init__.py', 'cli.py', 'storage.py']
TESTS_FILES = ['__init__.py', 'test_cli.py', 'test_storage.py']


def make_files(p, files):
    """
    Creates the files in the path passed to it.
    :param p: path to put files
    :param files: filenames and extensions to create
    :return: nothing
    """
    old_dir = os.getcwd()
    os.chdir(p)
    for file in files:
        with open(file, 'w') as f:
            pass
    os.chdir(old_dir)


def main():
    """
    Exeecutes on run
    :return: nothing
    """

    for folder in REQ_FOLDERS:
        os.mkdir(os.path.join(os.getcwd(), folder))

    make_files('.\\docs', DOCS_FILES)
    make_files('.\\{}'.format(PROJECT_NAME), PROJECT_FILES)
    make_files('.\\{}\\tests'.format(PROJECT_NAME), TESTS_FILES)


if __name__ == '__main__':
    """This executes if the file is run by itself."""
    main()