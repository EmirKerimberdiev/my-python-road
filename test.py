import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('C:\Telegram\Sticers\sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("👨‍🏫 Направление")
    item2 = types.KeyboardButton("📷 Фото учителей")
    item3 = types.KeyboardButton("🗺 Наше место положение")


    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть протатипом.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '👨‍🏫 Направление':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("💻 IT",callback_data='it' )
            item2 = types.InlineKeyboardButton("🔧 Сваршик", callback_data='swar')
            item3 = types.InlineKeyboardButton("🔪 Ашпозчу", callback_data='kux')
            item4 = types.InlineKeyboardButton("🐾 Ветеринар", callback_data='veterenar')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Выбери направление', reply_markup=markup)




        elif message.text == '📷 Фото учителей':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item12 = types.InlineKeyboardButton("💻 IT", callback_data='itp')
            item13 = types.InlineKeyboardButton("Сваршик 🔧", callback_data='swarp')

            markup.add(item12, item13)

            bot.send_message(message.chat.id, 'Выбери фото', reply_markup=markup)

        elif message.text == '🗺 Наше место положение':
            file = open(r'/c/Users/User/Desktop/Python/Photos/ce737577-02d9-47a2-9644-86a688cd4168.jpg', 'rb')

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'it':
                bot.send_message(call.message.chat.id,'🚀💻 Көңүл бургула, IT дүйнөсүнө күйгөн студенттер! 💻🚀\n\nСиз маалыматтык технологиялардын кызыктуу дүйнөсүнө сүңгүүнү каалайсызбы? Биздин жаңы IT курсубузга кошулуңуз! Бул динамикалык талаанын негизги аспектилерин тажрыйбалуу адистерден үйрөнүңүз.\n\n🌐 Сизди эмне күтөт:\n\n· Программалоону жана иштеп чыгууну өздөштүрүү\n\n· Заманбап технологияларды жана куралдарды изилдөө\n\n· Чыныгы долбоорлордун үстүндө иштөө\n\n· Инновациялык чөйрөдө жөндөмүңүздү өнүктүрүү мүмкүнчүлүгү\n\nМаалыматтык технологиялар тармагындагы кесипти өздөштүрүү жана чексиз мүмкүнчүлүктөр дүйнөсүн ачуу мүмкүнчүлүгүн колдон чыгарбаңыз! Азыр катталып, IT адиси болуңуз. 💡🌐\n\nТолук маалымат жана каттоо үчүн биздин окуу борборубузга кайрылыңыз. Сиздин технология дүйнөсүндөгү келечегиңиз ушул жерден башталат! 🚀🔗')
            elif call.data == 'swar':
                bot.send_message(call.message.chat.id, '🔧🔥 Көңүл бургула, мектеп окуучулары! 🔥🔧\n\nШиретүүнүн кызыктуу дүйнөсүнө сүңгүп киргиңиз келеби? Биздин жаңы ширетүү курсуна кошулуңуз! Бул кызыктуу жана изделген кол өнөрчүлүктүн негиздерин тажрыйбалуу адистерден үйрөнүңүз.\n\n🌐Сизди эмне күтөт:\n\n· Ширетүү техникасынын теориясы жана практикасы\n\n· Ар кандай материалдар менен иштөө\n\n· Заманбап жабдуулар менен таанышуу\n\n· Достук чөйрөдө өз жөндөмүңүздү өнүктүрүү мүмкүнчүлүгү\n\nШиретүүчү кесибин үйрөнүү мүмкүнчүлүгүн колдон чыгарбаңыз жана эмгек рыногунда көптөгөн мүмкүнчүлүктөрдү ачыңыз! Азыр катталып, өз ишиңиздин чебери болуңуз. 🛠️💼\n\nТолук маалымат жана жазуу үчүн биздин окуу борборуна кайрылыңыз. Келечектеги ийгилигиңиз ушул жерден башталат! 🚀🔗')
            elif call.data == 'kux':
                bot.send_message(call.message.chat.id,'🔪🍳 Көңүл бургула, ашпозчу амбициясы бар студенттер! 🍳🔪\n\nБиздин ашпозчулук курсуна кошулуңуз жана гастрономия дүйнөсүн ачыңыз! Биздин тажрыйбалуу ашпозчуларыбыздан даамдуу тамактарды жасоо өнөрүн үйрөнүңүз.\n\n🌐 Сизди эмне күтөт:\n\n· Ар кандай кулинардык ыкмаларды үйрөнүү\n\n· Тамак жасоого чыгармачылык мамиле кылуу\n\n· Жогорку сапаттагы ингредиенттерди киргизүү\n\n· Уникалдуу рецепттер менен практикалык сабактар\n\nКулинардык искусствонун чебери болуу жана чыныгы кулинардык шедеврлерди түзүү мүмкүнчүлүгүн колдон чыгарбаңыз! Азыр катталып, сыйкырдуу даам дүйнөсүнө чөмүлүңүз. 🌟🍴\n\nКөбүрөөк маалымат алуу жана каттоо үчүн биздин кулинардык борборго кайрылыңыз. Кулинардык чеберчиликке болгон саякатыңыз ушул жерден башталат! 🍽️🔗')
            elif call.data == 'veterenar':
                bot.send_message(call.message.chat.id,'🐾👩‍⚕️ Көңүл бургула, жаныбарларды сүйгөн студенттер! 👨‍⚕️🐾\n\nБиздин Ветеринария курсуна кошулуңуз жана төрт буттуу досторуңуздун ден соолугунун коргоочусу болуңуз! Тажрыйбалуу ветврачтардан кесиптин бардык татаал жана сырларын уйрвн.\n\n🌐 Сизди эмне күтөт:\n\n· Ветеринария илиминин негиздерин үйрөнүү\n\n· Жаныбарлар менен практикалык көнүгүүлөр\n\n· Ар кандай жаныбарлардын түрлөрүн аныктоо жана дарылоо\n\n· Заманбап медициналык жабдуулар менен иштөө\n\nҮй жаныбарларынын өмүрүн сактап калган жана жакшырткан маанилүү кесиптин бир бөлүгү болуу мүмкүнчүлүгүн колдон чыгарбаңыз! Азыр катталып, ветеринардык жардам дүйнөсүнө саякатыңызды баштаңыз. 🏥🐶🐱\n\nТолук маалымат жана жолугушууларды алуу үчүн биздин ветеринардык борборго кайрылыңыз. Сиздин жаныбарларга болгон сүйүүңүз ушул жерде жана азыр кесипке айланышы мүмкүн! 🐾🔗')

            # remove inline buttons

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

            if call.data == 'itp':
                file = open(r'C:\Telegram\Photos\GrinCardEmir.jpg', 'rb')
                bot.send_photo(call.message.chat.id, file, 'Учитель по IT Эмир')

                file = open(r'C:\Telegram\Photos\IMG_20230928_203601.jpg', 'rb')
                bot.send_photo(call.message.chat.id, file, 'Учитель по IT Салтанат')

            elif call.data == 'swarp':
                file = open(r'C:\Telegram\Photos\GrinCardEmir.jpg', 'rb')
                bot.send_photo(call.message.chat.id, file, 'Учитель по Сварке')

    except Exception as e:
        print(repr(e))




# RUN
bot.polling(none_stop=True)