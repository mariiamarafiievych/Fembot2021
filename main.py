import telebot
import datetime
import pandas as pd

try:
    import Image
except ImportError:
    from PIL import Image
import tg_analytic

bot = telebot.TeleBot("1372969532:AAEVJgqxGHbza1FQxFIYm0qfiawmLnRz_vo")

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Даша', 'Маша', 'Саша')
keyboard1.row('Соня', 'Катя', 'Чіта')
keyboard1.row('Історії', 'Бот створений за підтримки', 'Джерела інформації')

now = datetime.datetime.now()
df_mis = pd.read_csv('misyachni.csv', delimiter=';')
df_mis = df_mis.set_index('button')
df_obl = pd.read_csv('oblasti.csv', delimiter=';')
df_obl = df_obl.set_index('button')
df_gromo = pd.read_csv('gromo.csv', delimiter=';')
df_gromo = df_gromo.set_index('button')
df_sex = pd.read_csv('sex.csv', delimiter=';')
df_sex = df_sex.set_index('button')
df_docs = pd.read_csv('docs.csv', delimiter=';')
df_docs = df_docs.set_index('button')
df_acomm = pd.read_csv('accommodation.csv', delimiter=';')
df_acomm = df_acomm.set_index('button')
df_budget = pd.read_csv('budget.csv', delimiter=';')
df_budget = df_budget.set_index('button')
df_komunalka = pd.read_csv('komunalka.csv', delimiter=';')
df_komunalka = df_komunalka.set_index('button')
df_money = pd.read_csv('money.csv', delimiter=';')
df_money = df_money.set_index('button')
df_eat = pd.read_csv('eat.csv', delimiter=';')
df_eat = df_eat.set_index('button')
df_entertainment = pd.read_csv('entertainment.csv', delimiter=';')
df_entertainment = df_entertainment.set_index('button')
df_nasylstvo = pd.read_csv('nasylstvo.csv', delimiter=';')
df_nasylstvo = df_nasylstvo.set_index('button')
df_cps = pd.read_csv('cps.csv', delimiter=';')
df_cps = df_cps.set_index('button')
df_kdm = pd.read_csv('kdm.csv', delimiter=';')
df_kdm = df_kdm.set_index('button')
df_lin_deti = pd.read_csv('liniiDeti.csv', delimiter=';')
df_lin_deti = df_lin_deti.set_index('button')
df_lin_reg = pd.read_csv('liniiReg.csv', delimiter=';')
df_lin_reg = df_lin_reg.set_index('button')
df_lin_nas = pd.read_csv('liniiNas.csv', delimiter=';')
df_lin_nas = df_lin_nas.set_index('button')
df_histories = pd.read_csv('histories.csv', delimiter=';')
df_histories = df_histories.set_index('button')
df_support = pd.read_csv('support.csv', delimiter=';')
df_support = df_support.set_index('button')
df_sources = pd.read_csv('sources.csv', delimiter=';')
df_sources = df_sources.set_index('button')


