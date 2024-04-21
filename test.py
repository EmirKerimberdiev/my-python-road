import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open(r'C:\Users\User\Desktop\Python\Photos\Video.mp4', 'rb')
    bot.send_video(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("👨‍🏫 Направление")
    item2 = types.KeyboardButton("📷 Мугалимдердин сүрөтү")
    item3 = types.KeyboardButton("🗺 Биздин жайгашкан жерибиз")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Кош келиңиз, {0.first_name}!\nМен - <b>{1.first_name}</b>, бот жаратылган протатип болуу үчүн.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalalas(message):
    if message.chat.type == 'private':
        if message.text == '👨‍🏫 Направление':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("💻 IT", callback_data='it')
            item2 = types.InlineKeyboardButton("🔧 Сваршик", callback_data='swar')
            item3 = types.InlineKeyboardButton("🔪 Ашпозчу", callback_data='kux')
            item4 = types.InlineKeyboardButton("🐾 Ветеринар", callback_data='veterenar')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Багыты тандаңыз', reply_markup=markup)




        elif message.text == '📷 Мугалимдердин сүрөтү':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item12 = types.InlineKeyboardButton("💻 IT", callback_data='itp')
            item13 = types.InlineKeyboardButton("Сваршик 🔧", callback_data='swarp')

            markup.add(item12, item13)

            bot.send_message(message.chat.id, 'Сүрөт тандаңыз', reply_markup=markup)

        elif message.text == '🗺 Биздин жайгашкан жерибиз':
            file = open(r'C:\Users\User\Desktop\PycharmProjects\Python\Photos\ce737577-02d9-47a2-9644-86a688cd4168.jpg', 'rb')
            bot.send_photo(message.chat.id, file)
            bot.send_message(message.chat.id,'сл.Кызыл-суу Главная улица рядом с строй магазином Ак-Тилек \nhttps://www.google.com/maps/place/%D0%9B%D0%B8%D1%86%D0%B5%D0%B9-%E2%84%9655+%D0%9A%D1%8B%D0%B7%D1%8B%D0%BB-%D1%81%D1%83%D1%83+%D1%84%D0%B8%D0%BB%D0%B8%D0%B0%D0%BB%D1%8B/@42.3493065,78.0170934,17z/data=!4m12!1m5!8m4!1e2!2s108279573330634471486!3m1!1e1!3m5!1s0x38867700658e261f:0x383561d16fec9479!8m2!3d42.3489299!4d78.0175737!16s%2Fg%2F11vrzc35x7?entry=ttu')

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'it':
                bot.send_message(call.message.chat.id,
                                 '🚀💻 Көңүл бургула, IT дүйнөсүнө күйгөн студенттер! 💻🚀\n\nСиз маалыматтык технологиялардын кызыктуу дүйнөсүнө сүңгүүнү каалайсызбы? Биздин жаңы IT курсубузга кошулуңуз! Бул динамикалык талаанын негизги аспектилерин тажрыйбалуу адистерден үйрөнүңүз.\n\n🌐 Сизди эмне күтөт:\n\n· Программалоону жана иштеп чыгууну өздөштүрүү\n\n· Заманбап технологияларды жана куралдарды изилдөө\n\n· Чыныгы долбоорлордун үстүндө иштөө\n\n· Инновациялык чөйрөдө жөндөмүңүздү өнүктүрүү мүмкүнчүлүгү\n\nМаалыматтык технологиялар тармагындагы кесипти өздөштүрүү жана чексиз мүмкүнчүлүктөр дүйнөсүн ачуу мүмкүнчүлүгүн колдон чыгарбаңыз! Азыр катталып, IT адиси болуңуз. 💡🌐\n\nТолук маалымат жана каттоо үчүн биздин окуу борборубузга кайрылыңыз. Сиздин технология дүйнөсүндөгү келечегиңиз ушул жерден башталат! 🚀🔗')
            elif call.data == 'swar':
                bot.send_message(call.message.chat.id,
                                 '🔧🔥 Көңүл бургула, мектеп окуучулары! 🔥🔧\n\nШиретүүнүн кызыктуу дүйнөсүнө сүңгүп киргиңиз келеби? Биздин жаңы ширетүү курсуна кошулуңуз! Бул кызыктуу жана изделген кол өнөрчүлүктүн негиздерин тажрыйбалуу адистерден үйрөнүңүз.\n\n🌐Сизди эмне күтөт:\n\n· Ширетүү техникасынын теориясы жана практикасы\n\n· Ар кандай материалдар менен иштөө\n\n· Заманбап жабдуулар менен таанышуу\n\n· Достук чөйрөдө өз жөндөмүңүздү өнүктүрүү мүмкүнчүлүгү\n\nШиретүүчү кесибин үйрөнүү мүмкүнчүлүгүн колдон чыгарбаңыз жана эмгек рыногунда көптөгөн мүмкүнчүлүктөрдү ачыңыз! Азыр катталып, өз ишиңиздин чебери болуңуз. 🛠️💼\n\nТолук маалымат жана жазуу үчүн биздин окуу борборуна кайрылыңыз. Келечектеги ийгилигиңиз ушул жерден башталат! 🚀🔗')
            elif call.data == 'kux':
                bot.send_message(call.message.chat.id,
                                 '🔪🍳 Көңүл бургула, ашпозчу амбициясы бар студенттер! 🍳🔪\n\nБиздин ашпозчулук курсуна кошулуңуз жана гастрономия дүйнөсүн ачыңыз! Биздин тажрыйбалуу ашпозчуларыбыздан даамдуу тамактарды жасоо өнөрүн үйрөнүңүз.\n\n🌐 Сизди эмне күтөт:\n\n· Ар кандай кулинардык ыкмаларды үйрөнүү\n\n· Тамак жасоого чыгармачылык мамиле кылуу\n\n· Жогорку сапаттагы ингредиенттерди киргизүү\n\n· Уникалдуу рецепттер менен практикалык сабактар\n\nКулинардык искусствонун чебери болуу жана чыныгы кулинардык шедеврлерди түзүү мүмкүнчүлүгүн колдон чыгарбаңыз! Азыр катталып, сыйкырдуу даам дүйнөсүнө чөмүлүңүз. 🌟🍴\n\nКөбүрөөк маалымат алуу жана каттоо үчүн биздин кулинардык борборго кайрылыңыз. Кулинардык чеберчиликке болгон саякатыңыз ушул жерден башталат! 🍽️🔗')
            elif call.data == 'veterenar':
                bot.send_message(call.message.chat.id,
                                 '🐾👩‍⚕️ Көңүл бургула, жаныбарларды сүйгөн студенттер! 👨‍⚕️🐾\n\nБиздин Ветеринария курсуна кошулуңуз жана төрт буттуу досторуңуздун ден соолугунун коргоочусу болуңуз! Тажрыйбалуу ветврачтардан кесиптин бардык татаал жана сырларын уйрвн.\n\n🌐 Сизди эмне күтөт:\n\n· Ветеринария илиминин негиздерин үйрөнүү\n\n· Жаныбарлар менен практикалык көнүгүүлөр\n\n· Ар кандай жаныбарлардын түрлөрүн аныктоо жана дарылоо\n\n· Заманбап медициналык жабдуулар менен иштөө\n\nҮй жаныбарларынын өмүрүн сактап калган жана жакшырткан маанилүү кесиптин бир бөлүгү болуу мүмкүнчүлүгүн колдон чыгарбаңыз! Азыр катталып, ветеринардык жардам дүйнөсүнө саякатыңызды баштаңыз. 🏥🐶🐱\n\nТолук маалымат жана жолугушууларды алуу үчүн биздин ветеринардык борборго кайрылыңыз. Сиздин жаныбарларга болгон сүйүүңүз ушул жерде жана азыр кесипке айланышы мүмкүн! 🐾🔗')

            # remove inline buttons

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

            if call.data == 'itp':
                file = open(r'C:\Users\User\Desktop\Python\Photos\GrinCardEmir.jpg', 'rb')
                bot.send_photo(call.message.chat.id, file, 'Учитель по IT Эмир')

                file = open(r'C:\Users\User\Desktop\Python\Photos\IMG_20230928_203601.jpg', 'rb')
                bot.send_photo(call.message.chat.id, file, 'Учитель по IT Салтанат')

            elif call.data == 'swarp':
                file = open(r'C:\Users\User\Desktop\Python\Photos\GrinCardEmir.jpg', 'rb')
                bot.send_photo(call.message.chat.id, file, 'Учитель по Сварке')

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
