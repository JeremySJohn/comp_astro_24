input_file = 'assignment3\HD149026_assignment3_taskA_spectrumFC.dat'
output_file = 'assignment3\HD149026_assignment3_taskA_spectrum.dat'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        columns = line.split()
        # Remove the third column
        new_line = f"{columns[0]} {columns[1]} {columns[3]}\n"
        outfile.write(new_line)

print(f"Output written to {output_file}")