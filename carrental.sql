CREATE TABLE VehicleCategory (
    VehicleCategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(50) UNIQUE,
    Description VARCHAR(255)
);
CREATE TABLE Locations (
    LocationsID INT PRIMARY KEY,
    LocationName VARCHAR(100) UNIQUE,
    Address VARCHAR(255),
    ContactPerson VARCHAR(100),
    ContactNumber VARCHAR(20)
);
CREATE TABLE Customers (
    CustomersID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(20),
    Address VARCHAR(255)
);
CREATE TABLE Cars (
    CarsID INT PRIMARY KEY,
    Model VARCHAR(255),
    Brand VARCHAR(255),
    Year INT,
    RegistrationPlate VARCHAR(20) UNIQUE,
    FuelType VARCHAR(50),
    Color VARCHAR(50),
    Status VARCHAR(20),
    VehicleCategoryID INT,
    LocationsID INT,
    CONSTRAINT FK_Cars_Category FOREIGN KEY (VehicleCategoryID) REFERENCES VehicleCategory(VehicleCategoryID),
    CONSTRAINT FK_Cars_Location FOREIGN KEY (LocationsID) REFERENCES Locations(LocationsID)
);
CREATE TABLE Reservations (
    ReservationsID INT PRIMARY KEY,
    CustomersID INT,
    CarsID INT,
    PickupDate DATETIME,
    ReturnDate DATETIME,
    TotalCost DECIMAL(10, 2),
    PaymentsID INT,
    ReservationStatus VARCHAR(50),
    CONSTRAINT FK_Reservations_Customer FOREIGN KEY (CustomersID) REFERENCES Customers(CustomersID),
    CONSTRAINT FK_Reservations_Car FOREIGN KEY (CarsID) REFERENCES Cars(CarsID) -- CONSTRAINT FK_Reservations_Payment FOREIGN KEY (PaymentsID) REFERENCES Payments(PaymentsID)
);
CREATE TABLE Payments (
    PaymentsID INT PRIMARY KEY,
    ReservationsID INT,
    PaymentDate DATETIME,
    Amount DECIMAL(10, 2),
    PaymentMethod VARCHAR(50),
    PaymentStatus VARCHAR(50),
    CONSTRAINT FK_Payments_Reservation FOREIGN KEY (ReservationsID) REFERENCES Reservations(ReservationsID)
);