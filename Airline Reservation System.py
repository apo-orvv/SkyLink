import os
import smtplib
sem=os.environ.get('air_email')
spw=os.environ.get('air_passwd')
import mysql.connector as mc
from datetime import datetime,timedelta
from dateutil.parser import parse
import time
dic={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
ani=mc.connect(host='localhost',user='root',passwd='Anishasanabhi@123',database='anirudh')
crs=ani.cursor()
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tm
import random
d1=[]
x_=''
aflna=[]
alstps=[]
def menu_edit():
    global men
    men=tk.Menu(win)
    edit=tk.Menu(men,tearoff=0)
    edit.add_command(label="Edit Flight",command=lambda:official_login('eflight'))
    edit.add_command(label="Add Flight",command=lambda:official_login('aflight'))
    edit.add_command(label="Add/Edit Fare",command=lambda:official_login('aefare'))
    edit.add_command(label="Add/Edit Airport",command=lambda:official_login('aeairport'))
    men.add_cascade(label='Add - Edit',menu=edit)
    for separator in range(45):
        men.add_separator()
    men.add_command(label='Login',underline=0,command=cancel_tickets_blog)
    win.config(menu=men)
def search_flight():
    global d1,aflna,x_ 
    tr.delete(*tr.get_children())
    c=e3_3.get()
    b=e3_2.get()
    a=e3_1.get()
    if int(b)>12 or int(a)>31 or int(c)>ny+5:
        tm.showerror('Error','Date is Incorrect as per DD-MM-YYYY Format')
    else:
        x=datetime.date(datetime(int(c),int(b),int(a)))
        x_=x
        if x<nx:
            tm.showerror('Error',"Can't book ticket in PAST!")
        else:
            y=x.strftime('%w')
            day=dic[int(y)]
            if x==nx:
                if aflna!=[] and alstps!=[]:
                    if len(alstps)==1 and len(aflna)==1:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND Departure>'{}' AND FLIGHT_NAME IN ('{}') AND STOPS IN ('{}');".format(e1.get(),e2.get(),day,nt,aflna[0],alstps[0]))
                    elif len(aflna)==1:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND Departure>'{}' AND FLIGHT_NAME IN ('{}') AND STOPS IN {};".format(e1.get(),e2.get(),day,nt,aflna[0],tuple(alstps)))
                    elif len(alstps)==1:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND Departure>'{}' AND FLIGHT_NAME IN {} AND STOPS IN ('{}');".format(e1.get(),e2.get(),day,nt,tuple(aflna),alstps[0]))
                    else:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND Departure>'{}' AND FLIGHT_NAME IN {} AND STOPS IN {};".format(e1.get(),e2.get(),day,nt,tuple(aflna),tuple(alstps)))
                elif aflna!=[] and alstps==[]:
                    if len(aflna)==1:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND Departure>'{}' AND FLIGHT_NAME IN ('{}');".format(e1.get(),e2.get(),day,nt,aflna[0]))
                    else:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND Departure>'{}' AND FLIGHT_NAME IN {};".format(e1.get(),e2.get(),day,nt,tuple(aflna)))
                elif alstps!=[] and aflna==[]:
                    if len(alstps)==1:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND Departure>'{}' AND STOPS IN ('{}');".format(e1.get(),e2.get(),day,nt,alstps[0]))
                    else:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND Departure>'{}' AND STOPS IN {};".format(e1.get(),e2.get(),day,nt,tuple(alstps)))
                else:
                    crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND Departure>'{}';".format(e1.get(),e2.get(),day,nt))
            else:
                if aflna!=[] and alstps!=[]:
                    if len(alstps)==1 and len(aflna)==1:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND FLIGHT_NAME IN ('{}') AND STOPS IN ('{}');".format(e1.get(),e2.get(),day,aflna[0],alstps[0]))
                    elif len(aflna)==1:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND FLIGHT_NAME IN ('{}') AND STOPS IN {};".format(e1.get(),e2.get(),day,aflna[0],tuple(alstps)))
                    elif len(alstps)==1:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND FLIGHT_NAME IN {} AND STOPS IN ('{}');".format(e1.get(),e2.get(),day,tuple(aflna),alstps[0]))
                    else:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND FLIGHT_NAME IN {} AND STOPS IN {};".format(e1.get(),e2.get(),day,tuple(aflna),tuple(alstps)))
                elif aflna!=[] and alstps==[]:
                    if len(aflna)==1:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND FLIGHT_NAME IN ('{}');".format(e1.get(),e2.get(),day,aflna[0]))
                    else:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND FLIGHT_NAME IN {};".format(e1.get(),e2.get(),day,tuple(aflna)))
                elif alstps!=[] and aflna==[]:
                    if len(alstps)==1:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND STOPS IN ('{}');".format(e1.get(),e2.get(),day,alstps[0]))
                    else:
                        crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}' AND STOPS IN {};".format(e1.get(),e2.get(),day,tuple(alstps)))
                else:
                    crs.execute("SELECT Flight_No,Flight_Name,airplanes.from,airplanes.to,Departure,Arrival,Flight_Duration,Stops FROM airplanes WHERE airplanes.from='{}' AND airplanes.to='{}' AND airplanes.day='{}'".format(e1.get(),e2.get(),day))
            d=crs.fetchall()
            d1=d
            if d==[]:
                tm.showinfo('Information','Sorry, no Flights Found')
            for i in d:
                tr.insert('',1,text=i[0],values=i[1:])
mpd=[]
pd=[]
tf=0
gt=0
blog_cei=''
blog_cpw=''
def cancellation_policy(w):
    global can_pol,canp
    if can_pol==0:
        canp=tk.Toplevel(w)
        canp.geometry("900x90")
        canp.iconbitmap('airplane.ico')
        canp.title('Cancellation Policy')
        canpol=tk.StringVar()
        c_policy=tk.Text(canp)
        c_policy.insert(1.0,"Airline Reservation System allows cancellation only before 2 hrs from departure time.\n"+"=> Important\n"+"* The charges shown are indicative and may vary at the time of cancellation, as per airline policies.\n"+"* Convenience fee is non-refundable. Any cashback availed will be adjusted in final refund amount.\n")
        c_policy.config(state='disabled')
        c_policy.pack(fill='both',expand='yes')
        can_pol=1
    elif canp and can_pol==1:
        canp.destroy()
        can_pol=0
        cancellation_policy(w)        
def payment_button():
    for widget in fr10.winfo_children():
        widget.destroy()
    if blogorbok=='blog' and blog_cei!='' and blog_cpw!='':
        ttk.Button(fr10,text='Make Payment',command=lambda:payment_booking(blog_cei,blog_cpw),width=40).pack(padx=5,pady=5,fill=tk.BOTH)
    else:
        ttk.Button(fr10,text='Make Payment',command=login_register,width=40).pack(padx=5,pady=5,fill=tk.BOTH)
