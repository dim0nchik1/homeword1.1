import re
import csv



def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        row = csv.reader(f, delimiter=',')
        contact_list =  list(row)
    return contact_list

def name_list(contact_list):
    new_contact_list = []
    for item in contact_list:
        word = ' '.join(item[:3]).split(' ')
        result = [word[0],word[1],word[2],item[3],item[4],item[5],item[6]]
        new_contact_list.append(result)
    return new_contact_list

def number_list(contact_list):
    pattern = r'(\+7|8)[\s\(]*(\w{3})[\s\)-]*(\w{3})[-]*(\w{2})[-]*(\w{2})[\s]*[\(]*(доб.)*([\s])*(\w{4})*[\)]*'
    patter_new =r'+7(\2)\3-\4-\5\7\6\8'
    contacts_new_list = []
    for contact in  contact_list:
        contacts = ','.join(contact)

        new_number = re.sub(pattern, patter_new, contacts)
        new_list = new_number.split(',')
        contacts_new_list.append(new_list)
    return contacts_new_list


def double_full_name(contact_list):
    for contact in contact_list:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in contact_list:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "": contact[2] = new_contact[2]
                if contact[3] == "": contact[3] = new_contact[3]
                if contact[4] == "": contact[4] = new_contact[4]
                if contact[5] == "": contact[5] = new_contact[5]
                if contact[6] == "": contact[6] = new_contact[6]
    new_contact_list = []
    for contact in contact_list:
        if contact not in new_contact_list:
            new_contact_list.append(contact)
    return new_contact_list

def write_file(contact_list):
     with open('py-homeworks-advanced-1.csv', 'w', encoding='utf-8') as f:
         write = csv.writer(f, delimiter=',')
         write.writerows(contact_list)


if __name__=='__main__':
    contact = read_file('py-homeworks-advanced.csv')
    contact = name_list(contact)
    contact = number_list(contact)
    contact = double_full_name(contact)
    write_file(contact)
