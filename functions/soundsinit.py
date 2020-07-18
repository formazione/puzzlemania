import pygame
from glob import glob

def init(directory):
    '''
        "Initializing pygame and mixer"
    To play a sound:
        pygame.mixer.Sound.play(Puzzle.sounds[name])

    *'name' is the name of the wav file without wav.
    *Puzzle is the name of the class where you put:

    =============== EXAMPLE OF CODE =============
    from functions.soundinit import init, play

    class Puzzle:
        "Class with the global variables"
        #'sounds' is the dir where the sounds are (you can change it).
        sounds = init('sounds')

    def play(snd):
        "To play wav in sounds directory by the name"
        pygame.mixer.Sound.play(Puzzle.sounds[snd]))


    play("click")
    ==============================================
    '''

    # This is to avoid lag
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    pygame.mixer.quit()
    pygame.mixer.init(22050, -16, 2, 512)
    pygame.mixer.set_num_channels(32)
    # Load all sounds
    lsounds = glob(f"{directory}\\*.wav")
    # Dictionary with all sounds, keys are the name of wav
    sounds = {}
    for sound in lsounds:
        sounds[sound.split("\\")[1][:-4]] = pygame.mixer.Sound(f"{sound}")
    return sounds
