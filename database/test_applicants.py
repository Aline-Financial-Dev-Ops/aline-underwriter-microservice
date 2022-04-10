import pytest
import mysql.connector
from applicants import generate_applicant

@pytest.fixture
def setup_database():
    con = mysql.connector.connect(
        host="localhost",
        user="mtran",
        password="password",
        database="aline"
    )
    cur = con.cursor(dictionary=True)
    yield cur
    cur.execute("DELETE FROM applicant")

def test_genereate_applicant(setup_database):
    cur = setup_database
    generate_applicant()
    cur.execute("SELECT * FROM applicant")
    applicants = cur.fetchall()
    assert len(applicants) == 25
    assert (type(applicants) is list) == True
    assert (type(applicants[-1]["income"]) is int) == True
    assert (type(applicants[-1]["first_name"]) is str) == True
