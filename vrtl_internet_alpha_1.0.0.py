#КЛАССЫ

class server:
    def __init__(self, ip_domen_up, name):
        self.ip_domen_up = ip_domen_up
        self.name = name

class user:
    def __init__(self, name, ip_domen_down):
        self.name = name
        self.ip_domen_down = ip_domen_down

class website:
    def __init__(self, name, ip_domen_up, text, domen, ip_domen_down):
        self.name = name
        self.ip_domen_up = ip_domen_up
        self.text = text
        self.server = server
        self.domen = domen
        self.ip_domen_down = ip_domen_down
        
    def apend_to_list(self):
        ip_domens_up.append(self)
        
    def go_website(self, domen):
        print(f"домен: {self.domen}")
        print(f"название: {self.name}")
        print()
        print(f"{self.text}")
        print()
        _exit = input("1.выйти: ")
        if _exit == "1":
            brovser()
            
    def website_ip_domen(self):
        ip_website_domen.append({ip_domen_up: domen})
        

class dns:
    def __init__(self, ip_domen_up, name):
        self.ip_domen_up = ip_domen_up
        self.name = name
        
        
#СПИСКИ/ПЕРЕМЕНЫЕ
        
ip_website_domen = []
ip_domens_up = {"2.1.1"}
ip_domens_down = {"0.1.1", "0.2.1"}
user_name = [{"0.1.1": "maks"}, {"0.2.1": "NE_maks"}]
users_domen = [".maks"]
result_ip = ""

actyal_user_ip = "0.1.1"
actyal_name = ""

_d = False

#ПРОТОКОЛЫ

def protokol_ip(typee):
    one = ""
    two = ""
    three = "1"
    if typee == "server":
        one = "2"
    if typee =="website":
        one = "1"
    if typee == "user":
        one = "0"
        
    if typee == "user":
        number_user = len(ip_domens_down) + 2
        two = number_user
        
    if typee == "server" or "website":
        number_up_ip = len(ip_domens_up) + 2
        two = number_up_ip
    
    if typee == "server":
        type_ = " сервера"
        type_ip = "up"
        
    if typee == "website":
        type_ = " сайта"
        type_ip = "up"
        
    if typee == "user":
        type_ = ""
        type_ip = "down"

    result_ip_domen = f"{one}.{two}.{three}"
    result_ip = result_ip_domen
    print(f"ваш айпи{type_}: {result_ip_domen}")
    print(f"ваш тип айпи: {type_ip}")

def protokol_ip_to_name(user_ip):
    global actyal_name
    for i in user_name:
        if user_ip in i:
            _an = i[user_ip]
    actyal_name = _an
    
def protokol_ip_to_domen(domen):
    global domens_actyal
    for i in ip_website_domen:
        if domen in i:
            _id = i[domen]
        domens_actyal = _id
        #сорянчик,чет делал но понял что бесмыслено,можно чисто по домену поиск
            

#ФУНКЦИИ
def _exit_(type):
    if type == "brovser":
        brovser()
    if type == "menu":
        menu_admin(actyal_user_ip)
        
def menu_admin(user_ip):
    protokol_ip_to_name(user_ip)
    print(f"пользватель: {actyal_name}")
    print(f"айпи пользвателя: {user_ip}")
    print("0. сменить акаунт")
    print("1. браузер")
    _choice = input("> ")
    
    if _choice == "0":
        if actyal_user_ip == "0.1.1":
            menu_admin("0.2.1")
        elif actyal_user_ip == "0.2.1":
            menu_admin("0.1.1")
    elif _choice == "1":
        brovser()
    else:
        menu_admin(actyal_user_ip)
        
        
def created_website(user_ip):
    global web_site
    ip_creator = user_ip
    print("введите название сайта")
    name_website = input("> ")
    
    print("введите домен своего сайта с .maks")
    domen_website = input("> ")
    domen_check = domen_website[-5:]
    register_domen(domen_website)
    if domen_check == ".maks" and _d == True:
        print("успешно!")
    elif domen_check != ".maks":
        print(domen_check)
        print("ошибка! измените домен на .maks!")
        domen_website = ""
        created_website(actyal_user_ip)
        
    print("напишите текст для сайта")
    text_website = input("> ")
    print("успешно!")
    
    protokol_ip("website")
    web_site = website(name_website, result_ip, text_website, domen_website, user_ip)
    web_site.apend_to_list
    web_site.website_ip_domen
    _exit_("menu")
    
def register_domen(domen):
    domen_origin = True
    for i in users_domen:
        if i == domen:
            domen_origin = False
    if domen_origin == False:
        print("ошибка!домен не доступен")
        created_website(actyal_user_ip)
    elif domen_origin == True:
        _d = True
        users_domen.append(domen)
        print("домен успешно зарегестрирован!")

def website_spicok(domen):
    for i in users_domen:
        if domen == i:
            _ws = i
            print("0. назад")
            print(f"1. {_ws}")
            _choice_website = input("> ")
            if _choice_website == "0":
                _exit_("brovser")
            if _choice_website == "1":
                web_site.go_website(domen)
            else:
                print("не найдено")
                _exit_("brovser")
                
            
    
def brovser():
    print()
    print("браузер ")
    print("1.поиск")
    print("2.создать сайт")
    print("3.назад в меню")
    __choice = input("> ")
    
    if __choice == "1":
        _search = input("введите домен сайта: ")
        website_spicok(_search)
    
    if __choice == "2":
        created_website(actyal_user_ip)
        
    if __choice == "3":
        _exit_("menu")
        
    
    

menu_admin(actyal_user_ip)

        


        
