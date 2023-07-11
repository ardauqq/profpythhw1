import Accounting.salary as AS
import Accounting.people as AP
import datetime
import matplotlib


def main():
    print(AS.calculate_salary())
    print(AP.get_employees())
    print(datetime.datetime.now())


if __name__ == '__main__':
    main()
    AS.calculate_salary()
    AP.get_employees()