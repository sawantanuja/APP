from tkinter import*
from tkinter import ttk,filedialog,messagebox
import os,shutil

class Sorting_App:
    def __init__(self,root):
        self.root=root
        self.root.title("Sorting Application")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.logo_icon=PhotoImage(file="D:\\images\\folders.png")
        title=Label(self.root,text="Files Sorting Application",image=self.logo_icon,compound=LEFT,padx=10,font=("impact",40),bg="#023548",fg="white",anchor="w").place(x=0,y=0,relwidth=1)
        
        self.var_foldername=StringVar()
        lbl_selc_fold=Label(self.root,text="Select Folder",font=("times new roman",20,"bold"),bg="white").place(x=30,y=150)
        txt_fol_name=Entry(self.root,textvariable=self.var_foldername,font=("times new roman",15,"bold"),state="readonly",bg="lightyellow").place(x=220,y=150,height=40,width=680)
        btn_browse=Button(self.root,command=self.browse_function,text="Browse",font=("times new roman",20,"bold"),bg="#262626",fg="white",activebackground="#262626",activeforeground="white",cursor="hand2").place(x=990,y=150,height=40,width=140)
        hr=Label(self.root,bg="lightgray").place(x=20,y=200,height=2,width=1500)


          #==========All Extensions=====
        self.image_extension=["Image Extension",".png",".jpg"]
        self.audio_extension=["Audio Extension",".mp3",".amr"]
        self.video_extension=["Video Extension",".mp4",".avi",".mpeg4",".3gp"]
        self.doc_extension=["Document Extension",".doc",".xlsx",".ppt",".pdf"]

        self.folders={
                    'videos':self.video_extension,
                    'audios':self.audio_extension,
                    'images':self.image_extension,
                    'documents':self.doc_extension
                }
                

        lbl_support_ext=Label(self.root,text="Various Extension Supports",font=("times new roman",25,"bold"),bg="white").place(x=20,y=210)
        self.image_box=ttk.Combobox(self.root,values=self.image_extension,font=("times new roman",15,),state="readonly",justify=CENTER)
        self.image_box.place(x=80,y=280,width=270,height=35)
        self.image_box.current(0)


        self.video_box=ttk.Combobox(self.root,values=self.video_extension,font=("times new roman",15,),state="readonly",justify=CENTER)
        self.video_box.place(x=450,y=280,height=35,width=270)
        self.video_box.current(0)

        
        self.audio_box=ttk.Combobox(self.root,values=self.audio_extension,font=("times new roman",15,),state="readonly",justify=CENTER)
        self.audio_box.place(x=850,y=280,height=35,width=270)
        self.audio_box.current(0)

        
        self.doc_box=ttk.Combobox(self.root,values=self.doc_extension,font=("times new roman",15,),state="readonly",justify=CENTER)
        self.doc_box.place(x=1200,y=280,height=35,width=270)
        self.doc_box.current(0)

         #=========All Imageicons=======#
        self.image_icon=PhotoImage(file="D:\\images\\img.png")
        self.video_icon=PhotoImage(file="D:\\images\\video.png")
        self.audio_icon=PhotoImage(file="D:\\images\\audio.png")
        self.doc_icon=PhotoImage(file="D:\\images\\doc.png")
        self.other_icon=PhotoImage(file="D:\\images\\other.png")

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=20,y=360,width=1460,height=350)
        self.lbl_total_files=Label(Frame1,font=("times new roman",15,"bold"),bg="white")
        self.lbl_total_files.place(x=20,y=10)

        self.lbl_total_image=Label(Frame1,bd=2,relief=RAISED,image=self.image_icon,compound=TOP,font=("times new roman",12,"bold"),bg="#0875B7",fg="white")
        self.lbl_total_image.place(x=10,y=40,width=230,height=250)

        self.lbl_total_video=Label(Frame1,bd=2,relief=RAISED,image=self.video_icon,compound=TOP,font=("times new roman",12,"bold"),bg="#DF002A",fg="white")
        self.lbl_total_video.place(x=290,y=40,width=230,height=250)

        self.lbl_total_audio=Label(Frame1,bd=2,relief=RAISED,image=self.audio_icon,compound=TOP,font=("times new roman",12,"bold"),bg="#008EA4",fg="white")
        self.lbl_total_audio.place(x=570,y=40,width=230,height=250)

        self.lbl_total_doc=Label(Frame1,bd=2,relief=RAISED,image=self.doc_icon,compound=TOP,font=("times new roman",12,"bold"),bg="#0875B7",fg="white")
        self.lbl_total_doc.place(x=860,y=40,width=230,height=250)

        self.lbl_total_other=Label(Frame1,bd=2,relief=RAISED,image=self.other_icon,compound=TOP,font=("times new roman",12,"bold"),bg="#0875B7",fg="white")
        self.lbl_total_other.place(x=1200,y=40,width=230,height=250)

        lbl_status=Label(self.root,text="STATUS",font=("times new roman",25,"bold"),bg="white").place(x=40,y=730)
        self.lbl_st_total=Label(self.root,text="",font=("times new roman",25,"bold"),bg="white",fg="green")
        self.lbl_st_total.place(x=270,y=730)
        self.lbl_st_move=Label(self.root,text="",font=("times new roman",25,"bold"),bg="white",fg="blue")
        self.lbl_st_move.place(x=500,y=730)
        self.lbl_st_left=Label(self.root,text="",font=("times new roman",25,"bold"),bg="white",fg="orange")
        self.lbl_st_left.place(x=800,y=730)
        
         #=======Buttons=========#
        self.btn_clear=Button(self.root,text="CLEAR",command=self.clear,font=("times new roman",20,"bold"),bg="#607d8b",fg="white",activebackground="#262626",activeforeground="white",cursor="hand2")
        self.btn_clear.place(x=1050,y=730,height=40,width=140)

        self.btn_start=Button(self.root,text="START",state=DISABLED,command=self.start_function,font=("times new roman",20,"bold"),bg="#ff5722",fg="white",activebackground="#262626",activeforeground="white",cursor="hand2")
        self.btn_start.place(x=1250,y=730,height=40,width=140)

    def Total_Count(self):
        images=0
        videos=0
        audios=0
        documents=0
        others=0
        self.count=0
        cbine_list=[]
        for i in self.all_files:
             if os.path.isfile(os.path.join(self.directory,i))==True:
                 self.count+=1
                 ext="."+i.split(".")[-1]
                 for folder_name in self.folders.items():
                    #  print(folder_name)
                    for x in folder_name[1]:
                        cbine_list.append(x)
                    if  ext in folder_name[1] and folder_name[0]=="images":  
                        images+=1
                    if ext in folder_name[1] and folder_name[0]=="videos":  
                        videos+=1
                    if ext in folder_name[1] and folder_name[0]=="audios":  
                        audios+=1
                    if ext in folder_name[1] and folder_name[0]=="documents":  
                        documents+=1
        #======For calculating other file=======#               
        for i in self.all_files:
             if os.path.isfile(os.path.join(self.directory,i))==True:
                 ext="."+i.split(".")[-1]
                 if ext.lower() not in cbine_list:
                     others+=1
        self.lbl_total_image.config(text="Total Images:"+  str(images))
        self.lbl_total_video.config(text="Total Videos:"+  str(videos))
        self.lbl_total_audio.config(text="Total Audios:"+  str(audios))
        self.lbl_total_doc.config(text="Total Documents:"+  str(documents))
        self.lbl_total_other.config(text="Other Files:"+  str(others))
        self.lbl_total_files.config(text="Total Files: "+str(self.count))


    def browse_function(self):
        op=filedialog.askdirectory(title="SELECT FOLDER FOR SORTING") 
        if op!=None:
            # print(op)
            self.var_foldername.set(str(op))
            self.directory=self.var_foldername.get() 
            self.other_name="others"
            self.rename_folder()
            self.all_files=os.listdir(self.directory)
            length=len(self.all_files)
            self.count=1
            self.Total_Count()
            self.btn_start.config(state=NORMAL)
           
    

    def start_function(self):
        if self.var_foldername.get()!="":
            self.btn_clear.config(state=DISABLED)
            c=0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directory,i))==True:
                    c+=1
                    self.create_move(i.split(".")[-1],i) 
                    self.lbl_st_total.config(text="TOTAL: "+str(self.count))
                    self.lbl_st_move.config(text="MOVED: "+str(c))
                    self.lbl_st_left.config(text="LEFT: "+str(self.count-c))

                    self.lbl_st_total.update()
                    self.lbl_st_move.update()
                    self.lbl_st_left.update()
                    
            messagebox.showinfo("Success" ,"All Files Has Moved Successfully")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)


        else:
            messagebox.showerror("Error","Please select folder")

    def clear(self):
        self.btn_start.config( state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text= " ")
        self.lbl_st_move.config(text="")
        self.lbl_st_left.config(text="")
        self.lbl_total_image.config(text="")
        self.lbl_total_video.config(text=":")
        self.lbl_total_audio.config(text="")
        self.lbl_total_doc.config(text="")
        self.lbl_total_other.config(text=":")
        self.lbl_total_files.config(text="Total Files")

        


    def rename_folder(self):
        for folder in os.listdir(self.directory):
            if os.path.isdir(os.path.join(self.directory,folder))==True:
                os.rename(os.path.join(self.directory,folder),os.path.join(self.directory,folder.lower()))


    def create_move(self,ext,file_name):
        find=False
        for folder_name in self.folders:
            find=False
            if "."+ext in self.folders[folder_name]:
                if folder_name not in  os.listdir(self.directory):
                    os.mkdir(os.path.join(self.directory,folder_name))
                shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,folder_name))
                find=True
                break
        
        if find!=True:
            if self.other_name not in os.listdir(self.directory):
                os.mkdir(os.path.join(self.directory,self.other_name))
            shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,self.other_name))

    
root=Tk()
obj=Sorting_App(root)
root.mainloop()




        
    
  

