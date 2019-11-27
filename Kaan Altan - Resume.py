"""
Kaan Altan - Resume.py

Author: Kaan Altan
Date: 2019-11-26

Description
===========
This script is a Python version of my resume featuring a command line interface
to interact with the information

History
=======
2019-11-25  Initial prototype of the script
            Information is entered in the form of dictionaries
            Command line interface allows to access specific information:
                -i      : Prints all content in the info dictionary
                -n      : Prints "Name" value in the info dictionary
                -p      : Prints "Phone" value in the info dictionary
                -e      : Prints "Email" value in the info dictionary
                -l      : Prints "Linkedin" value in the info dictionary
                -f      : Prints all content in the features dictionary
                -lsf    : Lists keys in the features dictionary (Feature titles)
                -fid    : Prints specified feature when a feature title is passed in
                -s      : Prints all content in the skills dictionary
                -lss    : Lists keys in the skills dictionary (Skill titles)
                -sid    : Prints specified skills when a skill title is passed in
"""

import argparse

"""Dictionary containing identifying information"""
kaan_info = {   "Name"      : "Kaan Altan",
                "Phone"     : "+1 (415) 707-9854",
                "Email"     : "me@kaanaltan.com",
                "Linkedin"  : "linkedin.com/in/kaanaltan/"}

"""Dictionary containing feature information"""
kaan_features = {   "OBJECTIVE":

"""Data Analyst with a mechanical engineering background; 
currently seeking a position in an innovative, fast-paced, growing organization 
to leverage my creative problem-solving skills to achieve key initiatives""",

                    "PROFESSIONAL EXPERIENCE":

"""Luminex Corporation     Chicago, IL
Systems Engineer        June 2019 – Present

•	Performed structured troubleshooting on multiple aspects of the Verigene II platform – including hardware, software, consumables, and reagents – to ultimately improve assay reliability
•	Contributed to a root-cause analysis that ultimately mitigated a prominent failure mode by 90%
•	Delivered production-ready Python scripts to augment the R&D organization’s ETL pipeline
•	Designed and published Tableau dashboards for various stakeholders in Systems R&D, Assay Development, and Manufacturing
•	Performed ad hoc data aggregation, cleaning, and analysis from diverse sources (flat files, relational databases, equipment logs, spreadsheets, etc.) 
•	Developed a Python app to streamline multiple scientist and technician workflows
•	Served as point-of-contact for equipment and software issues
•	Facilitated communication between cross-functional teams with clear, concise data visualizations
•	Led Python educational sessions to introduce coworkers to the fundamentals of coding""",
                    
                    "RESEARCH":

"""Energy Transport Research Laboratory | British Petroleum PLC        Champaign, IL
Researcher, Prof. Nenad Miljkovic       May 2018 - February 2019

•	Performed applied research on nano-engineered superhydrophobic surfaces that substantially enhance heat exchange efficiency of two-phase systems by utilizing coalescence-induced droplet jumping phenomena
•	Designed, conducted and analyzed results of abrasion experiments with the principal of contact angle hysteresis to successfully quantify the durability of fabricated surfaces
•	Presented research results at the 2018 Materials Research Society Fall Meeting & Exhibit held between Nov 25-30, 2018 in Boston, Massachusetts""",
                    
                    "INTERNSHIP EXPERIENCE":

"""Ford Motor Company      Istanbul, Turkey
Vehicle Safety Intern       July 2017 - August 2017

•	Utilized Altair HyperWorks CAE Software Suite to run CAE models in conformity with the Euro NCAP standards on RADIOSS finite element solver for the safety analysis of the Ford Truck, Transit, Transit Custom PHEV (Plug-In Hybrid Electrical Vehicle) and Courier projects
•	Prepared 15 includes (CAE models that are subsets of an assembly) for assembly (editing meshing, defining material properties, environmental boundaries and assembly parameters) for  the 2018 Ford Truck project
•	Assisted occupant safety engineers in the Ford Courier project and side impact engineers in the Ford Transit project by preparing individual parts to go into the includes
•	Contributed in the Ford Transit Custom PHEV project by meshing and assembling numerous parts for individual simulations""",

                    "EDUCATION":
                    
"""University of Illinois at Urbana-Champaign      December 2018
Bachelor of Science in Mechanical Engineering
Technical GPA (Engineering and fundamental courses): 3.0/4.0""",

                    "AWARDS & ACCOMPLISHMENTS":
                    
"""Layered Fuse, Senior Design Project     August 2018 - December 2018
Littelfuse, Inc., Team Lead

•	Led a team of 4 mechanical engineering seniors to successfully complete an outsourced engineering project assigned by Littelfuse Inc. to design and manufacture attachment tabs for the assembly of high voltage multi-layered fuses
•	Structured team operations and served as a liaison between the University and Littelfuse
•	Contributed in the design and CAD phases of the project and took ownership of failure analysis by dynamically modeling failure modes utilizing Abaqus

Mechanical Design Project Competition 1st Place     May 2017

•	As a team of 4 mechanical engineering students, designed and fabricated a DC powered robot that utilizes Chebyshev’s Lambda Mechanism to climb a cable for a competition held by the department of Mechanical Science and Engineering, UIUC
•	Contributed in the design and CAD phases of the project, simulated mechanism motion in MATLAB
•	Received first place award for building the fastest mechanism in the competition with 40 participant teams""",

                    "PROFESSIONAL ORGANIZATIONS & ACTIVITIES":
                    
"""American Society of Mechanical Engineers, Member        April 2017 - Present 
Society of Automotive Engineers International, Member       May 2017 - Present 
AKL – Alpha Kappa Lambda Fraternity     September 2013 - May 2015""",
                }

