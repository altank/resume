"""
scrape_resume.py

Author: Kaan Altan
Date: 2019-11-28

Description
===========
Script to parse resume files.
    - When run as __main__:
        Reads files in ./static/ relative path, parses id and features
        information and prints applicant id and features for each file.

Requirements
============
Current version of tika(pdf module) does not work very well unless the following change is made in the source:
    - Remove closing on bytes line "encodedData.close() # closes the file reading data"
    from tika/tika.py file at line ~550 


History
=======
2019-11-28  Initial prototype of the script
            Write needed regex patterns
            Extract & parse functionality for .docx files

2019-11-30  Add pdf parsing functionality (see requirements)
            Modularize functions for import compatibility
"""

from pathlib import Path
import textract
from tika import parser
import re
import pprint
import os

"""Regex patterns to search for single occurence"""
year_regex = re.compile(r'[1,2]\d{3}')
name_regex = re.compile(r'[A-Z]{1}[A-Za-z]*(\s[A-Za-z]+)+')
linkedin_regex = re.compile(r'http(s)?:\/\/([\w]+\.)?linkedin\.com\/in\/[A-Za-z0-9_-]+\/?')

def get_path(path = r'./static/'):
    return Path(path)

def extract_text(file_path):
    """Extracts text content from .docx and .pdf files

    Parameters
    ==========
    file_path : Path object
        Path to the file to extract text from

    Returns
    =======
    text : String
        String containing extracted text
    
    text_list : List
        List form of text content split at newlines
    """
    if file_path.name.endswith('.docx'):
        text = str(textract.process(file_path))
        text_list = text.split('\\n')
        return text, text_list
    elif file_path.name.endswith('.pdf'):
        rawText = parser.from_file(str(file_path))
        text = rawText["content"]
        text_list = text.split('\\n')
        return text, text_list

"""Dictionary containing regex patterns to search for multiple occurences"""
applicant_id_patterns = {
    'Phone'             :               r"(?:\+ *\d{1,2})?[\s.-]*(?:\(* *\d{3} *\)*)[\s.-]*(?:\d{3})[\s.-]*(?:\d{2})[\s.-]*(?:\d{2})[\s.-]*",
    'Email'             :               r"[A-Za-z0-9\.\*_-]+@[A-Za-z0-9\.\*_-]*",
}

def build_applicant_id(text):
    """Builds applicant id from text content using regex searches

    Parameters
    ==========
    text : String
        String containing extracted text

    Returns
    =======
    applicant_id : Dictionary
        Dictionary containing applicant id
    """
    applicant_id = {
        'Name'          :               re.search(name_regex, text).group(0),
        'Phone'         :               None,
        'Email'         :               None,
        'Linkedin'      :               re.search(linkedin_regex, text).group(0) if re.search(linkedin_regex, text) else 'N/A'
    }
    for key in applicant_id_patterns:
        match = re.findall(applicant_id_patterns[key], text)
        if match:
            applicant_id[key] = match
    
    return applicant_id

def build_applicant_features(text_list):
    """Builds applicant features from text list

    Parameters
    ==========
    text_list : List
        List form of text content split at newlines

    Returns
    =======
    feature_dict : Dictionary
        Dictionary containing applicant features
    """
    clean_text = []
    for i in text_list:
        i = i.replace('\\t', '') #clean tabs
        i = re.sub(r'(\\[a-z0-9]{3})+', '', i) #clean encodings
        i = i.strip() #remove spaces
        clean_text.append(i)
    
    clean_text = [i for i in clean_text if i != '' and i != '\\t']

    feature_titles = {}
    for i, line in enumerate(clean_text):
        if line == line.upper() and not re.search(r'\d', line) and line != '':
            feature_titles[line] = i

    splice_1 = list(feature_titles.values())
    splice_2 = list(feature_titles.values())
    splice_2.pop(0)
    splice_2.append(splice_1[-1])
    feature_splices = [list(i) for i in zip(splice_1, splice_2)]

    splices_collected = []
    for index_pair in feature_splices:
        if index_pair == feature_splices[-1]:
            splices_collected.append(clean_text[index_pair[0]:])
        else:
            splices_collected.append(clean_text[index_pair[0]:index_pair[1]])

    features_collected = []
    for i in splices_collected:
        for j in i:
            match = re.search(year_regex, j)
            if match:
                features_collected.append(i)
                break
    
    feature_dict = {}
    for feature in features_collected:
        feature_dict[feature[0]] = "\n".join(feature[1:])  

    return feature_dict

if __name__ == '__main__':
    folder_path = get_path()
    for filename in os.listdir(folder_path):
        try:
            text, text_list = extract_text(folder_path / filename)
            applicant_id = build_applicant_id(text)
            applicant_features = build_applicant_features(text_list)
        except:
            print("Can't extract text from this file, check file extension.")
            break
        print(applicant_id)
        print('\n\n{}\n\n'.format('#' * 100))
        for feature in applicant_features:
            print(feature)
            pprint.PrettyPrinter(indent=4).pprint(applicant_features[feature])
            print('\n\n{}\n\n'.format('#' * 100))