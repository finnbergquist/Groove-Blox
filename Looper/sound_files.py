import pygame
from pygame import mixer
import os

class mix:
    pygame.mixer.pre_init(22050, -16, 2, 256)#22050=default frequecy,-16=size(16 signed bits per audio sample
    pygame.mixer.init()                      #2-->stereo sound, 512=buffersize
    pygame.init()
    
    #initialize channels in the mixer, with four channels
    channels = [pygame.mixer.Channel(0), pygame.mixer.Channel(1),
                pygame.mixer.Channel(2), pygame.mixer.Channel(3)]
    
    #sounds dictionary
    # Accessing sounds: 
#     each combination will have a 3-digit code. That code comes from
#     the MIDI, effect and inst inputs. Each of those resistor values
#     will be sorted into a single digit value from 0-10 with the sort 
#     function. Then they will be concatanated into a 3-digit code. 
#     000 representing the default. There will be a dictionary with 
#     these codes that will inform the Raspi which .wav to play.

    sounds = {
        "001" : pygame.mixer.Sound("Looper/Audio_Files/Choir.wav"),
        "010" : pygame.mixer.Sound("Looper/Audio_Files/drums.wav"),
        "100" : pygame.mixer.Sound("Looper/Audio_Files/Track3.wav"),
        "002" : pygame.mixer.Sound("Looper/Audio_Files/2_SECOND_PIANO.wav"),
        "020" : pygame.mixer.Sound("Looper/Audio_Files/Track1.wav"),
        "200" : pygame.mixer.Sound("Looper/Audio_Files/techno.wav"),
        "300" : pygame.mixer.Sound("Looper/Audio_Files/keys.wav"),
        "030" : pygame.mixer.Sound("Looper/Audio_Files/highs.wav"),
        "003" : pygame.mixer.Sound("Looper/Audio_Files/sax.wav"),
        
    }

    #this play should be used in looper lounge
    def play(self, sound_code, channel_number): 
            """Play arg1 sound in arg2 channel           
            ex) mix.play(1, 0) will play sound 1 in channel 0"""
            #make code readable by dict
            
            code = "'" + sound_code + "'"
            if (code in self.sounds):#there is no audio file in this position, so do nothing
                print("sound not in dictionary")
            else:#play specified sound in specified channel
                # print(type(code))
                # print(self.sounds.get(code))
                self.channels[channel_number].play(self.sounds[sound_code])

    #this play method should used in the step sequencer
    def play_step(self, sound_code, channel_number): 
            """Play sound_code sound in channel_number channel           
            ex) mix.play(1, 0) will play sound 1 in channel 0"""
            #make code readable by dict
            
            code = "'" + sound_code + "'"
            if sound_code == '000':
                return
            else:#play specified sound in specified channel
                # print(type(code))
                # print(self.sounds.get(code))
                self.channels[channel_number].play(self.sounds[sound_code])            


    def update_channel_volume(self, channel_number, volume):
        """sets the volume of a specific chanel"""     
        self.channels[channel_number].set_volume(volume)
            
            
    def cleanup(self):#need to use an exception handler!!!!! in driver
        """called at end of driver"""
        pygame.quit()