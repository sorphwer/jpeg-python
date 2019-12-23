import tkinter as tk
from PIL import Image,ImageTk
import encoder
import decoder
# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()
window.geometry('600x800')
top_frame = tk.Frame(window)
windowWidth=600
windowHeight=800
screenWidth,screenHeight = window.maxsize()
geometryParam = '%dx%d+%d+%d'%(windowWidth, windowHeight, (screenWidth-windowWidth)/2, (screenHeight - windowHeight)/2)

window.geometry(geometryParam)
window.wm_attributes('-topmost',1)

#img=Image.open('DSC0030.jpg')
#image_file=ImageTk.PhotoImage(img)
image_file=None
img=None
label_img = tk.Label(window,image=image_file)
label_img.pack()

# 將元件分為 top/bottom 兩群並加入主視窗
top_frame.pack()
bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)

# 建立事件處理函式（event handler），透過元件 command 參數存取
def echo_hello():
    print('hello world :)')

def fresh():
    global img
    global image_file
    url1="test1.jpg"
    img = Image.open(url1)
    image_file= ImageTk.PhotoImage(img)
    label_img.configure(image = image_file)
    #image=canvas.create_image(0,0,anchor="nw",image=image_file)
    window.update_idletasks()
    print("fresh?")

# 以下為 top 群組

# 以下為 bottom 群組
# bottom_button 綁定 echo_hello 事件處理，點擊該按鈕會印出 hello world :)
bottom_button = tk.Button(bottom_frame ,text='fresh', fg='black', command=fresh)
bottom_button1 = tk.Button(bottom_frame ,text='fresh1', fg='black', command=fresh)
bottom_button2 = tk.Button(bottom_frame ,text='fresh2', fg='black', command=fresh)
# 讓系統自動擺放元件（靠下方）
bottom_button.pack(side=tk.LEFT)
bottom_button1.pack(side=tk.LEFT)
bottom_button2.pack(side=tk.LEFT)
# 運行主程式
window.mainloop()