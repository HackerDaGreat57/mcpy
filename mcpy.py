from tkinter import *
from turtle import *
from PIL import * #pip install pillow
import time
from openal import * #pip install pyopenal
import random
import sys
from OpenGL.GL import * #pip install pyopengl
from OpenGL.GLU import * #pip install pyopengl
import glfw #pip install glfw

if not glfw.init():
    raise Exception("GLFW can not be initialized!")

indev = ("This partition under development.")
button_sound = oalOpen(r"C:\src\python3\projects\mcpy\minecraftFiles\audio\button\buttonclick.wav")
window = Tk()
w = 1366
h = 768
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.title('Minecraft: Python Edition')
window.resizable(False, False)
frame = Frame(window)
width = 1366
height = 768

#All def functions listed here

def create_new_world():
    #Destroy Tkinter Window, play button sound
    button_sound.play()
    #window.destroy()
    
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 6)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)

    window = glfw.create_window(width, height, "Minecraft: Python Edition (Singleplayer)", None, None)

    if not window:
        glfw.terminate()
        raise Exception("glfw window can not be created!")
    
    framebuffer_size = glfw.get_framebuffer_size(window)
    
    def framebuffer_size_callback(*args, **kwargs):
        glViewport(0, 0, framebuffer_size[0], framebuffer_size[1])
    
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)
    glfw.set_window_pos(window, 400, 200)
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClearColor(1.0, 0.0, 0.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT)
        
        glfw.poll_events()
        glfw.swap_buffers(window)

    glfw.terminate()

def tkinter_background_sound():
    picker = random.choice(["m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8", "m9", "m10", "m11", "m12"])
    if picker == "m1":
        source1 = oalOpen(r"C:\src\python3\projects\mcpy\minecraftFiles\audio\tkinter_background\m1.wav")
        source1.play()
        #oalQuit()
    
    if picker == "m2":
        source2 = oalOpen(r"C:\src\python3\projects\mcpy\minecraftFiles\audio\tkinter_background\m2.wav")
        source2.play()
        #oalQuit()

    if picker == "m3":
        source3 = oalOpen(r"C:\src\python3\projects\mcpy\minecraftFiles\audio\tkinter_background\m3.wav")
        source3.play()
        #oalQuit()
    
    if picker == "m4":
        source4 = oalOpen(r"C:\src\python3\projects\mcpy\minecraftFiles\audio\tkinter_background\m4.wav")
        source4.play()
        #oalQuit()
    
    if picker == "m5":
        source5 = oalOpen(r"C:\src\python3\projects\mcpy\minecraftFiles\audio\tkinter_background\m5.wav")
        source5.play()
        #oalQuit()
    
    if picker == "m6":
        source6 = oalOpen(r"C:\src\python3\projects\mcpy\minecraftFiles\audio\tkinter_background\m6.wav")
        source6.play()
        #oalQuit()
    
    if picker == "m7":
        source7 = oalOpen(r"C:\src\python3\projects\mcpy\minecraftFiles\audio\tkinter_background\m7.wav")
        source7.play()
        #oalQuit()
    
    if picker == "m8":
        source8 = oalOpen(r"C:\src\python3\projects\mcpy\minecraftFiles\audio\tkinter_background\m8.wav")
        source8.play()
        #oalQuit()
    
    if picker == "m9":
        source9 = oalOpen(r"C:\src\python3\projects\mcpy\minecraftFiles\audio\tkinter_background\m9.wav")
        source9.play()
        #oalQuit()
    
    if picker == "m10":
        source10 = oalOpen(r"C:\src\python3\projects\mcpy\minecraftFiles\audio\tkinter_background\m10.wav")
        source10.play()
        #oalQuit()
    
    if picker == "m11":
        source11 = oalOpen(r"C:\src\python3\projects\mcpy\minecraftFiles\audio\tkinter_background\m11.wav")
        source11.play()
        #oalQuit()

    if picker == "m12":
        source12 = oalOpen(r"C:\src\python3\projects\mcpy\minecraftFiles\audio\tkinter_background\m12.wav")
        source12.play()
        #oalQuit()
tkinter_background_sound()
window.lift()

def settings_page():
    #Place all settings widgets
    back_to_home.place(x = 20, y = 20)
    render_distance_text.place(x = 2, y = 74)
    video_settings_button.place(x = 200, y = 200)
    render_distance_slider.place(x = 2, y = 95)
    video_settings_button.place
    button_sound.play()
    
    #Remove all home screen widgets
    play_button.place_forget()
    settings_button.place_forget()
    made_by_label.place_forget()
    version_number.place_forget()
    logo_place.place_forget()
    quit_button.place_forget()

def show_video_settings():
    print(indev)
    button_sound.play()

