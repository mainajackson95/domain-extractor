import csv

def extract_domains(input_file, output_file):
    domains = set()  # Use a set to avoid duplicates
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile, delimiter='|')
            for row in reader:
                if len(row) >= 2:  # Ensure there are enough columns
                    domain = row[1].strip()  # Extract the 2nd column (domain)
                    if domain:  # Skip empty domains
                        domains.add(domain)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Write domains to output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for domain in sorted(domains):  # Sort alphabetically (optional)
            outfile.write(domain + '\n')

    print(f"Domains extracted successfully to '{output_file}'.")

# Example usage:
input_filename = 'domains.csv'  # Replace with your input file name
output_filename = 'domains.txt'  # Output will be saved here
extract_domains(input_filename, output_filename)