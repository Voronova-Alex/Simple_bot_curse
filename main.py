from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update
import random
import logging
import PySimpleGUI as sg
import time

logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

updater = None

dic = {1: 'Балбес',
       2: 'Балда',
       3: 'Бамбук',
       4: 'Баран',
       5: 'Бестолочь',
       6: 'Болван',
       7: 'Валенок',
       8: 'Глупец',
       9: 'Глупыш',
       10: 'Говнюк',
       11: 'Даун',
       12: 'Двоешник',
       13: 'Дебил',
       14: 'Дегенерат',
       15: 'Дуб',
       16: 'Дубина',
       17: 'Дундук',
       18: 'Дура',
       19: 'Дурак',
       20: 'Дурень',
       21: 'Дурилка',
       22: 'Дуримар',
       23: 'Дурында',
       24: 'Дятел',
       25: 'Идиот',
       26: 'Имбецил',
       27: 'Индюк',
       28: 'Козёл',
       29: 'Кретин',
       30: 'Ламер',
       31: 'Лапоть',
       32: 'Лопух',
       33: 'Лох',
       34: 'Микроцефал',
       35: 'Мудак',
       36: 'Муфлон',
       37: 'Недогоняло',
       38: 'Недоумок',
       39: 'Оболтус',
       40: 'Обормот',
       41: 'Олух',
       42: 'Осел',
       43: 'Остолоп',
       44: 'Отморозок',
       45: 'Охламон',
       46: 'Пентюх',
       47: 'Пень',
       48: 'Придурок',
       49: 'Простофиля',
       50: 'Сельпо',
       51: 'Тормоз',
       52: 'Троглодит',
       53: 'Тупица',
       54: 'Тупорыл',
       55: 'Тюфяк',
       56: 'Тюха-матюха',
       57: 'УО',
       58: 'Урод',
       59: 'Чайник',
       60: 'Чурбан'
       }

dic_2 = {1: "Стёб из твоих уст не будет засчитан — ведь ты же не похож на нормального человека)))",
         2: "Я б вас послал, да вижу — вы оттуда!",
         3: "Даааа… С таким юмором ты далеко пойдёшь, ха, ха)",
         4: "Скажи ещё что нибудь, я таких дурачков ещё не видел, удивительно интересно откуда ты такой нарисовался?",
         5: "Я не знаю, что вы едите за завтраком, но это реально действует, интеллект стремится к нулю!",
         6: "Тебя наверно мама в детстве мало обнимала, поэтому ты такой злой? Давай я тебя обниму…",
         7: "Вы часом не Баран по гороскопу?",
         8: "Ты крашеная блондинка или натуральная дура?",
         9: "Вы напоминаете мне океан… Меня от вас так же тошнит.",
         10: "Бабайку вами в детстве не пугали?",
         11: "Тебе зубы жмут? или два глаза это роскошь?",
         12: "А почему бы вам не заняться спасением природы? У меня есть знакомый хирург он может вас стерилизовать.",
         13: "Да кто на ней женится! Самоубийство нынче не в моде.",
         14: "Твое чувство юмора в стадии зачатия.",
         15: "Только не надо вынимать наушники из ушей: Не дай Бог сквозняком застудишь мозг изнутри.",
         16: "С чего это вы взяли, что я вас пугаю? Я, что, зеркало, что ли?",
         17: "Да… ронял тебя аист по дороге.",
         18: "Слышишь ты, сырьё для фотошопа.",
         19: "Единственное на что у тебя может хватить ума, так это сделать из сигареты пепел.",
         20: "Правильно делаешь, что хихикаешь: С твоими зубами не смеются!",
         21: "Если бы идиоты умели летать, то всей вашей семье пришлось бы жить на аэродроме.",
         22: "Вам надо было надеть красную кофточку: Под цвет ваших глаз.",
         23: "Попадешь под горячую руку — улетишь под горячую ногу.",
         24: "Ещё один гудок с твоей платформы, и твой зубной состав тронется.",
         25: "Как много интересного вы говорите! Как жаль, что это меня мало интересует.",
         26: "Если бы мне доставляло удовольствие общаться с …, у меня бы давно уже была собака.",
         27: "Попадешь под горячую руку — улетишь под горячую ногу",
         28: "Если бы дебилизм был смертельной болезнью, то тебя бы похоронили еще в детстве.",
         29: "С чего это вы взяли, что я вас пугаю? Я, что, зеркало, что ли?",
         30: "Дурдом на выезде, психи на природе!",
         31: "Зубы не волосы, вылетят — не поймаешь:",
         32: "Так это вы в кино играли Шрека?",
         33: "Да ты шутник? смотри шуткой не подавись!",
         34: "Тебе в кунсткамеру бы можно и при жизни!",
         35: "Глядя на вас начинаю понимать, что ничто человеческого Богу не чуждо.",
         36: "Тебе идет мейк-ап а-ля Валуев.",
         37: "Вы просто очень плохо думаете о людях, если считаете, что они равны вам.",
         38: "Ваш ум затмить способен свет торшера:",
         39: "Хочешь почувствовать себя звездой? сядь на ёлку и звезди сколько влезет.",
         40: "Как много интересного вы говорите! Как жаль, что это меня мало интересует.",
         41: "Ты так больше не шути, а то я со смеху…",
         42: "Бьюсь об заклад, тебя зачали на спор!",
         43: "Чтобы меня шокировать, вам придётся сказать что-нибудь умное.",
         44: "А ты я вижу, дура… — а ты я вижу плохо видишь!",
         45: "Я бы вас послал, да вижу — вы оттуда!",
         46: "А вы кофточку (рубашечку) под мышками специально намочили?"}

