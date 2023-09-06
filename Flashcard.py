import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox as mb

questions=[
    "Fatehpur Sikri was founded as the capital of the Mughal Empire by ______.",
    "What is the maximum number of Members in Lok Sabha?",
    "Dayanand Saraswati was the founder of which of the following missions? ",
    "English is the official language of _________.",
    "Panna National Park is in which state?",
    "World Tourism Day is celebrated on-",
    "When is the International Yoga Day celebrated ?",
    "Prime Minister Narendra Modi launched 'Swachha Bharat Mission' officially on -",
    "'Ozone Layer Preservation Day' is celebrated on -",
    "Organization related to 'Red Data Book' or 'Red List' is -",
]

answer_choice=[
    ["Jahangir","Akbar","Babur","Humayun"],
    ["512","542","552","532"],
    ["Arya Samaj","Prarthana Samaj","Brahmo Samaj","Chinmaya Mission"],
    ["Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Delhi"],
    ["Rajasthan","Maharashtra","Gujarat","Madhya Pradesh"],
    ["September 12","September 25","September 27","September 29"],
    ["June 21","March 21","April 22","May 31"],
    ["Independence Day","Republic Day","Gandhi Jayanti","Environment Day"],
    ["16th September","5th June","23rd March","21st April"],
    ["U.T.E.S.","I.U.C.N.","I.B.W.C.","W.W.F."],
]

answers=[1,2,0,0,3,2,0,2,0,1]
user_ans=[]

indexes=[]
def gen():
    global indexes
    while(len(indexes)<5):
        x=random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
def showresult(score):
    lbl_ques.destroy()
    r1.destroy() 
    r2.destroy()
    r3.destroy()
    r4.destroy()
    lbl.destroy()

    root.config(background="white") 
      
    lbl_img=Label(root,background="white",border=0)
    lbl_img.pack(pady=(50,30))
    label_result=Label(root,font=("Consolas",20),background="white")
    label_result.pack()
    
    if score>=20:
        img=PhotoImage(file="great.png")
        lbl_img.configure(image=img)
        lbl_img.image=img
        label_result.configure(text="You are Excellent...")
    elif score<20 and score>=10:
        img=PhotoImage(file="ok.png")
        lbl_img.configure(image=img)
        lbl_img.image=img
        label_result.configure(text="You can be Better...")
    else:
        img=PhotoImage(file="bad.png")
        lbl_img.configure(image=img)
        lbl_img.image=img
        label_result.configure(text="You Should Work Hard!!")    
            
            
def calc():
    global indexes,user_ans,answers 
    x=0
    score=0 
    for i in indexes:
        if user_ans[x]==answers[i]:
            score=score+5
        x+=1
    print(score)
    showresult(score)    
    mb.showinfo("Result",f"Your Score is: {score}\nThanks for Participating Quiz")
              
ques=1
def selected():
    global rad_btn,user_ans 
    global lbl_ques,r1,r2,r3,r4
    global ques
    x=rad_btn.get() 
    user_ans.append(x)
    rad_btn.set(-1)          
    if ques<5:
        lbl_ques.config(text=questions[indexes[ques]])
        r1['text']=answer_choice[indexes[ques]][0]
        r2['text']=answer_choice[indexes[ques]][1]
        r3['text']=answer_choice[indexes[ques]][2]
        r4['text']=answer_choice[indexes[ques]][3]
        ques +=1
    else:
        print(indexes)
        print(user_ans)
        calc()   
   

    
def startquiz():
    global lbl_ques,r1,r2,r3,r4,lbl
    
    lbl_ques=Label(root,text=questions[indexes[0]],font=("Franklin Gothic",20),width=700,justify="center",wraplength=400,fg="black",background="white")
    lbl_ques.pack(pady=(100,30))
    
    global rad_btn
    rad_btn=IntVar()
    rad_btn.set(-1)

    r1=Radiobutton(root,text=answer_choice[indexes[0]][0],font=("Franklin Gothic Book",12),value=0,variable=rad_btn,command=selected,background="blue",fg="white")
    r1.pack(pady=10) 
    r1.place(x=250,y=210) 

    r2=Radiobutton(root,text=answer_choice[indexes[0]][1],font=("Franklin Gothic Book",12),value=1,variable=rad_btn,command=selected,background="blue",fg="white")
    r2.pack(pady=5) 
    r2.place(x=250,y=240)    

    r3=Radiobutton(root,text=answer_choice[indexes[0]][2],font=("Franklin Gothic Book",12),foreground="white",highlightcolor="red",value=2,variable=rad_btn,command=selected,background="blue")
    r3.pack(pady=5)
    r3.place(x=250,y=270)     

    r4=Radiobutton(root,text=answer_choice[indexes[0]][3],font=("Franklin Gothic Book",12),value=3,variable=rad_btn,command=selected,background="blue",fg="white")
    r4.pack(pady=5) 
    r4.place(x=250,y=300) 
    
    lbl=Label(root,text="*******MY Quiz*******",font=("algerian",20),background="blue",fg="white")
    
    lbl.place(x=230,y=450)
        

def startispressed():
    label_image.destroy()
    label_text.destroy()
    btn_start.destroy()
    inst.destroy()
    rule.destroy()
    
    gen()
    root.config(background="blue")
    startquiz()
    

root = Tk()

root.title("My Quiz")
root.geometry("700x600")
root.config(background="white")
root.resizable(0,0)

img1=PhotoImage(file="transparentGradHat.png")
label_image = Label(root,image = img1,background="white")
label_image.pack(pady=(40,0))

label_text=Label(root,text="Welcome to My Quiz",background="white",font=("georgia",20))
label_text.pack()

img2=PhotoImage(file="Frame.png")
btn_start=Button(root,image=img2,border=0,relief=FLAT,command=startispressed,background='white')
btn_start.pack(pady=(20,0))

inst=Label(root,text="Read The Rules And\nClick Start Once You are ready",background="white",font=("Imprint MT shadow",14),justify="center")

inst.pack(pady=(30,0))

rule=Label(root,text="This quiz contains 5 quetions and Each Question is 5 Point\nOnce you select a radio button that will be a final choice\nHence think before you select",
          width=100,
           font=("time",14),
           background="black",
           foreground="yellow"
          )
rule.pack(pady=(105,0))
root.mainloop()


