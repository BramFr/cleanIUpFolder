#!/usr/bin/env python3

import os
import sys
import logging
import time



class FolderInfo:
    def __init__(self, folderToClean = None, retentionDays = 365, logging_level="INFO", delete = bool(False)):
        self.workingdir = os.path.dirname(os.path.realpath(__file__))
        self.log_level = self.logging_config(logging_level)
        self.today = time.time()
        self.folderToClean = folderToClean
        self.retentionDays = retentionDays
        self.retentionSec = retentionDays * 86400
        self.retentionTime = self.today - self.retentionSec
        self.delete = delete

        if self.folderToClean == None:
            print(f'please provide a folder to clean.')
            sys.exit()

    def logging_config(self, logging_level):
        logfile = self.workingdir + '/cleanUpFolder.log'
        logging.basicConfig(filename=logfile, filemode='a', format='%(asctime)s %(levelname)s:%(message)s', level=logging_level)

        if not os.path.isfile(logfile):
            os.mknod(logfile)
            logging.info('Log file created!')

        logging.debug('Logging_config done!')
        logging.debug('LogFile:' + logfile)
        return logging_level

    def deleteFile(self, dirpath, filename):
        if not dirpath.endswith('/'):
            dirpath = dirpath + '/'
        fullpath = dirpath + filename
        if os.path.isfile(fullpath):
            fileTimeStamp =  os.path.getmtime(dirpath + filename)
            if fileTimeStamp < self.retentionTime:
                logging.debug('Remove File: {}'.format(fullpath))
                logging.debug('UnixTimeStamp: {}'.format(fileTimeStamp))
                print('{}'.format(fullpath))
                if self.delete:
                    os.remove(fullpath)
        

    def lookupFiles(self):
        if os.path.isdir(self.folderToClean):
            lookupInfo = []
            filename = ""
            for (dirpath, _, filenames) in os.walk(self.folderToClean):
                for filename in filenames:
                    self.deleteFile(dirpath, filename)

def main():
    folderInfo = FolderInfo("/mnt/nfs/temp", logging_level="DEBUG")
    if folderInfo.log_level:
        logging.debug(folderInfo.__dict__)
    folderInfo.lookupFiles()

if __name__ == '__main__':
    main()
    
    