"""Dictionary containing skills information"""
kaan_skills = {     "Languages"                            :       ["Python",
                                                                    "SQL",
                                                                    "MATLAB",
                                                                    "R",
                                                                    "HTML/CSS"],

                    "Tools, Frameworks & Libraries"        :       ["Git & Github",
                                                                    "Pandas",
                                                                    "Flask",
                                                                    "Regular Expressions",
                                                                    "Requests",
                                                                    "Beautiful Soup",
                                                                    "Tkinter",
                                                                    "Matplotlib",
                                                                    "Seaborn",],

                    "Software"                             :       ["Windows",
                                                                    "Linux",
                                                                    "VS Code",
                                                                    "Tableau",],

                    "Engineering"                          :       ["CAE",
                                                                    "CAD",
                                                                    "FEA",
                                                                    "FMEA",
                                                                    "G-Code",
                                                                    "GD&T",
                                                                    "Photolithography",],

                    "Engineering Software"                 :       ["Abaqus",
                                                                    "PTC Creo",
                                                                    "Altair HyperWorks",
                                                                    "Simulink",
                                                                    "FAMAS",],
                }
def parse_arguments():
    """Sets up and configures argparse object

    Parameters
    ==========
    None

    Returns
    =======
    arguments
        Dictionary containing parsed arguments
    """

    parser = argparse.ArgumentParser()

    parser._actions[0].help = """============== Kaan Altan - Resume.py ==============
                                 ====================================================
                                 This script is a version of my resume written in Python. It 
                                 provides a command line interface for interaction. You can 
                                 use the following flags to display various items of my resume 
                                 or simply run it  without flags to display full resume.                              
                                 ===================================================="""

    parser.add_argument("-i", "--info", 
                        help = "Displays applicant information",
                        action = "store_true",)

    parser.add_argument("-n", "--name", 
                        help = "Display applicant name",
                        action = "store_true",)

    parser.add_argument("-p", "--phone", 
                        help = "Display applicant phone number",
                        action = "store_true",)

    parser.add_argument("-e", "--email", 
                        help = "Display applicant email address",
                        action = "store_true",)

    parser.add_argument("-l", "--linkedin", 
                        help = "Display applicant linkedin address",
                        action = "store_true",)

    parser.add_argument("-f", "--features", 
                        help = "Display all applicant features",
                        action = "store_true",)

    parser.add_argument("-fid", "--featureid", 
                        help="Pass in title of the feature you wish to view (copy & paste from feature titles)", 
                        nargs='+')

    parser.add_argument("-lsf", "--listFeatureTitles", 
                        help = "Display applicant feature titles",
                        action = "store_true",)

    parser.add_argument("-s", "--skills", 
                        help = "Display all applicant skills",
                        action = "store_true",)

    parser.add_argument("-sid", "--skillsid", 
                        help = "Pass in title of the skills you wish to view (copy & paste from skills titles)", 
                        nargs='+')

    parser.add_argument("-lss", "--listSkillTitles", 
                        help = "Display applicant skills titles",
                        action = "store_true",)

    args = parser.parse_args()

    info = args.info
    name = args.name
    phone = args.phone
    email = args.email
    linkedin = args.linkedin
    features = args.features
    feature_titles = args.listFeatureTitles
    skills = args.skills
    skill_titles = args.listSkillTitles

    if args.featureid:
        feature_id = ' '.join(args.featureid)
    else:
        feature_id = None
    
    if args.skillsid:
        skills_id = ' '.join(args.skillsid)
    else:
        skills_id = None

    arguments = {   "Info":info, 
                    "Name":name,
                    "Phone":phone,
                    "Email":email, 
                    "Linkedin":linkedin, 
                    "Features":features,
                    "Feature_Titles":feature_titles, 
                    "Skills":skills, 
                    "Skill_Titles":skill_titles,
                    "Feature_ID":feature_id,
                    "Skills_ID":skills_id,
                }
    
    return arguments

