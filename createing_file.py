companyA_q1_data = {
    'Company': 'Company A',
    'Quarter': 'Q1',
    'Revenue': '$1,500,000',
    'Expenses': '$900,000',
    'Net Income': '$600,000',
    'EPS': '$1.20',
    'Assets': '$3,000,000',
    'Liabilities': '$1,200,000',
    'Equity': '$1,800,000'


}

with open('CompanyA_Quarter1.txt', 'w') as file:
    for key, value in companyA_q1_data.items():
        file.write(f'{key}:{value}\n')




companyA_data_q2 = {
    'Company': 'Company A',
    'Quarter': 'Q2',
    'Revenue': '$1,800,000',
    'Expenses': '$1,000,000',
    'Net Income': '$800,000',
    'EPS': '$1.60',
    'Assets': '$3,500,000',
    'Liabilities': '$1,400,000',
    'Equity': '$2,100,000'

}

with open("CompanyA_Quarter2.txt", 'w') as file2:
    for key, value in companyA_data_q2.items():
        file2.write(f"{key}:{value}\n")



companyB_data_q1 = {
    'Company': 'Company B',
    'Quarter': 'Q1',
    'Revenue': '$2,000,000',
    'Expenses': '$1,200,000',
    'Net Income': '$800,000',
    'EPS': '$2.00',
    'Assets': '$4,500,000',
    'Liabilities': '$2,000,000',
    'Equity': '$2,500,000'

}

with open("CompanyB_Quarter1.txt", 'w') as file3:
    for key, value in companyB_data_q1.items():
        file3.write(f"{key}:{value}\n")


companyB_data_q2 = {
    'Company': 'Company B',
    'Quarter': 'Q2',
    'Revenue': '$2,300,000',
    'Expenses': '$1,300,000',
    'Net Income': '$1,000,000',
    'EPS': '$2.50',
    'Assets': '$5,000,000',
    'Liabilities': '$2,200,000',
    'Equity': '$2,800,000'

}

with open("CompanyB_Quarter2.txt", 'w') as file4:
    for key, value in companyB_data_q2.items():
        file4.write(f"{key}:{value}\n")