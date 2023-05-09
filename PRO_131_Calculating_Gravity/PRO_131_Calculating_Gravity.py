import csv

all_data = []
full_data = []
gravity = []

def cal_gravity(mass,radius):
    return ((float(mass)/float(radius)**2) * 6.67e-11)
    

def is_list_full(list):
    for i in list:
        if not i:
            return False
    return True
    

with open('main.csv', 'r') as f:
    csv_reader = csv.reader(f)
    all_data = list(csv_reader)


for row in all_data:
    if is_list_full(row):
        full_data.append(row)

for index,row in enumerate(full_data[1:]):
    try:
        new_mass = float(row[2]) * 1.989e+30
        full_data[1 + index][2] = new_mass

        new_radius = float(row[3]) * 6.957e+8
        full_data[1 + index][3] = new_radius
    except:
        full_data.remove(row)

for row in full_data[1:]:
    gravity.append(cal_gravity(row[2], row[3]))