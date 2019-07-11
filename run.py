import csv

ignore_tags = ['theme', 'descriptor', 'qualifier', 'general']

with open('tags.csv') as tag_file:
    csv_reader = csv.reader(tag_file, delimiter=",")
    line_count = 1
    for row in csv_reader:
        if row[1] not in ignore_tags:    
            print(row)