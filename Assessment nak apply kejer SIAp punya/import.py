import csv

# Read the CSV file and store data in a dictionary
table_data = {}
with open('Table_Input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header
    for row in reader:
        table_data[row[0]] = int(row[1])  # Store symbol as key and value as integer

# Process the data for Table 2
alpha_value = table_data['A5'] + table_data['A20']
beta_value = table_data['A15'] / table_data['A7']
charlie_value = table_data['A13'] * table_data['A12']

# Print the values for verification
print(f"Alpha: {alpha_value}")
print(f"Beta: {beta_value}")
print(f"Charlie: {charlie_value}")
