import os
import argparse
from pathlib import pathlib
import sys
import logging as logs



argumentDealer = argparse.ArgumentParser(allow_abbrev=False, prog='File Organizer')

# The arguments to use with the program.
argumentDealer.add_argument(
    '--dir',
    default=userHomeFolder,
    help='Specify a directory to work in.',
    required=True
)
argumentDealer.add_argument(
    '--docs',
    help='Only organize your document files'
    )
argumentDealer.add_argument(
    '--audio',
    help='Only organize your audio files.'
)
argumentDealer.add_argument(
    '--video',
    help='Only organize your video files'
)
argumentDealer.add_argument(
    '--pictures',
    help='Only organize your picture files'
)
argumentDealer.add_argument(
    '-d', '--debug',
    help="Print lots of debugging statements",
    action="store_const", dest="loglevel", const=logging.DEBUG,
    default=logging.WARNING,
)
argumentDealer.add_argument(
    '-v', '--verbose',
    help="Be verbose",
    action="store_const", dest="loglevel", const=logging.INFO,
)

argumentHandler = argumentDealer.parse_args()

def pickDir(value):
    for category, ekstensi in SUBDIR.items():
        for suffix in ekstensi:
            if suffix == value:
                return category

def organizeAll():
    if args.verbose:
        logs.basicConfig(level=logging.INFO)
    
    for item in os.scandir(path=argumentHandler.dir()):
                
        #just looking for file, skip the directory
        if item.is_dir():
                logs.WARNING(item.name() + 'is a directory, I need to skip this.')
                continue
                
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDir(fileType)
        
        #just skip, if the file extension not defined.
        if directory == None:
            logs.WARNING(item.name() + 'does not have an extension, I need to skip this.')
            continue
        
        directoryPath = Path(directory)
        #make new directory if the category's directory not found.
        if directoryPath.is_dir() != True:
                logs.INFO(Path(directory) + 'does not exist in either the specified directory or your user profile, I\'m creating it right now.')
                directoryPath.mkdir()
        logs.INFO('I\'m moving' + filePath + 'into' + directoryPath)
        filePath.rename(directoryPath.joinpath(filePath))


def organizeDocs():
    if args.verbose:
        logs.basicConfig(level=logging.INFO)
    
    for item in os.scandir(path=argumentHandler.dir()):
                
        #just looking for file, skip the directory
        if item.is_dir():
                logs.WARNING(item.name() + 'is a directory, I need to skip this.')
                continue
                
        filePath = Path(item)
        fileType = [".doc",".docx",".txt",".odt",".gdoc"]
        directory = 'Documents'
        
        #just skip, if the file extension not defined.
        if directory == None:
            logs.WARNING(item.name() + 'does not have an extension, I need to skip this.')
            continue
        
        directoryPath = Path(directory)
        #make new directory if the category's directory not found.
        if directoryPath.is_dir() != True:
                logs.INFO(Path(directory) + 'does not exist in either the specified directory or your user profile, I\'m creating it right now.')
                directoryPath.mkdir()
        logs.INFO('I\'m moving' + filePath + 'into' + directoryPath)
        filePath.rename(directoryPath.joinpath(filePath))

def organizeAudio():
    if args.verbose:
        logs.basicConfig(level=logging.INFO)
    
    for item in os.scandir(path=argumentHandler.dir()):
                
        #just looking for file, skip the directory
        if item.is_dir():
                logs.WARNING(item.name() + 'is a directory, I need to skip this.')
                continue
                
        filePath = Path(item)
        fileType = [".mp3",".wav",".flac"]
        directory = 'Music'
        
        #just skip, if the file extension not defined.
        if directory == None:
            logs.WARNING(item.name() + 'does not have an extension, I need to skip this.')
            continue
        
        directoryPath = Path(directory)
        #make new directory if the category's directory not found.
        if directoryPath.is_dir() != True:
                logs.INFO(Path(directory) + 'does not exist in either the specified directory or your user profile, I\'m creating it right now.')
                directoryPath.mkdir()
        logs.INFO('I\'m moving' + filePath + 'into' + directoryPath)
        filePath.rename(directoryPath.joinpath(filePath))

def organizeVideo():
    if args.verbose:
        logs.basicConfig(level=logging.INFO)
    
    for item in os.scandir(path=argumentHandler.dir()):
                
        #just looking for file, skip the directory
        if item.is_dir():
                logs.WARNING(item.name() + 'is a directory, I need to skip this.')
                continue
                
        filePath = Path(item)
        fileType = [".mp4",".wmv",".webm",".mkv",".flv",".avi",".mov"]
        directory = 'Videos'
        
        #just skip, if the file extension not defined.
        if directory == None:
            logs.WARNING(item.name() + 'does not have an extension, I need to skip this.')
            continue
        
        directoryPath = Path(directory)
        #make new directory if the category's directory not found.
        if directoryPath.is_dir() != True:
                logs.INFO(Path(directory) + 'does not exist in either the specified directory or your user profile, I\'m creating it right now.')
                directoryPath.mkdir()
        logs.INFO('I\'m moving' + filePath + 'into' + directoryPath)
        filePath.rename(directoryPath.joinpath(filePath))

def organizePictures():
    if args.verbose:
        logs.basicConfig(level=logging.INFO)
    
    for item in os.scandir(path=argumentHandler.dir()):
                
        #just looking for file, skip the directory
        if item.is_dir():
                logs.WARNING(item.name() + 'is a directory, I need to skip this.')
                continue
                
        filePath = Path(item)
        fileType = [".png",".jpg",".jiff",".bmp",".raw",".jpeg",".tiff",".gif"]
        directory = 'Documents'
        
        #just skip, if the file extension not defined.
        if directory == None:
            logs.WARNING(item.name() + 'does not have an extension, I need to skip this.')
            continue
        
        directoryPath = Path(directory)
        #make new directory if the category's directory not found.
        if directoryPath.is_dir() != True:
                logs.INFO(Path(directory) + 'does not exist in either the specified directory or your user profile, I\'m creating it right now.')
                directoryPath.mkdir()
        logs.INFO('I\'m moving' + filePath + 'into' + directoryPath)
        filePath.rename(directoryPath.joinpath(filePath))

def mainProcess():
    if argumentHandler.video:
        organizeVideo()
    elif argumentHandler.picture:
        organizePictures()
    elif argumentHandler.docs:
         organizeDocs()
    elif argumentHandler.audio:
         organizeAudio()
    elif argumentHandler.all:
         organizeAll()