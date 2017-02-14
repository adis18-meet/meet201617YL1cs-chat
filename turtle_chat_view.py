#2016-2017 PERSONAL PROJECTS: TurtleChat!
#WRITE YOUR NAME HERE!adi
#####################################################################################
#                                   IMPORTS                                         #
#####################################################################################
import turtle 
#import the Client class from the turtle_chat_client module
from turtle_chat_client import Client
#Finally, from the turtle_chat_widgets module, import two classes: Button and TextInput
from turtle_chat_widgets import Button
from turtle_chat_widgets import TextInput
####
#####################################################################################
#                                   TextBox                                         #
#####################################################################################
class TextBox(TextInput):
    def draw_box(self):
        turtle.goto (50,50)
        turtle.pendown()
        turtle.goto(500,50)
        turtle.goto (500,10)
        turtle.goto(50,10)
        turtle.goto(50,50)
    def write_msg(self):
        self.writer.clear()
        self.writer.write(self.new_msg)
        
        
    

######################################################################################
#                                  SendButton                                       #
#####################################################################################
class SendButton(Button):
    def fun(self,x=None,y=None):
        self.view.send_msg()
    def __init__(self,view):
        self.view = view
        super(SendButton,self).__init__()
        
    

##################################################################
#                             View                               #
##################################################################
#Make a new class called View.  It does not need to have a parent
#class mentioned explicitly.
#
#Read the comments below for hints and directions.
##################################################################
##################################################################
class View:
    _MSG_LOG_LENGTH=5 #Number of messages to retain in view
    _SCREEN_WIDTH=300
    _SCREEN_HEIGHT=600
    _LINE_SPACING=round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))

    def __init__(self,username='Me',partner_name='Partner'):
        self.partner_name = partner_name
        self.username = username

        self.my_client = Client()

        ###
        #Set screen dimensions using turtle.setup
        #You can get help on this function, as with other turtle functions,
        #by typing
        #
        #   import turtle
        #   help(turtle.setup)
        #
        #at the Python shell.
        ###

        ###
        #This list will store all of the messages.
        #You can add strings to the front of the list using
        #   self.msg_queue.insert(0,a_msg_string)
        #or at the end of the list using
        #   self.msg_queue.append(a_msg_string)
        self.msg_queue=[]
        ###

        ###
        self.writer = turtle.clone()
        
        #Create one turtle object for each message to display.
        #You can use the clear() and write() methods to erase
        #and write messages for each
        ###

        ###
        self.TextBox = TextBox()
        self.SendButton = SendButton(self)
        #Create a TextBox instance and a SendButton instance and
        #Store them inside of this instance
        ###

        ###
        #Call your setup_listeners() function, if you have one,
        #and any other remaining setup functions you have invented.
        ###

    def send_msg(self):
        self.my_client.send(self.TextBox.new_msg)
        self.msg_queue.insert(0,self.TextBox.new_msg)
        self.TextBox.clear_msg()
        self.display_msg()
      
    def get_msg(self):
        return self.textbox.get_msg()

    

    def setup_listeners(self):
        '''
        Set up send button - additional listener, in addition to click,
        so that return button will send a message.
        To do this, you will use the turtle.onkeypress function.
        The function that it will take is
        self.send_btn.fun
        where send_btn is the name of your button instance

        Then, it can call turtle.listen()
        '''
        pass

    def msg_received(self,msg):
        print(msg) 
        show_this_msg=self.partner_name+' says:\r'+ msg
        self.msg_queue.insert(0,msg)
        self.display_msg()

    def display_msg(self):
        self.writer.clear()
        self.writer.write(self.msg_queue[0])
        '''
        This method should update the messages displayed in the screen.
        You can get the messages you want from self.msg_queue
        '''     

    def get_client(self):
        return self.my_client
#########################################################
#Leave the code below for now - you can play around with#
#it once you have a working view, trying to run you chat#
#view in different ways.                                #
#########################################################
if __name__ == '__main__':
    my_view=View()
    _WAIT_TIME=200 #Time between check for new message, ms
    def check() :
        #msg_in=my_view.my_client.receive()
        msg_in=my_view.get_client().receive()
        if not(msg_in is None):
            if msg_in==Client._END_MSG:
                print('End message received')
                sys.exit()
            else:
                my_view.msg_received(msg_in)
        turtle.ontimer(check,_WAIT_TIME) #Check recursively
    check()
    turtle.mainloop()
