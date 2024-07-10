@echo off

:: Define the log file
set LOGFILE=pipeline_log.txt

:: log the start time
echo Running pipeline at %date% %time% >> %LOGFILE%

:: Run the main.py and log the output
C:/Users/Jerry/anaconda3/python.exe main.py >> %LOGFILE% 2>&1

:: log the end time
echo Pipeline Completed at %date% %time% >> %LOGFILE%

echo. >> %LOGFILE%