/*********************** 
 * Stroop 10-9-19 Test *
 ***********************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'Stroop 10-9-19';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const InstructionsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(InstructionsLoopBegin, InstructionsLoopScheduler);
flowScheduler.add(InstructionsLoopScheduler);
flowScheduler.add(InstructionsLoopEnd);
const PracticeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(PracticeLoopBegin, PracticeLoopScheduler);
flowScheduler.add(PracticeLoopScheduler);
flowScheduler.add(PracticeLoopEnd);
flowScheduler.add(full_instrRoutineBegin);
flowScheduler.add(full_instrRoutineEachFrame);
flowScheduler.add(full_instrRoutineEnd);
const TrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(TrialsLoopBegin, TrialsLoopScheduler);
flowScheduler.add(TrialsLoopScheduler);
flowScheduler.add(TrialsLoopEnd);
flowScheduler.add(thanksRoutineBegin);
flowScheduler.add(thanksRoutineEachFrame);
flowScheduler.add(thanksRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var instrClock;
var Stroop_Instr;
var Ready;
var cont;
var fixationClock;
var fixation_cross;
var prac_trialClock;
var Stroop_Text;
var prac_key_resp;
var practice_cue_txt;
var prac_cont;
var full_instrClock;
var full_instr_txt;
var full_instr_key;
var full_instr_cont;
var trialClock;
var Stroop_Text_Full;
var thanksClock;
var text_2;
var key_resp;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  Stroop_Instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'Stroop_Instr',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Ready = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  cont = new visual.TextStim({
    win: psychoJS.window,
    name: 'cont',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fixation_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation_cross',
    text: '+',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "prac_trial"
  prac_trialClock = new util.Clock();
  Stroop_Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Stroop_Text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  prac_key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  practice_cue_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_cue_txt',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  prac_cont = new visual.TextStim({
    win: psychoJS.window,
    name: 'prac_cont',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.45)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "full_instr"
  full_instrClock = new util.Clock();
  full_instr_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'full_instr_txt',
    text: 'Good work! \n\nNext we will begin the full task. \n\nOn this part, you will not press SPACE.\nItems will appear one by one.\n\nPlease respond quickly.\n',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  full_instr_key = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  full_instr_cont = new visual.TextStim({
    win: psychoJS.window,
    name: 'full_instr_cont',
    text: 'Press SPACE to begin.',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fixation_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation_cross',
    text: '+',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  Stroop_Text_Full = new visual.TextStim({
    win: psychoJS.window,
    name: 'Stroop_Text_Full',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Good work!\n\nYou have completed this task.\n\nPress SPACE to continue.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var Instructions;
var currentLoop;
var trialIterator;
function InstructionsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  Instructions = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'SCWT_Instr.xlsx',
    seed: undefined, name: 'Instructions'});
  psychoJS.experiment.addLoop(Instructions); // add the loop to the experiment
  currentLoop = Instructions;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = Instructions[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisInstruction = result.value;
    thisScheduler.add(importConditions(Instructions));
    thisScheduler.add(instrRoutineBegin);
    thisScheduler.add(instrRoutineEachFrame);
    thisScheduler.add(instrRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function InstructionsLoopEnd() {
  psychoJS.experiment.removeLoop(Instructions);

  return Scheduler.Event.NEXT;
}

var Practice;
function PracticeLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  Practice = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'SCWT_trials.xlsx', '0:6'),
    seed: undefined, name: 'Practice'});
  psychoJS.experiment.addLoop(Practice); // add the loop to the experiment
  currentLoop = Practice;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = Practice[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisPractice = result.value;
    thisScheduler.add(importConditions(Practice));
    thisScheduler.add(fixationRoutineBegin);
    thisScheduler.add(fixationRoutineEachFrame);
    thisScheduler.add(fixationRoutineEnd);
    thisScheduler.add(prac_trialRoutineBegin);
    thisScheduler.add(prac_trialRoutineEachFrame);
    thisScheduler.add(prac_trialRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function PracticeLoopEnd() {
  psychoJS.experiment.removeLoop(Practice);

  return Scheduler.Event.NEXT;
}

var Trials;
function TrialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  Trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'SCWT_trials.xlsx', '6:77'),
    seed: undefined, name: 'Trials'});
  psychoJS.experiment.addLoop(Trials); // add the loop to the experiment
  currentLoop = Trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = Trials[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial = result.value;
    thisScheduler.add(importConditions(Trials));
    thisScheduler.add(fixationRoutineBegin);
    thisScheduler.add(fixationRoutineEachFrame);
    thisScheduler.add(fixationRoutineEnd);
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function TrialsLoopEnd() {
  psychoJS.experiment.removeLoop(Trials);

  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var instrComponents;
function instrRoutineBegin() {
  //------Prepare to start Routine 'instr'-------
  t = 0;
  instrClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  Stroop_Instr.setText(text);
  Ready.keys = undefined;
  Ready.rt = undefined;
  cont.setText(cont_text);
  // keep track of which components have finished
  instrComponents = [];
  instrComponents.push(Stroop_Instr);
  instrComponents.push(Ready);
  instrComponents.push(cont);
  
  instrComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function instrRoutineEachFrame() {
  //------Loop for each frame of Routine 'instr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instrClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Stroop_Instr* updates
  if (t >= 0.0 && Stroop_Instr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Stroop_Instr.tStart = t;  // (not accounting for frame time here)
    Stroop_Instr.frameNStart = frameN;  // exact frame index
    Stroop_Instr.setAutoDraw(true);
  }

  
  // *Ready* updates
  if (t >= 0.0 && Ready.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Ready.tStart = t;  // (not accounting for frame time here)
    Ready.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { Ready.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { Ready.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { Ready.clearEvents(); });
  }

  if (Ready.status === PsychoJS.Status.STARTED) {
    let theseKeys = Ready.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *cont* updates
  if (t >= 0.0 && cont.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cont.tStart = t;  // (not accounting for frame time here)
    cont.frameNStart = frameN;  // exact frame index
    cont.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  instrComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instrRoutineEnd() {
  //------Ending Routine 'instr'-------
  instrComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "instr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var fixationComponents;
function fixationRoutineBegin() {
  //------Prepare to start Routine 'fixation'-------
  t = 0;
  fixationClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.500000);
  // update component parameters for each repeat
  // keep track of which components have finished
  fixationComponents = [];
  fixationComponents.push(fixation_cross);
  
  fixationComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function fixationRoutineEachFrame() {
  //------Loop for each frame of Routine 'fixation'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = fixationClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *fixation_cross* updates
  if (t >= 1 && fixation_cross.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    fixation_cross.tStart = t;  // (not accounting for frame time here)
    fixation_cross.frameNStart = frameN;  // exact frame index
    fixation_cross.setAutoDraw(true);
  }

  frameRemains = 1 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (fixation_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    fixation_cross.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  fixationComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function fixationRoutineEnd() {
  //------Ending Routine 'fixation'-------
  fixationComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

var prac_trialComponents;
function prac_trialRoutineBegin() {
  //------Prepare to start Routine 'prac_trial'-------
  t = 0;
  prac_trialClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  Stroop_Text.setColor(new util.Color(StroopColor));
  Stroop_Text.setText(StroopText);
  prac_key_resp.keys = undefined;
  prac_key_resp.rt = undefined;
  practice_cue_txt.setText(practice_cue);
  prac_cont.setText(practice_cont);
  // keep track of which components have finished
  prac_trialComponents = [];
  prac_trialComponents.push(Stroop_Text);
  prac_trialComponents.push(prac_key_resp);
  prac_trialComponents.push(practice_cue_txt);
  prac_trialComponents.push(prac_cont);
  
  prac_trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function prac_trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'prac_trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = prac_trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Stroop_Text* updates
  if (t >= 0 && Stroop_Text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Stroop_Text.tStart = t;  // (not accounting for frame time here)
    Stroop_Text.frameNStart = frameN;  // exact frame index
    Stroop_Text.setAutoDraw(true);
  }

  
  // *prac_key_resp* updates
  if (t >= 0 && prac_key_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    prac_key_resp.tStart = t;  // (not accounting for frame time here)
    prac_key_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { prac_key_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { prac_key_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { prac_key_resp.clearEvents(); });
  }

  if (prac_key_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = prac_key_resp.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *practice_cue_txt* updates
  if (t >= 1 && practice_cue_txt.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    practice_cue_txt.tStart = t;  // (not accounting for frame time here)
    practice_cue_txt.frameNStart = frameN;  // exact frame index
    practice_cue_txt.setAutoDraw(true);
  }

  
  // *prac_cont* updates
  if (t >= 1 && prac_cont.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    prac_cont.tStart = t;  // (not accounting for frame time here)
    prac_cont.frameNStart = frameN;  // exact frame index
    prac_cont.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  prac_trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function prac_trialRoutineEnd() {
  //------Ending Routine 'prac_trial'-------
  prac_trialComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "prac_trial" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var full_instrComponents;
function full_instrRoutineBegin() {
  //------Prepare to start Routine 'full_instr'-------
  t = 0;
  full_instrClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  full_instr_key.keys = undefined;
  full_instr_key.rt = undefined;
  // keep track of which components have finished
  full_instrComponents = [];
  full_instrComponents.push(full_instr_txt);
  full_instrComponents.push(full_instr_key);
  full_instrComponents.push(full_instr_cont);
  
  full_instrComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function full_instrRoutineEachFrame() {
  //------Loop for each frame of Routine 'full_instr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = full_instrClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *full_instr_txt* updates
  if (t >= 0.0 && full_instr_txt.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    full_instr_txt.tStart = t;  // (not accounting for frame time here)
    full_instr_txt.frameNStart = frameN;  // exact frame index
    full_instr_txt.setAutoDraw(true);
  }

  
  // *full_instr_key* updates
  if (t >= 0.0 && full_instr_key.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    full_instr_key.tStart = t;  // (not accounting for frame time here)
    full_instr_key.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { full_instr_key.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { full_instr_key.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { full_instr_key.clearEvents(); });
  }

  if (full_instr_key.status === PsychoJS.Status.STARTED) {
    let theseKeys = full_instr_key.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *full_instr_cont* updates
  if (t >= 0.0 && full_instr_cont.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    full_instr_cont.tStart = t;  // (not accounting for frame time here)
    full_instr_cont.frameNStart = frameN;  // exact frame index
    full_instr_cont.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  full_instrComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function full_instrRoutineEnd() {
  //------Ending Routine 'full_instr'-------
  full_instrComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "full_instr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var trialComponents;
function trialRoutineBegin() {
  //------Prepare to start Routine 'trial'-------
  t = 0;
  trialClock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.000000);
  // update component parameters for each repeat
  Stroop_Text_Full.setColor(new util.Color(StroopColor));
  Stroop_Text_Full.setText(StroopText);
  // keep track of which components have finished
  trialComponents = [];
  trialComponents.push(Stroop_Text_Full);
  
  trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Stroop_Text_Full* updates
  if (t >= 0.0 && Stroop_Text_Full.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Stroop_Text_Full.tStart = t;  // (not accounting for frame time here)
    Stroop_Text_Full.frameNStart = frameN;  // exact frame index
    Stroop_Text_Full.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Stroop_Text_Full.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Stroop_Text_Full.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEnd() {
  //------Ending Routine 'trial'-------
  trialComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

var thanksComponents;
function thanksRoutineBegin() {
  //------Prepare to start Routine 'thanks'-------
  t = 0;
  thanksClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp.keys = undefined;
  key_resp.rt = undefined;
  // keep track of which components have finished
  thanksComponents = [];
  thanksComponents.push(text_2);
  thanksComponents.push(key_resp);
  
  thanksComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function thanksRoutineEachFrame() {
  //------Loop for each frame of Routine 'thanks'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = thanksClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_2* updates
  if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_2.tStart = t;  // (not accounting for frame time here)
    text_2.frameNStart = frameN;  // exact frame index
    text_2.setAutoDraw(true);
  }

  
  // *key_resp* updates
  if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp.tStart = t;  // (not accounting for frame time here)
    key_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
  }

  if (key_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  thanksComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function thanksRoutineEnd() {
  //------Ending Routine 'thanks'-------
  thanksComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "thanks" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