def print_resume(arguments):
    """Function that handles printing logic according to the flags passed into the command line

    Parameters
    ==========
    arguments : dictionary
        Dictionary containing parsed arguments

    Returns
    =======
    None
    """
    if any(arguments.values()):
        if arguments["Feature_Titles"]:
            for key in kaan_features.keys():
                print(key)

        if arguments["Skill_Titles"]:
            for key in kaan_skills.keys():
                print(key)

        if arguments["Info"]:
            for key in kaan_info.keys():
                print(key + ' : ' + kaan_info[key])
        else:
            for key in list(arguments.keys())[1:5]:
                if arguments[key]:
                    print(key + ' : ' + kaan_info[key])

        if arguments["Feature_ID"]:
            if arguments["Feature_ID"] in kaan_features.keys():
                print(arguments["Feature_ID"] + ':\n')
                print(kaan_features[arguments["Feature_ID"]])
                print('\n')
            else:
                print('Invalid title entered')

        elif arguments["Features"]:
            for key in kaan_features.keys():
                print(key + '\n')
                print(kaan_features[key])
                print('\n')

        if arguments["Skills_ID"]:
            if arguments["Skills_ID"] in kaan_skills.keys():
                print(arguments["Skills_ID"] + ':\n')
                print(kaan_skills[arguments["Skills_ID"]])
                print('\n')
            else:
                print('Invalid title entered')
                    
        elif arguments["Skills"]:
            for key in kaan_skills.keys():
                print(key + '\n')
                print(kaan_skills[key])
                print('\n')
    
    else:
        for key in kaan_info.keys():
            print(key + ' : ' + kaan_info[key])
        print('\n')

        for key in kaan_features.keys():
            print(key + '\n')
            print(kaan_features[key])
            print('\n')

        for key in kaan_skills.keys():
            print(key + '\n')
            print(kaan_skills[key])
            print('\n')

def main():
    arguments = parse_arguments()
    print_resume(arguments)

if __name__ == '__main__':
    main()