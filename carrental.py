from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
import customtkinter

customtkinter.set_appearance_mode("Light")  
customtkinter.set_default_color_theme("green")  

class first(customtkinter.CTk):
    def __init__(self):

        super().__init__()
        self.geometry("900x700+350+50")
        self.title("Welcome to CAR RENTAL")
        self.resizable(width = False, height = False)

        # ============ create frames ============

        # configure grid layout (3x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=180, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_mid = customtkinter.CTkFrame(master=self)
        self.frame_mid.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.frame_mid1 = customtkinter.CTkFrame(master=self)
        self.frame_mid1.grid(row=5, column=0,columnspan = 5, sticky="nswe", padx=20, pady=20)

        self.frame_right = customtkinter.CTkFrame(master=self, width=180, corner_radius=0)
        self.frame_right.grid(row=0, column=2, sticky="nswe")

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left, text="Select View")  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        def iExit():
            iExit = tkinter.messagebox.askyesno("CAR RENTAL", "Confirm if you want to exit")
            if iExit:
                self.destroy()
                return

        def distroy():
            self.frame_mid1.destroy
            self.frame_mid1 = customtkinter.CTkFrame(master=self)
            self.frame_mid1.grid(row=5, column=0,columnspan = 5, sticky="nswe", padx=20, pady=20)
            
        def desplay():
            self.frame_mid.destroy
            self.frame_mid = customtkinter.CTkFrame(master=self)
            self.frame_mid.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.button1 = customtkinter.CTkButton(master=self.frame_left, text="Exit", command=iExit)
        self.button1.grid(row=9, column=0, pady=10, padx=20)

        def selectTable(tb):
            distroy()
            desplay()
            # ScrollBar
            scrolly = Scrollbar(master=self.frame_mid1, orient = VERTICAL)

            if tb == 'VehicleCategory':
    # Function variables
                VehicleCategoryID = StringVar()
                CategoryName = StringVar()
                Description = StringVar()

                def iExit():
                    iExit = tkinter.messagebox.askyesno("CAR RENTAL", "Confirm if you want to exit")
                    if iExit:
                        # Assuming self is the tkinter root window
                        self.destroy()
                        return

                def Reset():
                    VehicleCategoryID.set("")
                    CategoryName.set("")
                    Description.set("")

                    # Assuming self.ent1, self.ent2, and self.ent3 are Entry widgets
                    self.ent1.delete(0, END)
                    self.ent2.delete(0, END)
                    self.ent3.delete(0, END)


                def addCategory():
                    if VehicleCategoryID.get() == "":
                        tkinter.messagebox.showerror("CAR RENTAL", "Enter correct Details")
                    else:
                        sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                        cur = sqlCon.cursor()
                        cur.execute("INSERT INTO VehicleCategory VALUES(%s,%s,%s)",
                                    (VehicleCategoryID.get(), CategoryName.get(), Description.get()))
                        sqlCon.commit()
                        dispCategory()
                        sqlCon.close()
                        Reset()

                        tkinter.messagebox.showinfo("CAR RENTAL", "Record Entered Successfully")

                def dispCategory():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute("SELECT * FROM VehicleCategory")
                    dispList = []

                    for i in cur:
                        dispList.append(i)

                    if dispList == []:
                        tkinter.messagebox.showinfo("CAR RENTAL", "NO RECORDS TO DISPLAY")
                    else:
                        records.delete(*records.get_children())
                        for row in dispList:
                            records.insert('', END, values=row)

                    sqlCon.commit()
                    sqlCon.close()

                def Infoo(e):
                    viewInfo = records.focus()
                    learnData = records.item(viewInfo)
                    row = learnData['values']
                    VehicleCategoryID.set(row[0])
                    CategoryName.set(row[1])
                    Description.set(row[2])

                def updateCategory():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute("UPDATE VehicleCategory SET CategoryName = %s, Description = %s WHERE VehicleCategoryID = %s",
                                (CategoryName.get(), Description.get(), VehicleCategoryID.get()))
                    sqlCon.commit()
                    dispCategory()
                    sqlCon.close()
                    Reset()

                    tkinter.messagebox.showinfo("CAR RENTAL", "Record Updated Successfully")

                def deleteCategory():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute("DELETE FROM VehicleCategory WHERE VehicleCategoryID = %s", VehicleCategoryID.get())
                    sqlCon.commit()
                    dispCategory()
                    sqlCon.close()
                    Reset()

                    tkinter.messagebox.showinfo("CAR RENTAL", "Record Deleted Successfully")


                
       
                self.lb1 = customtkinter.CTkLabel(master=self.frame_mid, text="Vehicle Category ID")
                self.lb1.grid(row=1, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent1 = customtkinter.CTkEntry(master=self.frame_mid, width=150, textvariable=VehicleCategoryID)
                self.ent1.grid(row=1, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb2 = customtkinter.CTkLabel(master=self.frame_mid, text="Category Name")
                self.lb2.grid(row=2, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent2 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=CategoryName)
                self.ent2.grid(row=2, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb3 = customtkinter.CTkLabel(master=self.frame_mid, text="Description")
                self.lb3.grid(row=3, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent3 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=Description)
                self.ent3.grid(row=3, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                # To view the categories
                records = ttk.Treeview(master=self.frame_mid1, height=14,
                                    columns=("VehicleCategoryID", "CategoryName", "Description"), xscrollcommand=scrolly.set)
                scrolly.pack(side=RIGHT, fill=Y)

                # Columns and their headings
                records.heading("VehicleCategoryID", text="Vehicle Category ID")
                records.heading("CategoryName", text="Category Name")
                records.heading("Description", text="Description")

                records['show'] = 'headings'

                records.column("VehicleCategoryID", width=100)
                records.column("CategoryName", width=100)
                records.column("Description", width=200)

                records.pack(fill=BOTH, expand=1)
                records.bind("<ButtonRelease-1>", Infoo)

                self.label_1 = customtkinter.CTkLabel(master=self.frame_left, text="Select View")
                self.label_1.grid(row=0, column=4, columnspan=1, pady=20, padx=10, sticky="")

                self.btn1 = customtkinter.CTkButton(master=self.frame_right, text="Add Category", command=addCategory)
                self.btn1.grid(row=1, column=4, pady=10, padx=20)
                self.btn2 = customtkinter.CTkButton(master=self.frame_right, text="Display", command=dispCategory)
                self.btn2.grid(row=2, column=4, pady=10, padx=20)
                self.btn3 = customtkinter.CTkButton(master=self.frame_right, text="Update", command=updateCategory)
                self.btn3.grid(row=3, column=4, pady=10, padx=20)
                self.btn4 = customtkinter.CTkButton(master=self.frame_right, text="Delete", command=deleteCategory)
                self.btn4.grid(row=4, column=4, pady=10, padx=20)

            elif tb == 'Locations':
                # Function variables
                LocationsID = StringVar()
                LocationName = StringVar()
                Address = StringVar()
                ContactPerson = StringVar()
                ContactNumber = StringVar()

                def iExit():
                    iExit = tkinter.messagebox.askyesno("CAR RENTAL", "Confirm if you want to exit")
                    if iExit:
                        self.destroy()
                        return

                def Reset():
                    LocationsID.set("")
                    LocationName.set("")
                    Address.set("")
                    ContactPerson.set("")
                    ContactNumber.set("")

                    self.ent1.delete(0, END)
                    self.ent2.delete(0, END)
                    self.ent3.delete(0, END)
                    self.ent4.delete(0, END)
                    self.ent5.delete(0, END)

                def addData():
                    if LocationsID.get() == "":
                        tkinter.messagebox.showerror("CAR RENTAL", "Enter correct Details")
                    else:
                        sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                        cur = sqlCon.cursor()
                        cur.execute("INSERT INTO Locations VALUES(%s,%s,%s,%s,%s)", (
                            LocationsID.get(),
                            LocationName.get(),
                            Address.get(),
                            ContactPerson.get(),
                            ContactNumber.get()
                        ))
                        sqlCon.commit()
                        dispData()
                        sqlCon.close()
                        Reset()

                        tkinter.messagebox.showinfo("CAR RENTAL", "Record Entered Successfully")

                def dispData():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()

                    cur.execute("SELECT * FROM Locations")
                    dispList = []

                    for i in cur:
                        dispList.append(i)

                    if dispList == []:
                        tkinter.messagebox.showinfo("CAR RENTAL", "NO RECORDS TO DISPLAY")
                    else:
                        records.delete(*records.get_children())
                        for row in dispList:
                            records.insert('', END, values=row)

                    sqlCon.commit()
                    sqlCon.close()

                def Infoo(e):
                    viewInfo = records.focus()
                    learnData = records.item(viewInfo)
                    row = learnData['values']
                    LocationsID.set(row[0])
                    LocationName.set(row[1])
                    Address.set(row[2])
                    ContactPerson.set(row[3])
                    ContactNumber.set(row[4])

                def update():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute(
                        "UPDATE Locations SET LocationName = %s, Address = %s, ContactPerson = %s, ContactNumber = %s WHERE LocationsID = %s",
                        (
                            LocationName.get(),
                            Address.get(),
                            ContactPerson.get(),
                            ContactNumber.get(),
                            LocationsID.get(),
                        ))
                    sqlCon.commit()
                    dispData()
                    sqlCon.close()
                    Reset()

                    tkinter.messagebox.showinfo("CAR RENTAL", "Record Updated Successfully")

                def deleteRecords():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute("DELETE FROM Locations WHERE LocationsID = %s", LocationsID.get())
                    sqlCon.commit()
                    dispData()
                    sqlCon.close()
                    Reset()

                    tkinter.messagebox.showinfo("CAR RENTAL", "Record Deleted Successfully")

                # GUI elements
                self.lb1 = customtkinter.CTkLabel(master=self.frame_mid, text="Locations ID")
                self.lb1.grid(row=1, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent1 = customtkinter.CTkEntry(master=self.frame_mid, width=150, textvariable=LocationsID)
                self.ent1.grid(row=1, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb2 = customtkinter.CTkLabel(master=self.frame_mid, text="Location Name")
                self.lb2.grid(row=2, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent2 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=LocationName)
                self.ent2.grid(row=2, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb3 = customtkinter.CTkLabel(master=self.frame_mid, text="Address")
                self.lb3.grid(row=3, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent3 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=Address)
                self.ent3.grid(row=3, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb4 = customtkinter.CTkLabel(master=self.frame_mid, text="Contact Person")
                self.lb4.grid(row=4, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent4 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=ContactPerson)
                self.ent4.grid(row=4, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb5 = customtkinter.CTkLabel(master=self.frame_mid, text="Contact Number")
                self.lb5.grid(row=5, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent5 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=ContactNumber)
                self.ent5.grid(row=5, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                # To view the tables
                records = ttk.Treeview(master=self.frame_mid1, height=14,
                                    columns=("LocationsID", "LocationName", "Address", "ContactPerson", "ContactNumber"),
                                    xscrollcommand=scrolly.set)
                scrolly.pack(side=RIGHT, fill=Y)

                # Columns and their headings
                records.heading("LocationsID", text="Locations ID")
                records.heading("LocationName", text="Location Name")
                records.heading("Address", text="Address")
                records.heading("ContactPerson", text="Contact Person")
                records.heading("ContactNumber", text="Contact Number")

                records['show'] = 'headings'

                records.column("LocationsID", width=100)
                records.column("LocationName", width=100)
                records.column("Address", width=200)
                records.column("ContactPerson", width=150)
                records.column("ContactNumber", width=120)

                records.pack(fill=BOTH, expand=1)
                records.bind("<ButtonRelease-1>", Infoo)

                self.label_1 = customtkinter.CTkLabel(master=self.frame_left, text="Select View")
                self.label_1.grid(row=0, column=4, columnspan=1, pady=20, padx=10, sticky="")

                self.btn1 = customtkinter.CTkButton(master=self.frame_right, text="Add Data", command=addData)
                self.btn1.grid(row=1, column=4, pady=10, padx=20)
                self.btn2 = customtkinter.CTkButton(master=self.frame_right, text="Display", command=dispData)
                self.btn2.grid(row=2, column=4, pady=10, padx=20)
                self.btn3 = customtkinter.CTkButton(master=self.frame_right, text="Update", command=update)
                self.btn3.grid(row=3, column=4, pady=10, padx=20)
                self.btn4 = customtkinter.CTkButton(master=self.frame_right, text="Delete", command=deleteRecords)
                self.btn4.grid(row=4, column=4, pady=10, padx=20)

            elif tb == 'Customers':
                # Function variables
                CustomersID = StringVar()
                FirstName = StringVar()
                LastName = StringVar()
                Email = StringVar()
                Phone = StringVar()
                Address = StringVar()

                def iExit():
                    iExit = tkinter.messagebox.askyesno("CAR RENTAL", "Confirm if you want to exit")
                    if iExit:
                        self.destroy()
                        return

                def Reset():
                    CustomersID.set("")
                    FirstName.set("")
                    LastName.set("")
                    Email.set("")
                    Phone.set("")
                    Address.set("")

                    self.ent1.delete(0, END)
                    self.ent2.delete(0, END)
                    self.ent3.delete(0, END)
                    self.ent4.delete(0, END)
                    self.ent5.delete(0, END)
                    self.ent6.delete(0, END)

                def addData():
                    if CustomersID.get() == "":
                        tkinter.messagebox.showerror("CAR RENTAL", "Enter correct Details")
                    else:
                        sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                        cur = sqlCon.cursor()
                        cur.execute("INSERT INTO Customers VALUES(%s,%s,%s,%s,%s,%s)", (
                            CustomersID.get(),
                            FirstName.get(),
                            LastName.get(),
                            Email.get(),
                            Phone.get(),
                            Address.get()
                        ))
                        sqlCon.commit()
                        dispData()
                        sqlCon.close()
                        Reset()

                        tkinter.messagebox.showinfo("CAR RENTAL", "Record Entered Successfully")

                def dispData():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()

                    cur.execute("SELECT * FROM Customers")
                    dispList = []

                    for i in cur:
                        dispList.append(i)

                    if dispList == []:
                        tkinter.messagebox.showinfo("CAR RENTAL", "NO RECORDS TO DISPLAY")
                    else:
                        records.delete(*records.get_children())
                        for row in dispList:
                            records.insert('', END, values=row)

                    sqlCon.commit()
                    sqlCon.close()

                def Infoo(e):
                    viewInfo = records.focus()
                    learnData = records.item(viewInfo)
                    row = learnData['values']
                    CustomersID.set(row[0])
                    FirstName.set(row[1])
                    LastName.set(row[2])
                    Email.set(row[3])
                    Phone.set(row[4])
                    Address.set(row[5])

                def update():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute("UPDATE Customers SET FirstName = %s, LastName = %s, Email = %s, Phone = %s, Address = %s WHERE CustomersID = %s", (
                        FirstName.get(),
                        LastName.get(),
                        Email.get(),
                        Phone.get(),
                        Address.get(),
                        CustomersID.get(),
                    ))
                    sqlCon.commit()
                    dispData()
                    sqlCon.close()
                    Reset()

                    tkinter.messagebox.showinfo("CAR RENTAL", "Record Updated Successfully")

                def deleteRecords():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute("DELETE FROM Customers WHERE CustomersID = %s", CustomersID.get())
                    sqlCon.commit()
                    dispData()
                    sqlCon.close()
                    Reset()

                    tkinter.messagebox.showinfo("CAR RENTAL", "Record Deleted Successfully")

                # GUI elements
                self.lb1 = customtkinter.CTkLabel(master=self.frame_mid, text="Customer ID")
                self.lb1.grid(row=1, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent1 = customtkinter.CTkEntry(master=self.frame_mid, width=150, textvariable=CustomersID)
                self.ent1.grid(row=1, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb2 = customtkinter.CTkLabel(master=self.frame_mid, text="First Name")
                self.lb2.grid(row=2, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent2 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=FirstName)
                self.ent2.grid(row=2, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb3 = customtkinter.CTkLabel(master=self.frame_mid, text="Last Name")
                self.lb3.grid(row=3, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent3 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=LastName)
                self.ent3.grid(row=3, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb4 = customtkinter.CTkLabel(master=self.frame_mid, text="Email")
                self.lb4.grid(row=4, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent4 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=Email)
                self.ent4.grid(row=4, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb5 = customtkinter.CTkLabel(master=self.frame_mid, text="Phone")
                self.lb5.grid(row=5, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent5 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=Phone)
                self.ent5.grid(row=5, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb6 = customtkinter.CTkLabel(master=self.frame_mid, text="Address")
                self.lb6.grid(row=6, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent6 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=Address)
                self.ent6.grid(row=6, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                # To view the tables
                records = ttk.Treeview(master=self.frame_mid1, height=14,
                                    columns=("CustomersID", "FirstName", "LastName", "Email", "Phone", "Address"),
                                    xscrollcommand=scrolly.set)
                scrolly.pack(side=RIGHT, fill=Y)

                # Columns and their headings
                records.heading("CustomersID", text="Customer ID")
                records.heading("FirstName", text="First Name")
                records.heading("LastName", text="Last Name")
                records.heading("Email", text="Email")
                records.heading("Phone", text="Phone")
                records.heading("Address", text="Address")

                records['show'] = 'headings'

                records.column("CustomersID", width=100)
                records.column("FirstName", width=100)
                records.column("LastName", width=100)
                records.column("Email", width=100)
                records.column("Phone", width=100)
                records.column("Address", width=100)

                records.pack(fill=BOTH, expand=1)
                records.bind("<ButtonRelease-1>", Infoo)

                self.label_1 = customtkinter.CTkLabel(master=self.frame_left, text="Select View")
                self.label_1.grid(row=0, column=4, columnspan=1, pady=20, padx=10, sticky="")

                self.btn1 = customtkinter.CTkButton(master=self.frame_right, text="Add Data", command=addData)
                self.btn1.grid(row=1, column=4, pady=10, padx=20)
                self.btn2 = customtkinter.CTkButton(master=self.frame_right, text="Display", command=dispData)
                self.btn2.grid(row=2, column=4, pady=10, padx=20)
                self.btn3 = customtkinter.CTkButton(master=self.frame_right, text="Update", command=update)
                self.btn3.grid(row=3, column=4, pady=10, padx=20)
                self.btn4 = customtkinter.CTkButton(master=self.frame_right, text="Delete", command=deleteRecords)
                self.btn4.grid(row=4, column=4, pady=10, padx=20)

            elif tb == 'Cars':
                # Function variables
                CarsID = StringVar()
                Model = StringVar()
                Brand = StringVar()
                Year = StringVar()
                RegistrationPlate = StringVar()
                FuelType = StringVar()
                Color = StringVar()
                Status = StringVar()
                VehicleCategoryID = StringVar()
                LocationsID = StringVar()

                def iExit():
                    iExit = tkinter.messagebox.askyesno("CAR RENTAL", "Confirm if you want to exit")
                    if iExit:
                        self.destroy()
                        return

                def Reset():
                    CarsID.set("")
                    Model.set("")
                    Brand.set("")
                    Year.set("")
                    RegistrationPlate.set("")
                    FuelType.set("")
                    Color.set("")
                    Status.set("")
                    VehicleCategoryID.set("")
                    LocationsID.set("")

                    self.ent1.delete(0, END)
                    self.ent2.delete(0, END)
                    self.ent3.delete(0, END)
                    self.ent4.delete(0, END)
                    self.ent5.delete(0, END)
                    self.ent6.delete(0, END)
                    self.ent7.delete(0, END)
                    self.ent8.delete(0, END)
                    self.ent9.delete(0, END)

                def addData():
                    if CarsID.get() == "":
                        tkinter.messagebox.showerror("CAR RENTAL", "Enter correct Details")
                    else:
                        sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                        cur = sqlCon.cursor()
                        cur.execute("INSERT INTO Cars VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                            CarsID.get(),
                            Model.get(),
                            Brand.get(),
                            Year.get(),
                            RegistrationPlate.get(),
                            FuelType.get(),
                            Color.get(),
                            Status.get(),
                            VehicleCategoryID.get(),
                            LocationsID.get()
                        ))
                        sqlCon.commit()
                        dispData()
                        sqlCon.close()
                        Reset()

                        tkinter.messagebox.showinfo("CAR RENTAL", "Record Entered Successfully")

                def dispData():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()

                    cur.execute("SELECT * FROM Cars")
                    dispList = []

                    for i in cur:
                        dispList.append(i)

                    if dispList == []:
                        tkinter.messagebox.showinfo("CAR RENTAL", "NO RECORDS TO DISPLAY")
                    else:
                        records.delete(*records.get_children())
                        for row in dispList:
                            records.insert('', END, values=row)

                    sqlCon.commit()
                    sqlCon.close()

                def Infoo(e):
                    viewInfo = records.focus()
                    learnData = records.item(viewInfo)
                    row = learnData['values']
                    CarsID.set(row[0])
                    Model.set(row[1])
                    Brand.set(row[2])
                    Year.set(row[3])
                    RegistrationPlate.set(row[4])
                    FuelType.set(row[5])
                    Color.set(row[6])
                    Status.set(row[7])
                    VehicleCategoryID.set(row[8])
                    LocationsID.set(row[9])

                def update():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute("UPDATE Cars SET Model = %s, Brand = %s, Year = %s, RegistrationPlate = %s, FuelType = %s, Color = %s, Status = %s, VehicleCategoryID = %s, LocationsID = %s WHERE CarsID = %s", (
                        Model.get(),
                        Brand.get(),
                        Year.get(),
                        RegistrationPlate.get(),
                        FuelType.get(),
                        Color.get(),
                        Status.get(),
                        VehicleCategoryID.get(),
                        LocationsID.get(),
                        CarsID.get()
                    ))
                    sqlCon.commit()
                    dispData()
                    sqlCon.close()
                    Reset()

                    tkinter.messagebox.showinfo("CAR RENTAL", "Record Updated Successfully")

                def deleteRecords():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute("DELETE FROM Cars WHERE CarsID = %s", CarsID.get())
                    sqlCon.commit()
                    dispData()
                    sqlCon.close()
                    Reset()

                    tkinter.messagebox.showinfo("CAR RENTAL", "Record Deleted Successfully")

                # GUI elements
                self.lb1 = customtkinter.CTkLabel(master=self.frame_mid, text="Cars ID")
                self.lb1.grid(row=1, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent1 = customtkinter.CTkEntry(master=self.frame_mid, width=150, textvariable=CarsID)
                self.ent1.grid(row=1, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb2 = customtkinter.CTkLabel(master=self.frame_mid, text="Model")
                self.lb2.grid(row=2, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent2 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=Model)
                self.ent2.grid(row=2, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb3 = customtkinter.CTkLabel(master=self.frame_mid, text="Brand")
                self.lb3.grid(row=3, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent3 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=Brand)
                self.ent3.grid(row=3, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb4 = customtkinter.CTkLabel(master=self.frame_mid, text="Year")
                self.lb4.grid(row=4, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent4 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=Year)
                self.ent4.grid(row=4, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb5 = customtkinter.CTkLabel(master=self.frame_mid, text="Registration Plate")
                self.lb5.grid(row=5, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent5 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=RegistrationPlate)
                self.ent5.grid(row=5, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb6 = customtkinter.CTkLabel(master=self.frame_mid, text="Fuel Type")
                self.lb6.grid(row=6, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent6 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=FuelType)
                self.ent6.grid(row=6, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb7 = customtkinter.CTkLabel(master=self.frame_mid, text="Color")
                self.lb7.grid(row=7, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent7 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=Color)
                self.ent7.grid(row=7, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb8 = customtkinter.CTkLabel(master=self.frame_mid, text="Status")
                self.lb8.grid(row=8, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent8 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=Status)
                self.ent8.grid(row=8, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb9 = customtkinter.CTkLabel(master=self.frame_mid, text="Vehicle Category ID")
                self.lb9.grid(row=9, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent9 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=VehicleCategoryID)
                self.ent9.grid(row=9, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb10 = customtkinter.CTkLabel(master=self.frame_mid, text="Locations ID")
                self.lb10.grid(row=10, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent10 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=LocationsID)
                self.ent10.grid(row=10, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                # To view the tables
                records = ttk.Treeview(master=self.frame_mid1, height=14, columns=("CarsID", "Model", "Brand", "Year", "RegistrationPlate", "FuelType", "Color", "Status", "VehicleCategoryID", "LocationsID"), xscrollcommand=scrolly.set)
                scrolly.pack(side=RIGHT, fill=Y)

                # Columns and their headings
                records.heading("CarsID", text="Cars ID")
                records.heading("Model", text="Model")
                records.heading("Brand", text="Brand")
                records.heading("Year", text="Year")
                records.heading("RegistrationPlate", text="Registration Plate")
                records.heading("FuelType", text="Fuel Type")
                records.heading("Color", text="Color")
                records.heading("Status", text="Status")
                records.heading("VehicleCategoryID", text="Vehicle Category ID")
                records.heading("LocationsID", text="Locations ID")

                records['show'] = 'headings'

                records.column("CarsID", width=100)
                records.column("Model", width=100)
                records.column("Brand", width=100)
                records.column("Year", width=100)
                records.column("RegistrationPlate", width=100)
                records.column("FuelType", width=100)
                records.column("Color", width=100)
                records.column("Status", width=100)
                records.column("VehicleCategoryID", width=100)
                records.column("LocationsID", width=100)

                records.pack(fill=BOTH, expand=1)
                records.bind("<ButtonRelease-1>", Infoo)

                self.label_1 = customtkinter.CTkLabel(master=self.frame_left, text="Select View")
                self.label_1.grid(row=0, column=4, columnspan=1, pady=20, padx=10, sticky="")

                self.btn1 = customtkinter.CTkButton(master=self.frame_right, text="Add Data", command=addData)
                self.btn1.grid(row=1, column=4, pady=10, padx=20)
                self.btn2 = customtkinter.CTkButton(master=self.frame_right, text="Display", command=dispData)
                self.btn2.grid(row=2, column=4, pady=10, padx=20)
                self.btn3 = customtkinter.CTkButton(master=self.frame_right, text="Update", command=update)
                self.btn3.grid(row=3, column=4, pady=10, padx=20)
                self.btn4 = customtkinter.CTkButton(master=self.frame_right, text="Delete", command=deleteRecords)
                self.btn4.grid(row=4, column=4, pady=10, padx=20)

            elif tb == 'Reservations':
                # Function variables
                ReservationsID = StringVar()
                CustomersID = StringVar()
                CarsID = StringVar()
                PickupDate = StringVar()
                ReturnDate = StringVar()
                TotalCost = StringVar()
                PaymentsID = StringVar()
                ReservationStatus = StringVar()

                def iExit():
                    iExit = tkinter.messagebox.askyesno("CAR RENTAL", "Confirm if you want to exit")
                    if iExit:
                        self.destroy()
                        return

                def Reset():
                    ReservationsID.set("")
                    CustomersID.set("")
                    CarsID.set("")
                    PickupDate.set("")
                    ReturnDate.set("")
                    TotalCost.set("")
                    PaymentsID.set("")
                    ReservationStatus.set("")

                    self.ent1.delete(0, END)
                    self.ent2.delete(0, END)
                    self.ent3.delete(0, END)
                    self.ent4.delete(0, END)
                    self.ent5.delete(0, END)
                    self.ent6.delete(0, END)
                    self.ent7.delete(0, END)
                    self.ent8.delete(0, END)

                def addData():
                    if ReservationsID.get() == "":
                        tkinter.messagebox.showerror("CAR RENTAL", "Enter correct Details")
                    else:
                        sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                        cur = sqlCon.cursor()
                        cur.execute("INSERT INTO Reservations VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", (
                            ReservationsID.get(),
                            CustomersID.get(),
                            CarsID.get(),
                            PickupDate.get(),
                            ReturnDate.get(),
                            TotalCost.get(),
                            PaymentsID.get(),
                            ReservationStatus.get()
                        ))
                        sqlCon.commit()
                        dispData()
                        sqlCon.close()
                        Reset()

                        tkinter.messagebox.showinfo("CAR RENTAL", "Record Entered Successfully")

                def dispData():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()

                    cur.execute("SELECT * FROM Reservations")
                    dispList = []

                    for i in cur:
                        dispList.append(i)

                    if dispList == []:
                        tkinter.messagebox.showinfo("CAR RENTAL", "NO RECORDS TO DISPLAY")
                    else:
                        records.delete(*records.get_children())
                        for row in dispList:
                            records.insert('', END, values=row)

                    sqlCon.commit()
                    sqlCon.close()

                def Infoo(e):
                    viewInfo = records.focus()
                    learnData = records.item(viewInfo)
                    row = learnData['values']
                    ReservationsID.set(row[0])
                    CustomersID.set(row[1])
                    CarsID.set(row[2])
                    PickupDate.set(row[3])
                    ReturnDate.set(row[4])
                    TotalCost.set(row[5])
                    PaymentsID.set(row[6])
                    ReservationStatus.set(row[7])

                def update():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute("UPDATE Reservations SET CustomersID = %s, CarsID = %s, PickupDate = %s, ReturnDate = %s, TotalCost = %s, PaymentsID = %s, ReservationStatus = %s WHERE ReservationsID = %s", (
                        CustomersID.get(),
                        CarsID.get(),
                        PickupDate.get(),
                        ReturnDate.get(),
                        TotalCost.get(),
                        PaymentsID.get(),
                        ReservationStatus.get(),
                        ReservationsID.get()
                    ))
                    sqlCon.commit()
                    dispData()
                    sqlCon.close()
                    Reset()

                    tkinter.messagebox.showinfo("CAR RENTAL", "Record Updated Successfully")

                def deleteRecords():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute("DELETE FROM Reservations WHERE ReservationsID = %s", ReservationsID.get())
                    sqlCon.commit()
                    dispData()
                    sqlCon.close()
                    Reset()

                    tkinter.messagebox.showinfo("CAR RENTAL", "Record Deleted Successfully")

                # GUI elements
                self.lb1 = customtkinter.CTkLabel(master=self.frame_mid, text="Reservations ID")
                self.lb1.grid(row=1, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent1 = customtkinter.CTkEntry(master=self.frame_mid, width=150, textvariable=ReservationsID)
                self.ent1.grid(row=1, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb2 = customtkinter.CTkLabel(master=self.frame_mid, text="Customers ID")
                self.lb2.grid(row=2, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent2 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=CustomersID)
                self.ent2.grid(row=2, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb3 = customtkinter.CTkLabel(master=self.frame_mid, text="Cars ID")
                self.lb3.grid(row=3, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent3 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=CarsID)
                self.ent3.grid(row=3, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb4 = customtkinter.CTkLabel(master=self.frame_mid, text="Pickup Date")
                self.lb4.grid(row=4, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent4 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=PickupDate)
                self.ent4.grid(row=4, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb5 = customtkinter.CTkLabel(master=self.frame_mid, text="Return Date")
                self.lb5.grid(row=5, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent5 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=ReturnDate)
                self.ent5.grid(row=5, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb6 = customtkinter.CTkLabel(master=self.frame_mid, text="Total Cost")
                self.lb6.grid(row=6, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent6 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=TotalCost)
                self.ent6.grid(row=6, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb7 = customtkinter.CTkLabel(master=self.frame_mid, text="Payments ID")
                self.lb7.grid(row=7, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent7 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=PaymentsID)
                self.ent7.grid(row=7, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb8 = customtkinter.CTkLabel(master=self.frame_mid, text="Reservation Status")
                self.lb8.grid(row=8, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent8 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=ReservationStatus)
                self.ent8.grid(row=8, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                # To view the tables
                records = ttk.Treeview(master=self.frame_mid1, height=14, columns=("ReservationsID", "CustomersID", "CarsID", "PickupDate", "ReturnDate", "TotalCost", "PaymentsID", "ReservationStatus"), xscrollcommand=scrolly.set)
                scrolly.pack(side=RIGHT, fill=Y)

                # Columns and their headings
                records.heading("ReservationsID", text="Reservations ID")
                records.heading("CustomersID", text="Customers ID")
                records.heading("CarsID", text="Cars ID")
                records.heading("PickupDate", text="Pickup Date")
                records.heading("ReturnDate", text="Return Date")
                records.heading("TotalCost", text="Total Cost")
                records.heading("PaymentsID", text="Payments ID")
                records.heading("ReservationStatus", text="Reservation Status")

                records['show'] = 'headings'

                records.column("ReservationsID", width=100)
                records.column("CustomersID", width=100)
                records.column("CarsID", width=100)
                records.column("PickupDate", width=100)
                records.column("ReturnDate", width=100)
                records.column("TotalCost", width=100)
                records.column("PaymentsID", width=100)
                records.column("ReservationStatus", width=100)

                records.pack(fill=BOTH, expand=1)
                records.bind("<ButtonRelease-1>", Infoo)

                self.label_1 = customtkinter.CTkLabel(master=self.frame_left, text="Select View")
                self.label_1.grid(row=0, column=4, columnspan=1, pady=20, padx=10, sticky="")

                self.btn1 = customtkinter.CTkButton(master=self.frame_right, text="Add Data", command=addData)
                self.btn1.grid(row=1, column=4, pady=10, padx=20)
                self.btn2 = customtkinter.CTkButton(master=self.frame_right, text="Display", command=dispData)
                self.btn2.grid(row=2, column=4, pady=10, padx=20)
                self.btn3 = customtkinter.CTkButton(master=self.frame_right, text="Update", command=update)
                self.btn3.grid(row=3, column=4, pady=10, padx=20)
                self.btn4 = customtkinter.CTkButton(master=self.frame_right, text="Delete", command=deleteRecords)
                self.btn4.grid(row=4, column=4, pady=10, padx=20)

            elif tb == 'Payments':
                # Function variables
                PaymentsID = StringVar()
                ReservationsID = StringVar()
                PaymentDate = StringVar()
                Amount = StringVar()
                PaymentMethod = StringVar()
                PaymentStatus = StringVar()

                def iExit():
                    iExit = tkinter.messagebox.askyesno("CAR RENTAL", "Confirm if you want to exit")
                    if iExit:
                        self.destroy()
                        return

                def Reset():
                    PaymentsID.set("")
                    ReservationsID.set("")
                    PaymentDate.set("")
                    Amount.set("")
                    PaymentMethod.set("")
                    PaymentStatus.set("")

                    self.ent1.delete(0, END)
                    self.ent2.delete(0, END)
                    self.ent3.delete(0, END)
                    self.ent4.delete(0, END)
                    self.ent5.delete(0, END)
                    self.ent6.delete(0, END)


                def addData():
                    if PaymentsID.get() == "":
                        tkinter.messagebox.showerror("CAR RENTAL", "Enter correct Details")
                    else:
                        sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                        cur = sqlCon.cursor()
                        cur.execute("INSERT INTO Payments VALUES(%s,%s,%s,%s,%s,%s)", (

                            PaymentsID.get(),
                            ReservationsID.get(),
                            PaymentDate.get(),
                            Amount.get(),
                            PaymentMethod.get(),
                            PaymentStatus.get()
                        ))
                        sqlCon.commit()
                        dispData()
                        sqlCon.close()
                        Reset()

                        tkinter.messagebox.showinfo("CAR RENTAL", "Record Entered Succesfully")

                def dispData():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()

                    cur.execute("SELECT * FROM Payments")
                    dispList = []

                    for i in cur:
                        dispList.append(i)

                    if dispList == []:
                        tkinter.messagebox.showinfo("CAR RENTAL", "NO RECORDS TO DISPLAY")

                    else:
                        records.delete(*records.get_children())
                        for row in dispList:
                            records.insert('', END, values=row)

                    sqlCon.commit()
                    sqlCon.close()

                def dispData1():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute("SELECT * FROM Payments")
                    dispList = []

                    for i in cur:
                        dispList.append(i)

                    records.delete(*records.get_children())
                    for row in dispList:
                        records.insert('', END, values=row)

                    sqlCon.commit()
                    sqlCon.close()

                def Infoo(e):
                    viewInfo = records.focus()
                    learnData = records.item(viewInfo)
                    row = learnData['values']
                    PaymentsID.set(row[0])
                    ReservationsID.set(row[1])
                    PaymentDate.set(row[2])
                    Amount.set(row[3])
                    PaymentMethod.set(row[4])
                    PaymentStatus.set(row[5])

                def update():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute("UPDATE Payments SET ReservationsID = %s, PaymentDate = %s, Amount = %s, PaymentMethod = %s, PaymentStatus = %s WHERE PaymentsID = %s", (

                        ReservationsID.get(),
                        PaymentDate.get(),
                        Amount.get(),
                        PaymentMethod.get(),
                        PaymentStatus.get(),
                        PaymentsID.get(),
                    ))
                    sqlCon.commit()
                    dispData()
                    sqlCon.close()
                    Reset()

                    tkinter.messagebox.showinfo("CAR RENTAL", "Record Updated Succesfully")

                def deleteRecords():
                    sqlCon = pymysql.connect(host="localhost",port=808, user="root", password="", database="car_rental")
                    cur = sqlCon.cursor()
                    cur.execute("DELETE FROM Payments WHERE PaymentsID = %s", PaymentsID.get())
                    sqlCon.commit()
                    dispData1()
                    sqlCon.close()
                    Reset()

                    tkinter.messagebox.showinfo("CAR RENTAL", "Record Deleted Succesfully")

                # GUI elements
                self.lb1 = customtkinter.CTkLabel(master=self.frame_mid, text="Payments ID")
                self.lb1.grid(row=1, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent1 = customtkinter.CTkEntry(master=self.frame_mid, width=150, textvariable=PaymentsID)
                self.ent1.grid(row=1, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb2 = customtkinter.CTkLabel(master=self.frame_mid, text="Reservations ID")
                self.lb2.grid(row=2, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent2 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=ReservationsID)
                self.ent2.grid(row=2, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb3 = customtkinter.CTkLabel(master=self.frame_mid, text="Payment Date")
                self.lb3.grid(row=3, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent3 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=PaymentDate)
                self.ent3.grid(row=3, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb4 = customtkinter.CTkLabel(master=self.frame_mid, text="Amount")
                self.lb4.grid(row=4, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent4 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=Amount)
                self.ent4.grid(row=4, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb5 = customtkinter.CTkLabel(master=self.frame_mid, text="Payment Method")
                self.lb5.grid(row=5, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent5 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=PaymentMethod)
                self.ent5.grid(row=5, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                self.lb6 = customtkinter.CTkLabel(master=self.frame_mid, text="Payment Status")
                self.lb6.grid(row=6, column=0, columnspan=1, pady=5, padx=5, sticky="")
                self.ent6 = customtkinter.CTkEntry(master=self.frame_mid, width=44, textvariable=PaymentStatus)
                self.ent6.grid(row=6, column=1, columnspan=2, pady=5, padx=5, sticky="we")

                # To view the tables
                records = ttk.Treeview(master=self.frame_mid1, height=14, columns=("PaymentsID", "ReservationsID", "PaymentDate", "Amount", "PaymentMethod", "PaymentStatus"), xscrollcommand=scrolly.set)
                scrolly.pack(side=RIGHT, fill=Y)

                # Columns and their headings
                records.heading("PaymentsID", text="Payments ID")
                records.heading("ReservationsID", text="Reservations ID")
                records.heading("PaymentDate", text="Payment Date")
                records.heading("Amount", text="Amount")
                records.heading("PaymentMethod", text="Payment Method")
                records.heading("PaymentStatus", text="Payment Status")

                records['show'] = 'headings'

                records.column("PaymentsID", width=100)
                records.column("ReservationsID", width=100)
                records.column("PaymentDate", width=100)
                records.column("Amount", width=100)
                records.column("PaymentMethod", width=100)
                records.column("PaymentStatus", width=100)

                records.pack(fill=BOTH, expand=1)
                records.bind("<ButtonRelease-1>", Infoo)

                self.label_1 = customtkinter.CTkLabel(master=self.frame_left, text="Select View")
                self.label_1.grid(row=0, column=4, columnspan=1, pady=20, padx=10, sticky="")

                self.btn1 = customtkinter.CTkButton(master=self.frame_right, text="Add Data", command=addData)
                self.btn1.grid(row=1, column=4, pady=10, padx=20)
                self.btn2 = customtkinter.CTkButton(master=self.frame_right, text="Display", command=dispData)
                self.btn2.grid(row=2, column=4, pady=10, padx=20)
                self.btn3 = customtkinter.CTkButton(master=self.frame_right, text="Update", command=update)
                self.btn3.grid(row=3, column=4, pady=10, padx=20)
                self.btn4 = customtkinter.CTkButton(master=self.frame_right, text="Delete", command=deleteRecords)
                self.btn4.grid(row=4, column=4, pady=10, padx=20)

                
        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left, values=["VehicleCategory", "Locations", "Customers", "Cars", "Reservations", "Payments"], command = selectTable)
        self.optionmenu_1.set("Select View")
        self.optionmenu_1.grid(row=2, column=0, pady=10, padx=20, sticky="w")

app = first()
app.mainloop()