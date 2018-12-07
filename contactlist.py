from tkinter import *
#creating Logic
# f_name='name'

# contact_l={
#     'f_name':f_name
#     # 'l_name':l_name
#     # 'p_number':p_number

# }




# Creating window and widgets
window=Tk()
window.title('Contact list')
window.configure(bg='black')
t_frame=Frame(window)
c_frame=Frame(window)
s_frame=Frame(window)
t_frame.configure(bg='green')
c_frame.configure(bg='black')
title=Label(t_frame,text='Contact',bg ='yellow',width=125)

  

#   Function to get name entered in the search  frame after button is clicked
def name():
    con=search.get()
    
    con_list=[con]
    contact_l.configure(text=con_list)
        
    for l in range(0,len(con_list)):
        if l==0:
            l=l+1
            app=search.get()
            con_list.append(app)  
            contact_l.configure(text=con_list.append(app))
        
        
            
    print(con_list)

a_btn=Button(s_frame,text='Add',command=name)
contact_l=Label(c_frame,height=125,bg='white',text='This is where contacts display',width=125)
search=Entry(s_frame)




# Displaying in window
title.pack(padx=12,pady=12)
a_btn.pack(side=RIGHT,padx=5)
search.pack(side=LEFT)
contact_l.pack(padx=12,pady=12)
t_frame.pack(padx=30,pady=30)
s_frame.pack(padx=20,pady=20)
c_frame.pack(padx=30,pady=30)
# contact_l.configure(text=name)


window.mainloop()

