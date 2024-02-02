import hashlib
import csv
import time

def user(number_of_users):
    users = []
    for i in range(1, number_of_users + 1):
        name = input(f"User {i}: ")
        password = input(f"password {i}: ")

        hashed_string  = hashlib.sha256(password.encode()).hexdigest()
        user = {
            'name': name,
            'password': hashed_string
        }
        users.append(user)

    return users
def read_from_csv(flie_name):
    middle_thing = []
    with open(flie_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_thing = {
                "name" : row[0],
                "pass" : row[1]
            }
            middle_thing.append(new_thing)
    return middle_thing

def generator ():
    gen = []
    for i in range(1000 , 10000) :
        my_str = str(i)
        f = hashlib.sha256(my_str.encode()).hexdigest()
        codes = {
            "real_pas" : my_str,
            "hash" : f
        }
        gen.append(codes)
    return gen
def write_into(users_data , file__name = "the_list12") : 
    with open(file__name, "w" ) as file:
        for i in users_data :
            writer = csv.writer(file)
            writer.writerow(i.values())


users_data = user(20)
write_into(users_data)

last_thing = read_from_csv("the_list12")
last_gen = generator()
last_out = []
for i in last_thing :
    for j in last_gen :
        if i['pass'] == j['hash'] :
            out_put = {
                "the_name" : i["name"],
                "the_password" : j["real_pas"]
            }
            last_out.append(out_put)

with open("new_list", "w") as file:
    writer = csv.writer(file)
    for i in last_out :
        writer.writerow(i.values()) 

