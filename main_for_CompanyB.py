#removing symbols from values, like '$', ',' and '.'
def remove_symbols(val):
    try:
        return float(val.replace("$", "").replace(",","").replace(".",""))
    except ValueError:
        return val
    
#open files for reading
with open("CompanyB_Quarter1.txt", 'r') as file:
    quarter_1 = file.readlines()

with open("CompanyB_Quarter2.txt", 'r') as file:
    quarter_2 = file.readlines()

#creating dictionaries for non_symbolic txt
calc_1 = {}
calc_2 = {}

for line in quarter_1:
    key, value = line.strip().split(":")
    if key == "Company" or key == "Quarter":
        calc_1[key] = value
    calc_1[key] = remove_symbols(value)

for line in quarter_2:
    key, value = line.strip().split(":")
    calc_2[key] = remove_symbols(value)

#calculating differences between values
differences = {}

for key in calc_1.keys():
    if key not in ['Company', 'Quarter']:
        differences[key] = abs(float(calc_2[key])- float(calc_1[key]))

print(differences, end = " \n")

   