def book_flight():
    global tf,blogorbok
    curItem=tr.focus()
    if d1==[] or curItem=='':
        tm.showwarning('Warning','Select a Flight to Proceed')
    else:
        global chfln,chfld,win2
        chfln=tr.item(curItem)['text']
        chfld=tr.item(curItem)['values']
        win2=tk.Toplevel(win)
        win2.title('Booking Details')
        win2.iconbitmap('airplane.ico')
        fr3=tk.Frame(win2)
        fr3.pack()
        tr1=ttk.Treeview(fr3,height=1)
        tr1.pack(padx=5,pady=8)
        tr1['columns']=('sa','doj')
        tr1.column('#0',width=80)
        tr1.column('sa',width=120,anchor='c')
        tr1.column('doj',width=120,anchor='c')
        tr1.heading('#0',text='Flight No.')
        tr1.heading('sa',text='Seats Available')
        tr1.heading('doj',text='Date of Journey')
        crs.execute("SELECT FLIGHT_NO,SEATS_AVAILABLE,DATE_OF_JOURNEY FROM seats WHERE FLIGHT_NO='{}' AND DATE_OF_JOURNEY='{}';".format(chfln,x_))
        d2=crs.fetchall()
        if d2==[]:
            crs.execute("INSERT INTO SEATS (FLIGHT_NO, DATE_OF_JOURNEY) VALUES('{}','{}');".format(chfln,x_))
            ani.commit()
            crs.execute("SELECT FLIGHT_NO,SEATS_AVAILABLE,DATE_OF_JOURNEY FROM seats WHERE FLIGHT_NO='{}' AND DATE_OF_JOURNEY='{}';".format(chfln,x_))
            d2=crs.fetchall()
            for i in d2:
                tr1.insert('',1,text=i[0],values=i[1:])
                sa=i[1]
        else:
            for i in d2:
                tr1.insert('',1,text=i[0],values=i[1:])
                sa=i[1]
        fr4=tk.Frame(win2)
        fr4.pack()
        tk.Label(fr4,text='             Age:').grid(row=0,column=2)
        tk.Label(fr4,text='>=12').grid(row=0,column=3)
        tk.Label(fr4,text='<12>=2').grid(row=0,column=4)
        tk.Label(fr4,text='<2').grid(row=0,column=5)
        tk.Label(fr4,text='       Traveller:').grid(row=1,column=2)
        tk.Label(fr4,text='Adults').grid(row=1,column=3)
        tk.Label(fr4,text='Children').grid(row=1,column=4)
        tk.Label(fr4,text='Infants').grid(row=1,column=5)
        tk.Label(fr4,text='No.of Travellers:').grid(row=2,column=2)
        s1_3=1
        crs.execute("SELECT FARE FROM fare WHERE CLASS='{}' AND TRAVELLER='{}' AND fare.FROM='{}' AND fare.TO='{}';".format('ECONOMY','ADULTS',chfld[1],chfld[2]))
        tfl=crs.fetchall()
        for i in tfl:
            for j in i:
                tf=j
        def total_fare():
            global tf
            crs.execute("SELECT {}*FARE FROM fare WHERE CLASS='{}' AND TRAVELLER='{}' AND fare.FROM='{}' AND fare.TO='{}';".format(s1.get(),vr[cl.get()],'ADULTS',chfld[1],chfld[2]))
            af=crs.fetchall()
            crs.execute("SELECT {}*FARE FROM fare WHERE CLASS='{}' AND TRAVELLER='{}' AND fare.FROM='{}' AND fare.TO='{}';".format(s2.get(),vr[cl.get()],'CHILDREN',chfld[1],chfld[2]))
            af+=crs.fetchall()
            crs.execute("SELECT {}*FARE FROM fare WHERE CLASS='{}' AND TRAVELLER='{}' AND fare.FROM='{}' AND fare.TO='{}';".format(s3.get(),vr[cl.get()],'INFANTS',chfld[1],chfld[2]))
            af+=crs.fetchall()
            tf=0
            for i in af:
                for j in i:
                    tf+=j
            lisbox.delete(0)
            lisbox.insert(1,'Rs. '+str(int(tf+(0.1*tf))))
            
        def infget():
            global s1_3
            s1_3=s1.get()
            s3.config(to=s1_3)
            if s1.get()+s2.get()+s3.get()==sa:
                s1.config(to=s1.get())
            total_fare()
        def s2l():
            if s1.get()+s2.get()+s3.get()==sa:
                s2.config(to=s2.get())
            total_fare()
        def s3l():
            if s1.get()+s2.get()+s3.get()==sa:
                s3.config(to=s3.get())
            total_fare()
        s1=tk.Spinbox(fr4,from_=1,to=10,width=6,command=infget)
        s2=tk.Spinbox(fr4,from_=0,to=10,width=8,command=s2l)
        s3=tk.Spinbox(fr4,from_=0,to=s1_3,width=6,command=s3l)
        s1.grid(row=2,column=3)
        s2.grid(row=2,column=4)
        s3.grid(row=2,column=5)
        fr5=tk.Frame(win2)
        fr5.pack(padx=5)
        tk.Label(fr5,text='Class:').grid(row=0,column=0,padx=1)
        vr=['Economy','Premium Economy','Business Class']
        cl=tk.IntVar()
        for i in range(3):
            ttk.Radiobutton(fr5,text=vr[i],variable=cl,value=i,command=total_fare).grid(row=0,column=i+1,padx=1)
        fr6=tk.Frame(win2)
        fr6.pack()
        tk.Label(fr6,text='Total Airfare:').grid(row=0,column=0,pady=5)
        lisbox=tk.Listbox(fr6,width=10,height=1,selectmode=tk.SINGLE)
        lisbox.insert(1,'Rs. '+str(tf))
        lisbox.grid(row=0,column=1,pady=5)
        def passenger_details():
            global blogorbok,gt
            window=tk.Toplevel(win)
            if int(s1.get())+int(s2.get())+int(s3.get())>=5:
                if int(s2.get())!=0 or int(s3.get())!=0:
                    window.geometry('1072x399')
                elif int(s1.get())!=0 and int(s2.get())==0 and int(s3.get())==0:
                    window.geometry('800x399')
            else:
                if int(s1.get())+int(s2.get())+int(s3.get())==1:
                    window.geometry('800x163')
                elif int(s1.get())+int(s2.get())+int(s3.get())==2:
                    if int(s2.get())!=0 or int(s3.get())!=0:
                        window.geometry('1072x220')
                    elif int(s1.get())!=0 and int(s2.get())==0 and int(s3.get())==0:
                        window.geometry('800x220')
                elif int(s1.get())+int(s2.get())+int(s3.get())==3:
                    if int(s2.get())!=0 or int(s3.get())!=0:
                        window.geometry('1072x280')
                    elif int(s1.get())!=0 and int(s2.get())==0 and int(s3.get())==0:
                        window.geometry('800x280')
                elif int(s1.get())+int(s2.get())+int(s3.get())==4:
                    if int(s2.get())!=0 or int(s3.get())!=0:
                        window.geometry('1072x339')
                    elif int(s1.get())!=0 and int(s2.get())==0 and int(s3.get())==0:
                        window.geometry('800x339')
            canvas=tk.Canvas(window)
            canvas.pack(side=tk.LEFT,expand='yes',fill='both')
            win3=tk.Frame(canvas)
            win3.pack(expand='yes',fill='both')
            vsb1=ttk.Scrollbar(window,orient="vertical",command=canvas.yview)
            vsb1.pack(fill=tk.Y,side=tk.RIGHT)
            win3.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            canvas.create_window((0,0),window=win3,anchor="nw")
            canvas.configure(yscrollcommand=vsb1.set)
            window.title('Passenger Details')
            window.iconbitmap('airplane.ico')
            fr7=tk.Frame(win3)
            fr7.pack(fill='both',expand='yes')
            dat={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            dafn={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            damn={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            daln={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            daf={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            for i in range(1,int(s1.get())+1):
                daf[i]=tk.LabelFrame(fr7,text='Adult '+str(i))
                tk.Label(daf[i],text='*Tiltle').grid(row=0,column=0,padx=5,pady=5)
                dat[i]=ttk.Combobox(daf[i],width='5')
                dat[i]['values']=['Mr','Ms','Mrs']
                dat[i].grid(row=0,column=1,padx=5,pady=5)
                tk.Label(daf[i],text='*First Name:').grid(row=0,column=2,padx=5,pady=5)
                dafn[i]=ttk.Entry(daf[i])
                dafn[i].grid(row=0,column=3,padx=5,pady=5)
                tk.Label(daf[i],text='Middle Name:').grid(row=0,column=4,padx=5,pady=5)
                damn[i]=ttk.Entry(daf[i])
                damn[i].grid(row=0,column=5,padx=5,pady=5)
                tk.Label(daf[i],text='Last Name:').grid(row=0,column=6,padx=5,pady=5)
                daln[i]=ttk.Entry(daf[i])
                daln[i].grid(row=0,column=7,padx=5,pady=5)
                daf[i].pack(fill="both",expand="yes",padx=5,pady=5)
            dct={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            dcfn={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            dcmn={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            dcln={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            dcdd={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            dcdm={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            dcdy={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            dcf={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            for i in range(1,int(s2.get())+1):
                def cdob_limit(*args):
                    for i in range(1,int(s2.get())+1):
                        cdy=dcdy[i].get()
                        cdm=dcdm[i].get()
                        cdd=dcdd[i].get()
                        if cdy=='':
                            cdy=0
                        if cdm=='':
                            cdm=0
                        if cdd=='':
                            cdd=0
                        if int(cdm)==1 or int(cdm)==3 or int(cdm)==5 or int(cdm)==7 or int(cdm)==8 or int(cdm)==10 or int(cdm)==12:
                            dcdd[i].config(values=[i for i in range(1,32)])
                            if int(cdd)>31:
                                dcdd[i].current(30)
                        elif int(cdm)==4 or int(cdm)==6 or int(cdm)==9 or int(cdm)==11:
                            dcdd[i].config(values=[i for i in range(1,31)])
                            if int(cdd)>30:
                                dcdd[i].current(29)
                        elif (int(cdm)==2 and int(cdy)%400==0) or (int(cdm)==2 and int(cdy)%4==0 and int(cdy)%100!=0):
                            dcdd[i].config(values=[i for i in range(1,30)])
                            if int(cdd)>29:
                                dcdd[i].current(28)
                        else:
                            dcdd[i].config(values=[i for i in range(1,29)])
                            if int(cdd)>28:
                                dcdd[i].current(27)
                        if int(x_.year)-2==int(cdy):
                            dcdm[i].config(values=[i for i in range(1,int(x_.month)+1)])
                            if int(cdm)>int(x_.month):
                                dcdm[i].current(int(x_.month)-1)
                                cdm=dcdm[i].get()
                            if int(x_.month)==int(cdm): 
                                dcdd[i].config(values=[i for i in range(1,int(x_.day)+1)])
                                if int(cdd)>int(x_.day):
                                    dcdd[i].current(int(x_.day)-1)
                        elif int(x_.year)-12==int(cdy):
                            dcdm[i].config(values=[i for i in range(int(x_.month),13)])
                            if int(cdm)<int(x_.month):
                                dcdm[i].current(0)
                                cdm=dcdm[i].get()
                            if int(x_.month)==int(cdm):
                                dcdd[i].config(values=[i for i in range(int(x_.day)+1,int(dcdd[i]['values'][-1])+1)])
                                if int(cdd)<(int(x_.day)+1):
                                    dcdd[i].current(0)
                        else:
                            dcdm[i].config(values=[i for i in range(1,13)])
                dcf[i]=tk.LabelFrame(fr7,text='Child '+str(i))
                tk.Label(dcf[i],text='*Tiltle').grid(row=0,column=0,padx=5,pady=5)
                dct[i]=ttk.Combobox(dcf[i],width='5')
                dct[i]['values']=['Ms','Mstr']
                dct[i].grid(row=0,column=1,padx=5,pady=5)
                tk.Label(dcf[i],text='*First Name:').grid(row=0,column=2,padx=5,pady=5)
                dcfn[i]=ttk.Entry(dcf[i])
                dcfn[i].grid(row=0,column=3,padx=5,pady=5)
                tk.Label(dcf[i],text='Middle Name:').grid(row=0,column=4,padx=5,pady=5)
                dcmn[i]=ttk.Entry(dcf[i])
                dcmn[i].grid(row=0,column=5,padx=5,pady=5)
                tk.Label(dcf[i],text='Last Name:').grid(row=0,column=6,padx=5,pady=5)
                dcln[i]=ttk.Entry(dcf[i])
                dcln[i].grid(row=0,column=7,padx=5,pady=5)
                dcf[i].pack(fill="both",expand="yes",padx=5,pady=5)
                tk.Label(dcf[i],text='*Date of Birth:').grid(row=0,column=8,padx=5,pady=5)
                dcdd[i]=ttk.Combobox(dcf[i],width='4')
                dcdd[i]['values']=[i for i in range(1,32)]
                dcdd[i].bind("<<ComboboxSelected>>",cdob_limit)
                dcdd[i].grid(row=0,column=9,padx=5,pady=5)
                dcdm[i]=ttk.Combobox(dcf[i],width='4')
                dcdm[i]['values']=[i for i in range(1,13)]
                dcdm[i].bind("<<ComboboxSelected>>",cdob_limit)
                dcdm[i].grid(row=0,column=10,padx=5,pady=5)
                dcdy[i]=ttk.Combobox(dcf[i],width='6')
                dcdy[i]['values']=[i for i in range(int(x_.year)-12,int(x_.year)-1)]
                dcdy[i].bind("<<ComboboxSelected>>",cdob_limit)
                dcdy[i].grid(row=0,column=11,padx=5,pady=5)
            dit={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            difn={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            dimn={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            diln={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            didd={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            didm={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            didy={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            dif={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
            for i in range(1,int(s3.get())+1):
                def idob_limit(*args):
                    for i in range(1,int(s3.get())+1):
                        idy=didy[i].get()
                        idm=didm[i].get()
                        idd=didd[i].get()
                        if idy=='':
                            idy=0
                        if idm=='':
                            idm=0
                        if idd=='':
                            idd=0
                        if int(idm)==1 or int(idm)==3 or int(idm)==5 or int(idm)==7 or int(idm)==8 or int(idm)==10 or int(idm)==12:
                            didd[i].config(values=[i for i in range(1,32)])
                            if int(idd)>31:
                                didd[i].current(30)
                        elif int(idm)==4 or int(idm)==6 or int(idm)==9 or int(idm)==11:
                            didd[i].config(values=[i for i in range(1,31)])
                            if int(idd)>30:
                                didd[i].current(29)
                        elif (int(idm)==2 and int(idy)%400==0) or (int(idm)==2 and int(idy)%4==0 and int(idy)%100!=0):
                            didd[i].config(values=[i for i in range(1,30)])
                            if int(idd)>29:
                                didd[i].current(28)
                        else:
                            didd[i].config(values=[i for i in range(1,29)])
                            if int(idd)>28:
                                didd[i].current(27)
                        if int(x_.year)-2==int(idy):
                            didm[i].config(values=[i for i in range(int(x_.month),13)])
                            if int(idm)<int(x_.month):
                                didm[i].current(0)
                                idm=didm[i].get()
                            if int(x_.month)==int(idm):
                                didd[i].config(values=[i for i in range(int(x_.day)+1,int(didd[i]['values'][-1])+1)])
                                if int(idd)<(int(x_.day)+1) and int(idd)!=0:
                                    didd[i].current(0)
                        elif int(ny)==int(idy):
                            if int(nd)==1:
                                didm[i].config(values=[i for i in range(1,int(nm))])
                                if int(idm)>(int(nm)-1):
                                    didm[i].current(int(nm)-2)
                                    idob_limit()
                            else:
                                didm[i].config(values=[i for i in range(1,int(nm)+1)])
                                if int(idm)>int(nm):
                                    didm[i].current(int(nm)-1)
                                    idm=didm[i].get()
                            if int(nm)==int(idm):
                                didd[i].config(values=[i for i in range(1,int(nd))])
                                if int(idd)>(int(nd)-1):
                                    didd[i].current(int(nd)-2)
                        else:
                            didm[i].config(values=[i for i in range(1,13)])
                dif[i]=tk.LabelFrame(fr7,text='Infant '+str(i))
                tk.Label(dif[i],text='*Tiltle').grid(row=0,column=0,padx=5,pady=5)
                dit[i]=ttk.Combobox(dif[i],width='5')
                dit[i]['values']=['Ms','Mstr']
                dit[i].grid(row=0,column=1,padx=5,pady=5)
                tk.Label(dif[i],text='*First Name:').grid(row=0,column=2,padx=5,pady=5)
                difn[i]=ttk.Entry(dif[i])
                difn[i].grid(row=0,column=3,padx=5,pady=5)
                tk.Label(dif[i],text='Middle Name:').grid(row=0,column=4,padx=5,pady=5)
                dimn[i]=ttk.Entry(dif[i])
                dimn[i].grid(row=0,column=5,padx=5,pady=5)
                tk.Label(dif[i],text='Last Name:').grid(row=0,column=6,padx=5,pady=5)
                diln[i]=ttk.Entry(dif[i])
                diln[i].grid(row=0,column=7,padx=5,pady=5)
                dif[i].pack(fill="both",expand="yes",padx=5,pady=5)
                tk.Label(dif[i],text='*Date of Birth:').grid(row=0,column=8,padx=5,pady=5)
                didd[i]=ttk.Combobox(dif[i],width='4')
                didd[i]['values']=[i for i in range(1,32)]
                didd[i].bind("<<ComboboxSelected>>",idob_limit)
                didd[i].grid(row=0,column=9,padx=5,pady=5)
                didm[i]=ttk.Combobox(dif[i],width='4')
                didm[i]['values']=[i for i in range(1,13)]
                didm[i].bind("<<ComboboxSelected>>",idob_limit)
                didm[i].grid(row=0,column=10,padx=5,pady=5)
                didy[i]=ttk.Combobox(dif[i],width='6')
                didy[i]['values']=[i for i in range(int(x_.year)-2,int(ny)+1)]
                didy[i].bind("<<ComboboxSelected>>",idob_limit)
                didy[i].grid(row=0,column=11,padx=5,pady=5)
            ci=tk.LabelFrame(fr7,text='Contact Information')
            ci.pack(fill="both",expand="yes",padx=5,pady=5)
            tk.Label(ci,text='*Email:').grid(row=0,column=0,padx=5,pady=5)
            ciem=ttk.Entry(ci,width=35)
            ciem.grid(row=0,column=1,padx=5,pady=5)
            tk.Label(ci,text='*Phone Number:').grid(row=0,column=2,padx=5,pady=5)
            cipn=ttk.Entry(ci)
            cipn.grid(row=0,column=3,padx=5,pady=5)
            def show():
                global blogorbok,gt,notr,blog_cei,blog_cpw,noa,noc,noi
                notr=int(s1.get())+int(s2.get())+int(s3.get())
                noac=int(s1.get())+int(s2.get())
                noa=int(s1.get())
                noc=int(s2.get())
                noi=int(s3.get())
                global mpd,pd
                mpd=[]
                pd=[]
                atr=''
                for i in ciem.get():
                    if i=='@':
                        atr='@'
                if cipn.get()=='' or ciem.get()=='':
                    tm.showerror('Error','Provide your Contact Information')
                elif atr!='@' or ciem.get()[-4:]!='.com':
                    tm.showerror('Error','Email Id is Incorrect')
                elif len(cipn.get())!=10 or cipn.get()[0] in '123457':
                    tm.showerror('Error','Phone Number is Incorrect')
                else:
                    for i in range(1,int(s1.get())+1):
                        crs.execute("SELECT PASSENGER_ID FROM PASSENGER_DETAILS WHERE PASSENGER_ID LIKE 'PIA%';")
                        alapi=crs.fetchall()
                        pi=random.randint(1,999999999999999)
                        while pi in [int(i[0].lstrip('PIA')) for i in alapi]:
                            pi=random.randint(1,999999999999999)
                        fpi='PIA'+('0'*(15-len(str(pi))))+str(pi)
                        if dat[i].get()=='' or dafn[i].get()=='':
                            tm.showerror('Error','Fill the Mandatory Fields for Adult '+str(i))
                        elif dat[i].get() not in dat[i]['values']:
                            tm.showerror('Error','Improper Title for Adult '+str(i))
                        if dat[i].get()=='Mr' and dafn[i].get()!='':
                            pd.append((fpi,(dafn[i].get()+' '+damn[i].get()+' '+daln[i].get()).strip(),'M','ADULT',' ',' ',vr[cl.get()]))
                            mpd.append((fpi,chfln,(dafn[i].get()+' '+damn[i].get()+' '+daln[i].get()).strip(),'M','ADULT',vr[cl.get()],x_,int(cipn.get()),ciem.get()))
                        elif (dat[i].get()=='Ms' or dat[i].get()=='Mrs') and dafn[i].get()!='':
                            pd.append((fpi,(dafn[i].get()+' '+damn[i].get()+' '+daln[i].get()).strip(),'F','ADULT',' ',' ',vr[cl.get()]))
                            mpd.append((fpi,chfln,(dafn[i].get()+' '+damn[i].get()+' '+daln[i].get()).strip(),'F','ADULT',vr[cl.get()],x_,int(cipn.get()),ciem.get()))
                    for i in range(1,int(s2.get())+1):
                        crs.execute("SELECT PASSENGER_ID FROM PASSENGER_DETAILS WHERE PASSENGER_ID LIKE 'PIC%';")
                        alapi=crs.fetchall()
                        pi=random.randint(1,999999999999999)
                        while pi in [int(i[0].lstrip('PIC')) for i in alapi]:
                            pi=random.randint(1,999999999999999)
                        fpi='PIC'+('0'*(15-len(str(pi))))+str(pi)
                        z=0
                        cdy=dcdy[i].get()
                        cdm=dcdm[i].get()
                        cdd=dcdd[i].get()
                        if dct[i].get()=='' or cdy=='' or cdm=='' or cdd=='' or dcfn[i].get()=='':
                            tm.showerror('Error','Fill the Mandatory Fields for Child '+str(i))
                        elif dct[i].get() not in dct[i]['values']:
                            tm.showerror('Error','Improper Title for Child '+str(i))
                        elif cdy not in dcdy[i]['values'] or cdm not in dcdm[i]['values'] or cdd not in dcdd[i]['values']:
                            tm.showerror('Error','Date of Birth for Child '+str(i)+' is Incorrect')
                        else:
                            dob=datetime.date(datetime(int(cdy),int(cdm),int(cdd)))
                            z+=1
                        if dct[i].get()=='Mstr' and z==1:
                            pd.append((fpi,(dcfn[i].get()+' '+dcmn[i].get()+' '+dcln[i].get()).strip(),'M','CHILD',int((nx-dob).days/365),dob,vr[cl.get()]))
                            mpd.append((fpi,chfln,(dcfn[i].get()+' '+dcmn[i].get()+' '+dcln[i].get()).strip(),'M','CHILD',int((nx-dob).days/365),dob,vr[cl.get()],x_,int(cipn.get()),ciem.get()))
                        elif dct[i].get()=='Ms' and z==1:
                            pd.append((fpi,(dcfn[i].get()+' '+dcmn[i].get()+' '+dcln[i].get()).strip(),'F','CHILD',int((nx-dob).days/365),dob,vr[cl.get()]))
                            mpd.append((fpi,chfln,(dcfn[i].get()+' '+dcmn[i].get()+' '+dcln[i].get()).strip(),'F','CHILD',int((nx-dob).days/365),dob,vr[cl.get()],x_,int(cipn.get()),ciem.get()))
                    for i in range(1,int(s3.get())+1):
                        crs.execute("SELECT PASSENGER_ID FROM PASSENGER_DETAILS WHERE PASSENGER_ID LIKE 'PII%';")
                        alapi=crs.fetchall()
                        pi=random.randint(1,999999999999999)
                        while pi in [int(i[0].lstrip('PII')) for i in alapi]:
                            pi=random.randint(1,999999999999999)
                        fpi='PII'+('0'*(15-len(str(pi))))+str(pi)
                        z=0
                        idy=didy[i].get()
                        idm=didm[i].get()
                        idd=didd[i].get()
                        if dit[i].get()=='' or idy=='' or idm=='' or idd=='' or difn[i].get()=='':
                            tm.showerror('Error','Fill the Mandatory Fields for Infant '+str(i))
                        elif dit[i].get() not in dit[i]['values']:
                            tm.showerror('Error','Improper Title for Infant '+str(i))
                        elif idy not in didy[i]['values'] or idm not in didm[i]['values'] or idd not in didd[i]['values']:
                            tm.showerror('Error','Date of Birth for Infant '+str(i)+' is Incorrect')
                        else:
                            dob=datetime.date(datetime(int(idy),int(idm),int(idd)))
                            z+=1
                        if dit[i].get()=='Mstr' and z==1:
                            pd.append((fpi,(difn[i].get()+' '+dimn[i].get()+' '+diln[i].get()).strip(),'M','INFANT',int((nx-dob).days/365),dob,vr[cl.get()]))
                            mpd.append((fpi,chfln,(difn[i].get()+' '+dimn[i].get()+' '+diln[i].get()).strip(),'M','INFANT',int((nx-dob).days/365),dob,vr[cl.get()],x_,int(cipn.get()),ciem.get()))
                        elif dit[i].get()=='Ms' and z==1:
                            pd.append((fpi,(difn[i].get()+' '+dimn[i].get()+' '+diln[i].get()).strip(),'F','INFANT',int((nx-dob).days/365),dob,vr[cl.get()]))
                            mpd.append((fpi,chfln,(difn[i].get()+' '+dimn[i].get()+' '+diln[i].get()).strip(),'F','INFANT',int((nx-dob).days/365),dob,vr[cl.get()],x_,int(cipn.get()),ciem.get()))
                    if len(pd)==notr:
                        condet=tm.askyesno('Confirmation','Are you sure, to Confirm Details?')
                        if condet:
                            global win4
                            window.destroy()
                            win4=tk.Toplevel(win)
                            win4.title('Traveller Information')
                            win4.iconbitmap('airplane.ico')
                            fr8=tk.Frame(win4)
                            fr8.pack(side=tk.LEFT,fill='both',expand='yes')
                            finf=tk.LabelFrame(fr8,text='Flight Details')
                            finf.pack(padx=5,pady=5,fill="x",side=tk.TOP)
                            tvfd=ttk.Treeview(finf,height=1)
                            tvfd['columns']=('fname','from','to','dep','arr','fdurn','stops','doj','day')
                            tvfd.column('#0',width=80,anchor='c')
                            tvfd.column('fname',width=100,anchor='c')
                            tvfd.column('from',width=110,anchor='c')
                            tvfd.column('to',width=110,anchor='c')
                            tvfd.column('dep',width=80,anchor='c')
                            tvfd.column('arr',width=80,anchor='c')
                            tvfd.column('fdurn',width=90,anchor='c')
                            tvfd.column('doj',width=95,anchor='c')
                            tvfd.column('day',width=90,anchor='c')
                            tvfd.column('stops',width=70,anchor='c')
                            tvfd.heading('#0',text='Flight No.')
                            tvfd.heading('fname',text='Flight Name')
                            tvfd.heading('from',text='From')
                            tvfd.heading('to',text='To')
                            tvfd.heading('dep',text='Departure')
                            tvfd.heading('arr',text='Arrival')
                            tvfd.heading('fdurn',text='Flight Duration')
                            tvfd.heading('doj',text='Date of Journey')
                            tvfd.heading('day',text='Day')
                            tvfd.heading('stops',text='Stops')
                            tvfd.insert('',1,text=chfln,values=chfld+[d2[0][-1]]+[x_.strftime("%A")])
                            tvfd.pack(padx=5,pady=8,fill="both",expand="yes")
                            crs.execute("SELECT AIRPORT FROM AIRPORTS WHERE PLACE='{}';".format(d1[0][2]))
                            dairp=crs.fetchall()[0][0]
                            crs.execute("SELECT AIRPORT FROM AIRPORTS WHERE PLACE='{}';".format(d1[0][3]))
                            aairp=crs.fetchall()[0][0]
                            strdes=tk.LabelFrame(fr8,text='Start - Destination')
                            strdes.pack(padx=5,pady=5,fill="x",side=tk.TOP)
                            arp=ttk.Treeview(strdes,height=1)
                            arp['columns']=('arrat')
                            arp.column('arrat',anchor='c')
                            arp.heading('#0',text='Departure From')
                            arp.heading('arrat',text='Arrival At')
                            arp.insert('',1,text=dairp,values=[aairp])
                            arp.pack(padx=5,pady=8,fill="both",expand="yes")
                            tif=tk.LabelFrame(fr8,text="Passenger's Details")
                            tif.pack(padx=5,pady=5,fill="x",side=tk.TOP)
                            tr2=ttk.Treeview(tif,height=notr)
                            tr2.pack(padx=5,pady=8,fill="both")
                            tr2['columns']=('pasngname','gender','tvrl','age','dob','clas')
                            tr2.column('#0',width=110,anchor='c')
                            tr2.column('pasngname',width=120,anchor='c')
                            tr2.column('gender',width=40,anchor='c')
                            tr2.column('tvrl',width=80,anchor='c')
                            tr2.column('age',width=55,anchor='c')
                            tr2.column('dob',width=90,anchor='c')
                            tr2.column('clas',width=125,anchor='c')
                            tr2.heading('#0',text='Passenger ID')
                            tr2.heading('pasngname',text='Passenger Name')
                            tr2.heading('gender',text='Sex')
                            tr2.heading('tvrl',text='Traveller')
                            tr2.heading('age',text='Age')
                            tr2.heading('dob',text='Date of Birth')
                            tr2.heading('clas',text='Class')
                            for i in pd:
                                tr2.insert('','end',text=i[0],values=i[1:])
                            cif=tk.LabelFrame(fr8,text='Contact Information')
                            cif.pack(padx=5,pady=5,fill="x")
                            tk.Label(cif,text='Email Id: ').grid(row=0,column=0,padx=5,pady=5)
                            lbem=tk.Listbox(cif,width=35,height=1,selectmode=tk.SINGLE)
                            lbem.insert(1,mpd[0][-1])
                            lbem.grid(row=0,column=1,pady=5)
                            tk.Label(cif,text='Phone No. : ').grid(row=0,column=2,padx=5,pady=5)
                            lbpn=tk.Listbox(cif,height=1,selectmode=tk.SINGLE)
                            lbpn.insert(1,mpd[0][-2])
                            lbpn.grid(row=0,column=3,pady=5)
                            fr9=ttk.Frame(win4)
                            fr9.pack(side=tk.LEFT,fill='both',expand='yes')
                            gt=int(tf+(0.1*tf))+(int(0.05*tf)*noac)
                            fd=tk.LabelFrame(fr9,text='Fare Details',font='arial 16')
                            fd.pack(ipadx=5,padx=5,pady=5,side=tk.TOP,fill=tk.X)
                            fdfr=tk.Frame(fd)
                            fdfr.pack()
                            note=tk.Frame(fr9)
                            note.pack(ipadx=5,padx=5,side=tk.TOP)
                            global t_c
                            t_c=str(int(0.1*tf)+int(0.05*tf)*noac)
                            tk.Label(fdfr,text='Total Base Fare:').grid(pady=3,padx=10,row=0,column=0)
                            tk.Label(fdfr,text='Total Taxes & Fees:').grid(padx=10,row=1,column=0)
                            tk.Label(fdfr,text='---------------------------').grid(padx=10,row=2,column=0)
                            tk.Label(fdfr,text='Total Airfare:',font='arial 10 bold').grid(padx=10,row=3,column=0)
                            tk.Label(fdfr,text='Total Convenience Fee:').grid(padx=10,row=4,column=0)
                            tk.Label(fdfr,text='---------------------------').grid(padx=10,row=5,column=0)
                            tk.Label(fdfr,text='Grand Total:',font='arial 12 bold').grid(padx=10,row=6,column=0)
                            tk.Label(fdfr,text='---------------------------').grid(padx=10,row=7,column=0)
                            tk.Label(fdfr,text='Rs. '+str(tf),font='arial 10 bold').grid(row=0,column=1)
                            tk.Label(fdfr,text='Rs. '+str(int(0.1*tf)),font='arial 10 bold').grid(row=1,column=1)
                            tk.Label(fdfr,text='----------------------').grid(row=2,column=1)
                            tk.Label(fdfr,text='Rs. '+str(int(tf+(0.1*tf))),font='arial 11 bold').grid(row=3,column=1)
                            tk.Label(fdfr,text='Rs. '+str(int(0.05*tf)*noac),font='arial 10 bold').grid(row=4,column=1)
                            tk.Label(fdfr,text='----------------------').grid(row=5,column=1)
                            tk.Label(fdfr,text='Rs. '+str(gt),font='arial 12 bold').grid(row=6,column=1)
                            tk.Label(fdfr,text='----------------------').grid(row=7,column=1)
                            tk.Label(note,text='*Convenience Fee is Non-Refundable.').grid(row=0,column=0)
                            tk.Label(note,text='Cancellation Policy').grid(row=0,column=1)
                            defaultbg=win4.cget('bg')
                            tk.Button(note,text='(i)',underline=1,relief='flat',bg=defaultbg,fg='darkblue',font='calibri 11 italic underline',command=lambda:cancellation_policy(win4)).grid(row=0,column=2)
                            global fr10
                            fr10=ttk.Frame(fr9)
                            fr10.pack(padx=5,side=tk.TOP,fil=tk.X)
                            payment_button()
                            blogorbok='book'
            tk.Label(fr7,text='*Mandatory Fields').pack(padx=15,side=tk.LEFT)
            ttk.Button(fr7,text='Confirm Details',command=show).pack(side=tk.RIGHT,padx=15,pady=5)
        ttk.Button(fr6,text='Continue Booking',command=passenger_details).grid(row=0,column=2,pady=5,padx=25)
def ticket(ltd,tpasng,ttrvl):
    t=['                                                                  ARS - AIRLINE RESERVATION SYSTEM\n', '                                                                     E-Ticket Itinerary Receipt\n', '\n', 'Customer must present this receipt along with a valid photo identification to enter the Airport. We seek your attention to make a note of our Terms and Condition.\n', '\n', 'Issuing Airline:- %s\n', 'Issuing Date:- %s\n', '\n', 'Passenger Details:-\n', '+--------------------+--------------------------+-----+-----------+-----+---------------+\n', '|    PASSENGER ID    |      PASSENGER NAME      | SEX | TRAVELLER | AGE | DATE OF BIRTH |\n', '+--------------------+--------------------------+-----+-----------+-----+---------------+\n', '| %s | %s | %s   | %s | %s | %s    |\n', '+--------------------+--------------------------+-----+-----------+-----+---------------+\n', '\n', 'Travel Information:- \n', '+------------+--------------------------+--------------------------+-----------+-----------+-----------------+-------+-----------------+\n', '| FLIGHT NO. |           FROM           |            TO            | DEPARTURE |  ARRIVAL  |      CLASS      | STOPS | DATE OF JOURNEY |\n', '+------------+--------------------------+--------------------------+-----------+-----------+-----------------+-------+-----------------+\n', '| %s | %s | %s | %s | %s | %s | %s     | %s      |\n', '+------------+--------------------------+--------------------------+-----------+-----------+-----------------+-------+-----------------+\n', '\n', 'Fare Details:-\n', '+-----------+------------------+----------+   \n', '| TRAVELLER | NO. OF TRAVELLER |   FARE   |                                   \n', '+-----------+------------------+----------+                                   \n', '| %s | %s | %s |                                   \n', '+------------------------------+----------+                                   \n', '|   TAXES AND CONVENIENCE FEES | %s |                   \n', '+------------------------------+----------+                   \n', '|                 TOTAL AMOUNT | %s |                   \n', '+-----------------------------------------+                   \n', '\n', 'Payment Details:-\n', '+----------------+---------------------------+\n', '| NAME ON CARD   | %s |\n', '+----------------+---------------------------+\n', '| CARD NUMBER    | ************%s          |\n', '+----------------+---------------------------+\n', '| AUTH CODE      | %s |\n', '+----------------+---------------------------+\n', '| TRANSACTION ID | %s       |\n', '+--------------------------------------------+\n', '\n', 'Additional Contact Details:-\n', '+-------------+---------------------------+\n', '| CONTACT NO. | %s                |\n', '+-------------+---------------------------+\n', '| EMAIL ID    | %s |\n', '+-------------+---------------------------+']
    t1=[]
    for i in range(len(t)):
        if i==12:
            for j in range(tpasng):
                t1.append(t[i])
        elif i==26:
            for j in range(ttrvl):
                t1.append(t[i])
        else:
            t1.append(t[i])
    z=0
    ft=[]
    for i in t1:
        if '%s' in i:
            i=i%ltd[z]
            z+=1
        ft.append(i)
    ptic=tk.Toplevel(win)
    tic_nam=(time.strftime("%b %d %Y %H%M%S",time.localtime(time.time())))
    ptic.geometry("1300x520")
    ptic.iconbitmap('airplane.ico')
    ptic.title('Ticket - '+tic_nam)
    ticket=tk.Text(ptic)
    for i in ft:
        ticket.insert(tk.INSERT,i)
    ticket.config(state='disabled')
    ticket.pack(fill='both',expand='yes')
    file=open(".\\Tickets\\"+tic_nam+".txt",'w')
    file.writelines(ft)
    file.flush()
    file.close()
def payment_booking(cei,cpw):
    global paym
    paym=''
    win6=tk.Toplevel(win)
    win6.title('Payment')
    win6.iconbitmap('airplane.ico')
    cpay=tk.Frame(win6)
    cpay.pack()
    cdf=tk.Frame(win6)
    cdf.pack()
    tk.Label(cpay,text='Choose Paymemt Method:',font='arial 9').grid(row=0,column=0,padx=5,pady=5)
    pm=['','Debit/Credit/ATM Card','Net Banking']
    cpm=tk.StringVar()
    pmom=ttk.OptionMenu(cpay,cpm,*pm)
    pmom.grid(row=0,column=1,padx=5,pady=5)
    cpm.set('--Select a payment method--')
    def payment_details(*args):
        global paym
        if cpm.get()=='Debit/Credit/ATM Card':
            if paym!=cpm.get():
                def month_limit(*args):
                    q=0
                    if edm.get()=='':
                        q+=1 
                    if int(edy.get())==int(ny):
                        edm.config(values=[i for i in range(int(nm)+1,13)])
                        if q!=1:
                            if int(edm.get())<(int(nm)+1):
                                edm.current(0)
                    else:
                        edm.config(values=[i for i in range(1,13)])
                cd=tk.LabelFrame(cdf,text='Card Details',font='arial 12')
                fcd=tk.Frame(cd)
                fcd.pack()
                fcd2=tk.Frame(cd)
                fcd2.pack()
                cd.pack(padx=5,pady=5,fill='both',expand='yes')
                tk.Label(fcd,text='Name on Card:').grid(row=0,column=0,padx=5,pady=5)
                tk.Label(fcd,text='Expiry Date:').grid(row=0,column=2,padx=5,pady=5)                
                tk.Label(fcd2,text='Card Number:').pack(side=tk.LEFT,padx=5,pady=5)
                nc=ttk.Entry(fcd)
                nc.grid(row=0,column=1,padx=5,pady=5)
                def update_cn(*args):
                    global i
                    if len(cnu.get())==i:
                        cn.insert(i-1,' ')
                        i+=5
                    elif (i-len(cnu.get()))>5:
                        i-=5
                cnu=tk.StringVar()
                cnu.trace_variable('w',update_cn)
                cn=ttk.Entry(fcd2,width=30,textvariable=cnu)
                cn.pack(side=tk.LEFT,padx=5,pady=5)
                tk.Label(fcd2,text='CVV:').pack(side=tk.LEFT,padx=5,pady=5)
                cvv=ttk.Entry(fcd2,show='*',width=5)
                cvv.pack(side=tk.LEFT,padx=5,pady=5)
                edm=ttk.Combobox(fcd,width=3)
                edm['values']=[i for i in range(1,13)]
                edm.grid(row=0,column=3)
                edy=ttk.Combobox(fcd,width=4)
                if int(nm)!=12:
                    edy['values']=[i for i in range(ny,ny+21)]
                elif int(nm)==12:
                    edy['values']=[i for i in range(ny+1,ny+22)]
                edy.grid(row=0,column=4,padx=5,pady=5)
                edy.bind("<<ComboboxSelected>>",month_limit)
                paym=cpm.get()
                def final_payment():
                    cnws=''
                    for i in cnu.get():
                        if i!=' ':
                            cnws+=i
                    if nc=='' or edm.get()=='' or edy.get()=='' or cvv.get=='' or cnu.get()=='':
                        tm.showwarning('Empty Fields','Fill all the details, Correctly!')
                    elif len(cnu.get())!=19 or cnws.isdigit()==False:
                        tm.showerror('Error','Invalid Card Number')
                    elif edm.get() not in edm['values'] or edy.get() not in edy['values']:
                        tm.showerror('Error','Invalid Entry for Expiry Date')
                    elif len(cvv.get())!=3 or cvv.get().isdigit()==False:
                        tm.showerror('Error','Invalid Entry for CVV')
                    else:
                        global sem,spw,tf,gt
                        def send_otp(sub):
                            global otp
                            otp=random.randint(100000,999999)
                            body='Dear Customer, One-Time-Password(OTP) for making payment of Rs.'+str(gt)+' at Airline Reservation System is '+str(otp)+'. OTP is valid for 10 minutes only. Do Not share the OTP with anyone.'
                            msg=f'Subject:{sub}\n\n{body}'
                            with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                                smtp.ehlo()
                                smtp.starttls()
                                smtp.ehlo()
                                smtp.login(sem,spw)
                                smtp.sendmail(sem,cei,msg)
                                now=datetime.now()
                                global validity
                                validity=now+timedelta(minutes=10)
                                smtp.quit()
                        send_otp('OTP for verification')
                        fnc=nc.get()
                        fcnu=cnu.get().replace(' ','')
                        fed=('0'*(2-len(edm.get())))+edm.get()+'-'+edy.get()
                        fcvv=int(cvv.get())
                        win6.destroy()
                        win7=tk.Toplevel(win)
                        win7.title('OTP Verification')
                        win7.iconbitmap('airplane.ico')
                        vf=tk.Frame(win7)
                        vf.pack()
                        otplf=tk.LabelFrame(vf,text='Enter OTP',font='arial 12')
                        otplf.grid(row=0,column=0,padx=5,pady=5)
                        otpbyc=ttk.Entry(otplf)
                        otpbyc.pack()
                        def resend_otp():
                            send_otp('Resend OTP for verification')
                            n.config(text='OTP is sent to your Registered Email Id',fg='black')
                        ttk.Button(vf,text='Resend OTP',command=resend_otp).grid(row=0,column=1,padx=5,pady=5)
                        n=tk.Label(win7,text='OTP is sent to your Registered Email Id',fg='black')
                        n.pack(padx=5,pady=1)
                        def verification():
                            if otpbyc.get()!='':
                                if otpbyc.get().isdigit()==True:
                                    if datetime.now()<validity:
                                        if int(otpbyc.get())==otp:
                                            bookdt=datetime.now()
                                            global ltd,x_
                                            ltd=[]
                                            crs.execute("SELECT FLIGHT_NAME,AIRPLANES.FROM,AIRPLANES.TO,DEPARTURE,ARRIVAL,STOPS FROM AIRPLANES WHERE FLIGHT_NO='{}';".format(chfln))
                                            ffd=crs.fetchall()
                                            ltd.extend([ffd[0][0],datetime.date(bookdt)])
                                            crs.execute("SELECT TRANSACTION_ID FROM PAYMENTS;")
                                            alltid=crs.fetchall()
                                            tid=random.randint(1,999999999999999)
                                            while tid in [int(i[0]) for i in alltid]:
                                                tid=random.randint(1,9999999999999999999)
                                            ftid=('0'*(19-len(str(tid))))+str(tid)
                                            n.config(text='OTP verified, Succesfully!',fg='green')
                                            crs.execute("INSERT INTO PAYMENTS VALUES('{}','{}','{}','{}','{}','{}','{}');".format(ftid,fnc,fcnu,fed,fcvv,bookdt,gt))
                                            ani.commit()
                                            crs.execute("UPDATE SEATS SET SEATS_AVAILABLE=SEATS_AVAILABLE-{},SEATS_BOOKED=SEATS_BOOKED+{} WHERE FLIGHT_NO='{}' AND DATE_OF_JOURNEY='{}';".format(notr,notr,chfln,x_))
                                            ani.commit()
                                            allpcl=''
                                            for i in mpd:
                                                i+=(cei,ftid)
                                                if len(i)==11:
                                                    crs.execute("INSERT INTO PASSENGER_DETAILS (PASSENGER_ID,FLIGHT_NO,NAME,GENDER,TRAVELLER,CLASS,DATE_OF_JOURNEY,PHONE_NO,EMAIL_ID,AC_EMAIL_ID,TRANSACTION_ID) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",i)
                                                    ani.commit()
                                                    ltd.append((i[0],i[2]+(' '*(24-len(i[2]))),i[3],i[4]+(' '*(9-len(i[4]))),'   ','          '))
                                                    allpcl=i[5]
                                                    alcn=i[-4]
                                                    alei=i[-3]
                                                if len(i)==13:
                                                    crs.execute("INSERT INTO PASSENGER_DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",i)
                                                    ani.commit()
                                                    ltd.append((i[0],i[2]+(' '*(24-len(i[2]))),i[3],i[4]+(' '*(9-len(i[4]))),str(i[5])+(' '*(3-len(str(i[5])))),i[6]))    
                                            ltd.append((chfln+(' '*(10-len(chfln))),ffd[0][1]+(' '*(24-len(ffd[0][1]))),ffd[0][2]+(' '*(24-len(ffd[0][2]))),str(ffd[0][3])+(' '*(9-len(str(ffd[0][3])))),str(ffd[0][4])+(' '*(9-len(str(ffd[0][4])))),allpcl+(' '*(15-len(allpcl))),ffd[0][5],x_))
                                            crs.execute("SELECT FARE FROM FARE WHERE CLASS='{}' AND FARE.FROM='{}' AND FARE.TO='{}' ORDER BY FIELD (TRAVELLER,'ADULTS','CHILDREN','INFANTS');".format(allpcl,ffd[0][1],ffd[0][2]))
                                            allfare=crs.fetchall()
                                            ltd.append(('ADULTS'+(' '*(9-len('ADULTS'))),str(noa)+(' '*(16-len(str(noa)))),str(noa*allfare[0][0])+(' '*(8-len(str(noa*allfare[0][0]))))))
                                            dtrvl=1
                                            if noc>0:
                                                ltd.append(('CHILDREN'+(' '*(9-len('CHILDREN'))),str(noc)+(' '*(16-len(str(noc)))),str(noc*allfare[1][0])+(' '*(8-len(str(noc*allfare[1][0]))))))
                                                dtrvl+=1
                                            if noi>0:
                                                ltd.append(('INFANTS'+(' '*(9-len('INFANTS'))),str(noi)+(' '*(16-len(str(noi)))),str(noi*allfare[2][0])+(' '*(8-len(str(noi*allfare[2][0]))))))
                                                dtrvl+=1
                                            ltd.extend([t_c+(' '*(8-len(t_c))),str(gt)+(' '*(8-len(str(gt))))])
                                            ltd.extend([fnc+(' '*(25-len(fnc))),fcnu[-4:],str(otp)+(' '*(25-len(str(otp)))),ftid,alcn,alei+(' '*(25-len(alei)))])
                                            win7.destroy()
                                            win4.destroy()
                                            win2.destroy()
                                            ticket(ltd,noa+noc+noi,dtrvl)
                                            tm.showinfo('Payment Succesful','Transaction Completed Sucessfully!\n'+'Flight Booked Successfully!')
                                        else:
                                            n.config(text='Invalid OTP',fg='red')
                                    else:
                                        n.config(text='Invalid OTP',fg='red')
                                else:
                                    n.config(text='Invalid OTP',fg='red')
                            else:
                                n.config(text='Invalid OTP',fg='red')
                        ttk.Button(win7,text='Verify',command=verification).pack(padx=5,pady=5)
                ttk.Button(win6,text='Proceed to Pay',command=final_payment).pack(padx=5,pady=5)                
    cpm.trace('w',payment_details)
def bokhis_cantic(bc,vscb):
    vscb.pack(fill=tk.Y,side=tk.RIGHT)
    bc.configure(yscrollcommand=vscb.set)
    bc.pack(side=tk.LEFT,padx=5,pady=5)
    bc['columns']=('fno','pname','gender','trvlr','from','to','class','doj','dep','arr','pn','ea')
    bc.column('#0',width=150,anchor='c')
    bc.column('fno',width=70,anchor='c')
    bc.column('pname',width=130,anchor='c')
    bc.column('gender',width=40,anchor='c')
    bc.column('trvlr',width=80,anchor='c')
    bc.column('from',width=100,anchor='c')
    bc.column('to',width=100,anchor='c')
    bc.column('class',width=115,anchor='c')
    bc.column('doj',width=95,anchor='c')
    bc.column('dep',width=70,anchor='c')
    bc.column('arr',width=70,anchor='c')
    bc.column('pn',width=85,anchor='c')
    bc.column('ea',width=140,anchor='c')
    bc.heading('#0',text='Passenger ID')
    bc.heading('fno',text='Flight No.')
    bc.heading('pname',text='Name')
    bc.heading('gender',text='Sex')
    bc.heading('trvlr',text='Traveller')
    bc.heading('from',text='From')
    bc.heading('to',text='To')
    bc.heading('class',text='Class')
    bc.heading('doj',text='Date of Journey')
    bc.heading('dep',text='Departure')
    bc.heading('arr',text='Arrival')
    bc.heading('pn',text='Phone No.')
    bc.heading('ea',text='Email_ID')
def canceltic(cei,cpw):
    ct=tk.Toplevel(win)
    ct.iconbitmap('airplane.ico')
    ct.title('ARS Ticket Cancellation')
    fbh=tk.LabelFrame(ct,text='Booking History',font='arial 12 bold')
    fbh.pack(padx=5,pady=5)
    fct=tk.LabelFrame(ct,text='Cancellable Tickets',font='arial 12 bold')
    fct.pack(padx=5,pady=5,fill=tk.X)
    cttr=ttk.Treeview(fct,height=10)
    vsb2=ttk.Scrollbar(fct,orient="vertical",command=cttr.yview)
    bh=ttk.Treeview(fbh,height=10)
    vsb3=ttk.Scrollbar(fbh,orient="vertical",command=bh.yview)
    bokhis_cantic(bh,vsb3)
    crs.execute("SELECT PASSENGER_ID,PD.FLIGHT_NO,NAME,GENDER,TRAVELLER,AP.FROM,AP.TO,CLASS,DATE_OF_JOURNEY,AP.DEPARTURE,AP.ARRIVAL,PHONE_NO,EMAIL_ID FROM PASSENGER_DETAILS PD,AIRPLANES AP WHERE AC_EMAIL_ID='{}' AND AP.FLIGHT_NO=PD.FLIGHT_NO ORDER BY DATE_OF_JOURNEY DESC,DEPARTURE DESC;".format(cei))
    allpasng=crs.fetchall()
    for i in allpasng:
        bh.insert('',1,text=i[0],values=i[1:])
    frcnl=tk.Frame(ct)
    frcnl.pack(fill='x',padx=5)
    ctbfr=tk.Frame(frcnl)
    ctbfr.pack(side=tk.RIGHT)
    global start_ct
    start_ct=0
    def cancellable_tickets():
        global pasng,start_ct
        cttr.delete(*cttr.get_children())
        crs.execute("SELECT PASSENGER_ID,PD.FLIGHT_NO,NAME,GENDER,TRAVELLER,AP.FROM,AP.TO,CLASS,DATE_OF_JOURNEY,AP.DEPARTURE,AP.ARRIVAL,PHONE_NO,EMAIL_ID FROM PASSENGER_DETAILS PD,AIRPLANES AP WHERE AP.FLIGHT_NO=PD.FLIGHT_NO AND AC_EMAIL_ID='{}' AND ((DATE_OF_JOURNEY='{}' AND DEPARTURE>='{}') OR (DATE_OF_JOURNEY>'{}')) ORDER BY DATE_OF_JOURNEY DESC,DEPARTURE DESC;".format(cei,datetime.date(datetime.now()),datetime.time(datetime.now()+timedelta(hours=2)),datetime.date(datetime.now())))
        pasng=crs.fetchall()
        if pasng==[]:
            cttr.destroy()
            tk.Label(fct,text='No Tickets can be Cancelled as per ARS Cancellation Policy',font='arial 10').pack(padx=5,pady=5)
            ctbutn.config(state='disabled')
        else:
            if start_ct==0:
                bokhis_cantic(cttr,vsb2)
            for i in pasng:
                cttr.insert('',1,text=i[0],values=i[1:])
    def final_cancel():
        global pasng,start_ct
        start_ct+=1
        curct=cttr.focus()
        ctpid=cttr.item(curct)['text']
        ctd=cttr.item(curct)['values']
        if curct=='' or pasng==[]:
            tm.showwarning('Warning','Select a Passenger to Proceed')
        else:
            crs.execute("SELECT PASSENGER_ID FROM PASSENGER_DETAILS PD,AIRPLANES AP WHERE AP.FLIGHT_NO=PD.FLIGHT_NO AND AC_EMAIL_ID='{}' AND ((DATE_OF_JOURNEY='{}' AND DEPARTURE>='{}') OR (DATE_OF_JOURNEY>'{}'));".format(cei,datetime.date(datetime.now()),datetime.time(datetime.now()+timedelta(hours=2)),datetime.date(datetime.now())))
            cncheck=[i[0] for i in crs.fetchall()]
            if ctpid not in cncheck:
                cancellable_tickets()
                tm.showwarning('Time Up!',"Couldn't Cancel the Ticket as per Cancellation Policy.") 
            else:
                confirmed=tm.askyesno('Confirmation','Are you sure to CANCEL your ticket for passenger '+ctpid+' ?')
                if confirmed:
                    crs.execute("SELECT FLIGHT_NO,TRANSACTION_ID FROM PASSENGER_DETAILS WHERE PASSENGER_ID='{}';".format(ctpid))
                    a=crs.fetchall()
                    cnfno,cntid=a[0][0],a[0][1]
                    crs.execute("SELECT AIRPLANES.FROM,AIRPLANES.TO FROM AIRPLANES WHERE FLIGHT_NO='{}';".format(cnfno))
                    a=crs.fetchall()
                    cnfrom,cnto=a[0][0],a[0][1]
                    if ctd[3]=='ADULT':
                        ctd[3]='ADULTS'
                    elif ctd[3]=='CHILD':
                        ctd[3]='CHILDREN'
                    else:
                        ctd[3]='INFANTS'
                    crs.execute("SELECT FARE FROM FARE WHERE FARE.FROM='{}' AND FARE.TO='{}' AND TRAVELLER='{}' AND CLASS='{}';".format(cnfrom,cnto,ctd[3],ctd[6]))
                    refund=crs.fetchall()[0][0]
                    crs.execute("SELECT CARD_NUMBER FROM PAYMENTS WHERE TRANSACTION_ID='{}';".format(cntid))
                    cncardno=crs.fetchall()[0][0]
                    crs.execute("DELETE FROM PASSENGER_DETAILS WHERE PASSENGER_ID='{}';".format(ctpid))
                    ani.commit()
                    cancellable_tickets()
                    crs.execute("SELECT DISTINCT(TRANSACTION_ID) FROM PASSENGER_DETAILS;")
                    if cntid in [i[0] for i in crs.fetchall()]:
                        crs.execute("UPDATE PAYMENTS SET AMOUNT=AMOUNT-'{}' WHERE TRANSACTION_ID='{}';".format(refund,cntid))
                    else:
                        crs.execute("DELETE FROM PAYMENTS WHERE TRANSACTION_ID='{}';".format(cntid))
                    ani.commit()
                    crs.execute("UPDATE SEATS SET SEATS_AVAILABLE=SEATS_AVAILABLE+1,SEATS_BOOKED=SEATS_BOOKED-1 WHERE FLIGHT_NO='{}' AND DATE_OF_JOURNEY='{}';".format(ctd[0],ctd[7]))
                    ani.commit()
                    sub='Ticket Cancellation'
                    body='Dear Customer, Ticket of Passenger with Passengrer ID '+ctpid+' at Airline Reservation System is CANCELLED. Refund of Rs.'+str(refund)+' will be initiated within 24 hrs, to your CARD NUMBER ending with '+str(cncardno)[-4:]+'.'
                    msg=f'Subject:{sub}\n\n{body}'
                    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login(sem,spw)
                        smtp.sendmail(sem,cei,msg)
                        smtp.quit()
    defaultbg=ct.cget('bg')
    tk.Label(frcnl,text='Cancellation Policy').pack(pady=5,side=tk.LEFT)
    tk.Button(frcnl,text='(i)',underline=1,relief='flat',bg=defaultbg,fg='darkblue',font='calibri 11 italic underline',command=lambda:cancellation_policy(ct)).pack(pady=5,side=tk.LEFT)
    global ctbutn
    ctbutn=ttk.Button(ctbfr,text='Cancel Ticket',width=30,command=final_cancel)
    ctbutn.pack(side=tk.RIGHT,padx=10,pady=5)
    cancellable_tickets()
def logout(cei,cpw):
    global blogorbok,blog_cei,blog_cpw
    confirmed=tm.askyesno('Logout','Are you sure, you want to Logout?')
    if confirmed:
        menu_edit()
        blogorbok=''
        blog_cei=''
        blog_cpw=''
def login_register():
    win5=tk.Toplevel(win)
    win5.title('Login/Register')
    win5.iconbitmap('airplane.ico')
    fr8=tk.Frame(win5)
    fr8.pack()
    lf1=tk.LabelFrame(fr8,text='Log In to ARS',font='arial 12')
    lf1.pack(padx=5,pady=5)
    tk.Label(lf1,text='Email Id:').grid(padx=5,pady=5,row=0,column=0)
    ei=ttk.Entry(lf1,width=25)
    ei.grid(padx=5,pady=5,row=0,column=1)
    tk.Label(lf1,text='Password:').grid(padx=5,pady=5,row=1,column=0)
    pw=ttk.Entry(lf1,show='*',width=25)
    pw.grid(padx=5,pady=5,row=1,column=1)
    def login():
        if ei.get()=='' or pw.get()=='':
            tm.showwarning('Login','Username or Password Empty!')
        else:
            global pv,blog_cei,blog_cpw,blogorbok
            crs.execute("SELECT PASSWORD,NAME FROM ACCOUNT_DETAILS WHERE EMAIL_ID='{}';".format(ei.get()))
            pv=crs.fetchall()
            if pv==[]:
                tm.showerror('Error','Incorrect Email Id')
            else:
                if pv[0][0]==pw.get():
                    cei=ei.get()
                    cpw=pw.get()
                    if blogorbok=='book':
                        win5.destroy()
                        men.delete(0,47)
                        men.add_command(label='Hi! '+pv[0][1],state='disabled')
                        for i in range(40-int(len(pv[0][1])/2)):
                            men.add_separator()
                        men.add_command(label='Cancel Tickets',command=lambda:canceltic(cei,cpw))
                        men.add_command(label='Logout',command=lambda:logout(cei,cpw))
                        blog_cei=cei
                        blog_cpw=cpw
                        blogorbok='blog'
                        payment_button()
                        payment_booking(cei,cpw)
                    elif blogorbok=='blog':
                        win5.destroy()
                        men.delete(0,47)
                        men.add_checkbutton(label='Hi! '+pv[0][1],state='disabled')
                        for i in range(40-int(len(pv[0][1])/2)):
                            men.add_separator()
                        men.add_command(label='Cancel Tickets',command=lambda:canceltic(cei,cpw))
                        men.add_command(label='Logout',command=lambda:logout(cei,cpw))
                        blog_cei=cei
                        blog_cpw=cpw
                else:
                    tm.showerror('Error','Incorrect Password')
    def register():
        win5.destroy()
        reg=tk.Toplevel(win)
        reg.title('Registration')
        reg.iconbitmap('airplane.ico')
        cna=tk.LabelFrame(reg,text='Create New Account',font='arial 12')
        cna.pack(padx=5,pady=5)
        tk.Label(cna,text='Full Name:').grid(padx=5,pady=5,row=0,column=0)
        n=ttk.Entry(cna,width=25)
        n.grid(padx=5,pady=5,row=0,column=1)
        tk.Label(cna,text='Email Id:').grid(padx=5,pady=5,row=1,column=0)
        em=ttk.Entry(cna,width=25)
        em.grid(padx=5,pady=5,row=1,column=1)
        tk.Label(cna,text='Phone No. :').grid(padx=5,pady=5,row=1,column=2)
        ph=ttk.Entry(cna,width=25)
        ph.grid(padx=5,pady=5,row=1,column=3)
        tk.Label(cna,text='Create Password:').grid(padx=5,pady=5,row=2,column=0)
        cp=ttk.Entry(cna,width=25,show='*')
        cp.grid(padx=5,pady=5,row=2,column=1)
        tk.Label(cna,text='Confirm Password:').grid(padx=5,pady=5,row=2,column=2)
        ccp=ttk.Entry(cna,width=25,show='*')
        ccp.grid(padx=5,pady=5,row=2,column=3)
        def registration_details():
            atr=''
            for i in em.get():
                if i=='@':
                    atr=i
            if n.get()=='' or em.get()=='' or ph.get()=='' or cp.get()=='' or ccp.get()=='':
                tm.showwarning('Warning','Fill the Empty Fields')
            elif atr!='@' or em.get()[-4:]!='.com' or len(em.get())<7:
                tm.showerror('Error','Email Id is Incorrect')
            elif len(ph.get())!=10:
                tm.showerror('Error','Phone No. is Incorrect')
            elif cp.get()!=ccp.get():
                tm.showwarning('Error',"Confirmed Password doesn't match")
            else:
                breg.destroy()
                crs.execute("SELECT EMAIL_ID FROM ACCOUNT_DETAILS WHERE EMAIL_ID='{}';".format(em.get()))
                ve=crs.fetchall()
                crs.execute("SELECT PHONE_NO FROM ACCOUNT_DETAILS WHERE PHONE_NO='{}';".format(ph.get()))
                vp=crs.fetchall()
                if ve==[] and vp==[]:
                    otp=random.randint(10000,99999)
                    sub='OTP for Registration'
                    body='Dear Customer, One-Time-Password(OTP) for registration at Airline Reservation System is '+str(otp)+'. Do Not share the OTP with anyone.'
                    msg=f'Subject:{sub}\n\n{body}'
                    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login(sem,spw)
                        smtp.sendmail(sem,em.get(),msg)
                    otpfr=tk.Frame(reg)
                    otpfr.pack()
                    tk.Label(otpfr,text='Enter OTP:').grid(row=0,column=0,padx=5)
                    rgotp=ttk.Entry(otpfr)
                    rgotp.grid(row=0,column=1,padx=5)
                    bv=tk.Frame(reg)
                    bv.pack()
                    stm=tk.Label(bv,text='OTP is sent to your Email Id',fg='black')
                    stm.pack(padx=5,pady=1)
                    def regv():
                        if rgotp.get()!='':
                            if rgotp.get().isdigit()==True:
                                if int(rgotp.get())==otp:
                                    stm.config(text='Succesfully Verified',fg='green')
                                    crs.execute("INSERT INTO ACCOUNT_DETAILS VALUES('{}','{}','{}','{}');".format(n.get(),em.get(),ph.get(),ccp.get()))
                                    ani.commit()
                                    reg.destroy()
                                    login_register()
                                    tm.showinfo('Registration','Account Created Successfully! You may login now.')
                                else:
                                    stm.config(text='Invalid OTP',fg='red')
                            else:
                                stm.config(text='Invalid OTP',fg='red')
                        else:
                            stm.config(text='Invalid OTP',fg='red')
                    ttk.Button(otpfr,text='Verify',command=regv).grid(row=0,column=2,padx=5)
                else:
                    tm.showerror('Error','Email Id or Phone No. already in use!')
        global breg
        breg=ttk.Button(reg,text='Register',command=registration_details)
        breg.pack(padx=5,pady=5)
                    
    fr9=tk.Frame(win5)
    fr9.pack()
    ttk.Button(lf1,text='Sign In',width=15,command=login).grid(row=2,column=1,pady=5)
    lf2=tk.LabelFrame(fr8,text='Register to ARS',font='arial 12')
    lf2.pack(padx=5,pady=5,fill='both',expand='yes')
    tk.Label(lf2,text='New to Airline Reservation System ?').pack(pady=5,padx=5)
    ttk.Button(lf2,text='Create New Account',command=register).pack(padx=5,pady=5)
def official_login(olfw):
    ol=tk.Toplevel(win)
    ol.title('ARS Login')
    ol.iconbitmap('airplane.ico')
    olf=tk.LabelFrame(ol,text='Login - ARS Member',font='arial 14')
    olf.pack(padx=5,pady=2)
    ttk.Label(olf,text='Username:',font='arial').grid(row=0,column=0,padx=7,pady=5)
    un=ttk.Entry(olf,show='*')
    un.grid(row=0,column=1,padx=7,pady=5)
    ttk.Label(olf,text='Password:',font='arial').grid(row=1,column=0,padx=7,pady=5)
    pw=ttk.Entry(olf,show='*')
    pw.grid(row=1,column=1,padx=7,pady=5)
    log=ttk.Frame(ol)
    log.pack()
    def sign_in():
        if un.get()=='ARS@ars.com' and pw.get()=='ANI@Airlinereservsys':
            ol.destroy()
            if olfw=='eflight':
                edit_flight()
            elif olfw=='aflight':
                add_flight()
            elif olfw=='aefare':
                add_edit_fare()
            elif olfw=='aeairport':
                add_edit_airport()
        else:
            tm.showerror('Error','Incorrect Username or Password')
    ttk.Label(log,text='* For ARS Menber Only',font='arial 10').pack(padx=7)
    ttk.Button(log,text='Sign In',command=sign_in).pack(pady=5)
def flight_details(win,frame,aforef):
    global u1,u2,u3,u4_h,u4_m,u5_h,u5_m,u6,u7,u8_h,u8_m,u9,ckfn
    tk.Label(frame,text='  Flight Name:  ').grid(row=0,column=0,padx=2,pady=2)
    u1=ttk.Entry(frame)
    u1.grid(row=0,column=1,padx=2,pady=2)
    tk.Label(frame,text='From:').grid(row=1,column=0,padx=2,pady=2)
    u2=ttk.Entry(frame)
    u2.grid(row=1,column=1,padx=2,pady=2)
    tk.Label(frame,text='To:').grid(row=2,column=0,padx=2,pady=2)
    u3=ttk.Entry(frame)
    u3.grid(row=2,column=1,padx=2,pady=2)
    tk.Label(frame,text='Day:').grid(row=3,column=0,padx=2,pady=2)
    u6=ttk.Combobox(frame,width=17)
    u6['values']=['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY']
    u6.grid(row=3,column=1,padx=2,pady=2)
    tk.Label(frame,text='Stops:').grid(row=4,column=0,padx=2,pady=2)
    u7=ttk.Combobox(frame,width=17)
    u7['values']=[i for i in range(6)]
    u7.grid(row=4,column=1,padx=2,pady=2)
    frm3=tk.Frame(win)
    frm3.pack(padx=10)
    tk.Label(frm3,text='Flight Duration:').grid(row=0,column=0,padx=2,pady=2)
    u5_h=ttk.Combobox(frm3,width=3)
    u5_h['values']=[i for i in range(24)]
    u5_h.grid(row=0,column=1,padx=2,pady=2)
    tk.Label(frm3,text='H').grid(row=0,column=2)
    u5_m=ttk.Combobox(frm3,width=4)
    u5_m['values']=[i for i in range(60)]
    u5_m.grid(row=0,column=3,padx=2,pady=2)
    tk.Label(frm3,text='M').grid(row=0,column=4)
    frm2=tk.Frame(win)
    frm2.pack(padx=10)
    tk.Label(frm2,text='   Departure:   ').grid(row=0,column=0,padx=2,pady=2)
    u4_h=ttk.Combobox(frm2,width=5)
    u4_h['values']=[i for i in range(24)]
    u4_h.grid(row=0,column=1,pady=2)
    tk.Label(frm2,text=':').grid(row=0,column=2)
    u4_m=ttk.Combobox(frm2,width=5)
    u4_m['values']=[i for i in range(60)]
    u4_m.grid(row=0,column=3,pady=2)
    tk.Label(frm2,text='Arrival:').grid(row=1,column=0,padx=2,pady=2)
    u8_h=ttk.Combobox(frm2,width=5)
    u8_h['values']=[i for i in range(24)]
    u8_h.grid(row=1,column=1,pady=2)
    tk.Label(frm2,text=':').grid(row=1,column=2)
    u8_m=ttk.Combobox(frm2,width=5)
    u8_m['values']=[i for i in range(60)]
    u8_m.grid(row=1,column=3,pady=2)
    if aforef=='editflight':
        crs.execute("SELECT FLIGHT_NAME,AIRPLANES.FROM,AIRPLANES.TO,DEPARTURE,ARRIVAL,FLIGHT_DURATION,DAY,STOPS FROM AIRPLANES WHERE FLIGHT_NO='{}';".format(ckfn[0][0]))
        ifd=crs.fetchall()
        fdh=0
        wd={'SUNDAY':0,'MONDAY':1,'TUESDAY':2,'WEDNESDAY':3,'THURSDAY':4,'FRIDAY':5,'SATURDAY':6}
        u1.insert(0,ifd[0][0])
        u2.insert(0,ifd[0][1])
        u3.insert(0,ifd[0][2])
        u4_h.current((parse(str(ifd[0][3])).time()).strftime("%H"))
        u4_m.current((parse(str(ifd[0][3])).time()).strftime("%M"))
        u8_h.current((parse(str(ifd[0][4])).time()).strftime("%H"))
        u8_m.current((parse(str(ifd[0][4])).time()).strftime("%M"))
        for i in range(0,len(ifd[0][5])):
            if ifd[0][5][i]=='H':
                fdh=i
        u5_h.current(ifd[0][5][:fdh])
        u5_m.current(ifd[0][5][fdh+2:-1])
        u6.current(wd[ifd[0][6]])
        u7.current(ifd[0][7])
def arrival_check():
    if (int(u4_m.get())+int(u5_m.get()))<60:
        arrmchk=int(u4_m.get())+int(u5_m.get())
        c=0
    elif (int(u4_m.get())+int(u5_m.get()))>=60:
        arrmchk=(int(u4_m.get())+int(u5_m.get()))-60
        c=1
    if (int(u4_h.get())+int(u5_h.get()))<=23:
        arrhchk=int(u4_h.get())+int(u5_h.get())+c
    elif (int(u4_h.get())+int(u5_h.get()))>23:
        arrhchk=(int(u4_h.get())+int(u5_h.get()))-23+c
    if int(u8_m.get())!=arrmchk or int(u8_h.get())!=arrhchk:
        return True
def edit_flight():
    ef=tk.Toplevel(win)
    ef.title('Edit Flight')
    ef.iconbitmap('airplane.ico')
    frm=tk.Frame(ef)
    frm.pack(padx=10,pady=2)
    ttk.Label(frm,text='    Flight No. :  ').grid(row=0,column=0,padx=6,pady=2)
    efn=ttk.Entry(frm)
    efn.grid(row=0,column=1,padx=2,pady=2)
    frm1=tk.Frame(ef)
    frm1.pack(padx=10)
    nt=tk.Label(frm1,text='Enter the Flight No. you want to edit.')
    nt.pack(padx=5,pady=2)
    def update():
        global ckfn
        crs.execute("SELECT FLIGHT_NO FROM AIRPLANES WHERE FLIGHT_NO='{}';".format(efn.get()))
        ckfn=crs.fetchall()
        if ckfn==[]:
            nt.config(text="Entered Flight No doesn't exist",fg='red')
        else:
            global gefn
            gefn=efn.get()
            nt.destroy()
            but1.destroy()
            frm1.config(padx=5,pady=0)
            flight_details(ef,frm1,'editflight')
            def edit():
                crs.execute("SELECT FLIGHT_NO FROM AIRPLANES WHERE FLIGHT_NO='{}';".format(efn.get()))
                oc=crs.fetchall()
                if efn.get()=='' or u1.get()=='' or u2.get()=='' or u3.get()=='' or u4_h.get()=='' or u4_m.get()=='' or u5_h.get()=='' or u5_m.get()=='' or u6.get()=='' or u7.get()=='' or u8_h.get()=='' or u8_m.get()=='':
                    tm.showwarning('Empty Fields','Fill all the Fields, Correctly!')
                elif u7.get() not in u7['values'] or u6.get() not in u6['values'] or u4_h.get() not in u4_h['values'] or u4_m.get() not in u4_m['values'] or u5_h.get() not in u5_h['values'] or u5_m.get() not in u5_m['values'] or u8_h.get() not in u8_h['values'] or u8_m.get() not in u8_m['values']:
                    tm.showerror('Error','Fields are not Filled, Correctly!')
                elif oc!=[] and oc[0][0].lower()!=gefn.lower():
                    tm.showerror("Can't Update Flight",'Flight No. Already in Use')
                elif arrival_check():
                    tm.showerror("Error",'Arrival does not match as per Flight Duration')
                else:
                    confirmed=tm.askyesno('Confirmation','Are you sure, you want to make changes?')
                    if confirmed:
                        crs.execute("UPDATE AIRPLANES SET FLIGHT_NO='{}',FLIGHT_NAME='{}',AIRPLANES.FROM='{}',AIRPLANES.TO='{}',DEPARTURE='{}',ARRIVAL='{}',FLIGHT_DURATION='{}',DAY='{}',STOPS='{}' WHERE FLIGHT_NO='{}';".format(efn.get().upper(),u1.get().upper(),u2.get(),u3.get(),parse(u4_h.get()+':'+u4_m.get()).time(),parse(u8_h.get()+':'+u8_m.get()).time(),u5_h.get()+'H '+u5_m.get()+'M',u6.get(),u7.get(),gefn))
                        ani.commit()
                        crs.execute("UPDATE SEATS SET FLIGHT_NO='{}' WHERE FLIGHT_NO='{}';".format(efn.get(),gefn))
                        tm.showinfo('Update','Flight updated Succesfully!')
                        crs.execute("SELECT AC_EMAIL_ID,NAME FROM PASSENGER_DETAILS WHERE FLIGHT_NO='{}' AND DATE_OF_JOURNEY>='{}';".format(gefn,nx))
                        infp=crs.fetchall()
                        for i in infp:
                            sub='Update regarding Flight'
                            bdy1='Dear '+i[1]+' flight booked by you of Flight No.'+gefn+' at Airline Reservation System have some UPDATES:'
                            bdy2='Flight No.: '+efn.get()
                            bdy3='Flight Name: '+u1.get()
                            bdy4='From: '+u2.get()
                            bdy5='To: '+u3.get()
                            bdy6='Departure: '+u4_h.get()+':'+u4_m.get()
                            bdy7='Arrival: '+u8_h.get()+':'+u8_m.get()
                            bdy8='Flight Duration: '+u5_h.get()+'H '+u5_m.get()+'M'
                            bdy9='Stops: '+u7.get()
                            bdy10='Sorry for Inconvenience.'
                            msg=f'Subject:{sub}\n\n{bdy1}\n{bdy2}\n{bdy3}\n{bdy4}\n{bdy5}\n{bdy6}\n{bdy7}\n{bdy8}\n{bdy9}\n{bdy10}'
                            with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                                smtp.ehlo()
                                smtp.starttls()
                                smtp.ehlo()
                                smtp.login(sem,spw)
                                smtp.sendmail(sem,i[0],msg)
                                smtp.quit()
            ttk.Button(ef,text='Update',width=10,command=edit).pack(pady=10,padx=10)
    but1=ttk.Button(frm1,text='Next',command=update,width=10)
    but1.pack(padx=5,pady=5)
def add_flight():
    global aframe,aflightno
    af=tk.Toplevel(win)
    af.iconbitmap('airplane.ico')
    af.title('Add Flight')
    aframe=tk.Frame(af,bg='gray97')
    aframe.pack(fill='both',expand='yes')
    aflf=tk.LabelFrame(aframe,text='  Flight No.  ',bg='gray97')
    aflf.pack(padx=10,pady=5)
    aflightno=tk.Entry(aflf,bd=0,width=35,bg='gray97')
    aflightno.pack(padx=10,pady=5)
    def aflight_details():
        global aframe
        crs.execute("SELECT FLIGHT_NO FROM AIRPLANES WHERE FLIGHT_NO='{}';".format(aflightno.get()))
        if crs.fetchall()!=[]:
            tm.showwarning('Warning','Flight No. already exists, you can only Edit it.')
        else:
            addflightno=aflightno.get()
            aflf.destroy()
            nxt.destroy()
            aframe.destroy()
            aframe=tk.Frame(af)
            aframe.pack(padx=5)
            flight_details(af,aframe,'addflight')
            crs.execute("SELECT FARE FROM FARE WHERE FARE.FROM='{}' AND FARE.TO='{}';".format(u2.get(),u3.get(),u2.get(),u3.get()))
            s_dfare=crs.fetchall()
            def finally_add():
                if u1.get()=='' or u2.get()=='' or u3.get()=='' or u4_h.get()=='' or u4_m.get()=='' or u5_h.get()=='' or u5_m.get()=='' or u6.get()=='' or u7.get()=='' or u8_h.get()=='' or u8_m.get()=='':
                    tm.showwarning('Empty Fields','Fill all the Fields, Correctly!')
                elif u7.get() not in u7['values'] or u6.get() not in u6['values'] or u4_h.get() not in u4_h['values'] or u4_m.get() not in u4_m['values'] or u5_h.get() not in u5_h['values'] or u5_m.get() not in u5_m['values'] or u8_h.get() not in u8_h['values'] or u8_m.get() not in u8_m['values']:
                    tm.showerror('Error','Fields are not Filled, Correctly!')
                elif arrival_check():
                    tm.showerror("Error",'Arrival does not match as per Flight Duration')
                elif s_dfare==[]:
                    tm.showwarning('Error','First add all the Fares between '+u2.get()+' and '+u3.get()+'.')
                elif len(s_dfare[0])!=9:
                    tm.showerror('Error','First add all the Fares between '+u2.get()+' and '+u3.get()+'.') 
                else:
                    confirmed=tm.askyesno('Confirmation','Are you sure, you want to Add Flight?')
                    if confirmed:
                        crs.execute("INSERT INTO AIRPLANES VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(addflightno.upper(),u1.get().upper(),u2.get(),u3.get(),parse(u4_h.get()+':'+u4_m.get()).time(),parse(u8_h.get()+':'+u8_m.get()).time(),u5_h.get()+'H '+u5_m.get()+'M',u6.get(),u7.get()))
                        ani.commit()
                        af.destroy()
                        tm.showinfo('Successfull','Flight added Successfully!')
                        add_flight()
            ttk.Button(af,text='Add Flight',command=finally_add).pack(padx=5,pady=5)
    nxt=ttk.Button(aframe,text='Next',command=aflight_details)
    nxt.pack(padx=5,pady=10)
def add_edit_fare():
    aefare=tk.Toplevel(win)
    aefare.iconbitmap('airplane.ico')
    aefare.title('Add - Edit Fare')
    ftfare=tk.LabelFrame(aefare,text='Fare Details',font='arial 16')
    ftfare.pack(padx=5,pady=5,ipadx=5,ipady=5)
    tk.Label(ftfare,text='From:',font='arial 9').grid(row=0,column=0,padx=5,pady=3)
    frfrm=ttk.Entry(ftfare,width=25)
    frfrm.grid(row=0,column=1,padx=5,pady=3)
    tk.Label(ftfare,text='To:',font='arial 9').grid(row=1,column=0,padx=5,pady=3)
    frto=ttk.Entry(ftfare,width=25)
    frto.grid(row=1,column=1,padx=5,pady=3)
    tk.Label(ftfare,text='Traveller:',font='arial 9').grid(row=2,column=0,padx=5,pady=3)
    frtrvl=ttk.Combobox(ftfare,width=22)
    frtrvl.grid(row=2,column=1,padx=5,pady=3)
    frtrvl['values']=['ADULTS','CHILDREN','INFANTS']
    tk.Label(ftfare,text='Class:',font='arial 9').grid(row=3,column=0,padx=5,pady=3)
    frcl=ttk.Combobox(ftfare,width=22)
    frcl.grid(row=3,column=1,padx=5,pady=3)
    frcl['values']=['ECONOMY','PREMIUM ECONOMY','BUSINESS CLASS']
    def fare_change():
        def fare_details_check():
            crs.execute("SELECT PLACE FROM AIRPORTS WHERE PLACE IN ('{}','{}');".format(frfrm.get(),frto.get()))
            place=[]
            for i in crs.fetchall():
                for j in i:
                    place.append(j.lower())
            if frfrm.get()=='' or frto.get()=='' or frtrvl.get()=='' or frcl.get()=='':
                tm.showwarning('Fill the Blanks','Fill the Empty Fields Correctly!')
                return False
            elif frtrvl.get().upper() not in frtrvl['values'] or frcl.get().upper() not in frcl['values']:
                tm.showerror('Incorrect Values','Fields are filled Incorrectly!')
                return False
            elif place==[]:
                tm.showwarning('Unknown From - To','Add the Airports for '+frfrm.get()+' and '+frto.get()+'.')
                return False
            elif frfrm.get().lower() not in place:
                tm.showwarning('Unknown From - To','Add the Airport for '+frfrm.get()+'.')
                return False
            elif frto.get().lower() not in place:
                tm.showwarning('Unknown From - To','Add the Airport for '+frto.get()+'.')
                return False
            elif frto.get().lower()==frfrm.get().lower():
                tm.showwarning('Invalid From-To','From and To cannot be Same!')
                return False
            else:
                return True    
        if fare_details_check():
            def update_fare():
                if efare.get()=='':
                    tm.showwarning('Empty Fare','Fare cannot be Empty!')
                elif fare_details_check():
                    if fare==[]:
                        crs.execute("INSERT INTO FARE VALUES('{}','{}','{}','{}','{}');".format(frtrvl.get().upper(),efare.get(),frcl.get().upper(),frfrm.get().upper(),frto.get().upper()))
                        ani.commit()
                        tm.showinfo('Fare Update','Fare Added Successfully!')
                    else:
                        crs.execute("UPDATE FARE SET FARE='{}' WHERE TRAVELLER='{}' AND CLASS='{}' AND FARE.FROM='{}' AND FARE.TO='{}';".format(efare.get(),frtrvl.get(),frcl.get(),frfrm.get(),frto.get()))
                        ani.commit()
                        tm.showinfo('Fare Update','Fare Updated Successfully!')
                lfare.destroy()
                efare.destroy()
                nxt1.config(text='Next',command=fare_change)
            nxt1.config(text='Update',command=update_fare)
            lfare=tk.Label(ftfare,text='Fare:',font='arial 9')
            lfare.grid(row=4,column=0,padx=5,pady=3)
            efare=ttk.Entry(ftfare,width=25)
            efare.grid(row=4,column=1,padx=5,pady=3)
            crs.execute("SELECT FARE FROM FARE WHERE FARE.FROM='{}' AND FARE.TO='{}' AND TRAVELLER='{}' AND CLASS='{}';".format(frfrm.get(),frto.get(),frtrvl.get(),frcl.get()))
            fare=crs.fetchall()
            if fare!=[]:
                efare.insert(0,fare[0][0])
    nxt1=ttk.Button(aefare,text='Next',command=fare_change)
    nxt1.pack(padx=5,pady=5)
def add_edit_airport():
    aeap=tk.Toplevel(win)
    aeap.iconbitmap('airplane.ico')
    aeap.title('Add - Edit Airport')
    frmap=tk.Frame(aeap,bg='white')
    frmap.pack(fill='both',expand='yes')
    lfp=tk.LabelFrame(frmap,text=' Place ',font='arial 12',bg='white')
    lfp.grid(row=0,column=0,padx=10,pady=5)
    pl=tk.Entry(lfp,bd=0,width=45)
    pl.pack(padx=5,pady=2)
    def a_e_airport():
        crs.execute("SELECT * FROM AIRPORTS WHERE PLACE='{}';".format(pl.get()))
        airpn=crs.fetchall()
        lfan=tk.LabelFrame(frmap,text=' Airport ',font='arial 12',bg='white')
        lfan.grid(row=1,column=0,padx=10,pady=5)
        ap=tk.Entry(lfan,bd=0,width=45)
        ap.pack(padx=5,pady=2)
        def final_ap():
            if airpn==[]:
                crs.execute("INSERT INTO AIRPORTS VALUES('{}','{}');".format(pl.get(),ap.get()))
                ani.commit()
                tm.showinfo('Info','Airport added Successfully!')
            else:
                crs.execute("UPDATE AIRPORTS SET AIRPORT='{}' WHERE PLACE='{}';".format(ap.get(),pl.get()))
                ani.commit()
                tm.showinfo('Info','Airport updated Successfully!')
            lfan.destroy()
            nxt2.config(text='Next',command=a_e_airport)
        if airpn!=[]:
            ap.insert(0,airpn[0][1])
            nxt2.config(text='Update',command=final_ap)
        else:
            nxt2.config(text='Add',command=final_ap)
    nxt2=tk.Button(frmap,text='Next',font='arial 10 bold',width=10,relief='flat',bg='gray72',fg='white',activebackground='light grey',activeforeground='white',command=a_e_airport)
    nxt2.grid(row=2,column=0,padx=5,pady=5)
def cancel_tickets_blog():
    global blogorbok
    blogorbok='blog'
    login_register()
crs.execute("SELECT DISTINCT(AIRPLANES.FROM) FROM AIRPLANES;")
fromto=[i for j in crs.fetchall() for i in j]
paym=''
blogorbok=''
i=5
can_pol=0
n_x=datetime.now()
nx=datetime.date(n_x)
nd=nx.day
nm=nx.month
ny=nx.year
nt=datetime.time(n_x)
win=tk.Tk()
win.iconbitmap('airplane.ico')
win.title('Airline Reservation System - ARS')
menu_edit()
fr=tk.Frame(win)
fr1=tk.Frame(win)
fr2=tk.Frame(win)
fr.pack()
fr1.pack(padx=5)
fr2.pack(fill=tk.X)
tr=ttk.Treeview(fr1,height=5)
vsb=ttk.Scrollbar(fr1,orient="vertical",command=tr.yview)
vsb.pack(fill=tk.Y,side=tk.RIGHT)
tr.configure(yscrollcommand=vsb.set)
tr.pack(side=tk.LEFT,pady=3)
tr['columns']=('fname','from','to','dep','arr','fdurn','stops')
tr.column('#0',width=80,anchor='c')
tr.column('fname',width=100,anchor='c')
tr.column('from',width=110,anchor='c')
tr.column('to',width=110,anchor='c')
tr.column('dep',width=80,anchor='c')
tr.column('arr',width=80,anchor='c')
tr.column('fdurn',width=90,anchor='c')
tr.column('stops',width=70,anchor='c')
tr.heading('#0',text='Flight No.')
tr.heading('fname',text='Flight Name')
tr.heading('from',text='From')
tr.heading('to',text='To')
tr.heading('dep',text='Departure')
tr.heading('arr',text='Arrival')
tr.heading('fdurn',text='Flight Duration')
tr.heading('stops',text='Stops')
tk.Label(fr,text='From:').grid(row=0,column=0,padx=5,pady=5)
varfrm=tk.StringVar()
varto=tk.StringVar()
e1=ttk.Entry(fr,textvariable=varfrm)
lbc=0
def sug(*args,var):
    global lbc,l
    if lbc>0:
        l.destroy()
        lbc-=1
    if var.get()!='':
        l=tk.Listbox(win)
        if var==varfrm:
            l.place(x=60,y=28)
        elif var==varto:
            l.place(x=229,y=28)
        lbc+=1
        b=-1
        for i in fromto:
            if var.get().lower()==i[:len(var.get())].lower():
                b+=1
                l.insert(0,i)
        l.config(height=b+1)
        def lselect(*args):
            var.set(str((l.get(tk.ACTIVE))))
        l.bind('<<ListboxSelect>>',lselect)
        if l.get(0,b)==() or var.get() in l.get(0,b):
            l.destroy()
            lbc-=1
varfrm.trace('w',lambda a='',b='',c='': sug(var=varfrm))
varto.trace('w',lambda a='',b='',c='': sug(var=varto))
e1.grid(row=0,column=1,padx=1,pady=5)
tk.Label(fr,text='   To:').grid(row=0,column=2,padx=5,pady=5)
e2=ttk.Entry(fr,textvariable=varto)
e2.grid(row=0,column=3,padx=1,pady=5)
tk.Label(fr,text='   Date:').grid(row=0,column=4,padx=5,pady=5)
def date_limit(*args):
    yrs=int(e3_3.get())
    if int(e3_2.get())==1 or int(e3_2.get())==3 or int(e3_2.get())==5 or int(e3_2.get())==7 or int(e3_2.get())==8 or int(e3_2.get())==10 or int(e3_2.get())==12:
        e3_1['values']=[i for i in range(1,32)]
        if int(e3_1.get())>31:
            e3_1.current(30)
    elif int(e3_2.get())==4 or int(e3_2.get())==6 or int(e3_2.get())==9 or int(e3_2.get())==11:
        e3_1['values']=[i for i in range(1,31)]
        if int(e3_1.get())>30:
            e3_1.current(29)
    elif (int(e3_2.get())==2 and yrs%400==0) or (int(e3_2.get())==2 and yrs%4==0 and yrs%100!=0):
        e3_1['values']=[i for i in range(1,30)]
        if int(e3_1.get())>29:
            e3_1.current(28)
    else:
        e3_1['values']=[i for i in range(1,29)]
        if int(e3_1.get())>28:
            e3_1.current(27)
e3_1=ttk.Combobox(fr,width='5')
e3_2=ttk.Combobox(fr,width='5')
e3_3=ttk.Combobox(fr,width='7')
e3_1['values']=[i for i in range(1,32)]
e3_1.current(nd-1)
e3_2['values']=[i for i in range(1,13)]
e3_2.current(nm-1)
e3_3['values']=[i for i in range(ny,ny+6)]
e3_3.current(0)
e3_1.bind("<<ComboboxSelected>>",date_limit)
e3_2.bind("<<ComboboxSelected>>",date_limit)
e3_3.bind("<<ComboboxSelected>>",date_limit)
e3_1.grid(row=0,column=5,padx=1,pady=5)
e3_2.grid(row=0,column=6,padx=1,pady=5)
e3_3.grid(row=0,column=7,padx=1,pady=5)
ttk.Button(fr,text='Search',command=search_flight,width=10).grid(row=0,column=8,padx=5,pady=5)
fltr=ttk.Menubutton(fr,text='Filters')
fltr.grid(row=0,column=9,padx=5,pady=5)
fltr.menu=tk.Menu(fltr,tearoff=0)
fltr["menu"]=fltr.menu
crs.execute("SELECT DISTINCT(FLIGHT_NAME) FROM AIRPLANES;")
allfname=crs.fetchall()
ffln=tk.Menu(fltr,tearoff=0)
dicfn={}
def filter_in_flightname(flightname,adordel):
    if adordel==('1'+flightname):
        aflna.append(flightname)
    elif adordel==('0'+flightname):
        aflna.remove(flightname)
for i in allfname:
    for j in i:
        dicfn[j]=tk.StringVar()
        ffln.add_checkbutton(label=j,variable=dicfn[str(j)],onvalue='1'+j,offvalue='0'+j,command=lambda f=j:filter_in_flightname(f,dicfn[f].get()))
fltr.menu.add_cascade(label="Flight Name ",menu=ffln)
crs.execute("SELECT DISTINCT(STOPS) FROM AIRPLANES;")
alstops=crs.fetchall()
fstp=tk.Menu(fltr,tearoff=0)
dicstp={}
def filter_in_stops(stop,adordel):
    if adordel==('1'+stop):
        alstps.append(int(stop))
    elif adordel==('0'+stop):
        alstps.remove(int(stop))
for i in alstops:
    for j in i:
        dicstp[str(j)]=tk.StringVar()
        fstp.add_checkbutton(label=str(j),variable=dicstp[str(j)],onvalue='1'+str(j),offvalue='0'+str(j),command=lambda f=str(j):filter_in_stops(f,dicstp[f].get()))
fltr.menu.add_cascade(label="Stops",menu=fstp)     
ttk.Button(fr2,text='Book',command=book_flight,width=10).pack(side=tk.RIGHT,padx=20,pady=5)
tk.mainloop()
    