@bot.message_handler(commands=['start'])
def start_message(message):
    markdown = """
        *bold text*
        _italic text_
        [text](URL)
        """
    start_0_text = """Привітики ;) 
    
Ти в чат-боті  проекту “sisters straw”, а отже тобі не байдуже до потреб дівчаток- та жінок - випускниць інтернатних закладів і взагалі, ти – за права дівчаток, дівчат, жінок.

"""

    start_1_text = """*Чому sisters` straw?*"""
    start_2_text = """
У перекладі з англійської – це «сестринська соломка». Дівчатка, зокрема ті, які перебувають в інтернатах та всі його випускниці, на жаль, стикаються з багатьма проблемами. Ми не зможемо зовсім вберегтися від падінь, але завдяки цьому проекту, спробуємо «підстелити соломку» аби було хоч трішечки менш болісно.
    
"""

    start_3_text = """*У цьому боті зібралися подружки - Даша, Маша, Саша, Соня і Катя з крискою Чітою ))*"""

    start_4_text ="""
    
Ти тепер у нашій тусовці :)
Про нас: 

"""
    start_5_text ="""*Даша*"""
    start_6_text =""" - експертка з сексу;
    
"""

    start_7_text ="""*Маша*"""
    start_8_text =""" - може розповісти тобі про насильство;
    
"""

    start_9_text ="""*Саша*"""
    start_10_text =""" - займається правами людей і допоможе тобі з доками;
    
"""

    start_11_text ="""*Соня*"""
    start_12_text =""" - бізнес вумен, знає все про фінанси;
    
"""

    start_13_text ="""*Катя*"""
    start_14_text =""" - має список важливих контактів;
    
"""

    start_15_text ="""Ну і криска """
    start_16_text ="""*Чіта*"""
    start_17_text =""" буде відповідальна за твій класний настрій та смачну їжу."""
    start_text = start_0_text + start_1_text + start_2_text + start_3_text + start_4_text + start_5_text + start_6_text + start_7_text+start_8_text+start_9_text+start_10_text+start_11_text+start_12_text+start_13_text+start_14_text+start_15_text+start_16_text+start_17_text
    bot.send_message(message.chat.id, start_text, reply_markup=keyboard1, parse_mode="Markdown")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Даша":
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Все про секс', 'Місячні')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, """Йоу, мене звати Даша! Мені 19, і я з Києва. Моє статеве життя почалося в 16 років, я зустрічалася з 3 чуваками. 
Зараз у мене тривалі романтичні стосунки з Максимом, і взагалі все кльово. Я періодично обстежуюся у гінеколога, і багато про це знаю. 
І хочу тобі про все розповісти, запитай, що тебе цікавить))""", reply_markup=keyboard1)
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img1 = open('dasha.png', 'rb')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        bot.register_next_step_handler(message, dasha)
    elif message.text == "Маша":
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Детальніше', 'Важливо!', 'Куди звернутися?')
        keyboard1.row('Як?', 'Що буде?', 'Поради')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id,
                         "Привіт, я Маша. Мені 25, я психологиня, допоможу тобі розпізнати насильство та як себе захистити.",
                         reply_markup=keyboard1)
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img1 = open('masha.png', 'rb')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        bot.register_next_step_handler(message, nasylstvo)
    elif message.text == "Саша":
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Дія', 'Паспорт', 'Закордонний паспорт')
        keyboard1.row('Договір при оренді житла', 'Повідомлення про злочин', 'Загальна заява до поліції')
        keyboard1.row('Оскарження дій слідчих', 'У разі домашнього насильства')
        keyboard1.row('Безоплатна правова допомога', 'Рекомендую')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, """Хай, я - Саша, вже 4 роки працюю в громадській організації. 