ECHO, TASK, RE_START = range(3)


def start_bot():
    global updater
    updater = Updater(
        'Your tolken', use_context=True)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('Say_yes', start)],
        states={
            ECHO: [
                CallbackQueryHandler(echo),
            ],
            TASK: [
                CallbackQueryHandler(send_to_hell, pattern='^' + 'send_to_hell' + '$'),
                CallbackQueryHandler(curse, pattern='^' + 'curse' + '$'),
                CallbackQueryHandler(echo, pattern='^' + 'echo off' + '$'),
            ],
            RE_START: [
                CallbackQueryHandler(re_start, pattern='^' + 'good' + '$'),
            ],
        },
        fallbacks=[CommandHandler('Say_yes', start)],
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()


def start(update, context):
    keyboard = [[InlineKeyboardButton("Начать", callback_data='echo on'),
                 InlineKeyboardButton("Что-то не хочется", callback_data='echo off')]]
    update.message.reply_text("Приветсую вас. Здесь вы можете послать на 123 и обругать кого захочете. Собщения исчезнут чрез 5 секунд.",
                              reply_markup=InlineKeyboardMarkup(keyboard))
    return ECHO


def echo(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == "echo on":
        keyboard = [[InlineKeyboardButton("Обозвать", callback_data='curse'),
                     InlineKeyboardButton("Послать", callback_data='send_to_hell')]]
        update.callback_query.message.edit_text(
            "Обзывалка начала работу",
            reply_markup=InlineKeyboardMarkup(keyboard))
        return TASK
    elif query.data == "echo off":
        update.callback_query.message.edit_text("Захотите вернуться наберите команду /Say_yes")


def curse(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(f'{dic[random.randint(1, 60)]}')
    time.sleep(5)
    keyboard = [[InlineKeyboardButton("Круто", callback_data='good')]]
    update.callback_query.message.edit_text(
        "Понравилось?",
        reply_markup=InlineKeyboardMarkup(keyboard))

    return RE_START


def send_to_hell(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(f'{dic_2[random.randint(1, 46)]}')
    time.sleep(5)
    keyboard = [[InlineKeyboardButton("Круто", callback_data='good')]]
    update.callback_query.message.edit_text(
        "Понравилось?",
        reply_markup=InlineKeyboardMarkup(keyboard))
    return RE_START

def re_start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Обозвать", callback_data='curse'),
                 InlineKeyboardButton("Послать", callback_data='send_to_hell'),
                 InlineKeyboardButton("Закончить работу", callback_data='echo off')]]
    update.callback_query.message.edit_text(
        "Что делать дальше?",
        reply_markup=InlineKeyboardMarkup(keyboard))

    return TASK


def gui():
    layout = [[sg.Text('Bot Status: '), sg.Text('Stopped', key='status')],
              [sg.Button('Start'), sg.Button('Stop', disabled=True), sg.Exit()]]

    window = sg.Window('Finxter Bot Tutorial', layout)
    while True:
        event, _ = window.read()

        if event == 'Start':
            if updater is None:
                start_bot()
            else:
                updater.start_polling()
            window.FindElement('Start').Update(disabled=True)
            window.FindElement('Stop').Update(disabled=False)
            window.FindElement('status').Update('Running')
        if event == 'Stop':
            updater.stop()
            window.FindElement('Start').Update(disabled=False)
            window.FindElement('Stop').Update(disabled=True)
            window.FindElement('status').Update('Stopped')
        if event in (None, 'Exit'):
            break
    if updater is not None and updater.running:
        updater.stop()
    window.close()


gui()
