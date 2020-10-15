#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on November 19, 2019, at 16:27
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
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
psychopyVersion = '3.1.5'
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
    originPath='C:\\Users\\Jordan\\Documents\\Experiment Building\\4. Stroop Task\\Stroop 10-9-19_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='MBP_Monitor', color=[0,0,0], colorSpace='hsv',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
Stroop_Instr = visual.TextStim(win=win, name='Stroop_Instr',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
cont = visual.TextStim(win=win, name='cont',
    text='default text',
    font='Arial',
    pos=(0, -0.40), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "prac_trial"
prac_trialClock = core.Clock()
Stroop_Text = visual.TextStim(win=win, name='Stroop_Text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
practice_cue_txt = visual.TextStim(win=win, name='practice_cue_txt',
    text='default text',
    font='Arial',
    pos=(0,-0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
prac_cont = visual.TextStim(win=win, name='prac_cont',
    text='default text',
    font='Arial',
    pos=(0,-0.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# The import and pyo_init should always come early on:
import psychopy.voicekey as vk
vk.pyo_init(rate=44100, buffersize=256)

# What signaler class to use? Here just the demo signaler:
from psychopy.voicekey.demo_vks import DemoVoiceKeySignal as Signaler

# To use a LabJack as a signaling device:
#from voicekey.signal.labjack_vks import LabJackU3VoiceKeySignal as Signaler

# Initialize components for Routine "full_instr"
full_instrClock = core.Clock()
full_instr_txt = visual.TextStim(win=win, name='full_instr_txt',
    text='Good work! \n\nNext we will begin the full task. \n\nOn this part, you will not press SPACE.\nItems will appear one by one.\n\nPlease respond quickly.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
full_instr_cont = visual.TextStim(win=win, name='full_instr_cont',
    text='Press SPACE to begin.',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
Stroop_Text_Full = visual.TextStim(win=win, name='Stroop_Text_Full',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Good work!\n\nYou have completed this task.\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
Instructions = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SCWT_Instr.xlsx'),
    seed=None, name='Instructions')
thisExp.addLoop(Instructions)  # add the loop to the experiment
thisInstruction = Instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
if thisInstruction != None:
    for paramName in thisInstruction:
        exec('{} = thisInstruction[paramName]'.format(paramName))

for thisInstruction in Instructions:
    currentLoop = Instructions
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
    if thisInstruction != None:
        for paramName in thisInstruction:
            exec('{} = thisInstruction[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr"-------
    t = 0
    instrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Stroop_Instr.setText(text)
    Ready = keyboard.Keyboard()
    cont.setText(cont_text)
    # keep track of which components have finished
    instrComponents = [Stroop_Instr, Ready, cont]
    for thisComponent in instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instr"-------
    while continueRoutine:
        # get current time
        t = instrClock.getTime()
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
        
        # *cont* updates
        if t >= 0.0 and cont.status == NOT_STARTED:
            # keep track of start time/frame for later
            cont.tStart = t  # not accounting for scr refresh
            cont.frameNStart = frameN  # exact frame index
            win.timeOnFlip(cont, 'tStartRefresh')  # time at next scr refresh
            cont.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr"-------
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'Instructions'


# set up handler to look after randomisation of conditions etc
Practice = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SCWT_trials.xlsx', selection='0:6'),
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
    
    # ------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixation_cross]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t  # not accounting for scr refresh
            fixation_cross.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        frameRemains = 1 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fixation_cross.tStop = t  # not accounting for scr refresh
            fixation_cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "prac_trial"-------
    t = 0
    prac_trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Stroop_Text.setColor(StroopColor, colorSpace='rgb')
    Stroop_Text.setText(StroopText)
    prac_key_resp = keyboard.Keyboard()
    practice_cue_txt.setText(practice_cue
)
    prac_cont.setText(practice_cont)
    # Create a voice-key to be used:
    vpvk = vk.OnsetVoiceKey(
        sec=2, 
        file_out='data/trial_'+str(Practice.thisN).zfill(3)+'.wav')
    
    # Start it recording (and detecting):
      # non-blocking; don't block when using Builder
    vpvk.start()
    # keep track of which components have finished
    prac_trialComponents = [Stroop_Text, prac_key_resp, practice_cue_txt, prac_cont]
    for thisComponent in prac_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "prac_trial"-------
    while continueRoutine:
        # get current time
        t = prac_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stroop_Text* updates
        if t >= 0 and Stroop_Text.status == NOT_STARTED:
            # keep track of start time/frame for later
            Stroop_Text.tStart = t  # not accounting for scr refresh
            Stroop_Text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Stroop_Text, 'tStartRefresh')  # time at next scr refresh
            Stroop_Text.setAutoDraw(True)
        
        # *prac_key_resp* updates
        if t >= 0 and prac_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_key_resp.tStart = t  # not accounting for scr refresh
            prac_key_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(prac_key_resp, 'tStartRefresh')  # time at next scr refresh
            prac_key_resp.status = STARTED
            # keyboard checking is just starting
            prac_key_resp.clearEvents(eventType='keyboard')
        if prac_key_resp.status == STARTED:
            theseKeys = prac_key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *practice_cue_txt* updates
        if t >= 1 and practice_cue_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_cue_txt.tStart = t  # not accounting for scr refresh
            practice_cue_txt.frameNStart = frameN  # exact frame index
            win.timeOnFlip(practice_cue_txt, 'tStartRefresh')  # time at next scr refresh
            practice_cue_txt.setAutoDraw(True)
        
        # *prac_cont* updates
        if t >= 1 and prac_cont.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_cont.tStart = t  # not accounting for scr refresh
            prac_cont.frameNStart = frameN  # exact frame index
            win.timeOnFlip(prac_cont, 'tStartRefresh')  # time at next scr refresh
            prac_cont.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prac_trial"-------
    for thisComponent in prac_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # The recorded sound is saved upon .stop() by default. But
    # its a good idea to call .stop() explicitly, eg, if there's much slippage:
    
    vpvk.stop()
    
    # Add the detected time into the PsychoPy data file:
    thisExp.addData('vocal_RT', round(vpvk.event_onset, 3))
    thisExp.addData('bad_baseline', vpvk.bad_baseline)
    thisExp.addData('filename', vpvk.filename)
    thisExp.nextEntry()
    # the Routine "prac_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Practice'

# get names of stimulus parameters
if Practice.trialList in ([], [None], None):
    params = []
else:
    params = Practice.trialList[0].keys()
# save data for this loop
Practice.saveAsExcel(filename + '.xlsx', sheetName='Practice',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "full_instr"-------
t = 0
full_instrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
full_instr_key = keyboard.Keyboard()
# keep track of which components have finished
full_instrComponents = [full_instr_txt, full_instr_key, full_instr_cont]
for thisComponent in full_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "full_instr"-------
while continueRoutine:
    # get current time
    t = full_instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *full_instr_txt* updates
    if t >= 0.0 and full_instr_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        full_instr_txt.tStart = t  # not accounting for scr refresh
        full_instr_txt.frameNStart = frameN  # exact frame index
        win.timeOnFlip(full_instr_txt, 'tStartRefresh')  # time at next scr refresh
        full_instr_txt.setAutoDraw(True)
    
    # *full_instr_key* updates
    if t >= 0.0 and full_instr_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        full_instr_key.tStart = t  # not accounting for scr refresh
        full_instr_key.frameNStart = frameN  # exact frame index
        win.timeOnFlip(full_instr_key, 'tStartRefresh')  # time at next scr refresh
        full_instr_key.status = STARTED
        # keyboard checking is just starting
        full_instr_key.clearEvents(eventType='keyboard')
    if full_instr_key.status == STARTED:
        theseKeys = full_instr_key.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *full_instr_cont* updates
    if t >= 0.0 and full_instr_cont.status == NOT_STARTED:
        # keep track of start time/frame for later
        full_instr_cont.tStart = t  # not accounting for scr refresh
        full_instr_cont.frameNStart = frameN  # exact frame index
        win.timeOnFlip(full_instr_cont, 'tStartRefresh')  # time at next scr refresh
        full_instr_cont.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in full_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "full_instr"-------
for thisComponent in full_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "full_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SCWT_trials.xlsx', selection='6:77'),
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
    
    # ------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixation_cross]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t  # not accounting for scr refresh
            fixation_cross.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        frameRemains = 1 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fixation_cross.tStop = t  # not accounting for scr refresh
            fixation_cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    Stroop_Text_Full.setColor(StroopColor, colorSpace='rgb')
    Stroop_Text_Full.setText(StroopText)
    # Create a voice-key to be used:
    vpvk = vk.OnsetVoiceKey(
        sec=2, 
        file_out='data/trial_'+str(Trials.thisN).zfill(3)+'.wav')
    
    # Start it recording (and detecting):
      # non-blocking; don't block when using Builder
    vpvk.start()
    
    # keep track of which components have finished
    trialComponents = [Stroop_Text_Full]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stroop_Text_Full* updates
        if t >= 0.0 and Stroop_Text_Full.status == NOT_STARTED:
            # keep track of start time/frame for later
            Stroop_Text_Full.tStart = t  # not accounting for scr refresh
            Stroop_Text_Full.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Stroop_Text_Full, 'tStartRefresh')  # time at next scr refresh
            Stroop_Text_Full.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Stroop_Text_Full.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Stroop_Text_Full.tStop = t  # not accounting for scr refresh
            Stroop_Text_Full.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Stroop_Text_Full, 'tStopRefresh')  # time at next scr refresh
            Stroop_Text_Full.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # The recorded sound is saved upon .stop() by default. But
    # its a good idea to call .stop() explicitly, eg, if there's much slippage:
    
    vpvk.stop()
    
    # Add the detected time into the PsychoPy data file:
    thisExp.addData('vocal_RT', round(vpvk.event_onset, 3))
    thisExp.addData('bad_baseline', vpvk.bad_baseline)
    thisExp.addData('filename', vpvk.filename)
    thisExp.nextEntry()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Trials'

# get names of stimulus parameters
if Trials.trialList in ([], [None], None):
    params = []
else:
    params = Trials.trialList[0].keys()
# save data for this loop
Trials.saveAsExcel(filename + '.xlsx', sheetName='Trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp = keyboard.Keyboard()
# keep track of which components have finished
thanksComponents = [text_2, key_resp]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # not accounting for scr refresh
        text_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp* updates
    if t >= 0.0 and key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp.tStart = t  # not accounting for scr refresh
        key_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        key_resp.clearEvents(eventType='keyboard')
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
