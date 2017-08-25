#!/usr/bin/env python
import argparse
import logging
import os
from sets import Set

def deleteFiles(folder, test, logger):
    """
        Deletes *.NEF files either in the 'folder' or in 'folder/raw'

        Optional arguments:
            test: if set to True, it will only print the list of files that will be deleted but not actually delete them
    """
    jpgs = Set()
    nefs = Set()
    raw_folder = ''
    logger.info('Checking for missing JPG in folder: ' + folder)
    if os.path.isdir(folder) == False:
        logger.error(folder + ' is not a valid directory')
    else:
        for jpg_file in os.listdir(folder):
            if jpg_file.endswith('.JPG'):
                jpgs.add( jpg_file.rsplit('/',1)[0].split('.')[0] )
            if jpg_file.endswith('.NEF'):
                nefs.add( jpg_file.rsplit('/',1)[0].split('.')[0] )


    if os.path.isdir(folder + '/raw') == False:
        logger.info('Sub-directory /raw not found')
    else:
        raw_folder = 'raw/'
        for jpg_file in os.listdir(folder+'/raw'):
            if jpg_file.endswith('.NEF'):
                nefs.add( jpg_file.rsplit('/',1)[0].split('.')[0] )


    # now find the missing files
    missing_photos = nefs - jpgs
    for missing_raw_file in missing_photos:
        logger.debug(missing_raw_file + '.NEF: Removed')
        if test == False:
            os.remove(folder + raw_folder + missing_raw_file + '.NEF')

if __name__ == "__main__":
    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT)
    #logging.basicConfig()
    logger = logging.getLogger('filecleaner')
    logger.setLevel(logging.INFO)

    # fetch the list of arguments. we need at least 2
    parser = argparse.ArgumentParser(description="Directory cleaner: It finds deleted JPG files and deletes the corresponding .NEF file in the sub-folder named \"raw\"")
    parser.add_argument('--folder', help="Folder to check for .JPG files", required=True)
    parser.add_argument('--test', help="Just print the names of file that will be deleted.",action="store_false",
                        required=False)
    parser.add_argument('-v','--verbose', help="Bump up the logging level to see names of each file being deleted.",action="store_true",
                        required=False)

    args = parser.parse_args()
    if args.verbose==True:
        logger.setLevel(logging.DEBUG)
    deleteFiles(args.folder, args.test, logger)
    logger.info('Cleaning up of files is now complete.')
