import json

PersonalInformations = [
    {
        'Name': "Kim Hyun H. Min",
        'Description': "Python Programmer",
        'Address': "San Jose Del Monte, Bulacan, Philippines",
        'Nationality': "Half-Filipino, Half-Korean",
        'Birthdate': "February 29, 1996",
        'ContactDet': "CONTACT",
        'Details':[
            {
                'Number': "+(63) 923 789 9201",
                'Email': "Kim_Min@email.com",
                'Github': "github.com/Kim_Min",
                'Linkedin': "linkedin.com/in/Kim_Min"
            }
        ],
        'Education': "EDUCATIONAL BACKGROUND",
        'EducationBackG':[
            {
                'Elem': "ELEMENTARY",
                'ElemSchool': "Aukamm Elementary School",
                'ESchoolYear': "2000-2006",
                'Sec': "SECONDARY",
                'SecSchool': "Joongdong High School",
                'SSchoolYear': "2006-2011",
                'Ter': "TERTIARY",
                'TerSchool': "Polytechnic University of the Philippines",
                'TSchoolYear': "2011-2014",
                'Course': "Bachelor of Science in Computer Engineering"
            }
        ],
        'Skill': "SKILLS",
        'Skills':[
            {
                'SkillOne': "Photography, Modelling, Editing",
                'SkillTwo': "Programming Skills: Python, Hadoop, SQL, Linux, Kafka, C++, C#, Java"
            }
        ],
        'CareerObj': "CAREER OBJECTIVE",
        'CareerObjective': " As a Python programmer, I would love to say that I have a lot of knowledge that I can use in creating", 
        'Continuation': "new datas in Python and I am willing to continue developing my skills and adapt new learnings that I", 
        'Cont': "may use in future purposes. I am ready to give my best in this field",
        'WorkExperience': "WORK EXPERIENCE",
        'WorkExp':[
            {
                'Work': "Python Developer",
                'Company': "BoTree Technologies",
                'When': "February 2016-December 2018",
                'Where': "Ahmedabad, India",
                'ShortDesc': "Developed using best practices for Python"
            }
        ]
    }
]

info = json.dumps(PersonalInformations, indent = 4)
with open('Resume.json', 'w') as f:
    f.write(info)
    f.close
