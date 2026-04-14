##Program Name: KiCAD csv to Converter Tool
##Author: Miller DeMark
##Date: 12/19/2024
##
## Description: This program will take your csv from KiCAD and convert it to
## a usuable csv for the CHARMHIGH Converter Tool. To use, make sure the csv
## is in the same folder as the program, run the program and enter your csv name.
## The program will swap columns as needed and save the csv back to the original
## file.

import csv

def rearrange_columns(input, output, new_column_order):
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)  

    with open(output_file, mode='w', newline='') as outfile:
 
        writer = csv.DictWriter(outfile, fieldnames=new_column_order)
        writer.writeheader()

        for row in rows:
            reordered_row = {column: row[column] for column in new_column_order}
            writer.writerow(reordered_row)

# We want this to run without using IDLE
if __name__ == "__main__":
    input_file = input('Enter your csv name as "my_file.csv":')
    output_file = input('What would you like to name your file (include.csv): ')
    new_column_order = ['Ref', 'Package', 'PosX', 'PosY', 'Side', 'Rot', 'Val']  

    rearrange_columns(input_file, output_file, new_column_order)
    print(f"CSV columns rearranged and saved to {output_file}")



