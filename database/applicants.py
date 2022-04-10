from faker import Faker
import requests

fake = Faker()

def generate_applicant():
    url = "http://localhost:4200/api/applicants"
    token = login()
    headers = { "Authorization": token }
    for i in range(25):
        Faker.seed(i)
        gender = fake.random.choice(["MALE", "FEMALE", "OTHER", "UNSPECIFIED"])
        name = ""
        if gender == "MALE":
            name = fake.name_male()
        elif gender == "FEMALE":
            name = fake.name_female()
        else:
            name = f"{fake.first_name()} {fake.last_name()}"
        name = name.split(" ")
        data = {
            "firstName": name[0],
            "lastName": name[1],
            "dateOfBirth": str(fake.date_of_birth(minimum_age=18)),
            "gender": gender,
            "email": fake.free_email(),
            "phone": fake.bothify("(###) ###-####"),
            "socialSecurity": fake.ssn(),
            "driversLicense": fake.bothify("DL#######"),
            "income": fake.random_int(min=20000, max=100000),
            "address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "zipcode": fake.zipcode(),
            "mailingAddress": fake.street_address(),
            "mailingCity": fake.city(),
            "mailingState": fake.state(),
            "mailingZipcode": fake.zipcode()
        }
        res = requests.post(url, json=data, headers=headers)
        print(res)

def login():
    url = "http://localhost:4200/login"
    payload = {
        "username": "AdminMT",
        "password": "Admin123!!!"
    }
    res = requests.post(url, json=payload)
    return res.headers["Authorization"]

if __name__ == "__main__":
    generate_applicant()
