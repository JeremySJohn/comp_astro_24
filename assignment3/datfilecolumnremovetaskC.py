#Code for remove the third column from the file Simple_Transmission_retrievalFC.dat and write the output to Simple_Transmission_retrieval.dat

input_file = 'assignment3\Simple_Transmission_retrievalFC.dat'
output_file = 'assignment3\Simple_Transmission_retrieval.dat'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        columns = line.split()
        # Remove the third column
        new_line = f"{columns[0]} {columns[1]} {columns[3]}\n"
        outfile.write(new_line)

print(f"Output written to {output_file}")