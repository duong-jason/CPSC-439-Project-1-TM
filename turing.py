# class Tape(object):
#     blank_symbol = " "
#     def __init__(self, tape_string = ""):
#         self.tape = dict((enumerate(tape_string)))
        
#     def __str__(self):
#         s = ""
#         min_used_index = min(self.tape.keys()) 
#         max_used_index = max(self.tape.keys())
#         for i in range(min_used_index, max_used_index):
#             s += self.tape[i]
#         return s    
   
#     def __getitem__(self,index):
#         if index in self.tape:
#             return self.tape[index]
#         else:
#             return Tape.blank_symbol

#     def __setitem__(self, pos, char):
#         self.tape[pos] = char 

        
# class TuringMachine(object):
#     def __init__(self, tape = "", blank_symbol = " ",initial_state = "",
#                  final_states = None, transition_function = None):
#         self.tape = Tape(tape)
#         self.head_position = 0
#         self.blank_symbol = blank_symbol
#         self.current_state = initial_state
        
#         if transition_function == None:
#             self.transition_function = {}
#         else:
#             self.transition_function = transition_function
#         if final_states == None:
#             self.final_states = set()
#         else:
#             self.final_states = set(final_states)
        
#     def get_tape(self): 
#         return str(self.tape)
    
#     def step(self):
#         char_under_head = self.tape[self.head_position]
#         x = (self.current_state, char_under_head)
#         if x in self.transition_function:
#             y = self.transition_function[x]
#             self.tape[self.head_position] = y[1]
#             if y[2] == "R":
#                 self.head_position += 1
#             elif y[2] == "L":
#                 self.head_position -= 1
#             self.current_state = y[0]

#     def final(self):
#         if self.current_state in self.final_states:
#             return True
#         else:
#             return False
        

# initial_state = "init",
# accepting_states = ["final"],
# transition_function = {("init","0"):("init", "1", "R"),
#                        ("init","1"):("init", "0", "R"),
#                        ("init"," "):("final"," ", "N"),
#                        }
# final_states = {"final"}

# t = TuringMachine("01001100 ", 
#                   initial_state = "init",
#                   final_states = final_states,
#                   transition_function = transition_function)

# print("Input on Tape:\n" + t.get_tape())

# while not t.final():
#     t.step()

# print("Turing Machine Result:")    
# print(t.get_tape())



# LOAD AN EXAMPLE TO TRY
# then load an input and click play

# Syntax:

# -------CONFIGURATION
# name: [name_of_machine]
# init: [initial_state]
# accept: [accept_state_1],... ,[accept_state_n]

# -------DELTA FUNCTION:
# [current_state],[read_symbol]
# [new_state],[write_symbol],[>|<|-]

# < = left
# > = right
# - = hold
# use underscore for blank cells

# States and symbols are case-sensitive

# Load your code and click COMPILE.
# or load an example (top-right).

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
