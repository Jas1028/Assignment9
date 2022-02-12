from fileinput import filename
import json
from fpdf import FPDF

#Create FPDF object
pdf = FPDF('P', 'cm', 'A4')

#Add a page
pdf.add_page()

#Open and Read JSON file
with open('Resume.json') as PersonalDetails:
    PersonalInfo = json.load(PersonalDetails)


#Personal Informations
for details in PersonalInfo:
    
    pdf.set_font("times", 'B', 30)
    pdf.cell(19, 1, details['Name'], align= "C", ln=1)
    pdf.set_font("times", 'I', 20)
    pdf.cell(19, 1, details['Description'], align='C', ln=1)
    pdf.cell(2, 0.5, ln=1)

    pdf.set_font("helvetica", 'B', 16)
    pdf.cell(19, 1, f"PERSONAL INFORMATIONS", align='C', border=1, ln=1)
    pdf.cell(2, 0.5, ln=1)

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(2, 0.5, f"Address: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(2, 0.5, details ['Address'], ln=1)

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(2.4, 0.5, f"Nationality: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(2, 0.5, details ['Nationality'], ln=1)

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(2.1, 0.5, f"Birthdate:  ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(2, 0.5, details ['Birthdate'], ln=1)
    pdf.cell(2, 0.5, ln=1)

 #Skills Info
pdf.set_font("helvetica", 'B', 16)
pdf.cell(19, 1, details['ContactDet'], border=1, align='C', ln=1)
pdf.cell(2, 0.5, ln=1)

for Account in details['Details']:
    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(3.6, 0.5, f"Contact Number: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(2, 0.5, Account['Number'], ln=1)

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(1.4, 0.5, f"Email: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(2, 0.5, Account['Email'], ln=1)

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(1.6, 0.5, f"Github: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(2, 0.5, Account['Github'], ln=1)   

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(2, 0.5, f"LinkedIn: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(2, 0.5, Account['Linkedin'], ln=1)
    pdf.cell(2, 0.5, ln=1)

#Education Info
pdf.set_font("helvetica", 'B', 16)
pdf.cell(19, 1, details['Education'], border=1, align='C', ln=1)
pdf.cell(2, 0.5, ln=1)

for Education in details['EducationBackG']:
    pdf.set_font("helvetica", 'B', 14)
    pdf.cell(19, 1, Education['Elem'], ln=1)

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(1.7, 0.5, f"School: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(12, 0.5, Education['ElemSchool'])

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(2.8, 0.5, f"School Year: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(2, 0.5, Education['ESchoolYear'], ln=1)

    pdf.set_font("helvetica", 'B', 14)
    pdf.cell(19, 1, Education['Sec'], ln=1)
    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(1.7, 0.5, f"School: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(12, 0.5, Education['SecSchool'])

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(2.8, 0.5, f"School Year: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(2, 0.5, Education['SSchoolYear'], ln=1)

    pdf.set_font("helvetica", 'B', 14)
    pdf.cell(19, 1, Education['Ter'], ln=1)
    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(1.7, 0.5, f"School: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(12, 0.5, Education['TerSchool'])

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(2.8, 0.5, f"School Year: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(2, 0.5, Education['TSchoolYear'], ln=1)

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(1.7, 0.5, f"Course: ",)
    pdf.set_font("helvetica", '', 12)
    pdf.cell(12, 0.5, Education['Course'], ln=1)
    pdf.cell(2, 0.5, ln=1)

#Skills Info
pdf.set_font("helvetica", 'B', 16)
pdf.cell(19, 1, details['Skill'], border=1, align='C', ln=1)
pdf.cell(2, 0.5, ln=1)

for Skill in details['Skills']:
    pdf.set_font("helvetica", '', 12)
    pdf.cell(19, 0.5, Skill['SkillOne'], ln=1)

    pdf.set_font("helvetica", '', 12)
    pdf.cell(19, 0.5, Skill['SkillTwo'], ln=1)
    pdf.cell(2, 0.5, ln=1)

#career Objective Info
pdf.set_font("helvetica", 'B', 16)
pdf.cell(19, 1, details['CareerObj'], border=1, align='C', ln=1)
pdf.cell(2, 0.5, ln=1)
pdf.set_font("helvetica", '', 12)
pdf.cell(19, 0.5, details['CareerObjective'], ln=1)
pdf.cell(19, 0.5, details['Continuation'], ln=1)
pdf.cell(19, 0.5, details['Cont'], ln=1) 
pdf.cell(2, 0.5, ln=1)


#Work Experience Info
pdf.set_font("helvetica", 'B', 16)
pdf.cell(19, 1, details['WorkExperience'], border=1, align='C', ln=1)
pdf.cell(2, 0.5, ln=1)

for Work in details['WorkExp']:
    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(1.3, 0.5, f"Work: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(11, 0.5, Work['Work'])

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(2.2, 0.5, f"Company: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(2, 0.5, Work['Company'], ln=1)

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(1.3, 0.5, f"Year: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(11, 0.5, Work['When'])

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(2.2, 0.5, f"Location: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(2, 0.5, Work['Where'], ln=1)

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(3.4, 0.5, f"Job Description: ")
    pdf.set_font("helvetica", '', 12)
    pdf.cell(11, 0.5, Work['ShortDesc'])
    


pdf.output("MIN_KIMHYUN.pdf")