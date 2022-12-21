
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

def stage_2(total, year, filename):
    all_medals = {}
    medals_list = ["gold", "silver", "bronze"]
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split("\t")
            if data[9] == year and data[14] in medals_list:
                if data[6] in all_medals:
                    country_medals = all_medals[data[6]]
                    if data[14] == "Gold":
                        country_medals[0] += 1
                    elif data[14] == "Silver":
                        country_medals[1] += 1
                    elif data[14] == "Bronze":
                        country_medals[2] += 1
                else:
                    all_medals[data[6]] = [0, 0, 0]
                    country_medals = all_medals[data[6]]
                    if data[14] == "Gold":
                        country_medals[0] = 1
                    elif data[14] == "Silver":
                        country_medals[1] = 1
                    elif data[14] == "Bronze":
                        country_medals[2] = 1

    for key in all_medals:
        count = all_medals[key]
        print(f"{key}: {count[0]} _ {count[1]} _ {count[2]}")
def task3 (filename, country):
    medals ={}
    best_year = []
    for i in country:
        medals[i] = dict()
    with open(filename, 'r') as file:
        data = file.readline().split('\t')
        while len(data) > 1:
            if data[6] in medals:
                if data[9] not in medals[data[6]]:
                    medals[data[6]][data[9]] = 0
                medals[data[6]][data[9]] += 1
            data = file.readline().split('\t')
    for countries in medals:
        medals_years = medals[countries]
        all_medals = medals_years.values()
        max_data = max(all_medals)
        for year in medals_years:
            if medals_years[year] == max_data:
                best_year.append(f'{country}-{year}-{max_data}\n')
                print(f'{country}-{year}-{max_data}\n')