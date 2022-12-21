
def task1 (medals, output, filename, country, year, noc, sport):
    gold = 0
    silver = 0
    bronze = 0
    total = 0
    list_medals = ("Gold", "Silver", "Bronze")
    counter = 0
    output_file = None
    idx = 0
    print(gold, silver, bronze)
    if output is not None:
        output_file = open(output, 'wt')
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().strip('\t')
            if data[6] == country or data[7] == noc and data[9] == year and data[12] == sport and data[14] in list_medals:
                medalist = [data[1], data[12], data[14]]
                counter += 1
                total += 1
                if data[14] == list_medals[0]:
                    gold += 1
                if data[14] == list_medals[1]:
                    silver += 1
                if data[14] == list_medals[2]:
                    bronze += 1
                if counter <= 10:
                    first_medalist = ', '.join(medalist)
                    print(f'{first_medalist}')
                    print(gold, silver, bronze)
                    print(total)
    if output_file is not None:
        idx += 1
        output_file.write(str(idx) + ','.join(data) + '\n')
    if output_file is not None:
        output_file.close()

