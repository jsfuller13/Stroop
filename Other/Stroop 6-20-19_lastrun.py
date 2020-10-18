#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on Thu Jun 20 16:07:31 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, microphone, hardware, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'Stroop 6-20-19'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jordanfuller/Documents/Research/Dissertation/Experiment Building/Stroop 6-20-19_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')

# Enable sound input/output:
microphone.switchOn()
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instr_1"
Instr_1Clock = core.Clock()
Stroop_Instr = visual.TextStim(win=win, name='Stroop_Instr',
    text=' During this task, you will see three types of stimuli: colored asterisks, color words written in black, and color words written in color.\n\nPress SPACE to continue.\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Instr_2"
Instr_2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='If you see a color word written in white, read the word.\n \nPress SPACE to continue.\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Instr_3"
Instr_3Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='But, if you see a color word written in color, say the color that the word is written in. Do not read the word.\n \nSo, if you see "Red" written in Blue, you would say "Blue". You would not say "Red".\n \nLet’s practice.\n \nPress SPACE to continue.\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Stroop_Text = visual.TextStim(win=win, name='Stroop_Text',
    text=StroopText,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=StroopColor, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
msg = ''
text_3 = visual.TextStim(win=win, name='text_3',
    text=msg,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Instr_4"
Instr_4Clock = core.Clock()

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Stroop_Text = visual.TextStim(win=win, name='Stroop_Text',
    text=StroopText,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=StroopColor, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instr_1"-------
t = 0
Instr_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Ready = keyboard.Keyboard()
# keep track of which components have finished
Instr_1Components = [Stroop_Instr, Ready]
for thisComponent in Instr_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instr_1"-------
while continueRoutine:
    # get current time
    t = Instr_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Stroop_Instr* updates
    if t >= 0.0 and Stroop_Instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        Stroop_Instr.tStart = t  # not accounting for scr refresh
        Stroop_Instr.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Stroop_Instr, 'tStartRefresh')  # time at next scr refresh
        Stroop_Instr.setAutoDraw(True)
    
    # *Ready* updates
    if t >= 0.0 and Ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        Ready.tStart = t  # not accounting for scr refresh
        Ready.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Ready, 'tStartRefresh')  # time at next scr refresh
        Ready.status = STARTED
        # keyboard checking is just starting
        Ready.clearEvents(eventType='keyboard')
    if Ready.status == STARTED:
        theseKeys = Ready.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_1"-------
for thisComponent in Instr_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instr_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr_2"-------
t = 0
Instr_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp = keyboard.Keyboard()
# keep track of which components have finished
Instr_2Components = [text, key_resp]
for thisComponent in Instr_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instr_2"-------
while continueRoutine:
    # get current time
    t = Instr_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # not accounting for scr refresh
        text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text.tStop = t  # not accounting for scr refresh
        text.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
        text.setAutoDraw(False)
    
    # *key_resp* updates
    if t >= 0.0 and key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp.tStart = t  # not accounting for scr refresh
        key_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        key_resp.clearEvents(eventType='keyboard')
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_2"-------
for thisComponent in Instr_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Instr_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr_3"-------
t = 0
Instr_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = keyboard.Keyboard()
# keep track of which components have finished
Instr_3Components = [text_2, key_resp_2]
for thisComponent in Instr_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instr_3"-------
while continueRoutine:
    # get current time
    t = Instr_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # not accounting for scr refresh
        text_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_2.tStop = t  # not accounting for scr refresh
        text_2.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
        text_2.setAutoDraw(False)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # not accounting for scr refresh
        key_resp_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_3"-------
for thisComponent in Instr_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "Instr_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Practice = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Practice')
thisExp.addLoop(Practice)  # add the loop to the experiment
thisPractice = Practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in Practice:
    currentLoop = Practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3 = keyboard.Keyboard()
    mic_1 = microphone.AdvAudioCapture(name='mic_1', saveDir=wavDirName, stereo=False, chnl='0')
    # keep track of which components have finished
    TrialComponents = [Stroop_Text, key_resp_3, mic_1]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Trial"-------
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stroop_Text* updates
        if t >= 0.0 and Stroop_Text.status == NOT_STARTED:
            # keep track of start time/frame for later
            Stroop_Text.tStart = t  # not accounting for scr refresh
            Stroop_Text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Stroop_Text, 'tStartRefresh')  # time at next scr refresh
            Stroop_Text.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Stroop_Text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Stroop_Text.tStop = t  # not accounting for scr refresh
            Stroop_Text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Stroop_Text, 'tStopRefresh')  # time at next scr refresh
            Stroop_Text.setAutoDraw(False)
        
        # *key_resp_3* updates
        if t >= 0.5 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # not accounting for scr refresh
            key_resp_3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            key_resp_3.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = key_resp_3.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_3.keys = theseKeys.name  # just the last key pressed
                key_resp_3.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *mic_1* updates
        if t >= 0.0 and mic_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            mic_1.tStart = t  # not accounting for scr refresh
            mic_1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(mic_1, 'tStartRefresh')  # time at next scr refresh
            mic_1.status = STARTED
            mic_1.record(sec=2.0, block=False)  # start the recording thread
        
        if mic_1.status == STARTED and not mic_1.recorder.running:
            mic_1.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice.addData('Stroop_Text.started', Stroop_Text.tStartRefresh)
    Practice.addData('Stroop_Text.stopped', Stroop_Text.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    Practice.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        Practice.addData('key_resp_3.rt', key_resp_3.rt)
    Practice.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    Practice.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # mic_1 stop & responses
    mic_1.stop()  # sometimes helpful
    if not mic_1.savedFile:
        mic_1.savedFile = None
    # store data for Practice (TrialHandler)
    Practice.addData('mic_1.filename', mic_1.savedFile)
    Practice.addData('mic_1.started', mic_1.tStart)
    Practice.addData('mic_1.stopped', mic_1.tStop)
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback"-------
    t = 0
    FeedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if resp.corr:#stored on last run routine
      msg="Correct! RT=%.3f" %(resp.rt)
    else:
      msg="Oops! Not quite."
    # keep track of which components have finished
    FeedbackComponents = [text_3]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # not accounting for scr refresh
            text_3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_3.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice.addData('text_3.started', text_3.tStartRefresh)
    Practice.addData('text_3.stopped', text_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5 repeats of 'Practice'


# ------Prepare to start Routine "Instr_4"-------
t = 0
Instr_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Instr_4Components = []
for thisComponent in Instr_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instr_4"-------
while continueRoutine:
    # get current time
    t = Instr_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_4"-------
for thisComponent in Instr_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instr_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Trials')
thisExp.addLoop(Trials)  # add the loop to the experiment
thisTrial = Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in Trials:
    currentLoop = Trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3 = keyboard.Keyboard()
    mic_1 = microphone.AdvAudioCapture(name='mic_1', saveDir=wavDirName, stereo=False, chnl='0')
    # keep track of which components have finished
    TrialComponents = [Stroop_Text, key_resp_3, mic_1]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Trial"-------
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stroop_Text* updates
        if t >= 0.0 and Stroop_Text.status == NOT_STARTED:
            # keep track of start time/frame for later
            Stroop_Text.tStart = t  # not accounting for scr refresh
            Stroop_Text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Stroop_Text, 'tStartRefresh')  # time at next scr refresh
            Stroop_Text.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Stroop_Text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Stroop_Text.tStop = t  # not accounting for scr refresh
            Stroop_Text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Stroop_Text, 'tStopRefresh')  # time at next scr refresh
            Stroop_Text.setAutoDraw(False)
        
        # *key_resp_3* updates
        if t >= 0.5 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # not accounting for scr refresh
            key_resp_3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            key_resp_3.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = key_resp_3.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_3.keys = theseKeys.name  # just the last key pressed
                key_resp_3.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *mic_1* updates
        if t >= 0.0 and mic_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            mic_1.tStart = t  # not accounting for scr refresh
            mic_1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(mic_1, 'tStartRefresh')  # time at next scr refresh
            mic_1.status = STARTED
            mic_1.record(sec=2.0, block=False)  # start the recording thread
        
        if mic_1.status == STARTED and not mic_1.recorder.running:
            mic_1.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trials.addData('Stroop_Text.started', Stroop_Text.tStartRefresh)
    Trials.addData('Stroop_Text.stopped', Stroop_Text.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    Trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        Trials.addData('key_resp_3.rt', key_resp_3.rt)
    Trials.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    Trials.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # mic_1 stop & responses
    mic_1.stop()  # sometimes helpful
    if not mic_1.savedFile:
        mic_1.savedFile = None
    # store data for Trials (TrialHandler)
    Trials.addData('mic_1.filename', mic_1.savedFile)
    Trials.addData('mic_1.started', mic_1.tStart)
    Trials.addData('mic_1.stopped', mic_1.tStop)
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'Trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
