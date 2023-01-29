import customtkinter
from tkinter import *
import os
import mysql.connector
from time import sleep
import random
from datetime import date
from datetime import datetime
from os import mkdir

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("700x600")

root.title("Banco Digital")

def main():
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="usuarios"
    )
    
    mycursor = mydb.cursor()
    
    def login():
        
        name = entry1.get()
        password = entry2.get()
        
        mycursor.execute("SELECT * from users WHERE nombre = %s", (name,))
        myresult = mycursor.fetchall()
        for x in myresult:
            nombre = x[0]
            contra = x[3]
            if (name == nombre) and (password == contra):
                chequeado = checkbox.get()
                if (chequeado == 1):
                    mycursor.execute("UPDATE users set remember='1' where nombre= '"+nombre+"'")
                    mydb.commit()
                    mycursor.execute("UPDATE users set loged='1' where nombre= '"+nombre+"'")
                    mydb.commit()
                    mainPage()
                    label3.pack_forget()
                    entry1.pack_forget()
                    entry2.pack_forget()
                    checkbox.pack_forget()
                    button.pack_forget()
                    switch.pack_forget()  
                else:
                    mycursor.execute("UPDATE users set remember='0' where nombre= '"+nombre+"'")
                    mydb.commit()
                    mycursor.execute("UPDATE users set loged='1' where nombre= '"+nombre+"'")
                    mydb.commit()
                    mainPage()
                    label3.pack_forget()
                    entry1.pack_forget()
                    entry2.pack_forget()
                    checkbox.pack_forget()
                    button.pack_forget()
                    switch.pack_forget()
            else:
                label3.configure(text="Wrong user or password", font=('Roboto',20,'bold'),text_color='red')
                label3.pack(pady=12, padx=10)
        if (name == "admin") and (password == "root"):
            label3.pack_forget()
            entry1.pack_forget()
            entry2.pack_forget()
            checkbox.pack_forget()
            button.pack_forget()
            switch.pack_forget()
            adminmode()
    
    def newAccount():
        button.configure(text="Sign in", command=createAccount)
        
        checkbox.pack_forget()
        label3.pack_forget()
        
        switched = switch.get()
        
        if (switched == 1):
            label2.pack_forget()
            label3.pack_forget()
            entry3.pack(pady=12, padx=10)
            entry4.pack(pady=12, padx=10)
            entry5.pack(pady=12, padx=10)
            button.pack_forget()
            button.pack(pady=12, padx=10)
            
            switch.pack_forget()
            switch.pack(pady=12, padx=10)
        else:
            label2.pack_forget()
            label3.pack_forget()
            entry3.pack_forget()
            entry4.pack_forget()
            entry5.pack_forget()
            button.configure(text="Login", command=login)
            switch.pack_forget()
            checkbox.pack(pady=12, padx=10)
            switch.pack(pady=12, padx=10)
            
    def createAccount():
        registerName = entry1.get()
        registerPassword = entry2.get()
        registerDNI = entry3.get()
        registerEmail = entry4.get()
        registerTelefono = entry5.get()
        newCBU = random.randint(0,100000000)
        
        mycursor.execute("SELECT * from users WHERE nombre = %s", (registerName,))
        myresult = mycursor.fetchall()
        for x in myresult:
            nombre = x[0]
        
        try:
            nombre
        except NameError:
            if (registerName == "admin"):
                label2.configure(text="That name is not avaible")
                label2.pack(pady=35, padx=10)
            else:
                mycursor.execute("INSERT INTO users(nombre, dni, telefono, password, email, saldo, cbu, loged) VALUES('"+registerName+"','"+registerDNI+"','"+registerTelefono+"','"+registerPassword+"','"+registerEmail+"','1000','"+str(newCBU)+"', '0')")
                mydb.commit()
                label2.configure(text="Account created succesfuly")
                label2.pack(pady=35, padx=10)
        else:
            label2.configure(text="That name is not avaible")
            label2.pack(pady=35, padx=10)
            entry1.focus()
            
        
        
    def logout():
        
        mycursor.execute("SELECT * from users WHERE loged = 1")
        myresult = mycursor.fetchall()
        for x in myresult:
            nombre = x[0]
            mycursor.execute("UPDATE users set loged='0' where nombre= '"+nombre+"'")
            mydb.commit()
            mycursor.execute("UPDATE users set remember='0' where nombre= '"+nombre+"'")
            mydb.commit()
            
            
        button.pack_forget()
        button2.pack_forget()
        button3.pack_forget()
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()
        
        button.configure(text="Login", command=login)
        
        label2.pack_forget()
        label3.pack_forget()
        
        entry1.pack(pady=12, padx=10)
        entry2.pack(pady=12, padx=10)
        button.pack(pady=12, padx=10)
        checkbox.pack(pady=12, padx=10)
        switch.pack(pady=12, padx=10)
        
        entry1.configure(placeholder_text="User")
        entry1.delete(0, 'end')
        entry1.insert(0, "")
        entry1.configure(placeholder_text="User")
        entry2.configure(placeholder_text="Password")
        entry2.delete(0, 'end')
        entry2.insert(0, "")
        entry2.configure(placeholder_text="Password")
        root.focus()
    
    def consultarSaldo():
        
        mycursor.execute("SELECT * from users WHERE loged = 1")
        myresult = mycursor.fetchall()
        for x in myresult:
            saldo = x[5]
        
        label2.configure(text="Your money is: $" + str(saldo), font=('Roboto',24,'bold'),text_color='white')
        label2.pack(pady=12, padx=10)
        button2.pack_forget()
        button2.configure(text="Return", command=mainPage)
        button2.pack(pady=12, padx=10)
        button3.pack_forget()
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()
        
    def ingresarDinero():
        
        label2.configure(text="Deposit money", font=('Roboto',20,'bold'),text_color='white')
        label2.pack(pady=12, padx=10)
        entry1.configure(placeholder_text="Amount")
        entry1.delete(0, 'end')
        entry1.insert(0, "")
        root.focus()
        entry1.configure(placeholder_text="Amount")
        entry1.pack(pady=12, padx=10)
        button2.pack_forget()
        button2.configure(text="Deposit", command=ingreso)
        button2.pack(pady=12, padx=10)
        button3.pack_forget()
        button3.configure(text="Return", command=mainPage)
        button3.pack(pady=12, padx=10)
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()
        
    
    def ingreso():
        monto = int(entry1.get())
        mycursor.execute("SELECT * from users WHERE loged = 1")
        myresult = mycursor.fetchall()
        for x in myresult:
            saldo = x[5]
            nombre = x[0]
        mycursor.execute("UPDATE users set saldo='"+str(saldo+monto)+"' where nombre= '"+nombre+"'")
        mydb.commit()
        label3.configure(text="Your money was deposited, your current money is: $" +str(saldo+monto), font=('Roboto',20,'bold'),text_color='white')
        label3.pack(pady=12, padx=10)
    
    def retirarDinero():
        
        label2.configure(text="Withdraw money", font=('Roboto',20,'bold'),text_color='white')
        label2.pack(pady=12, padx=10)
        entry1.configure(placeholder_text="Amount")
        entry1.delete(0, 'end')
        entry1.insert(0, "")
        root.focus()
        entry1.configure(placeholder_text="Amount")
        entry1.pack(pady=12, padx=10)
        button2.pack_forget()
        button2.configure(text="Withdraw", command=retiro)
        button2.pack(pady=12, padx=10)
        button3.pack_forget()
        button3.configure(text="Return", command=mainPage)
        button3.pack(pady=12, padx=10)
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()

    def retiro():
        monto = int(entry1.get())
        mycursor.execute("SELECT * from users WHERE loged = 1")
        myresult = mycursor.fetchall()
        for x in myresult:
            saldo = x[5]
            nombre = x[0]
        if (saldo-monto < -20000):
            label3.configure(text="Your debt limit was reached: $-20.000", font=('Roboto',20,'bold'),text_color='white')
            label3.pack(pady=12, padx=10)
            button.pack_forget()
            button2.pack_forget()
        else:
            mycursor.execute("UPDATE users set saldo='"+str(saldo-monto)+"' where nombre= '"+nombre+"'")
            mydb.commit()
            label3.configure(text="Your money was withdrawed, your current money is: $" +str(saldo-monto), font=('Roboto',20,'bold'),text_color='white')
            label3.pack(pady=12, padx=10)

        
    def transferencia():
        label2.configure(text="Transfer money", font=('Roboto',20,'bold'),text_color='white')
        label2.pack(pady=12, padx=10)
        entry1.configure(placeholder_text="Amount")
        entry1.delete(0, 'end')
        entry1.insert(0, "")
        root.focus()
        entry1.configure(placeholder_text="Amount")
        entry1.pack(pady=12, padx=10)
        entry2.configure(placeholder_text="CBU", show="")
        entry2.delete(0, 'end')
        entry2.insert(0, "")
        root.focus()
        entry2.configure(placeholder_text="CBU")
        entry2.pack(pady=12, padx=10)
        button2.pack_forget()
        button2.configure(text="Transfer", command=transferir)
        button2.pack(pady=12, padx=10)
        button3.pack_forget()
        button3.configure(text="Return", command=mainPage)
        button3.pack(pady=12, padx=10)
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()
        
    def transferir():
        monto = int(entry1.get())
        cbuRecibe = int(entry2.get())
        mycursor.execute("SELECT * from users WHERE loged = 1")
        myresult = mycursor.fetchall()
        for x in myresult:
            saldo = x[5]
            nombre = x[0]
        
        def crearDeuda():
            mycursor.execute("SELECT * from users WHERE loged = 1")
            myresult = mycursor.fetchall()
            for x in myresult:
                saldo = x[5]
                nombre = x[0]
                
            if (saldo-monto < -20000):
                label3.configure(text="Your debt limit was reached: $-20.000", font=('Roboto',20,'bold'),text_color='white')
                label3.pack(pady=12, padx=10)
                button.pack_forget()
                button2.pack_forget()
            else:
                mycursor.execute("SELECT * from users WHERE cbu = %s", (cbuRecibe,))
                myresult = mycursor.fetchall()
                for x in myresult:
                    nombreRecibe = x[0]
                    saldo = x[5]
                mycursor.execute("UPDATE users set saldo='"+str(saldo+monto)+"' where cbu= '"+str(cbuRecibe)+"'")
                mydb.commit()
                mycursor.execute("SELECT * from users WHERE loged = 1")
                myresult = mycursor.fetchall()
                for x in myresult:
                    saldo = x[5]
                    cbuEnvia = x[6]
                    nombreEnvia = x[0]
                mycursor.execute("UPDATE users set saldo='"+str(saldo-monto)+"' where nombre= '"+str(nombreEnvia)+"'")
                mydb.commit()
                
                
                label3.configure(text="Money transfered, your currently money is: $" +str(saldo-monto), font=('Roboto',20,'bold'),text_color='white')
                label3.pack(pady=12, padx=10)
                dt = datetime.now()       
                upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                digits = '0123456789'
                upper, nums, = True, True,
                all = ''
                if upper:
                    all += upper_letter
                if nums:
                    all += digits
                    length = 12
                    for x in range(1):
                        nitro = ''.join(random.sample(all, length))
                today = date.today()
                mycursor.execute("INSERT INTO transacciones(id, monto, emisor, remitente, date) VALUES('"+str(nitro)+"','"+str(monto)+"','"+str(cbuEnvia)+"','"+str(cbuRecibe)+"','"+str(today)+"')")
                mydb.commit()
                if (os.path.isdir("Receipts")):
                    print("")
                else:
                    os.mkdir("Receipts")
                    
                file = open("Receipts\Transfer - "+str(nitro)+".txt", "w")
                file.write(os.linesep)
                file.write("# Digital Bank #")
                file.write("\n")
                file.write("\n")
                file.write("\n")
                file.write(os.linesep)
                file.write("" + str(dt))
                file.write("\n")
                file.write("\n")
                file.write(os.linesep)
                file.write("Transfer from: " + nombreEnvia + " to "+ nombreRecibe)
                file.write(os.linesep)
                file.write("\n")
                file.write("Transfer name:" + str(cbuEnvia) + " to "+ str(cbuRecibe))
                file.write("\n")
                file.write("\n")
                file.write("Amount: $" + str(monto))
                file.write(os.linesep)
                file.write("\n")
                file.write("Operation number: #" + nitro)
                file.write("\n")
                file.write("\n")
                file.write("Digital Bank developed by Rusher")
                file.write("\n")
                file.write("\n")
                file.write("\n")
                file.write("\n")
                file.write("\n")
                file.write("\n")
                file.write("\n")
                file.write("\n")
                file.write("\n")
                file.write("     Thank you for trusting digital bank")
                file.close()
                button4.pack_forget()
                button5.configure(text="Return", command=mainPage)
                button5.pack(pady=12, padx=10)

        if (saldo < monto):
            if ((saldo < -20000) or (saldo-monto < -20000)):
                label3.configure(text="Your debt limit was reached: $-20.000", font=('Roboto',20,'bold'),text_color='white')
                label3.pack(pady=12, padx=10)
                button.pack_forget()
                button2.pack_forget()
            else:
                entry1.pack_forget()
                entry2.pack_forget()
                
                label3.pack_forget()
                button4.pack_forget()
                button5.pack_forget()
                label3.pack(pady=12, padx=10)
                label3.configure(text="Your money is insufficient, do you want to get into debt about: $-" + str(monto-saldo) + "?", font=('Roboto',20,'bold'),text_color='white')
                
                button.pack_forget()
                button2.pack_forget()
                button3.pack_forget()
                button4.pack_forget()
                button5.pack_forget()
                button4.configure(text="Yes", command=crearDeuda)
                button5.configure(text="No", command=mainPage)
                button4.pack(pady=12, padx=10)
                button5.pack(pady=12, padx=10)
                label3.pack(pady=12, padx=10)
                
        else:
            mycursor.execute("SELECT * from users WHERE loged = 1")
            myresult = mycursor.fetchall()
            for x in myresult:
                saldo = x[5]
                cbuEnvia = x[6]
                nombreEnvia = x[0]
            mycursor.execute("UPDATE users set saldo='"+str(saldo-monto)+"' where nombre= '"+nombre+"'")
            mydb.commit()
            dt = datetime.now()       
            upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            digits = '0123456789'
            upper, nums, = True, True,
            all = ''
            if upper:
                all += upper_letter
            if nums:
                all += digits
                length = 12
                for x in range(1):
                    nitro = ''.join(random.sample(all, length))
            today = date.today()
            mycursor.execute("SELECT * from users WHERE cbu = %s", (cbuRecibe,))
            myresult = mycursor.fetchall()
            for x in myresult:
                nombreRecibe = x[0]
                saldo = x[5]
            mycursor.execute("SELECT * from users WHERE loged = 1")
            myresult = mycursor.fetchall()
            for x in myresult:
                saldo = x[5]
                cbuEnvia = x[6]
                nombreEnvia = x[0]
            mycursor.execute("INSERT INTO transacciones(id, monto, emisor, remitente, date) VALUES('"+str(nitro)+"','"+str(monto)+"','"+str(cbuEnvia)+"','"+str(cbuRecibe)+"','"+str(today)+"')")
            mydb.commit()
            if (os.path.isdir("Receipts")):
                print("")
            else:
                os.mkdir("Receipts")
            file = open("Receipts\Transfer - "+str(nitro)+".txt", "w")
            file.write(os.linesep)
            file.write("# Digital Bank #")
            file.write("\n")
            file.write(os.linesep)
            file.write("" + str(dt))
            file.write("\n")
            file.write("\n")
            file.write(os.linesep)
            file.write("Transfer from: " + nombreEnvia + " to "+ nombreRecibe)
            file.write(os.linesep)
            file.write("\n")
            file.write("Transfer name:" + str(cbuEnvia) + " to "+ str(cbuRecibe))
            file.write("\n")
            file.write("\n")
            file.write("Amount: $" + str(monto))
            file.write(os.linesep)
            file.write("\n")
            file.write("Operation number: #" + nitro)
            file.write("\n")
            file.write("\n")
            file.write("Digital Bank developed by Rusher")
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("     Thank you for trusting digital bank")
            file.close()
            mycursor.execute("SELECT * from users WHERE loged = 1")
            myresult = mycursor.fetchall()
            for x in myresult:
                saldo = x[5]
                cbuEnvia = x[6]
                nombreEnvia = x[0]
            label3.configure(text="Money transfered, your currently money is: $" +str(saldo), font=('Roboto',20,'bold'),text_color='white')
            label3.pack(pady=12, padx=10)
            
            mycursor.execute("SELECT * from users WHERE cbu = %s", (cbuRecibe,))
            myresult = mycursor.fetchall()
            for x in myresult:
                nombre = x[0]
                saldo = x[5]
            mycursor.execute("UPDATE users set saldo='"+str(saldo+monto)+"' where cbu= '"+str(cbuRecibe)+"'")
            mydb.commit()
            
    def consultarDeudas():
        mycursor.execute("SELECT * from users WHERE loged = 1")
        myresult = mycursor.fetchall()
        for x in myresult:
            saldo = x[5]
        
        if (saldo < 0):
            label2.configure(text="Your debt is about: $" + str(saldo), font=('Roboto',24,'bold'),text_color='white')
            label2.pack(pady=12, padx=10)
            button2.pack_forget()
            button2.configure(text="Return", command=mainPage)
            button2.pack(pady=12, padx=10)
            button3.pack_forget()
            button4.pack_forget()
            button5.pack_forget()
            button6.pack_forget()
            button7.pack_forget()
            button8.pack_forget()            
        elif (saldo > 0):
            label2.configure(text="You haven't debts", font=('Roboto',24,'bold'),text_color='white')
            label2.pack(pady=12, padx=10)
            button2.pack_forget()
            button2.configure(text="Return", command=mainPage)
            button2.pack(pady=12, padx=10)
            button3.pack_forget()
            button4.pack_forget()
            button5.pack_forget()
            button6.pack_forget()
            button7.pack_forget()
            button8.pack_forget()
            
    def ajustes():
        entry1.pack_forget()
        entry2.pack_forget()
        button.pack_forget()
        checkbox.pack_forget()
        switch.pack_forget()
        label2.pack_forget()
        label3.pack_forget()
        
        button.pack_forget()
        button2.pack_forget()
        button3.pack_forget()
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()
        
        button2.configure(text="Change name", command=cambiarNombre)
        button2.pack(pady=12, padx=10)
        button3.configure(text="Change DNI", command=cambiarDNI)
        button3.pack(pady=12, padx=10)
        button4.configure(text="Change Tel number", command=cambiarTelefono)
        button4.pack(pady=12, padx=10)
        button5.configure(text="Change password", command=cambiarPassword)
        button5.pack(pady=12, padx=10)
        button6.configure(text="Change email", command=cambiarEmail)
        button6.pack(pady=12, padx=10)
        button7.configure(text="Close your account", command=cerrarCuenta)
        button7.pack(pady=12, padx=10)
        button8.configure(text="Return", command=mainPage)
        button8.pack(pady=12, padx=10)
        
    def cambiarNombre():
        
        def cambiandoNombre():
            newName = entry1.get()
            mycursor.execute("SELECT * from users WHERE loged = 1")
            myresult = mycursor.fetchall()
            for x in myresult:
                nombre = x[0]
            
            mycursor.execute("UPDATE users set nombre='"+newName+"' where nombre= '"+nombre+"'")
            mydb.commit()
            label3.configure(text="Your name was changed, your new name is: " +str(newName), font=('Roboto',20,'bold'),text_color='white')
            label3.pack(pady=12, padx=10)
        
        label2.configure(text="Change name", font=('Roboto',20,'bold'),text_color='white')
        label2.pack(pady=12, padx=10)
        entry1.configure(placeholder_text="New name")
        entry1.delete(0, 'end')
        entry1.insert(0, "")
        root.focus()
        entry1.configure(placeholder_text="New name")
        entry1.pack(pady=12, padx=10)
        button2.pack_forget()
        button2.configure(text="Confirm", command=cambiandoNombre)
        button2.pack(pady=12, padx=10)
        button3.pack_forget()
        button3.configure(text="Return", command=ajustes)
        button3.pack(pady=12, padx=10)
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()
            
                
                
                
    def cambiarDNI():
        
        def cambiandoDNI():
            newDNI = entry1.get()
            mycursor.execute("SELECT * from users WHERE loged = 1")
            myresult = mycursor.fetchall()
            for x in myresult:
                nombre = x[0]
            
            mycursor.execute("UPDATE users set dni='"+newDNI+"' where nombre= '"+nombre+"'")
            mydb.commit()
            label3.configure(text="Your DNI was changed succesfully, your new DNI is: " +str(newDNI), font=('Roboto',20,'bold'),text_color='white')
            label3.pack(pady=12, padx=10)
            
        label2.configure(text="Cambio de DNI", font=('Roboto',20,'bold'),text_color='white')
        label2.pack(pady=12, padx=10)
        entry1.configure(placeholder_text="New DNI")
        entry1.delete(0, 'end')
        entry1.insert(0, "")
        root.focus()
        entry1.configure(placeholder_text="New DNI")
        entry1.pack(pady=12, padx=10)
        button2.pack_forget()
        button2.configure(text="Confirm", command=cambiandoDNI)
        button2.pack(pady=12, padx=10)
        button3.pack_forget()
        button3.configure(text="Return", command=ajustes)
        button3.pack(pady=12, padx=10)
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()
        
    def cambiarTelefono():
        
        def cambiandoTel():
            newTel = entry1.get()
            mycursor.execute("SELECT * from users WHERE loged = 1")
            myresult = mycursor.fetchall()
            for x in myresult:
                nombre = x[0]
            
            mycursor.execute("UPDATE users set telefono='"+newTel+"' where nombre= '"+nombre+"'")
            mydb.commit()
            label3.configure(text="Telephone number was changed, your new telephone number is: " +str(newTel), font=('Roboto',20,'bold'),text_color='white')
            label3.pack(pady=12, padx=10)
            
        label2.configure(text="Telephone number change", font=('Roboto',20,'bold'),text_color='white')
        label2.pack(pady=12, padx=10)
        entry1.configure(placeholder_text="New telephone number")
        entry1.delete(0, 'end')
        entry1.insert(0, "")
        root.focus()
        entry1.configure(placeholder_text="New telephone number")
        entry1.pack(pady=12, padx=10)
        button2.pack_forget()
        button2.configure(text="Confirm", command=cambiandoTel)
        button2.pack(pady=12, padx=10)
        button3.pack_forget()
        button3.configure(text="Return", command=ajustes)
        button3.pack(pady=12, padx=10)
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()     
    
    def cambiarPassword():
        
        def cambiandoPassword():
            newPass = entry1.get()
            mycursor.execute("SELECT * from users WHERE loged = 1")
            myresult = mycursor.fetchall()
            for x in myresult:
                nombre = x[0]
            
            mycursor.execute("UPDATE users set password='"+newPass+"' where nombre= '"+nombre+"'")
            mydb.commit()
            label3.configure(text="Password was changed succesfully", font=('Roboto',20,'bold'),text_color='white')
            label3.pack(pady=12, padx=10)
            
        label2.configure(text="Password change", font=('Roboto',20,'bold'),text_color='white')
        label2.pack(pady=12, padx=10)
        entry1.configure(placeholder_text="New password")
        entry1.delete(0, 'end')
        entry1.insert(0, "")
        root.focus()
        entry1.configure(placeholder_text="New password")
        entry1.pack(pady=12, padx=10)
        button2.pack_forget()
        button2.configure(text="Confirm", command=cambiandoPassword)
        button2.pack(pady=12, padx=10)
        button3.pack_forget()
        button3.configure(text="Return", command=ajustes)
        button3.pack(pady=12, padx=10)
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()  
         
    def cambiarEmail():
        
        def cambiandoEmail():
            newEmail = entry1.get()
            mycursor.execute("SELECT * from users WHERE loged = 1")
            myresult = mycursor.fetchall()
            for x in myresult:
                nombre = x[0]
            
            mycursor.execute("UPDATE users set password='"+newEmail+"' where nombre= '"+nombre+"'")
            mydb.commit()
            label3.configure(text="Email was changed succesfully, your new email is: " +str(newEmail), font=('Roboto',20,'bold'),text_color='white')
            label3.pack(pady=12, padx=10)
            
        label2.configure(text="Email change", font=('Roboto',20,'bold'),text_color='white')
        label2.pack(pady=12, padx=10)
        entry1.configure(placeholder_text="New email")
        entry1.delete(0, 'end')
        entry1.insert(0, "")
        root.focus()
        entry1.configure(placeholder_text="New email")
        entry1.pack(pady=12, padx=10)
        button2.pack_forget()
        button2.configure(text="Confirm", command=cambiandoEmail)
        button2.pack(pady=12, padx=10)
        button3.pack_forget()
        button3.configure(text="Return", command=ajustes)
        button3.pack(pady=12, padx=10)
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget() 
        
    def cerrarCuenta():

        def cerrandoCuenta():
            check = entry1.get()
            
            if (check == "confirm"):
                mycursor.execute("SELECT * from users WHERE loged = 1")
                myresult = mycursor.fetchall()
                for x in myresult:
                    nombre = x[0]
                
                mycursor.execute("DELETE from users WHERE nombre = %s", (nombre,))
                mydb.commit()
                
                logout()
            
        label2.configure(text="Cerrar cuenta", font=('Roboto',20,'bold'),text_color='white')
        label2.pack(pady=12, padx=10)
        entry1.configure(placeholder_text='Write: "confirm"')
        entry1.delete(0, 'end')
        entry1.insert(0, "")
        root.focus()
        entry1.configure(placeholder_text='Write: "confirm"')
        entry1.pack(pady=12, padx=10)
        button2.pack_forget()
        button2.configure(text="Confirm", command=cerrandoCuenta)
        button2.pack(pady=12, padx=10)
        button3.pack_forget()
        button3.configure(text="Return", command=ajustes)
        button3.pack(pady=12, padx=10)
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget() 

    def mainPage():
        entry1.pack_forget()
        entry2.pack_forget()
        button.pack_forget()
        checkbox.pack_forget()
        switch.pack_forget()
        label2.pack_forget()
        label3.pack_forget()
        
        button.pack_forget()
        button2.pack_forget()
        button3.pack_forget()
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()
        
        button2.configure(text="Consult money", command=consultarSaldo)
        button2.pack(pady=12, padx=10)
        button3.configure(text="Deposit money", command=ingresarDinero)
        button3.pack(pady=12, padx=10)
        button4.configure(text="Withdraw money", command=retirarDinero)
        button4.pack(pady=12, padx=10)
        button5.configure(text="Transfer money", command=transferencia)
        button5.pack(pady=12, padx=10)
        button6.configure(text="Consult debts", command=consultarDeudas)
        button6.pack(pady=12, padx=10)
        button7.configure(text="Account settings", command=ajustes)
        button7.pack(pady=12, padx=10)
        button8.configure(text="Log out", command=logout)
        button8.pack(pady=12, padx=10)
    
    def adminmode():
        mytxt.pack_forget()
        label3.pack_forget()
        entry1.pack_forget()
        button.pack_forget()
        button2.pack_forget()
        button3.pack_forget()
        label2.configure(text="Admin Panel")
        label2.pack(pady=12, padx=10)
        
        button.configure(text="Review transactions", command=revisandoT)
        button2.configure(text="Review Account movements", command=revisandoM)
        button3.configure(text="Salir", command=logout)
        
        button.pack(pady=12, padx=10)
        button2.pack(pady=12, padx=10)
        button3.pack(pady=12, padx=10)
        
    def revisandoT():
        button.pack_forget()
        def revision():
            operacion = entry1.get()
            mytxt.configure(state="normal", height=100)
            mytxt.delete('0.0', END)
            mycursor.execute("SELECT * from transacciones WHERE id = %s", (str(operacion),))
            myresult = mycursor.fetchall()
            for x in myresult:
                monto = x[1]
                emisor = x[2]
                remitente = x[3]
                dia = x[4]
            mytxt.pack()
            mytxt.insert("0.0", "Operation number: #" + str(operacion) + "\nMonto: $"+ str(monto) + "\nCBU Emisor: "+ str(emisor) + "\nCBU Receptor: " + str(remitente) + "\nFecha: "+ str(dia))
            mytxt.configure(state="disabled", height=100)
            
        label2.configure(text="Transactions revision", font=('Roboto',20,'bold'),text_color='white')
        label2.pack(pady=12, padx=10)
        entry1.configure(placeholder_text="Operation number")
        entry1.delete(0, 'end')
        entry1.insert(0, "")
        root.focus()
        entry1.configure(placeholder_text="Operation number")
        entry1.pack(pady=12, padx=10)
        button2.pack_forget()
        button2.configure(text="Search", command=revision)
        button2.pack(pady=12, padx=10)
        button3.pack_forget()
        button3.configure(text="Return", command=adminmode)
        button3.pack(pady=12, padx=10)
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()
    
    def revisandoM():
        button.pack_forget()
        def revisionM():
            cbu = entry1.get()
            mytxt.configure(state="normal", height=190)
            mytxt.delete('0.0', END)
            mycursor.execute("SELECT * from transacciones WHERE emisor = %s", (str(cbu),))
            myresult = mycursor.fetchall()
            for x in myresult:
                id = x[0]
                monto = x[1]
                emisor = x[2]
                remitente = x[3]
                dia = x[4]
                mytxt.pack()
                mytxt.insert("0.0", "Operation number: #" + str(id) + "\nAmount: $"+ str(monto) + "\nCBU from: "+ str(emisor) + "\nCBU to: " + str(remitente) + "\nDate: "+ str(dia) + "\n\n")  
            mytxt.configure(state="disabled", height=190)
            
            mytxt.configure(state="normal", height=190)
            mycursor.execute("SELECT * from transacciones WHERE remitente = %s", (str(cbu),))
            myresult = mycursor.fetchall()
            for x in myresult:
                id = x[0]
                monto = x[1]
                emisor = x[2]
                remitente = x[3]
                dia = x[4]
                mytxt.pack()
                mytxt.insert("0.0", "Operation number: #" + str(id) + "\nAmount: $"+ str(monto) + "\nCBU from: "+ str(emisor) + "\nCBU to: " + str(remitente) + "\nDate: "+ str(dia) + "\n\n")  
            mytxt.configure(state="disabled")
            
        label2.configure(text="Account movements revision", font=('Roboto',20,'bold'),text_color='white')
        label2.pack(pady=12, padx=10)
        entry1.configure(placeholder_text="Operation number")
        entry1.delete(0, 'end')
        entry1.insert(0, "")
        root.focus()
        entry1.configure(placeholder_text="Operation number")
        entry1.pack(pady=12, padx=10)
        button2.pack_forget()
        button2.configure(text="Search", command=revisionM)
        button2.pack(pady=12, padx=10)
        button3.pack_forget()
        button3.configure(text="Return", command=adminmode)
        button3.pack(pady=12, padx=10)
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=25, padx=30, fill="both", expand=True)
    
    label = customtkinter.CTkLabel(master=frame, text="Digital Bank", font=('Roboto',30,'bold'))
    label.pack(pady=35, padx=10)
    
    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="User")
    
    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    
    entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="DNI")
    
    entry4 = customtkinter.CTkEntry(master=frame, placeholder_text="Email")
    
    entry5 = customtkinter.CTkEntry(master=frame, placeholder_text="Telephone number")
    
    button = customtkinter.CTkButton(master=frame, text="Login", command=login)
    
    button2 = customtkinter.CTkButton(master=frame, text="Consult money", command=consultarSaldo)
    button3 = customtkinter.CTkButton(master=frame, text="Deposit money", command=ingresarDinero)
    button4 = customtkinter.CTkButton(master=frame, text="Withdraw money", command=retirarDinero)
    button5 = customtkinter.CTkButton(master=frame, text="Transfer money", command=transferencia)
    button6 = customtkinter.CTkButton(master=frame, text="Consult debts", command=consultarDeudas)
    button7 = customtkinter.CTkButton(master=frame, text="Acount settings")
    button8 = customtkinter.CTkButton(master=frame, text="Log out", command=logout)
    
    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
    
    switch = customtkinter.CTkSwitch(master=frame, text="Haven't you an account?", command=newAccount)
    
    label2 = customtkinter.CTkLabel(master=frame, text="Account created succesfuly", font=('Roboto',14,'bold'))
    
    label3 = customtkinter.CTkLabel(master=frame, text="Account created succesfuly", font=('Roboto',14,'bold'))
    mytxt = customtkinter.CTkTextbox(master=frame, width=400, height=190)
    
    mycursor.execute("SELECT * from users WHERE remember = 1")
    myresult = mycursor.fetchall()
    for x in myresult:
        nombre = x[0]
        recordar = x[7]
        
    try:
        recordar
    except NameError:
        entry1.pack(pady=12, padx=10)
        entry2.pack(pady=12, padx=10)
        button.pack(pady=12, padx=10)
        checkbox.pack(pady=12, padx=10)
        switch.pack(pady=12, padx=10)
    else:
        mainPage()
    
    root.mainloop()

main()