"""Audio Looper driver method"""
import time
import smbus2
# from gpiozero import MCP3008, PWMLED
from drum_files import mix 
from looper import Looper
import math


# set up the bus
bus = smbus2.SMBus(1)
address = 0x04

def readBus():
    data = bus.read_i2c_block_data(address, 0, 3)
    return data


def timer(time, curr):
    if (round(time) != curr):
        curr = round(time)
        return curr
    else: 
        return 
        
def play_region(instr, channel_number):
    ##play loop from channel number 
    mixer.play(instr.get_loop(channel_number), channel_number)


def start_loop(instr):
    #initial time
    start_time = time.time()
    length = 16
    #set sequences
    kick = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
    open_hat = [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
    snare = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    snare_hits = []
    instruments = [kick, open_hat, snare]

    #set loops, THIS IS FUCKING WEIRD 
    instr.set_loop(0, '100')
    instr.set_loop(1, '200')
    instr.set_loop(2, '300')
    instr.set_loop(3, '400')

    #set last time and hit time
    last = -1
    hit_time = 0

    #vartiables  for button and inst
    recording = 0
    inst_state = 0
    last_state = -3

    while True:
        
        #start really keeping track of time 
        raw_time = time.time()       
        elapsed_time = raw_time - start_time
        #*4 is to make floor_time 240 BPM instead of 60, give it 16 beats
        floor_time = math.floor(elapsed_time * 4)
        #roll over if it goes over time
        if (floor_time >= float(length)):
            start_time = time.time()
            elapsed_time = raw_time - start_time
            floor_time = math.floor(elapsed_time)
            hit_time = 0
            for x in range(len(snare)):
                print(snare[x])
        #read bus t
        output = readBus()
        # #set vars
        hit = output[0]
        inst_state = output[1] - 1
        recording = output[2]
        print(inst_state)
        #inst_state
        if (inst_state != last_state):
            last_state = inst_state
            play_region(instr, inst_state)

        # #if its high, play snare, wait a little before checking again
        # if (hit == 1 and (elapsed_time - hit_time) > 0.3):
        #     play_region(instr, 1)  
        #     hit_time = elapsed_time
        #     #snare_hits.append(math.floor(hit_time * 4))
        #     if round(hit_time * 4) != length:
        #         snare[round(hit_time * 4)] = 1
            


        #when you are at an interval, update which instruments are playing
        # if (floor_time != last):
        #     last = floor_time
            # for x in instruments:
            #     if(x[last] == 1):
            #         play_region(instr, instruments.index(x))
            #         print(instruments.index(x))
           

            # if (kick[last] == 1):
            #     play_region(looper, 2)
            # if (snare[last] == 1):
            #      play_region(looper, 1)
            # if (open_hat[last] == 1):
            #     play_region(looper, 0)
            


        


        


#settig up channel data
TEMPO = 5    #how many instruments
CHANNELS = 4
looper = Looper(TEMPO, CHANNELS)#5 is the tempo, 2 channels, 8 steps
mixer = mix()
mixer.update_channel_volume(0, 1.0)
#start loop on sequencer

start_loop(looper)

       

            
    
        
        
        
    

