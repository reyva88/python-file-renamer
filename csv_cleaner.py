import csv

def clean_csv(input_file, output_file):
    seen_rows = set()

    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = [row for row in reader if any(field.strip() for field in row)]

    cleaned_rows = []
    for row in rows:
        row_tuple = tuple(row)
        if row_tuple not in seen_rows:
            seen_rows.add(row_tuple)
            cleaned_rows.append(row)

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_rows)

    print("CSV cleaned successfully!")

if __name__ == "__main__":
    input_file = input("Enter input CSV file path: ")
    output_file = input("Enter output CSV file path: ")
    clean_csv(input_file, output_file)
