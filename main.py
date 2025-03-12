import telebot
from telebot import types

bot = telebot.TeleBot("7849326046:AAHWM7DUp1PlwZHRu6JLyu4ITszTRrD9GEM")
admin_id = 5469194001

class User:
    def __init__(self, id, name, username):
        self.id = id
        self.name = name
        self.username = username
        self.orders = []
        self.busket = []
        self.promocodes = ["first15"]
    
    def show_info(self):
        bot.send_message(self.id, f"Id: {self.id}")
        bot.send_message(self.name, f"name {self.name}")
        bot.send_message(self.username, f"name {self.username}")
        
    def show_orders(self):
        if len(self.orders):
            bot.send_message(self.id, "Список заказов:")
            for order in self.orders:
                bot.send_message(self.id, order)
        else:
            bot.send_message(self.id, "Вы ещё ничего не покупали")
            
    def show_busket(self):
        if len(self.busket):
            bot.send_message(self.id, "Корзина:")
            for order in self.busket:
                bot.send_message(self.id, item)
        else:
            bot.send_message(self.id, "Вы ещё ничего не добавили")

@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, "qq")
    
    menu_button = types.InlineKeyboardMarkup()
    shop = types.InlineKeyboardButton("Посмотреть товары", callback_data="shop")
    help = types.InlineKeyboardButton("Помощь", callback_data="help")
    admin = types.InlineKeyboardButton("Обратиться к администратору", callback_data="admin")
    profile = types.InlineKeyboardButton("Профиль", callback_data="profile")
    edit_profile = types.InlineKeyboardButton("Редактировать профиль", callback_data="edit_profile")
    orders = types.InlineKeyboardButton("Мои заказы", callback_data="orders")
    
    for button in shop, help, admin, profile, edit_profile, orders:
        menu_button.row(button)
        
    bot.send_message(message.chat.id, "Выберите нужный пункт меню", reply_markup=menu_button)
    
@bot.callback_query_handler(func=lambda callback: True)
def main(callback):
    id = callback.message.chat.id
    
    match callback.data:
        case "shop":
            bot.send_message(id, "Список ключей:")
        case "help":
            bot.send_message(id, "хелпа")
        case "admin":
            bot.send_message(id, "Обратится к администратору")
            call_admin(callback.message)
        case "profile":
            bot.send_message(id, "Ваш профиль")
        case "edit_profile":
            bot.send_message(id, "изменение профиля")
        case "orders":
            bot.send_message(id, "Ваши покупки:")
            

def call_admin(message):
    message = bot.send_message(message.chat.id, "Опишите ваш вопрос")
    bot.register_next_step_handler(message, send_admin)
    
def send_admin(message):
    bot.send_message(message.chat.id, "Администратор скоро с вами свяжется")
    bot.send_message(admin_id, f"Вопрос от @{message.from_user.username} \n"
                                f"{message.text}")

bot.polling()