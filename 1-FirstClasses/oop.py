class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first_name, self.last_name, self.pay)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)
print(emp_2)

print(Employee.fullname(emp_1))

print(emp_1.fullname())
print(emp_2.fullname())