import csv

confidence_table_male = []
confidence_table_female = []
motivation_table_male = []
motivation_table_female = []


with open("data.csv", 'r') as file:

    ## Analysis for confidence
    csvreader = csv.reader(file)

    for row in csvreader:
        confidence_table_male.append(row[1:14])
        break
    

    
    for row in csvreader:
        if row[1] == "Male":
            confidence_table_male.append(row[1:14])
        else:
            confidence_table_female.append(row[1:14])

    ## Analysis for Motivation
    

with open("data.csv", 'r') as file:

    ## Analysis for motivation
    csvreader = csv.reader(file)

    for row in csvreader:
        new = [row[1]]+row[14:]
        motivation_table_male.append(new)
        break
    

    
    for row in csvreader:
        if row[1] == "Male":
            new = [row[1]]+row[14:]
            motivation_table_male.append(new)
        else:
            new = [row[1]]+row[14:]
            motivation_table_female.append(new)


confidence_table = confidence_table_male + confidence_table_female 
motivation_table = motivation_table_male + motivation_table_female

# Write data to confidence file
filename = './cleaned data/student_confidence_new.csv'
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerows(confidence_table)

# Write data to motivation file

filename = './cleaned data/student_motivation_new.csv'
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerows(motivation_table)