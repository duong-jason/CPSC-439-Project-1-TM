# Run in https://turingmachinesimulator.com/ for it to work
name: DFA Figure 6.3
init: q0
accept: q1

q0,0
q0,0,>

q0,1
q1,1,>

q1,0
q1,0,>

q1,1
q0,1,>

q1,_
q1,_,-


name: DFA Figure 6.4
init: q0
accept: q0

q0,0
q2,0,>

q0,1
q3,1,>

q1,0
q0,0,>

q1,1
q3,1,>

q2,0
q3,0,>

q2,1
q1,1,>

q3,0
q3,0,>

q3,1
q3,1,>

q0,_
q0,_,-


name: Project 1 TM
init: q0
accept: q0, q6

# initial state, separates depending on input
q0,0
q1,0,>

q0,1
q5,1,>

# satisfies Figure 6.4
q1,0
q3,0,>

q1,1
q4,1,>

q2,0
q1,0,>

q2,1
q4,1,>

q3,0
q4,0,>

q3,1
q2,1,>

q4,0
q4,0,>

q4,1
q4,1,>

q1,_
q1,_,-

# satisfies Figure 6.3
q5,0
q5,0,>

q5,1
q6,1,>

q6,0
q6,0,>

q6,1
q5,1,>

q6,_
q6,_,-