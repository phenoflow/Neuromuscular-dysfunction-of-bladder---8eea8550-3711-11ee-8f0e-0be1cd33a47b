# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"K164000","system":"readv2"},{"code":"K164100","system":"readv2"},{"code":"K16V100","system":"readv2"},{"code":"K16y400","system":"readv2"},{"code":"108426.0","system":"med"},{"code":"11162.0","system":"med"},{"code":"11490.0","system":"med"},{"code":"21278.0","system":"med"},{"code":"2248.0","system":"med"},{"code":"25398.0","system":"med"},{"code":"25836.0","system":"med"},{"code":"29881.0","system":"med"},{"code":"30941.0","system":"med"},{"code":"31097.0","system":"med"},{"code":"31318.0","system":"med"},{"code":"32697.0","system":"med"},{"code":"34452.0","system":"med"},{"code":"37444.0","system":"med"},{"code":"37502.0","system":"med"},{"code":"41628.0","system":"med"},{"code":"49372.0","system":"med"},{"code":"4998.0","system":"med"},{"code":"52174.0","system":"med"},{"code":"5309.0","system":"med"},{"code":"56009.0","system":"med"},{"code":"5993.0","system":"med"},{"code":"6676.0","system":"med"},{"code":"7680.0","system":"med"},{"code":"887.0","system":"med"},{"code":"90866.0","system":"med"},{"code":"98192.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('neuromuscular-dysfunction-of-bladder-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["neuromuscular-dysfunction-of-bladder---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["neuromuscular-dysfunction-of-bladder---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["neuromuscular-dysfunction-of-bladder---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
