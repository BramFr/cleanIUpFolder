# cleanupFolder
Cleanup folder based on retention time

This tool is just for learning python3 code. This will remove every file within a folder based on time.

## Program Options:
| Options   |      Value      |
|----------|:-------------:|
| logging_level |  DEBUG / INFO (default value INFO) |
| FolderInfo* |    path to folder   |
| retentionDays | how many day`s (default value 365) |
| delete | True / False (default value False) |
    

## Example`s
```
folderInfo = FolderInfo("/mnt/nfs/01-Movies", logging_level="DEBUG")

folderInfo = FolderInfo("/mnt/nfs/01-Movies", delete=True)

folderInfo = FolderInfo("/mnt/nfs/01-Movies", retentionDays=5 ,delete=True)

folderInfo = FolderInfo("/mnt/nfs/01-Movies", retentionDays=10 ,logging_level="DEBUG")
```

## Example debug s:
```
2021-06-09 11:24:30,719 DEBUG:Logging_config done!
2021-06-09 11:24:30,721 DEBUG:LogFile:/root/cleanupFolder/cleanUpFolder.log
2021-06-09 11:24:30,721 DEBUG:{'workingdir': '/root/cleanupFolder', 'log_level': 'DEBUG', 'today': 1623230670.7216446, 'folderToClean': '/mnt/nfs/temp', 'retentionDays': 365, 'retentionSec': 31536000, 'retentionTime': 1591694670.7216446, 'delete': False}
2021-06-09 11:24:32,616 DEBUG:Remove File: /mnt/nfs/temp/file.txt
2021-06-09 11:24:32,616 DEBUG:UnixTimeStamp: 1470862591.0
```