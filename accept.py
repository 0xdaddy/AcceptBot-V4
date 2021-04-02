
from time import sleep
from clear import clear
from headers import headers
class do:
    from color import printc, inputc
    import requests
    min = 60
    too_many_requests = 429
    cookie =''
    csrftoken = ''
    blocked = 0
    count = 0
    time = int()
    username = None
    follower = None
    public_id = ''
    public_mod = ''
    public_num = int()
    frist_sleep = int()
    find_id = []
    block_or_igrone_or_pass = ''
    def __init__(self, cookie) -> None:
        clear()
        self.printc.yellow("if someone follow you and unfollow you then follow you\n Do You to [b/i/p]\n p = pass him \n b = block him\n i = igrone him\n `Choose By letter`")
        self.block_or_igrone_or_pass = input()
        clear()
        from urls import url_set_private
        self.time = int(self.inputc.red("Sleep :"))
        self.frist_sleep = self.time
        clear()
        self.printc.yellow('Do You Want t0 Accept And Follow? [y/n]')#instagram : @0xdevil
        self.cookie = cookie
        self.csrftoken = cookie.get_dict()['csrftoken']
        self.requests.post(url_set_private(), headers=headers(self.csrftoken), data={
            'is_private': 'true'
        },cookies=cookie)
        mod = input()
        if mod == 'y':
            clear()
            self._accept_and_follow()
        else:
            clear()
            self.only_accept()
    def get_followers(self, user):
        from urls import url_users
        user = self.requests.get(
            url_users(user)+'/?__a=1', 
            headers=headers(''),#instagram : @0xdevil
             cookies=self.cookie)
        follow = user.json()['graphql']['user']['edge_followed_by']['count']#instagram : @0xdevil
        return follow
    def spam(self,id):        
            try:
                self.find_id.index(id)
                if self.block_or_igrone_or_pass == 'b':self.block(self.public_id)
                elif self.block_or_igrone_or_pass == 'i':self.igrone(self.public_id)        #instagram : @0xdevil   
                else:pass  
            except:pass             
    def _accept(self, f): 
            self.check_time()
            from colorama import init, Fore, Back, Style
            init()
            if self.public_mod == 'y': 
                try:
                    sleep(self.time)       
                    from urls import url_accept_follower , url_ignore_follower
                    self.public_id = self.get_follow_id()                    
                    self.follower = int(self.get_followers(self.username))  
                    self.spam(self.public_id) 
                    self.find_id.append(self.public_id)  
                    if self.follower > self.public_num:                 #instagram : @0xdevil          
                        accpet = self.requests.post(url_accept_follower(self.public_id),
                        headers=headers(self.csrftoken),
                        cookies=self.cookie)
                        if '{"status":"ok"}' in accpet.text:                              
                            clear()
                            self.count+=1
                            print(Fore.GREEN + Style.BRIGHT + f'Done Accept.\n Username : {self.username}\n His Followers is ({self.follower})\n'+Style.RESET_ALL+Fore.RED + Style.BRIGHT +f'Check Num:{self.count}'+ Style.RESET_ALL)
                        if f:
                            self.follow(self.public_id)
                        else: pass#instagram : @0xdevil
                    else: self.count+=1; clear(); self.requests.post(url_ignore_follower(self.public_id),headers=headers(self.csrftoken),cookies=self.cookie);print(Fore.RED + Style.BRIGHT + f'illegal User Request you. \n Some Info.\n Username : {self.username}\n'+Style.RESET_ALL+Fore.RED + Style.BRIGHT +f' His Followers is ({self.follower})\n \n Check Num:{self.count}'+ Style.RESET_ALL)
                except:
                        clear()
                        self.count+=1 
                        if self.username != None and self.follower != None:
                            print(Fore.GREEN + Style.BRIGHT + f'Last User Check.\n Username : {self.username}\n'+Style.RESET_ALL+Fore.RED + Style.BRIGHT +f' Last User Check Followers is ({self.follower})\n Check Num:{self.count}'+ Style.RESET_ALL)
                        else:#instagram : @0xdevil
                            print(Fore.GREEN + Style.BRIGHT + f'Last User Check.\n Username : We Do not Accept Any One Yet.\n'+Style.RESET_ALL+Fore.RED + Style.BRIGHT +f' Last User Check Followers is (None)\n None New Followers !\n Check Num:{self.count}'+ Style.RESET_ALL)
     
            else:
                try:
                    sleep(self.time)       
                    from urls import url_accept_follower
                    self.public_id = self.get_follow_id() 
                    self.spam(self.public_id)   
                    self.find_id.append(self.public_id)                                             
                    accpet = self.requests.post(url_accept_follower(self.public_id),
                    headers=headers(self.csrftoken),
                    cookies=self.cookie)
                    if '{"status":"ok"}' in accpet.text:                                   
                        clear()
                        self.count+=1
                        print(Fore.GREEN + Style.BRIGHT + f'Done Accept.\n Username : {self.username}'+Style.RESET_ALL+Fore.RED + Style.BRIGHT +f'Check Num:{self.count}'+ Style.RESET_ALL)
                    if f:
                            self.follow(self.public_id)
                    else: pass
                except:
                        clear()
                        self.count+=1 
                        if self.username != None and self.follower != None:
                            print(Fore.GREEN + Style.BRIGHT + f'Last User Check.\n Username : {self.username}\n'+Style.RESET_ALL+Fore.RED + Style.BRIGHT +f' Check Num:{self.count}'+ Style.RESET_ALL)
                        else:
                            print(Fore.GREEN + Style.BRIGHT + f'Last User Check.\n Username : We Do not Accept Any One Yet.\n'+Style.RESET_ALL+Fore.RED + Style.BRIGHT +f'None New Followers !\n Check Num:{self.count}'+ Style.RESET_ALL)
     
                  
    def only_accept(self):
        f = False
        self.printc.yellow('Do You Want To Check Followers For Requester? [Y/N]')
        self.public_mod = input()
        if self.public_mod.lower() == 'y':
                   self.public_num = int(self.inputc.yellow("Set a Num :"))
        clear()
        while 1 != 2: 
            self._accept(f)


    def follow(self, id):
                        import requests
                        from urls import url_follow
                        csrf = requests.get(url_follow(id), headers=headers(''), cookies=self.cookie).cookies.get_dict()['csrftoken']
                        requests.post(url_follow(id), headers=headers(csrf), cookies=self.cookie) 
    def _accept_and_follow(self):
        f = True
        self.printc.yellow('Do You Want To Check Followers For Requester? [Y/N]')
        self.public_mod = input()
        if self.public_mod.lower() == 'y':
            self.public_num = int(self.inputc.yellow("Set a Num :"))
        clear()
        while 2 != 1:
            self._accept(f)
                   
    def igrone(self, id):
        from colorama import init, Fore, Back, Style
        from urls import url_ignore_follower
        csrf = self.requests.get(url_ignore_follower(id), headers=headers(''), cookies=self.cookie).cookies.get_dict()['csrftoken']
        ig = self.requests.post(url_ignore_follower(id), headers=headers(f'{csrf}'),cookies=self.cookie)
        if '{"status":"ok"}' in ig.text:clear();print(Fore.RED + Style.BRIGHT + f'Done igrone.\n Username : {self.username}\n Because He spam follow\n'+Style.RESET_ALL+Fore.RED + Style.BRIGHT +f'Check Num:{self.count}'+ Style.RESET_ALL); sleep(8)
        else:clear();print(Fore.RED + Style.BRIGHT + f'Can not igrone.\n Username : {self.username}\n Because He spam follow\n'+Style.RESET_ALL+Fore.RED + Style.BRIGHT +f'Check Num:{self.count}'+ Style.RESET_ALL); sleep(8)
    
    def block(self,id):
        from urls import url_block
        from colorama import init, Fore, Back, Style
        csrf = self.requests.get(url_block(id), headers=headers(''), cookies=self.cookie).cookies.get_dict()['csrftoken']
        bl = self.requests.post(url_block(id), headers=headers(f'{csrf}'),cookies=self.cookie)
        if '{"status":"ok"}' in bl.text:
            clear()
            print(Fore.RED + Style.BRIGHT + f'Done Block.\n Username : {self.username}\n Because He spam follow\n'+Style.RESET_ALL+Fore.RED + Style.BRIGHT +f'Check Num:{self.count}'+ Style.RESET_ALL)
            sleep(8)
        else:
             clear()
             print(Fore.RED + Style.BRIGHT + f'Can not Block.\n Username : {self.username}\n Because He spam follow\n'+Style.RESET_ALL+Fore.RED + Style.BRIGHT +f'Check Num:{self.count}'+ Style.RESET_ALL)
    
    
    def get_follow_id(self):
        from urls import url_get_requests
        from colorama import init, Fore, Back, Style
        _id = self.requests.get(url_get_requests(), headers=headers(''),cookies=self.cookie)
        if _id.status_code != self.too_many_requests:
            id = _id.json()['graphql']['user']['edge_follow_requests']['edges'][0]['node']['id']   
            self.username = _id.json()['graphql']['user']['edge_follow_requests']['edges'][0]['node']['username']
                    
            return id
        else:
                if self.blocked != 1:
                    self.check_time()
                    self.blocked +=1
                    clear()
                    self.printc.red("You Get Blocked")
                    sleep(4)
                    clear()
                    self.time +=10
                    self.printc.yellow("We Up Your Sleep For 10 Sec More. \n Your Sleep Now {sleep}".format(sleep = self.time))
                    sleep(8)
                    clear()
                else:
                    self.check_time()
                    clear()
                    self.printc.red("You Get Blocked Again We Will Sleep 2Min!")
                    sleep(60+60)
                    clear()
                    self.time +=20
                    self.printc.yellow("We Up Your Sleep For 20 Sec More. \n Your Sleep Now {sleep}".format(sleep = self.time))
                    sleep(8)   
    def check_time(self):
        if self.time > self.min: self.time = self.frist_sleep; self.printc.red(f"You Sleep Time Exceed 60 second So We Rest it to {self.frist_sleep}'s")
        else: pass
        
#200 :P
