import Birthday_RyanK

print('\nNow let\'s talk about your major')

majorAbbr=input('pick any of the following: CS, GIS, IS, HIM. or NA: ')

if majorAbbr == 'CS':
    major='Computer Science'
if majorAbbr == 'IS':
    major='Information Systems'
if majorAbbr == 'HIM':
    major='Health Informatics and Management'
if majorAbbr == 'GIS':
    major='Geographic Information Science'
if majorAbbr =='NA':
    major= 'Undergraduate College'

print('You\'re majoring in', major)