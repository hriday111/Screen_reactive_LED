import keyboard
import time
import ctypes
import PIL.ImageGrab
from keyboard import is_pressed
import winsound 
import time
import serial
import sys
com=None
if len(sys.argv) == 2:
    com=(sys.argv[1])
else:
    com='COM8'
ser = serial.Serial('COM8',115200)

threshold=25
threshold_inc='ctrl + up'
threshold_dec='ctrl + down'

time.sleep(2)
S_WIDTH,S_HEIGHT = (PIL.ImageGrab.grab().size)
S_WIDTH,S_HEIGHT=S_HEIGHT,S_WIDTH
print(S_HEIGHT,S_WIDTH)
TOLERANCE=70
r_list,b_list,g_list=[],[],[]
r2_list,b2_list,g2_list=[],[],[]
from pynput.mouse import Button, Controller

def avg(lst):
    return sum(lst)// len(lst)
mouse = Controller()

while True:
    grabzone = 15
    if is_pressed(threshold_inc):
        threshold+=2
        print("Threshold:",threshold)
    if is_pressed(threshold_dec):
        threshold-=2
        print("Threshold:",threshold)
    pmap = PIL.ImageGrab.grab()
    #r, g, b = pmap.getpixel((x,y))
    #left side first
    for x in range(0,threshold):
        for y in range(0, S_WIDTH):
            r, g, b = pmap.getpixel((x,y))
            r_list.append(r)
            g_list.append(g)
            b_list.append(b)
    R=str(max(r_list))
    G=str(max(g_list))
    B=str(max(b_list))
#right
    for x2 in range(S_HEIGHT-threshold,S_HEIGHT):
        for y2 in range(0, S_WIDTH):
            r2, g2, b2 = pmap.getpixel((x2,y2))
            r2_list.append(r2)
            g2_list.append(g2)
            b2_list.append(b2)
    X=str(max(r2_list))
    Y=str(max(g2_list))
    Z=str(max(b2_list))
    '''
    #print(max(r_list),max(g_list),max(b_list))
    R, G, B = pmap.getpixel(mouse.position)
    
    R=str(R)
    G=str(G)
    B=str(B)
    '''
    ser.write(bytes('r '+R+'\n', encoding='utf-8'))
    ser.write(bytes('g '+G+'\n', encoding='utf-8'))
    ser.write(bytes('b '+B+'\n', encoding='utf-8'))
    ser.write(bytes('x '+X+'\n', encoding='utf-8'))
    ser.write(bytes('y '+Y+'\n', encoding='utf-8'))
    ser.write(bytes('z '+Z+'\n', encoding='utf-8'))
    #toSend=R+","+G+","+B+"\n"
    #print(toSend)
    #ser.write(bytes(toSend, encoding='utf8'))
    r_list,b_list,g_list=[],[],[]
    r2_list,b2_list,g2_list=[],[],[]