def back_to_home_com():
    render_distance_text.place_forget()
    render_distance_slider.place_forget()
    create_new_world_button.place_forget()
    back_to_home.place_forget()
    create_world.place_forget()
    world_list_box_yscrollbar.place_forget()
    world_list_box.place_forget()
    video_settings_button.place_forget()
    
    logo_place.place(x = 407, y = 85)
    
    play_button.place(x = 567, y = 320)
    settings_button.place(x = 572, y = 400)
    quit_button.place(x = 559, y = 600)
    made_by_label.place(x = 1, y = 726)
    version_number.place(x = 1209, y = 726)
    background_image_home_place.place(x = 0, y = 0)
    frame.pack(padx = 1000, pady = 1000)
    button_sound.play()

def world_generation_options():
    #Get rid of world list widgets
    create_new_world_button.place_forget()
    world_list_box.place_forget()
    
    #Make the world generation options (UI is defined in the 2D widgets section).
    create_world.place(x = 2, y = 40)
    back_to_home.place_forget()
    back_to_home.place(x = 2, y = 2)
    button_sound.play()
    
def world_list():
    #Get rid of most of the home screen widgets.
    play_button.place_forget()
    settings_button.place_forget()
    made_by_label.place_forget()
    version_number.place_forget()
    logo_place.place_forget()
    quit_button.place_forget()
    
    #Placement for all buttons and lists listed here
    
    button_sound.play()
    world_list_box.place(x = 2, y = 145)
    create_new_world_button.place(x = 200, y = 30)
    back_to_home.place(x = 20, y = 20)

def exit_game():
    button_sound.play()
    oalQuit()
    time.sleep(0.01)
    sys.exit()
 
#All 2D widgets on first Tkinter window defined here
background_image_home = PhotoImage(file = r"C:\src\python3\projects\mcpy\minecraftFiles\tkinter_img\background_edited_png.png")

background_image_home_place = Label(window, image = background_image_home, bg = 'white')

background_image_home_place.place(x = 0, y = 0)

logo = PhotoImage(file = r"C:\src\python3\projects\mcpy\minecraftFiles\tkinter_img\title.png")

logo_place = Label(window, image = logo)

logo_place.place(x = 407, y = 85)

play_button = Button(window, bd = 4, height = 3, width = 23, font = 'Minecraft', text = 'Play',
                     activebackground = 'green', command = world_list)

quit_button = Button(window, bd = 4, activebackground = 'purple', height = 2, width = 25, font = 'Minecraft', text = 'Quit Game', command = exit_game)

settings_button = Button(window, bd = 4, height = 2, width = 22, font = 'Minecraft', text = 'Settings', activebackground = 'green', command = settings_page)

made_by_label = Label(window, font = ('Minecraft', 22), text = 'By Akshat')

version_number = Label(window, font = ('Minecraft', 22), text = 'Alpha 0.0.1')

create_new_world_button = Button(window, bd = 4, height = 2, width = 22, font = ('Minecraft', 20), text = 'Create New World',
                                 activebackground = 'green', command = world_generation_options)

back_to_home = Button(window, bd = 4, width = 4, font = 'Minecraft', text = 'Back', activebackground = 'green', command = back_to_home_com)

world_list_box = Listbox(window, selectbackground = 'green', height = 38 , width = 223, selectmode = DISABLED)
world_list_box_yscrollbar = Scrollbar(window)
world_list_box.config(yscrollcommand = world_list_box_yscrollbar.set)
world_list_box.insert(1, 'Listbox currently under development. To go into a new world, click "Create New World"')
world_list_box_yscrollbar.config(command = world_list_box.yview)

#World Generation Options UI defined here
create_world = Button(window, bd = 4, height = 3, width = 23, font = 'Minecraft', text = 'Create', activebackground = 'green', command = create_new_world)

#Settings UI, divided into groups
video_settings_button = Button(window, bd = 4, font = 'Minecraft', text = 'Video Settings', command = show_video_settings)
coming_soon_label_video = Label(window, font = 'Minecraft', text = "Video settings don't do anything yet, but they will in Alpha 0.0.3.")

#Video settings
render_distance_text = Label(window, text = 'Render Distance (in chunks):')
render_distance_slider = Scale(window, from_=1, to_=64, length = 150, orient = HORIZONTAL, activebackground = 'green')

#Padding for every paddable widget on the home screen (except images) listed here
play_button.place(x = 567, y = 320)
settings_button.place(x = 572, y = 400)
quit_button.place(x = 559, y = 600)
made_by_label.place(x = 1, y = 726)
version_number.place(x = 1209, y = 726)
frame.pack(padx = 1000, pady = 100)
window.lift()

window.mainloop()
#window.lift()
