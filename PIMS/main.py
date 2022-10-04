#!/usr/bin/env python3
"""Python Inventory Managment System PIMS"""

import string


"""

"""

record_dictionary = {
        'Resistor' : {'Value' : None, 'Quantity' : None, 'Tolerance' : None, 'Power Rating' : None, 'Package Type' : None, 'Footprint' : None, 'Supplier P/N' : None, 'Location' : None,},
        'Transistor' : {'MFR P/N' : None, 'Polarity' : None, 'Quantity' : None, 'Description' : None, 'Package Type' : None, 'Footprint' : None,'Supplier P/N' : None, 'Location' : None,},
        'Diode' : {'MFR P/N' : None, 'Type' : None, 'Quantity' : None, 'Description' : None, 'Package Type' : None, 'Footprint' : None,'Supplier P/N' : None, 'Location' : None,},
        'Integrated Circuit' : {'MFR P/N' : None, 'Function' : None, 'Quantity' : None, 'Description' : None, 'Package Type' : None, 'Footprint' : None,'Supplier P/N' : None, 'Location' : None,},
        'Misc Electronic Componenet' : {'Value' : None, 'Quantity' : None, 'Description' : None, 'Supplier P/N' : None, 'Location' : None,},
        'Misc Object' : {'Description' : None, 'Quantity' : None, 'Location' : None,},
        }

footprint_list = ['THT','SMD']

RECORD_FILE_PATH = 'record_files/'

PROMPT = '> '

def create_record(record_dictionary):
    """Add new record to file"""
    path = RECORD_FILE_PATH + record_dictionary['Type'] + '_records.csv'
    record_line = ''
    for value in record_dictionary.values():
        record_line += value + ','
        
    #with open(path, 'a+') as f:
    print(record_line)
        
def get_user_filled_menu():
    print(f'What would you like to do?\n'
          f'A - Add a record\n'
          f'E - Edit a record\n'
          f'F - Find a record\n'
          f'R - Remove a record\n'
          f'D - Debug\n')
    return get_user_input(['A','E','R','F','D'])
    
    
def get_user_input(allowed):
    value = input(PROMPT).upper()
    while value not in allowed:
        print(f'\n***Please enter a vaild option***\n')
        value = get_user_input(allowed)
    return value
    

def get_user_filled_record():
    filled_record = {}
    for i, key in enumerate(record_dictionary):
        print(f'{i} - {key}')
    selections = [str(x) for x in range(len(record_dictionary))]
    value = get_user_input(selections)
    record_type = list(record_dictionary.keys())[int(value)]
    print(f'Please enter the following fields for a {record_type} record.')
    for key in record_dictionary[record_type]:
        filled_record[key] = input(f'{key}? {PROMPT}')
    filled_record['Record Type'] = record_type
    return filled_record
                  

def save_record_to_file():
    print(f'What kind of record would you like to add?')
    record = get_user_filled_record()
    path = RECORD_FILE_PATH + record['Record Type'] + '.csv'
    record_entry = ''
    record_header = ''
    for key, value in record.items():
        record_entry += f'{value},'
        record_header += f'{key},'
    record_entry += '\n'
    record_header+='\n'
    try:
        with open(path, 'x') as f:
            f.write(record_header)
            f.write(record_entry)
    except FileExistsError:
        with open(path, 'a') as f:
            f.write(record_entry)
            
def find_records():
    print(f'What type of record are you searching for?')
    search_record = get_user_filled_record()
    print(f'\nSearching for a match to {search_record}')
    file_records = [{'Value' : '10k', 'Quantity' : '25', 'Tolerance' : '5', 'Power Rating' : '1/2', 'Package Type' : 'THT', 'Footprint' : '', 'Supplier P/N' : 'xxxx-ND', 'Location' : 'A2B5',},
                    {'Value' : '10k', 'Quantity' : '53', 'Tolerance' : '1', 'Power Rating' : '1/8', 'Package Type' : 'SMD', 'Footprint' : '0805', 'Supplier P/N' : 'xxxx-ND', 'Location' : 'A2B5',}
                    ]
    matches = []
    for record in file_records:
        if records_match(record, search_record):
            matches.append(record)
        
    if matches:
        print(f'Found {len(matches)} matches')
        for record in matches:
            print(record)

def records_match(record_1, record_2):
    matches = []
    for value1, value2 in zip(record_1.values(), record_2.values()):
        if value1 == value2:
            return 1
    return 0
    


def debug():
    record_1 = {'Value' : '10k', 'Quantity' : '25', 'Tolerance' : '5', 'Power Rating' : '1/2', 'Package Type' : 'THT', 'Footprint' : '', 'Supplier P/N' : 'xxxx-ND', 'Location' : 'A2B5',}
    record_2 = {'Value' : '10k', 'Quantity' : None, 'Tolerance' : None, 'Power Rating' : None, 'Package Type' : None, 'Footprint' : None, 'Supplier P/N' : None, 'Location' : None,}
    
    x = find_records()
    print(f'\nFound {len(x)} matches')
    for m in x:
        print(m)
    



def main():
    menu_sel = get_user_filled_menu()
    if menu_sel == 'A':
        save_record_to_file()
    if menu_sel == 'F':
        find_records()
    if menu_sel == 'D':
        debug()
    
if __name__ == '__main__':
    main()
    
    
