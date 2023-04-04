from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

#Employee Model
class Employee(BaseModel):
    PersonID:str
    FirstName:str
    LastName:str
    SSN:str
    LastUpdatedBy:str
    LastUpdatedDate:datetime
    EmployeeNo:str
    EmploymentEndDate:datetime
    EmploymentStartDate:datetime
    Status:bool = False

#EmployeeUpdate Model
class EmployeeUpdate(BaseModel):
    PersonID:str
    FirstName:str
    LastName:str
    SSN:str
    Status:bool

app = FastAPI()

#Allow CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

employees = [
  {
    "PersonID": "fcc12c62-2782-45dd-bb36-07f5035d8679",
    "FirstName": "Carlos",
    "LastName": "Castano",
    "SSN": "111-22-1111",
    "LastUpdatedBy": "admin",
    "LastUpdatedDate": "2023-04-02T03:52:48.462000+00:00",
    "EmployeeNo": "0001",
    "EmploymentEndDate": "2023-04-02T03:52:48.462000+00:00",
    "EmploymentStartDate": "2023-04-02T03:52:48.462000+00:00",
    "Status": False
  },
  {
    "PersonID": "fcc12c62-2782-45dd-bb36-07f5035d8670",
    "FirstName": "William",
    "LastName": "Gates2",
    "SSN": "111-22-1111",
    "LastUpdatedBy": "admin",
    "LastUpdatedDate": "2023-04-02T03:52:48.462000+00:00",
    "EmployeeNo": "0001",
    "EmploymentEndDate": "2023-04-02T03:52:48.462000+00:00",
    "EmploymentStartDate": "2023-04-02T03:52:48.462000+00:00",
    "Status": False
  },
  {
    "PersonID": "fcc12c62-2782-45dd-bb36-07f5035d8671",
    "FirstName": "Ana",
    "LastName": "Rodriguez",
    "SSN": "111-22-1111",
    "LastUpdatedBy": "admin",
    "LastUpdatedDate": "2023-04-02T03:52:48.462000+00:00",
    "EmployeeNo": "0001",
    "EmploymentEndDate": "2023-04-02T03:52:48.462000+00:00",
    "EmploymentStartDate": "2023-04-02T03:52:48.462000+00:00",
    "Status": False
  }
]

@app.get('/')
def read_root():
    return {"message":"Welcome to the Management API"}

@app.get('/Employees')
def get_employees():
    return employees

@app.get('/Employees/{employeeId}')
def get_employee_byId(employeeId:str):
    for employee in employees:
        if employee['PersonID'] == employeeId:
            return employee
    return HTTPException(status_code=404, detail="Employee Not found")

@app.post('/Employees')
def create_employee(employee:Employee):
    employees.append(employee.dict())
    return {'Message':'The employee has been created'}

@app.delete('/Employees/{employeeId}')
def delete_employee(employeeId:str):
    for index, employee in enumerate(employees):
        if employee['PersonID'] == employeeId:
            employees.pop(index)
            return {'Message':'The employee has been deleted'}
    return HTTPException(status_code=404, detail="Employee Not found")

@app.put('/Employees')
def update_employee(newEmployee:EmployeeUpdate):
    newEmployeeObj = newEmployee.dict()
    for index, employee in enumerate(employees):
        if employee['PersonID'] == newEmployeeObj['PersonID']:
            employees[index]['PersonID'] = newEmployeeObj['PersonID']
            employees[index]['FirstName'] = newEmployeeObj['FirstName']
            employees[index]['LastName'] = newEmployeeObj['LastName']
            employees[index]['SSN'] = newEmployeeObj['SSN']
            employees[index]['Status'] = newEmployeeObj['Status']
            return {'Message':'The employee has been updated'}
    return HTTPException(status_code=404, detail="Employee Not found")