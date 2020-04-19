#!/usr/bin/env python3.8

import os


def Begin():
    choice = ReadStory('01-Start.txt')
    if choice == '1':
        SunnyMeadow()
    elif choice == '2':
        DarkForest()
    else :
        Begin()


def SunnyMeadow():
    choice = ReadStory('02-SunnyMeadow.txt')
    if choice == '1':
        EatPicnic()
    elif choice == '2':
        DarkForest()
    else :
        SunnyMeadow()


def DarkForest():
    choice = ReadStory('02-DarkForest.txt')
    if choice == '1':
        SunnyMeadow()
    elif choice == '2':
        LightStove()
    else :
        DarkForest()

def EatPicnic():
    ReadStory('03-EatPicnic.txt')


def LightStove():
    ReadStory('03-LightStove.txt')

def Clear_Screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def ReadStory(filename):
    Clear_Screen()
    file_location = './chapters/' + filename
    f = open(file_location, 'r', newline=None)
    text = f.read()
    Choice = input(text)
    f.close()
    return Choice

if __name__ == '__main__':
    Begin()
