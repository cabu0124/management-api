# Employee Management API

This is a CRUD API for managing employees in a company. It allows you to perform the following operations:

- Get all employees
- Get an employee by id
- Create a new employee
- Update employee information
- Delete an employee

## Technologies Used

This API is built using Python.

## Steps

- pip install fastapi
- pip install uvicorn
- uvicorn app:app --reload

## API Endpoints

The following endpoints are available for accessing employee data:

- `GET /employees`: Retrieves a list of all employees
- `GET /employees/<id>`: Retrieves details for a specific employee
- `POST /employees`: Creates a new employee record
- `PUT /employees`: Updates an existing employee record
- `DELETE /employees/<id>`: Deletes an employee record

## Contribution
Contributions are welcome! If you’d like to contribute:

- Fork the repository.
- Create a new branch (git checkout -b feature/new-feature).
- Make your changes and commit them (git commit -m 'Add new feature').
- Submit a pull request.
