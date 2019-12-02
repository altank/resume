# Kaan Altan - Resume

***v1.0***
My resume in Python featuring a command line interface for interaction

***v2.0***
Scraping mode introduced

## Usage

Command line interface allows access to specific information
> v1.0
- `-i`      Prints all content in the info dictionary
- `-n`      Prints "Name" value in the info dictionary
- `-p`      Prints "Phone" value in the info dictionary
- `-e`      Prints "Email" value in the info dictionary
- `-l`      Prints "Linkedin" value in the info dictionary
- `-f`      Prints all content in the features dictionary
- `-lsf`    Lists keys in the features dictionary (Feature titles)
- `-fid`    Prints specified feature when a feature title is passed in
- `-s`      Prints all content in the skills dictionary
- `-lss`    Lists keys in the skills dictionary (Skill titles)
- `-sid`    Prints specified skills when a skill title is passed in
> v2.0
- `-sc`     Enables scraping mode, scrapes & parses resume file passed in and uses that to display requested information

`Note: Skills are not supported in scraping mode`

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)