Можу розповісти тобі про твої права і допоможу не загубитися в документах. Звернись до мене.""",
                         reply_markup=keyboard1)
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img1 = open('sasha.png', 'rb')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        bot.register_next_step_handler(message, doc)
    elif message.text == "Соня":
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row("Житло", "Планування бюджету", "Комуналка")
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, """Звертайся до мене просто Соня. Мені 22, закінчила економічний універ. Моя мрія переїхати в Нью-Йорк, і я багато працюю над її реалізацією. 
Якщо тебе цікавить мій план, натискай кнопки:""", reply_markup=keyboard1)
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img1 = open('sonya.png', 'rb')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        bot.register_next_step_handler(message, money)
    elif message.text == "Катя":
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Центри планування сім`ї', 'Громадські організаціїї')
        keyboard1.row("Соціальні служби", 'Клініки дружні до молоді')
        keyboard1.row("Гарячі лінії")
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, """Hola, я Катя - працюю в секретній службі і знаю все про всіх. Але я надаю перевагу залишатися анонімною. 
Зіллю тобі базу важливих контактів, якщо тобі потрібно:""", reply_markup=keyboard1)
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img1 = open('katya.png', 'rb')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        bot.register_next_step_handler(message, contact)
    elif message.text == "Чіта":
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Що подивитись/почитати?', 'Хочу їсти')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id,
                         """Шух-шух, я криска Чіта. Моя домівка на кухні у Каті, я слідкую, як вона розважається, і що вона їсть. Розповім всі секретики.""",
                         reply_markup=keyboard1)
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img1 = open('chita.png', 'rb')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        bot.register_next_step_handler(message, chita)
    elif message.text == 'Історії':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row("Історія Юлі", "Історія Світлани")
        keyboard1.row("Історія Жанни", "Історія Ірини")
        keyboard1.row("Історія Домініки", "Тут допоможуть")
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, df_histories.loc[message.text]['text'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, histories)
    elif message.text == 'Бот створений за підтримки':
        bot.send_message(message.from_user.id, df_support.loc[message.text]['text'])
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img1 = open('жп.png', 'rb')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        img2 = open('вісь.png', 'rb')
        bot.send_photo(message.chat.id, img2)
        img2.close()
        bot.register_next_step_handler(message, handle_text)
    elif message.text == 'Джерела інформації':
        bot.send_message(message.from_user.id, df_sources.loc[message.text]['text'])
        bot.register_next_step_handler(message, handle_text)
    elif message.text[:10] == 'статистика' or message.text[:10] == 'Cтатистика':
        st = message.text.split(' ')
        if 'txt' in st or 'тхт' in st:
            tg_analytic.analysis(st, message.chat.id)
            with open('%s.txt' % message.chat.id, 'r', encoding='UTF-8') as file:
                bot.send_document(message.chat.id, file)
                tg_analytic.remove(message.chat.id)
        else:
            messages = tg_analytic.analysis(st, message.chat.id)
            bot.send_message(message.chat.id, messages)


def dasha(message):
    if message.text == 'Все про секс':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Що це?', 'Права', 'Сексуальність')
        keyboard1.row('Поганий вплив', 'Вагітність', 'Як захиститися?')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex)
    elif message.text == 'Місячні':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Кров – це ок', 'Перші місячні (менархе)', 'Підмивання')
        keyboard1.row('Засоби гігієни', 'Похід до гінеколог(ині)а', 'Календар місячних')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, df_mis.loc[message.text]['text'],
                         reply_markup=keyboard1)
        bot.register_next_step_handler(message, mis)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Даша', 'Маша', 'Саша')
        keyboard1.row('Соня', 'Катя', 'Чіта')
        keyboard1.row('Історії', 'Бот створений за підтримки', 'Джерела інформації')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, handle_text)


def chita(message):
    if message.text == 'Що подивитись/почитати?':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Серіали', 'Кіно', "Різне")
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, df_entertainment.loc[message.text]['text'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, entertainment)
    elif message.text == 'Хочу їсти':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row("Сніданок", "Обід", "Вечеря", "Перекус")
        keyboard1.row("Користь", "Економія")
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, df_eat.loc[message.text]['text'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, eat)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Даша', 'Маша', 'Саша')
        keyboard1.row('Соня', 'Катя', 'Чіта')
        keyboard1.row('Історії', 'Бот створений за підтримки', 'Джерела інформації')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, handle_text)


def histories(message):
    if message.text == 'Історія Юлі':
        bot.send_message(message.from_user.id, df_histories.loc[message.text]['text'])
        bot.register_next_step_handler(message, histories)
    elif message.text == 'Історія Світлани':
        bot.send_message(message.from_user.id, df_histories.loc[message.text]['text'])
        bot.register_next_step_handler(message, histories)
    elif message.text == 'Історія Жанни':
        bot.send_message(message.from_user.id, df_histories.loc[message.text]['text'])
        bot.register_next_step_handler(message, histories)
    elif message.text == 'Історія Ірини':
        bot.send_message(message.from_user.id, df_histories.loc[message.text]['text'])
        bot.register_next_step_handler(message, histories)
    elif message.text == 'Історія Домініки':
        bot.send_message(message.from_user.id, df_histories.loc[message.text]['text'])
        bot.register_next_step_handler(message, histories)
    elif message.text == 'Тут допоможуть':
        bot.send_message(message.from_user.id, df_histories.loc[message.text]['text'])
        bot.register_next_step_handler(message, histories)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Даша', 'Маша', 'Саша')
        keyboard1.row('Соня', 'Катя', 'Чіта')
        keyboard1.row('Історії', 'Бот створений за підтримки', 'Джерела інформації')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, handle_text)


def sex(message):
    if message.text == 'Що це?':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.from_user.id, df_sex.loc[message.text]['text'],
                         reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex)
    elif message.text == 'Права':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.from_user.id, df_sex.loc[message.text]['text'],
                         reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex)
    elif message.text == 'Сексуальність':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.from_user.id, df_sex.loc[message.text]['text'],
                         reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex)
    elif message.text == 'Поганий вплив':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Куріння', 'Алкоголь', 'Наркотики')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex_1)
    elif message.text == 'Вагітність':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Твої права', 'Аборт')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex_1)
    elif message.text == 'Як захиститися?':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Безпека', 'Інфекції (ІПСШ)', 'Контрацептиви')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex_1)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Все про секс', 'Місячні')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, dasha)


def sex_1(message):
    if message.text == 'Куріння':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.from_user.id, df_sex.loc[message.text]['text'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex_1)
    elif message.text == 'Алкоголь':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.from_user.id, df_sex.loc[message.text]['text'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex_1)
    elif message.text == 'Наркотики':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.from_user.id, df_sex.loc[message.text]['text'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex_1)
    elif message.text == 'Твої права':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.from_user.id, df_sex.loc[message.text]['text'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex_1)
    elif message.text == 'Аборт':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.from_user.id, df_sex.loc[message.text]['text'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex_1)
    elif message.text == 'Безпека':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.from_user.id, df_sex.loc[message.text]['text'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex_1)
    elif message.text == 'Інфекції (ІПСШ)':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.from_user.id, df_sex.loc[message.text]['text'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex_1)
    elif message.text == 'Контрацептиви':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Бар`єрні', 'Гормональні')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex_2)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Що це?', 'Права', 'Сексуальність')
        keyboard1.row('Поганий вплив', 'Вагітність', 'Як захиститися?')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex)


def sex_2(message):
    if message.text == 'Бар`єрні':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.from_user.id, df_sex.loc[message.text]['text'], reply_markup=keyboard1)
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('prez.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        img.close()
        bot.register_next_step_handler(message, sex_2)
    elif message.text == 'Гормональні':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.from_user.id, df_sex.loc[message.text]['text'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex_2)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Безпека', 'Інфекції (ІПСШ)', 'Контрацептиви')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, sex_1)


def eat(message):
    if message.text == 'Сніданок':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_eat.loc[message.text]['text'])
        bot.register_next_step_handler(message, eat)
    elif message.text == 'Обід':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_eat.loc[message.text]['text'])
        bot.register_next_step_handler(message, eat)
    elif message.text == 'Вечеря':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_eat.loc[message.text]['text'])
        bot.register_next_step_handler(message, eat)
    elif message.text == 'Перекус':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_eat.loc[message.text]['text'])
        bot.register_next_step_handler(message, eat)
    elif message.text == 'Економія':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_eat.loc[message.text]['text'])
        bot.register_next_step_handler(message, eat)
    elif message.text == 'Користь':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_eat.loc[message.text]['text'])
        bot.register_next_step_handler(message, eat)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Що подивитись/почитати?', 'Хочу їсти')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, chita)


def nasylstvo(message):
    if message.text == 'Детальніше':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_nasylstvo.loc[message.text]['text'])
        bot.register_next_step_handler(message, nasylstvo)
    elif message.text == 'Важливо!':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_nasylstvo.loc[message.text]['text'])
        bot.register_next_step_handler(message, nasylstvo)
    elif message.text == 'Куди звернутися?':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_nasylstvo.loc[message.text]['text'])
        bot.register_next_step_handler(message, nasylstvo)
    elif message.text == 'Як?':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_nasylstvo.loc[message.text]['text'])
        bot.register_next_step_handler(message, nasylstvo)
    elif message.text == 'Що буде?':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_nasylstvo.loc[message.text]['text'])
        bot.register_next_step_handler(message, nasylstvo)
    elif message.text == 'Поради':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Юристки', 'Психологині', 'План безпеки')
        keyboard1.row('Подивись', 'Контакти')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?",
                         reply_markup=keyboard1)
        bot.register_next_step_handler(message, nasylstvo_2)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Даша', 'Маша', 'Саша')
        keyboard1.row('Соня', 'Катя', 'Чіта')
        keyboard1.row('Історії', 'Бот створений за підтримки', 'Джерела інформації')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, handle_text)


def nasylstvo_2(message):
    if message.text == 'Юристки':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_nasylstvo.loc[message.text]['text'])
        bot.register_next_step_handler(message, nasylstvo_2)
    elif message.text == 'Психологині':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_nasylstvo.loc[message.text]['text'])
        bot.register_next_step_handler(message, nasylstvo_2)
    elif message.text == 'План безпеки':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_nasylstvo.loc[message.text]['text'])
        bot.register_next_step_handler(message, nasylstvo_2)
    elif message.text == 'Булінг':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_nasylstvo.loc[message.text]['text'])
        bot.register_next_step_handler(message, nasylstvo_2)
    elif message.text == 'Подивись':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_nasylstvo.loc[message.text]['text'])
        bot.register_next_step_handler(message, nasylstvo_2)
    elif message.text == 'Контакти':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_nasylstvo.loc[message.text]['text'])
        bot.register_next_step_handler(message, nasylstvo_2)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Детальніше', 'Важливо!', 'Куди звернутися?')
        keyboard1.row('Як?', 'Що буде?', 'Поради')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, nasylstvo)


def entertainment(message):
    if message.text == 'Серіали':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_entertainment.loc[message.text]['text'])
        bot.register_next_step_handler(message, entertainment)
    elif message.text == 'Кіно':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_entertainment.loc[message.text]['text'])
        bot.register_next_step_handler(message, entertainment)
    elif message.text == 'Різне':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_entertainment.loc[message.text]['text'])
        bot.register_next_step_handler(message, entertainment)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Що подивитись/почитати?', 'Хочу їсти')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, chita)


def money(message):
    if message.text == 'Житло':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Поради', 'Шахраї')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, money_2)
    elif message.text == 'Планування бюджету':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Додатки', 'Оплата карткою')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, money_2)
    elif message.text == 'Комуналка':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Що це?', 'Важливо', 'Як?', 'Коли?', 'Квитанції')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, money_2)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Даша', 'Маша', 'Саша')
        keyboard1.row('Соня', 'Катя', 'Чіта')
        keyboard1.row('Історії', 'Бот створений за підтримки', 'Джерела інформації')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, handle_text)


def money_2(message):
    if message.text == 'Поради':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_acomm.loc[message.text]['text'])
        bot.register_next_step_handler(message, money_2)
    elif message.text == 'Шахраї':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_acomm.loc[message.text]['text'])
        bot.register_next_step_handler(message, money_2)
    elif message.text == 'Додатки':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_budget.loc[message.text]['text'])
        bot.register_next_step_handler(message, money_2)
    elif message.text == 'Оплата карткою':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_budget.loc[message.text]['text'])
        bot.register_next_step_handler(message, money_2)
    elif message.text == 'Що це?':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_komunalka.loc[message.text]['text'])
        bot.register_next_step_handler(message, money_2)
    elif message.text == 'Важливо':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_komunalka.loc[message.text]['text'])
        bot.register_next_step_handler(message, money_2)
    elif message.text == 'Як?':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_komunalka.loc[message.text]['text'])
        bot.register_next_step_handler(message, money_2)
    elif message.text == 'Коли?':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_komunalka.loc[message.text]['text'])
        bot.register_next_step_handler(message, money_2)
    elif message.text == 'Квитанції':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_komunalka.loc[message.text]['text'])
        bot.register_next_step_handler(message, money_2)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row("Житло", "Планування бюджету", "Комуналка")
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, money)


def mis(message):
    if message.text == 'Перші місячні (менархе)':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Дізнатися більше')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, df_mis.loc[message.text]['text'],
                         reply_markup=keyboard1)
        bot.register_next_step_handler(message, mis_2)
    elif message.text == 'Засоби гігієни':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Одноразові прокладки', 'Тампони', 'Менструальна чаша')
        keyboard1.row('Багаторазові прокладки', 'Менструальні труси')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, mis_2)
    elif message.text == 'Похід до гінеколог(ині)а':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Більше інформації')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, df_mis.loc[message.text]['text'],
                         reply_markup=keyboard1)
        bot.register_next_step_handler(message, mis_2)
    elif message.text == 'Кров – це ок':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_mis.loc[message.text]['text'])
        bot.register_next_step_handler(message, mis)
    elif message.text == 'Підмивання':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_mis.loc[message.text]['text'])
        bot.register_next_step_handler(message, mis)
    elif message.text == 'Календар місячних':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_mis.loc[message.text]['text'])
        bot.register_next_step_handler(message, mis)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Все про секс', 'Місячні')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, dasha)


def mis_2(message):
    if message.text == 'Дізнатися більше':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_mis.loc[message.text]['text'])
        bot.register_next_step_handler(message, mis_2)
    elif message.text == 'Одноразові прокладки':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_mis.loc[message.text]['text'])
        bot.register_next_step_handler(message, mis_2)
    elif message.text == 'Тампони':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_mis.loc[message.text]['text'])
        bot.register_next_step_handler(message, mis_2)
    elif message.text == 'Менструальна чаша':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_mis.loc[message.text]['text'])
        bot.register_next_step_handler(message, mis_2)
    elif message.text == 'Багаторазові прокладки':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_mis.loc[message.text]['text'])
        bot.register_next_step_handler(message, mis_2)
    elif message.text == 'Менструальні труси':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_mis.loc[message.text]['text'])
        bot.register_next_step_handler(message, mis_2)
    elif message.text == 'Більше інформації':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_mis.loc[message.text]['text'])
        bot.register_next_step_handler(message, mis_2)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Кров – це ок', 'Перші місячні (менархе)', 'Підмивання')
        keyboard1.row('Засоби гігієни', 'Похід до гінеколог(ині)а', 'Календар місячних')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?",
                         reply_markup=keyboard1)
        bot.register_next_step_handler(message, mis)


def doc(message):
    if message.text == 'Дія':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_docs.loc[message.text]['text'])
        bot.register_next_step_handler(message, doc)
    elif message.text == 'Паспорт':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_docs.loc[message.text]['text'])
        bot.register_next_step_handler(message, doc)
    elif message.text == 'Закордонний паспорт':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_docs.loc[message.text]['text'])
        bot.register_next_step_handler(message, doc)
    elif message.text == 'Договір при оренді житла':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_docs.loc[message.text]['text'])
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('оренда_житла.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        img.close()
        bot.register_next_step_handler(message, doc)
    elif message.text == 'Повідомлення про злочин':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_docs.loc[message.text]['text'])
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('злочин.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        img.close()
        bot.register_next_step_handler(message, doc)
    elif message.text == 'Загальна заява до поліції':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_docs.loc[message.text]['text'])
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('загал_заява.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        img.close()
        bot.register_next_step_handler(message, doc)
    elif message.text == 'Оскарження дій слідчих':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_docs.loc[message.text]['text'])
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('скарга_1.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        img.close()
        img1 = open('скарга_2.jpg', 'rb')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        bot.register_next_step_handler(message, doc)
    elif message.text == 'У разі домашнього насильства':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_docs.loc[message.text]['text'])
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('насильство_1.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        img.close()
        img1 = open('насильство_2.jpg', 'rb')
        bot.send_photo(message.chat.id, img1)
        img1.close()
        bot.register_next_step_handler(message, doc)
    elif message.text == 'Безоплатна правова допомога':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_docs.loc[message.text]['text'])
        bot.register_next_step_handler(message, doc)
    elif message.text == 'Рекомендую':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id, df_docs.loc[message.text]['text'])
        bot.register_next_step_handler(message, doc)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Даша', 'Маша', 'Саша')
        keyboard1.row('Соня', 'Катя', 'Чіта')
        keyboard1.row('Історії', 'Бот створений за підтримки', 'Джерела інформації')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, handle_text)


def contact(message):
    if message.text == 'Центри планування сім`ї':
        tg_analytic.statistics(message.chat.id, message.text)
        inline_keyboard0 = telebot.types.InlineKeyboardMarkup(row_width=2)
        for i in range(40):
            if i != 0 and df_cps.iloc[i].name == df_cps.iloc[i - 1].name:
                continue
            else:
                cps = df_cps.iloc[i]
                button = telebot.types.InlineKeyboardButton(text=cps.name, callback_data=cps.name)
                inline_keyboard0.add(button)
        bot.send_message(message.chat.id, 'Центри планування сім`ї', reply_markup=inline_keyboard0)
        bot.register_next_step_handler(message, contact)
    elif message.text == 'Соціальні служби':
        tg_analytic.statistics(message.chat.id, message.text)
        inline_keybord1 = telebot.types.InlineKeyboardMarkup(row_width=2)
        for i in range(29):
            if i != 0 and df_obl.iloc[i].name == df_obl.iloc[i - 1].name:
                continue
            else:
                obl = df_obl.iloc[i]
                button = telebot.types.InlineKeyboardButton(text=obl.name, callback_data=obl.name)
                inline_keybord1.add(button)
        bot.send_message(message.chat.id, 'Соціальні служби', reply_markup=inline_keybord1)
        bot.register_next_step_handler(message, contact)
    elif message.text == 'Громадські організаціїї':
        tg_analytic.statistics(message.chat.id, message.text)
        inline_keybord2 = telebot.types.InlineKeyboardMarkup(row_width=2)
        for i in range(27):
            if i != 0 and df_gromo.iloc[i].name == df_gromo.iloc[i - 1].name:
                continue
            else:
                grom = df_gromo.iloc[i].name
                button = telebot.types.InlineKeyboardButton(text=grom, callback_data=grom)
                inline_keybord2.add(button)
        bot.send_message(message.chat.id, 'Громадські організаціїї', reply_markup=inline_keybord2)
        bot.register_next_step_handler(message, contact)
    elif message.text == 'Клініки дружні до молоді':
        tg_analytic.statistics(message.chat.id, message.text)
        inline_keybord3 = telebot.types.InlineKeyboardMarkup(row_width=2)
        for i in range(128):
            if i != 0 and df_kdm.iloc[i].name == df_kdm.iloc[i - 1].name:
                continue
            else:
                kdm = df_kdm.iloc[i].name
                button = telebot.types.InlineKeyboardButton(text=kdm, callback_data=kdm)
                inline_keybord3.add(button)
        bot.send_message(message.chat.id, 'Клініки дружні до молоді', reply_markup=inline_keybord3)
        bot.register_next_step_handler(message, contact)
    elif message.text == 'Гарячі лінії':
        tg_analytic.statistics(message.chat.id, message.text)
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Національна поліція України', 'Дитячі гарячі лінії')
        keyboard1.row('Регіональні служби у справах дітей', 'Гарячі лінії з питань запобігання насильству')
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, garyachi)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Даша', 'Маша', 'Саша')
        keyboard1.row('Соня', 'Катя', 'Чіта')
        keyboard1.row('Історії', 'Бот створений за підтримки', 'Джерела інформації')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, handle_text)


def garyachi(message):
    if message.text == 'Національна поліція України':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.from_user.id,
                         "102 або 0- 800-500-202( безкоштовно з мобільних та стаціонарних телефонів)")
        bot.register_next_step_handler(message, garyachi)
    elif message.text == 'Дитячі гарячі лінії':
        tg_analytic.statistics(message.chat.id, message.text)
        inline_keybord5 = telebot.types.InlineKeyboardMarkup(row_width=2)
        for i in range(4):
            linii_det = df_lin_deti.iloc[i].name
            button = telebot.types.InlineKeyboardButton(text=linii_det, callback_data=linii_det)
            inline_keybord5.add(button)
        bot.send_message(message.chat.id, 'Дитячі гарячі лінії', reply_markup=inline_keybord5)
        bot.register_next_step_handler(message, garyachi)
    elif message.text == 'Регіональні служби у справах дітей':
        tg_analytic.statistics(message.chat.id, message.text)
        inline_keybord6 = telebot.types.InlineKeyboardMarkup(row_width=2)
        for i in range(25):
            linii_reg = df_lin_reg.iloc[i].name
            button = telebot.types.InlineKeyboardButton(text=linii_reg, callback_data=linii_reg)
            inline_keybord6.add(button)
        bot.send_message(message.chat.id, 'Регіональні служби у справах дітей', reply_markup=inline_keybord6)
        bot.register_next_step_handler(message, garyachi)
    elif message.text == 'Гарячі лінії з питань запобігання насильству':
        tg_analytic.statistics(message.chat.id, message.text)
        inline_keybord7 = telebot.types.InlineKeyboardMarkup(row_width=2)
        for i in range(15):
            linii_nas = df_lin_nas.iloc[i].name
            button = telebot.types.InlineKeyboardButton(text=linii_nas, callback_data=linii_nas)
            inline_keybord7.add(button)
        bot.send_message(message.chat.id, 'Гарячі лінії з питань запобігання насильству', reply_markup=inline_keybord7)
        bot.register_next_step_handler(message, garyachi)
    elif message.text == 'Повернутись назад':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard1.row('Центри планування сім`ї', 'Громадські організаціїї')
        keyboard1.row("Соціальні служби", 'Клініки дружні до молоді')
        keyboard1.row("Гарячі лінії")
        keyboard1.row('Повернутись назад')
        bot.send_message(message.from_user.id, "Що тебе цікавить?", reply_markup=keyboard1)
        bot.register_next_step_handler(message, contact)


@bot.callback_query_handler(func=lambda call: True)
def contact_1(call):
    if call.message.text == 'Соціальні служби':
        for i in range(29):
            if call.data == df_obl.iloc[i].name:
                bot.send_message(call.message.chat.id, df_obl.iloc[i]['text'])
                bot.send_location(call.message.chat.id, df_obl.iloc[i]['latitude'],
                                  df_obl.iloc[i]['longitude'])
            else:
                continue
    elif call.message.text == 'Громадські організаціїї':
        for i in range(27):
            if call.data == df_gromo.iloc[i].name:
                bot.send_message(call.message.chat.id, df_gromo.iloc[i]['text'])
                bot.send_location(call.message.chat.id, df_gromo.iloc[i]['latitude'],
                                  df_gromo.iloc[i]['longitude'])
            else:
                continue
    elif call.message.text == 'Центри планування сім`ї':
        for i in range(40):
            if call.data == df_cps.iloc[i].name:
                bot.send_message(call.message.chat.id, df_cps.iloc[i]['text'])
                bot.send_location(call.message.chat.id, df_cps.iloc[i]['latitude'],
                                  df_cps.iloc[i]['longitude'])
            else:
                continue
    elif call.message.text == 'Клініки дружні до молоді':
        for i in range(128):
            if call.data == df_kdm.iloc[i].name:
                bot.send_message(call.message.chat.id, df_kdm.iloc[i]['text'])
                bot.send_location(call.message.chat.id, df_kdm.iloc[i]['latitude'],
                                  df_kdm.iloc[i]['longitude'])
            else:
                continue
    elif call.message.text == 'Дитячі гарячі лінії':
        for i in range(4):
            if call.data == df_lin_deti.iloc[i].name:
                bot.send_message(call.message.chat.id, df_lin_deti.iloc[i]['text'])
            else:
                continue
    elif call.message.text == 'Регіональні служби у справах дітей':
        for i in range(25):
            if call.data == df_lin_reg.iloc[i].name:
                bot.send_message(call.message.chat.id, df_lin_reg.iloc[i]['text'])
            else:
                continue
    elif call.message.text == 'Гарячі лінії з питань запобігання насильству':
        for i in range(15):
            if call.data == df_lin_nas.iloc[i].name:
                bot.send_message(call.message.chat.id, df_lin_nas.iloc[i]['text'])
            else:
                continue


if __name__ == '__main__':
    bot.polling()
