from aiogram import Bot, Dispatcher, filters, F, types
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


bot = Bot(token="7295691851:AAECaUMuUsqVqU26nTMCCD-wjYRrYaxAJUU")
dp = Dispatcher(bot=bot)


class Reg(StatesGroup):
    name = State()
    number = State()


class Card(StatesGroup):
    card_number = State()
    update_data = State()


class Karta(StatesGroup):
    card_number = State()
    update_data = State()


class Reg_uz(StatesGroup):
    ism = State()
    raqam = State()


menu_ru2 = [
    [InlineKeyboardButton(text="Еда", callback_data="еда"), InlineKeyboardButton(text="Напитки", callback_data="напитки"), InlineKeyboardButton(text="Назад", callback_data="назад")]
]
ru2_menu = InlineKeyboardMarkup(inline_keyboard=menu_ru2)

menu_uz2 = [
    [InlineKeyboardButton(text="Taomlar", callback_data="taomlar"), InlineKeyboardButton(text="Ichimliklar", callback_data="ichimliklar"), InlineKeyboardButton(text="Orqaga", callback_data="orqaga")]
]
uz2_menu = InlineKeyboardMarkup(inline_keyboard=menu_uz2)


menu_ru = [
    [KeyboardButton(text="Меню"), KeyboardButton(text="Корзинка"), KeyboardButton(text="О нас")],
    [KeyboardButton(text="О вас"), KeyboardButton(text="Поддержка"), KeyboardButton(text="Поменять язык")]
]

ru_menu = ReplyKeyboardMarkup(keyboard=menu_ru, resize_keyboard=True)

menu_uz = [
    [KeyboardButton(text="Menu"), KeyboardButton(text="Savat"), KeyboardButton(text="Biz haqimizda")],
    [KeyboardButton(text="Siz haqingizda"), KeyboardButton(text="Nima yordam kerak"), KeyboardButton(text="Tilni ozgartirish")]
]

uz_menu = ReplyKeyboardMarkup(keyboard=menu_uz, resize_keyboard=True)


language = [
    [KeyboardButton(text="Uz")],
    [KeyboardButton(text="Ru")]
]
main_button = ReplyKeyboardMarkup(keyboard=language, resize_keyboard=True)


eda_menu = [
    [InlineKeyboardButton(text="Лаваш", callback_data="лаваш"), InlineKeyboardButton(text="Фри", callback_data="фри"), InlineKeyboardButton(text="Шаурма", callback_data="шаурма")],
    [InlineKeyboardButton(text="Донар", callback_data="донар"), InlineKeyboardButton(text="Комбо", callback_data="комбо")],
    [InlineKeyboardButton(text="Назад", callback_data="nazad_yeda")],
]
eda_rus = InlineKeyboardMarkup(inline_keyboard=eda_menu,)


taom_menu = [
    [InlineKeyboardButton(text="Lavash", callback_data="lavash"), InlineKeyboardButton(text="Fri", callback_data="fri"), InlineKeyboardButton(text="Shaurma", callback_data="shaurma")],
     [InlineKeyboardButton(text="Donar", callback_data="donar"), InlineKeyboardButton(text="Combo", callback_data="combo")],
    [InlineKeyboardButton(text="Orqaga", callback_data="back_taom")]
]
taom_uz = InlineKeyboardMarkup(inline_keyboard=taom_menu)

uz_lavash_menu = [
    [KeyboardButton(text="Lavash mol-goshti"), KeyboardButton(text="Lavash tovuq-goshti")],
    [KeyboardButton(text="Orqaga")]
]
lavash_menu_uzb = ReplyKeyboardMarkup(keyboard=uz_lavash_menu, resize_keyboard=True)


uz_fri_menu = [
    [KeyboardButton(text="Fri mini (70gr)")],
    [KeyboardButton(text="Fri (100gr)")],
    [KeyboardButton(text="Orqaga")]
]
fri_menu_uzb = ReplyKeyboardMarkup(keyboard=uz_fri_menu, resize_keyboard=True)

uz_shaurma_menu = [
    [KeyboardButton(text="Shaurma mol-goshti"), KeyboardButton(text="Shaurma tovuq-goshti")],
    [KeyboardButton(text="Orqaga")]


]
shaurma_menu_uzb = ReplyKeyboardMarkup(keyboard=uz_shaurma_menu, resize_keyboard=True)


uz_donar_menu = [
    [KeyboardButton(text="Donar mol-goshti"), KeyboardButton(text="Donar tovuq-goshti")],
    [KeyboardButton(text="Orqaga")]

]
donar_menu_uzb = ReplyKeyboardMarkup(keyboard=uz_donar_menu, resize_keyboard=True)


uz_combo_menu = [
    [KeyboardButton(text="Combo mini")],
    [KeyboardButton(text="Combo")],
    [KeyboardButton(text="Combo 4 odam uchun")],
    [KeyboardButton(text="Orqaga")]
]
combo_menu_uzb = ReplyKeyboardMarkup(keyboard=uz_combo_menu, resize_keyboard=True)

ru_lavash_menu = [
    [ KeyboardButton(text="Лаваш говядина"), KeyboardButton(text="Лаваш куриный")],
    [KeyboardButton(text="назад")]
]
lavash_menu_ru = ReplyKeyboardMarkup(keyboard=ru_lavash_menu, resize_keyboard=True)


ru_fri_menu = [
    [KeyboardButton(text="Фри мини (70гр)")],
    [KeyboardButton(text="Фри (100гр)")],
    [KeyboardButton(text="назад")]
]
fri_menu_ru = ReplyKeyboardMarkup(keyboard=ru_fri_menu, resize_keyboard=True)


ru_shaurma_menu = [
    [KeyboardButton(text="Шаурма говядина "), KeyboardButton(text="Шаурма куриный ")],
    [KeyboardButton(text="назад")]
]
shaurma_menu_ru = ReplyKeyboardMarkup(keyboard=ru_shaurma_menu, resize_keyboard=True)


ru_donar_menu = [
    [KeyboardButton(text="Донар говядина"), KeyboardButton(text="Донар куриный")],
    [KeyboardButton(text="назад")]
]
donar_menu_ru = ReplyKeyboardMarkup(keyboard=ru_donar_menu, resize_keyboard=True)


ru_combo_menu = [
    [KeyboardButton(text="Комбо мини")],
    [KeyboardButton(text="Комбо")],
    [KeyboardButton(text="Комбо для 4 людей")],
    [KeyboardButton(text="назад")]
]
combo_menu_ru = ReplyKeyboardMarkup(keyboard=ru_combo_menu, resize_keyboard=True)


ichimli_menu = [
    [InlineKeyboardButton(text="Pepsi", callback_data="pepsi"), InlineKeyboardButton(text="Coca-cola", callback_data="cocacola")],
    [InlineKeyboardButton(text="Moxito", callback_data="moxito")],[InlineKeyboardButton(text="Sok", callback_data="sok"),]


]
ichimli_menu_uzb = InlineKeyboardMarkup(inline_keyboard=ichimli_menu)


pepsi_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Pepsi 0.5L"), KeyboardButton(text="Pepsi 1.5L")]
], resize_keyboard=True)


cola_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="CocaCola 0.5L"), KeyboardButton(text="CocaCola 1.5L")]
], resize_keyboard=True)


moxito_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Moxito malina"), KeyboardButton(text="Moxito sitrus")]
], resize_keyboard=True)


sok_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Sok Olmali"), KeyboardButton(text="Sok Multifrukt")],
    [KeyboardButton(text="Sok orikli")]
], resize_keyboard=True)


pepsi_menu_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пепси 0.5Л"), KeyboardButton(text="Пепси 1.5Л")]
], resize_keyboard=True)


cola_menu_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="КокаКола 0.5Л"), KeyboardButton(text="КокаКола 1.5Л")]
], resize_keyboard=True)


moxito_menu_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Мохито малина"), KeyboardButton(text="Мохито цитрус")]
], resize_keyboard=True)


sok_menu_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Сок яблочный"), KeyboardButton(text="Сок Мультифрукт")],
    [KeyboardButton(text="Сок абрикосовый")]
], resize_keyboard=True)


napitki_menu = [
    [InlineKeyboardButton(text="Пепси", callback_data="пепси"), InlineKeyboardButton(text="Кока-кола", callback_data="кокакола"), InlineKeyboardButton(text="Мохито", callback_data="мохито")],
    [InlineKeyboardButton(text="Сок", callback_data="сок")]

]
napitki_menu_ru = InlineKeyboardMarkup(inline_keyboard=napitki_menu)


sotib_olsih  = [
    [InlineKeyboardButton(text="Qo'shish", callback_data="plus")],
    [InlineKeyboardButton(text="Orqaga", callback_data="minus")]
]

buy_button = InlineKeyboardMarkup(inline_keyboard=sotib_olsih)


pokupka = [
    [InlineKeyboardButton(text="Добавить", callback_data="плюс")],
    [InlineKeyboardButton(text="Назад", callback_data="минус")]
]

buy_button_ru = InlineKeyboardMarkup(inline_keyboard=pokupka)


order = []
order_ru = []

lst = []
list = []

savat = [
    [InlineKeyboardButton(text="To'lash", callback_data="tolash"), InlineKeyboardButton(text="Savatni tozalash", callback_data="tozalash")]
]
savat_uz = InlineKeyboardMarkup(inline_keyboard=savat)

savat = [
    [InlineKeyboardButton(text="Платить", callback_data="платить"), InlineKeyboardButton(text="Очистить корзинку", callback_data="очистить")]
]
savat_rus = InlineKeyboardMarkup(inline_keyboard=savat)


card_uz = [
    [KeyboardButton(text="Uzcard kartasi"), KeyboardButton(text="Humo kartasi")]
]

uz_cards = ReplyKeyboardMarkup(keyboard=card_uz, resize_keyboard=True)

card_rus = [
    [KeyboardButton(text="Uzcard карта"), KeyboardButton(text="Humo карта")]
]

rus_cards = ReplyKeyboardMarkup(keyboard=card_rus, resize_keyboard=True)

@dp.message(F.text == "Uzcard kartasi")
async def pey_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Karta raqamini kiriting")

@dp.message(F.text == "Uzcard карта")
async def pey_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Ведите номер карты")


@dp.message(F.text == "Humo kartasi")
async def pey_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Karta raqamini kiriting")

@dp.message(F.text == "Humo карта")
async def pey_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Ведите номер карты")


@dp.message(Card.card_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer("Tolov o'tdi!", reply_markup=main_button)
    else:
        await message.answer("Boshidan urinib ko'ring !\nKartangizni raqami 16 sondan iborat bolishi kerak")
    await state.clear()


@dp.callback_query(F.data == 'tolash')
async def tolash(callback: CallbackQuery):
    await callback.message.answer("Karta tanlang: ",reply_markup=uz_cards)

@dp.callback_query(F.data == 'платить')
async def tolash(callback: CallbackQuery):
    await callback.message.answer("Выберите карту: ",reply_markup=rus_cards)


@dp.callback_query(F.data == "plus")
async def cancel(callback: CallbackQuery):
    order.append(lst[-1])
    await callback.answer(text=f"{callback.from_user.full_name} Sizni buyurtmangiz qabul qilindi.")


@dp.callback_query(F.data == "плюс")
async def cancel(callback: CallbackQuery):
    order_ru.append(list[-1])
    await callback.answer(text=f"{callback.from_user.full_name} Ваш заказ успешно принят.")



@dp.callback_query(F.data == "tozalash")
async def cancel(callback: CallbackQuery):
    order.clear()
    order_ru.clear()
    await callback.answer(text="Sizning buyurtmangiz muvaffaqiyatli ochirildi !")

@dp.callback_query(F.data == "очистить")
async def cancel(callback: CallbackQuery):
    order.clear()
    order_ru.clear()
    await callback.answer(text="Ваш заказ был удален !")


contact_button_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Kontakt jo'natish", request_contact=True)]
], resize_keyboard=True)
contact_button_ru = ReplyKeyboardMarkup( keyboard=[
    [KeyboardButton(text="Поделиться контактом", request_contact=True)]
], resize_keyboard=True)


@dp.message(filters.Command("start"))
async def start(message: types.Message):
    await message.answer('Выберите язык - Tilni tanlang', reply_markup=main_button)


@dp.message(F.text=="Ru")
async def reg1(message: types.Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите ваше имя')


@dp.message(Reg.name)
async def reg2(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите номер телефона', reply_markup=contact_button_ru)


@dp.message(Reg.number)
async def two_three(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Вы прошли регистрацию\nИмя:  {data["name"]}\nНомер:  {data["number"]}", reply_markup=ru_menu)
    await state.clear()


@dp.message(F.text=="Uz")
async def reg_uzz(message: types.Message, state: FSMContext):
    await state.set_state(Reg_uz.ism)
    await message.answer('Ismizni kiriting: ')


@dp.message(Reg_uz.ism)
async def reg_uzb(message: types.Message, state: FSMContext):
    await state.update_data(ism=message.text)
    await state.set_state(Reg_uz.raqam)
    await message.answer('Telefon raqamingizni kiriting: ', reply_markup=contact_button_uz)


@dp.message(Reg_uz.raqam)
async def two_three_uzb(message: types.Message, state: FSMContext):
    await state.update_data(raqam=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Siz muvaffaqaiyatli royxatdan otdingiz\nIsm:  {data["ism"]}\nTel raqam:  {data["raqam"]}", reply_markup=uz_menu)
    await state.clear()



@dp.message(F.text=="Tilni ozgartirish")
async def start(message: types.Message):
    await message.answer(' Tilni tanlang', reply_markup=main_button)


@dp.message(F.text==("Поменять язык"))
async def start(message: types.Message):
    await message.answer('Выберите язык', reply_markup=main_button)



@dp.message(F.text==("Меню"))
async def start(message: types.Message):
    await message.answer('Выберите категорию: ', reply_markup=ru2_menu)



@dp.message(F.text==("Menu"))
async def start(message: types.Message):
    await message.answer('Kategoriya tanlang: ', reply_markup=uz2_menu)


@dp.callback_query(F.data == 'minus')
async def orqaga(callback: CallbackQuery):
    await callback.message.answer("Siz menyudasiz", reply_markup=uz_menu)


@dp.callback_query(F.data == 'минус')
async def orqaga(callback: CallbackQuery):
    await callback.message.answer("Вы вернулись в меню", reply_markup=ru_menu)



@dp.callback_query(F.data == 'orqaga')
async def orqaga(callback: CallbackQuery):
    await callback.message.answer("Siz orqaga qaytingiz", reply_markup=uz_menu)


@dp.callback_query(F.data == 'назад')
async def orqaga(callback: CallbackQuery):
    await callback.message.answer("Вы вернулись обратно", reply_markup=ru_menu)


@dp.callback_query(F.data == 'nazad_yeda')
async def orqaga(callback: CallbackQuery):
    await callback.message.answer("Вы вернулись обратно", reply_markup=ru2_menu)

@dp.callback_query(F.data == 'back_taom')
async def orqaga(callback: CallbackQuery):
    await callback.message.answer("Menyuga qaytingiz", reply_markup=uz2_menu)


@dp.callback_query(F.data == 'еда')
async def eda(callback: CallbackQuery):
    await callback.message.answer("Выберите блюдо: ", reply_markup=eda_rus)


@dp.callback_query(F.data == 'taomlar')
async def taomlar(callback: CallbackQuery):
    await callback.message.answer("Taom tanlang: ", reply_markup=taom_uz)




@dp.callback_query(F.data == 'lavash')
async def taomlar(callback: CallbackQuery):
    await callback.message.answer("Lavash tanlang: ", reply_markup=lavash_menu_uzb)



@dp.callback_query(F.data == 'fri')
async def taomlar(callback: CallbackQuery):
    await callback.message.answer("Fri tanlang: ", reply_markup=fri_menu_uzb)


@dp.callback_query(F.data == 'shaurma')
async def taomlar(callback: CallbackQuery):
    await callback.message.answer("Lavash tanlang: ", reply_markup=shaurma_menu_uzb)



@dp.callback_query(F.data == 'donar')
async def taomlar(callback: CallbackQuery):
    await callback.message.answer("Donar tanlang : ", reply_markup=donar_menu_uzb)


@dp.callback_query(F.data == 'combo')
async def taomlar(callback: CallbackQuery):
    await callback.message.answer("Lavash tanlang: ", reply_markup=combo_menu_uzb)


@dp.callback_query(F.data == 'ichimliklar')
async def ichimlilar(callback: CallbackQuery):
    await callback.message.answer("Ichimlik tanlang: ", reply_markup=ichimli_menu_uzb)


@dp.callback_query(F.data == 'лаваш')
async def taomlar(callback: CallbackQuery):
    await callback.message.answer("Выберите лаваш: ", reply_markup=lavash_menu_ru)


@dp.callback_query(F.data == 'фри')
async def taomlar(callback: CallbackQuery):
    await callback.message.answer("Выберите фри: ", reply_markup=fri_menu_ru)


@dp.callback_query(F.data == 'шаурма')
async def taomlar(callback: CallbackQuery):
    await callback.message.answer("Выберите шаурму: ", reply_markup=shaurma_menu_ru)



@dp.callback_query(F.data == 'донар')
async def taomlar(callback: CallbackQuery):
    await callback.message.answer("Выберите донар : ", reply_markup=donar_menu_ru)


@dp.callback_query(F.data == 'комбо')
async def taomlar(callback: CallbackQuery):
    await callback.message.answer("Выберите комбо: ", reply_markup=combo_menu_ru)


@dp.callback_query(F.data == 'напитки')
async def ichimlilar(callback: CallbackQuery):
    await callback.message.answer("Выберите напитки: ", reply_markup=napitki_menu_ru)



@dp.message(F.text=="Lavash mol-goshti")
async def lavash(message: types.Message):
    lavash_photo_standart = "https://yukber.uz/image/cache/catalog/lavash-700x700.jpg"
    order.append("Lavash mol-goshti")
    order_ru.append("Лаваш говядина")
    await message.answer_photo(photo=lavash_photo_standart, caption=" Lavash mol-goshti standart\nNarxi: 35 000 so'm", reply_markup=buy_button)



@dp.message(F.text=="Lavash tovuq-goshti")
async def lavash(message: types.Message):
    lavash_photo_tovuq_standart = "https://ml1nrnpa6jqh.i.optimole.com/w:500/h:350/q:mauto/f:best/https://chicken-elika.kz/wp-content/uploads/2019/05/MG9O5DSAgPmCfS6qcvUQ.png"
    lst.append("Lavash tovuq-goshti")
    list.append("Лаваш куриный")
    await message.answer_photo(photo=lavash_photo_tovuq_standart, caption=" Lavash tovuq-goshti standart\nNarxi: 33 000 so'm", reply_markup=buy_button)


@dp.message(F.text=="Fri mini (70gr)")
async def lavash(message: types.Message):
    fri_photo_70 = "https://hips.hearstapps.com/hmg-prod/images/best-homemade-chips-645e4d046f5df.jpg"
    lst.append("Fri mini (70gr)")
    list.append("Фри мини (70гр)")
    await message.answer_photo(photo=fri_photo_70, caption="Fri mini\nNarxi: 12 000 so'm", reply_markup=buy_button)


@dp.message(F.text=="Fri (100gr)")
async def lavash(message: types.Message):
    fri_photo_standart = "https://www.seriouseats.com/thmb/Il7mv9ZSDh7n0cZz3t3V-28ImkQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__2018__04__20180309-french-fries-vicky-wasik-15-5a9844742c2446c7a7be9fbd41b6e27d.jpg"
    lst.append("Fri (100gr)")
    list.append("Фри (100гр)")
    await message.answer_photo(photo=fri_photo_standart, caption=" Fri standart\nNarxi: 29 000 so'm", reply_markup=buy_button)


@dp.message(F.text=="Shaurma mol-goshti")
async def lavash(message: types.Message):
    shaurma_standart = "https://t4.ftcdn.net/jpg/05/73/18/41/360_F_573184112_TgBWWxZAGNCkITMbFg7SzaFlDHh5I6NZ.jpg"
    lst.append("Shaurma mol-goshti")
    list.append("Шаурма говядина")
    await message.answer_photo(photo=shaurma_standart, caption="Shaurma mol-goshti standart\nNarxi: 36 000 so'm", reply_markup=buy_button)


@dp.message(F.text=="Shaurma tovuq-goshti")
async def lavash(message: types.Message):
    shaurma_tovuq_standart = "https://imageproxy.wolt.com/venue/61caadc0514c59068055ba6a/9935393e-a778-11ed-9a7f-464364fae894_1131dbe4_67a7_11ec_9bab_b6243be44d8e_ff428f46_906a_11eb_a3e5_42bebe8f9313_gldani_express.jpeg.webp"
    lst.append("Shaurma tovuq-goshti")
    list.append("Шаурма куриный")
    await message.answer_photo(photo=shaurma_tovuq_standart, caption="Shaurma tovuq-goshti standart\nNarxi: 32 000 so'm", reply_markup=buy_button)


@dp.message(F.text=="Donar mol-goshti")
async def lavash(message: types.Message):
    donar_photo_m = "https://i0.wp.com/thecitylife.org/wp-content/uploads/2023/03/Chicken.jpg?fit=1536%2C1039&ssl=1"
    lst.append("Donar mol-goshti")
    list.append("Донар говядина")
    await message.answer_photo(photo=donar_photo_m, caption="Donar mol-goshti standart\nNarxi: 36 000 so'm", reply_markup=buy_button)


@dp.message(F.text=="Donar tovuq-goshti")
async def lavash(message: types.Message):
    donar_st = "https://www.bildderfrau.de/BDF/ece_incoming/114033/image-thumb__114033__header/D%C3%B6ner%20selber%20machen.jpg"
    lst.append("Donar tovuq-goshti")
    list.append("Донар куриный")
    await message.answer_photo(photo=donar_st, caption="Donar tovuq-goshti standart\nNarxi: 32 000 so'm", reply_markup=buy_button)


@dp.message(F.text=="Combo mini")
async def lavash(message: types.Message):
    combo_ = "https://avatars.mds.yandex.net/get-sprav-products/9854027/2a0000018a742bafed87bddf2879de45a81e/M_height"
    lst.append("Combo mini")
    list.append("Комбо мини")
    await message.answer_photo(photo=combo_, caption="Combo bolalar uchun\nNarxi: 19 000 so'm", reply_markup=buy_button)




@dp.message(F.text=="Combo")
async def lavash(message: types.Message):
    combo1 = "https://media.rnztools.nz/rnz/image/upload/s--df_TqYQc--/c_scale,f_auto,q_auto,w_1050/v1643513123/4OTSHNP_copyright_image_73586"
    lst.append("Combo")
    list.append("Комбо")
    await message.answer_photo(photo=combo1, caption=" Combo Student\nNarxi: 24 000 so'm", reply_markup=buy_button)


@dp.message(F.text=="Combo 4 odam uchun")
async def lavash(message: types.Message):
    combo = "https://media.express24.uz/r/600/600/umuc8XjgzLtco1zTK7CyH.jpg"
    lst.append("Combo 4 odam uchun")
    list.append("Комбо для 4 людей")
    await message.answer_photo(photo=combo, caption="Combo 4x Dostlar uchun\nNarxi: 60 000 so'm", reply_markup=buy_button)


@dp.message(F.text=="Лаваш говядина")
async def lavash(message: types.Message):
    lavash_photo_standart = "https://yukber.uz/image/cache/catalog/lavash-700x700.jpg"
    lst.append("Lavash mol-goshti")
    list.append("Лаваш говядина")
    await message.answer_photo(photo=lavash_photo_standart, caption="Лаваш говядина стандарт\nЦена: 35 000 сум", reply_markup=buy_button)


@dp.message(F.text=="Лаваш куриный")
async def lavash(message: types.Message):
    lavash_photo_tovuq_standart = "https://ml1nrnpa6jqh.i.optimole.com/w:500/h:350/q:mauto/f:best/https://chicken-elika.kz/wp-content/uploads/2019/05/MG9O5DSAgPmCfS6qcvUQ.png"
    lst.append("Lavash tovuq-goshti")
    list.append("Лаваш куриный")
    await message.answer_photo(photo=lavash_photo_tovuq_standart, caption="Лаваш куриный стандарт\nNarxi: 33 000 сум", reply_markup=buy_button)


@dp.message(F.text=="Фри мини (70гр)")
async def lavash(message: types.Message):
    fri_photo_70 = "https://hips.hearstapps.com/hmg-prod/images/best-homemade-chips-645e4d046f5df.jpg"
    lst.append("Fri mini (70gr)")
    list.append("Фри мини (70гр)")
    await message.answer_photo(photo=fri_photo_70, caption="Фри мини (70гр)\nЦена: 12 000 сум", reply_markup=buy_button)


@dp.message(F.text=="Фри стандарт (100гр)")
async def lavash(message: types.Message):
    fri_photo_standart = "https://www.seriouseats.com/thmb/Il7mv9ZSDh7n0cZz3t3V-28ImkQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__2018__04__20180309-french-fries-vicky-wasik-15-5a9844742c2446c7a7be9fbd41b6e27d.jpg"
    lst.append("Fri (100gr)")
    list.append("Фри (100гр)")
    await message.answer_photo(photo=fri_photo_standart, caption="Фри стандарт (120гр)\nЦена: 29 000 сум", reply_markup=buy_button)


@dp.message(F.text=="Шаурма говядина")
async def lavash(message: types.Message):
    shaurma_standart = "https://t4.ftcdn.net/jpg/05/73/18/41/360_F_573184112_TgBWWxZAGNCkITMbFg7SzaFlDHh5I6NZ.jpg"
    lst.append("Shaurma mol-goshti")
    list.append("Шаурма говядина")
    await message.answer_photo(photo=shaurma_standart, caption="Шаурма говядина стандарт\nЦена: 36 000 сум", reply_markup=buy_button)


@dp.message(F.text=="Шаурма куриный")
async def lavash(message: types.Message):
    shaurma_tovuq_standart = "https://imageproxy.wolt.com/venue/61caadc0514c59068055ba6a/9935393e-a778-11ed-9a7f-464364fae894_1131dbe4_67a7_11ec_9bab_b6243be44d8e_ff428f46_906a_11eb_a3e5_42bebe8f9313_gldani_express.jpeg.webp"
    lst.append("Shaurma tovuq-goshti")
    list.append("Шаурма куриный")
    await message.answer_photo(photo=shaurma_tovuq_standart, caption="Шаурма куриный стандарт\nЦена: 32 000 сум", reply_markup=buy_button)


@dp.message(F.text=="Донар говядина")
async def lavash(message: types.Message):
    donar_photo_m = "https://i0.wp.com/thecitylife.org/wp-content/uploads/2023/03/Chicken.jpg?fit=1536%2C1039&ssl=1"
    lst.append("Donar mol-goshti")
    list.append("Донар говядина")
    await message.answer_photo(photo=donar_photo_m, caption="Донар говядина стандарт\nЦена: 36 000 сум", reply_markup=buy_button)


@dp.message(F.text=="Донар куриный")
async def lavash(message: types.Message):
    donar_st = "https://www.bildderfrau.de/BDF/ece_incoming/114033/image-thumb__114033__header/D%C3%B6ner%20selber%20machen.jpg"
    lst.append("Donar tovuq-goshti")
    list.append("Донар куриный")
    await message.answer_photo(photo=donar_st, caption="Донар куриный стандарт\nЦена: 32 000 сум", reply_markup=buy_button)


@dp.message(F.text=="Комбо мини")
async def lavash(message: types.Message):
    combo_ = "https://avatars.mds.yandex.net/get-sprav-products/9854027/2a0000018a742bafed87bddf2879de45a81e/M_height"
    lst.append("Combo mini")
    list.append("Комбо mini")
    await message.answer_photo(photo=combo_, caption="Комбо для детей\nЦена: 19 000 сум", reply_markup=buy_button)


@dp.message(F.text=="Комбо")
async def lavash(message: types.Message):
    combo1 = "https://media.rnztools.nz/rnz/image/upload/s--df_TqYQc--/c_scale,f_auto,q_auto,w_1050/v1643513123/4OTSHNP_copyright_image_73586"
    lst.append("Combo")
    list.append("Комбо")
    await message.answer_photo(photo=combo1, caption="Комбо Студент\nЦена: 24 000 сум", reply_markup=buy_button)


@dp.message(F.text=="Комбо для 4 людей")
async def lavash(message: types.Message):
    combo = "https://media.express24.uz/r/600/600/umuc8XjgzLtco1zTK7CyH.jpg"
    lst.append("Combo 4 odam uchun")
    list.append("Комбо для 4 людей")
    await message.answer_photo(photo=combo, caption="Комбо для друзей 4x\nЦена: 60 000 сум", reply_markup=buy_button)




@dp.message(F.text==("Поддержка"))
async def start(message: types.Message):
    await message.answer("Позвоните по этому номеру:\n+998(97)004-18-80")


@dp.message(F.text==("Nima yordam kerak"))
async def start(message: types.Message):
    await message.answer("Shu nomerga murojat qiling:\n+998(97)004-18-80")



@dp.message(F.text==("Biz haqimizda"))
async def start(message: types.Message):
    await message.answer("Kompaniyamizning birinchi filiali 2006 yilda ochilgan bo’lib, shu kungacha muvaffaqiyatli faoliyat yuritib kelmoqdaligini bilarmidingiz? 15 yil davomida kompaniya avtobus bekatidagi kichik ovqatlanish joyidan zamonaviy, kengaytirilgan tarmoqqa aylandi, u bugungi kunda O‘zbekiston bo‘ylab 65 dan ortiq restoranlarni, o‘zining eng tezkor yetkazib berish xizmatini, zamonaviy IT-infratuzilmasini va 2000 dan ortiq xodimlarni o‘z ichiga oladi.")


@dp.message(F.text==("О нас"))
async def start(message: types.Message):
    await message.answer("Знаете ли вы, что первый филиал нашей компании был открыт в 2006 году и успешно работает по сей день? За 15 лет компания выросла из небольшой забегаловки на автобусной остановке в современную, расширенную сеть, которая сегодня насчитывает более 65 ресторанов по всему Узбекистану, самую быструю службу доставки, современную ИТ-инфраструктуру и насчитывает более 2000 сотрудников.")


@dp.message(F.text==("Siz haqingizda"))
async def start(message: types.Message):
    await message.answer(f"Siz haqizda: \nIsm: {message.from_user.full_name}\nUsername: {message.from_user.username}\nId: {message.from_user.id}")


@dp.message(F.text==("О вас"))
async def start(message: types.Message):
    await message.answer(f"О вас: \nИмя: {message.from_user.full_name}\nЮзернейм: {message.from_user.username}\nАйди: {message.from_user.id}")



@dp.message(F.text==("Orqaga"))
async def start(message: types.Message):
    await message.answer('Tanlang ', reply_markup=uz_menu)

@dp.message(F.text==("назад"))
async def start(message: types.Message):
    await message.answer('Выберите ', reply_markup=ru_menu)


@dp.message(F.text==("Savat"))
async def start(message: types.Message):
    if order:
        await message.answer(f"Sinzing zakazingiz: {', '.join(order)}")

    else:
        await message.answer("Sizda xali buyurtma yoq")
    await message.answer('Tanlang ', reply_markup=savat_uz)


@dp.message(F.text==("Корзинка"))
async def start(message: types.Message):
    if order_ru:
        await message.answer(f"Ваши заказы: {', '.join(order_ru)}")

    else:
        await message.answer("Вы не заказали еще")
    await message.answer('Выберите', reply_markup=savat_rus)


@dp.callback_query(F.data == 'pepsi')
async def pepsi(callback: CallbackQuery):
    await callback.message.answer("Pepsi tanlang: ", reply_markup=pepsi_menu)


@dp.callback_query(F.data == 'cocacola')
async def pepsi(callback: CallbackQuery):
    await callback.message.answer("CocaCola tanlang: ", reply_markup=cola_menu)


@dp.callback_query(F.data == 'moxito')
async def pepsi(callback: CallbackQuery):
    await callback.message.answer("Moxito tanlang: ", reply_markup=moxito_menu)


@dp.callback_query(F.data == 'sok')
async def pepsi(callback: CallbackQuery):
    await callback.message.answer("Sok tanlang: ", reply_markup=sok_menu)




@dp.callback_query(F.data == 'пепси')
async def pepsi(callback: CallbackQuery):
    await callback.message.answer("Выберите пепси: ", reply_markup=pepsi_menu_ru)


@dp.callback_query(F.data == 'кокакола')
async def pepsi(callback: CallbackQuery):
    await callback.message.answer("Выберите Колу: ", reply_markup=cola_menu_ru)


@dp.callback_query(F.data == 'мохито')
async def pepsi(callback: CallbackQuery):
    await callback.message.answer("Выберите мохито: ", reply_markup=moxito_menu_ru)


@dp.callback_query(F.data == 'сок')
async def pepsi(callback: CallbackQuery):
    await callback.message.answer("Выберите сок : ", reply_markup=sok_menu_ru)


@dp.message(F.text==("Pepsi 0.5L"))
async def nolbesh(message: types.Message):
    pepsi_photo = "https://1119001045.rsc.cdn77.org/wa-data/public/shop/products/86/30/3086/images/2216/Napitok_Gazirovannyy_PEPSI_05_l.650@2x.jpg"
    lst.append("Pepsi 0.5L")
    list.append("Пепси 0.5Л")
    await message.answer_photo(photo=pepsi_photo, caption='Pepsi 500ml \nNarxi: 6000 som ', reply_markup=buy_button)



@dp.message(F.text==("Pepsi 1.5L"))
async def nolbesh(message: types.Message):
    pepsi_photo_15 = "https://varus.ua/img/product/1140/1140/2637294"
    lst.append("Pepsi 1.5L")
    list.append("Пепси 1.5Л")
    await message.answer_photo(photo=pepsi_photo_15, caption='Pepsi 500ml \nNarxi: 16000 som ', reply_markup=buy_button)


@dp.message(F.text==("CocaCola 0.5L"))
async def nolbesh(message: types.Message):
    cola_photo = "https://5.imimg.com/data5/TB/DD/MK/SELLER-107310956/500ml-coca-cola-cold-drink-500x500.jpg"
    lst.append("CocaCola 0.5L")
    list.append("КокаКола 0.5Л")
    await message.answer_photo(photo=cola_photo, caption='CocaCola 500ml \nNarxi: 7000 som ', reply_markup=buy_button)


@dp.message(F.text==("CocaCola 1.5L"))
async def nolbesh(message: types.Message):
    cola_photo_15 = "https://karvonmarket.uz/public/uploads/media/nfQsXlq9Oq9lELJErM2IARkUxtyfFZGukkSO9RV3.png"
    lst.append("CocaCola 1.5L")
    list.append("КокаКола 1.5Л")
    await message.answer_photo(photo=cola_photo_15, caption='CocaCola 1500ml \nNarxi: 15000 som ', reply_markup=buy_button)

@dp.message(F.text==("Moxito malina"))
async def nolbesh(message: types.Message):
    moxito_photo = "https://img.freepik.com/premium-photo/raspberry-mojito-cocktail-white-background_690179-4725.jpg"
    lst.append("Moxito malina")
    list.append("Мохито малина")
    await message.answer_photo(photo=moxito_photo, caption='Moxito malina\nNarxi: 17000 som ', reply_markup=buy_button)


@dp.message(F.text==("Moxito sitrus"))
async def nolbesh(message: types.Message):
    moxito_photo_15 = "https://www.bpour.com/wp-content/uploads/2016/10/mojito.jpg"
    lst.append("Moxito sitrus")
    list.append("Мохито цитрус")
    await message.answer_photo(photo=moxito_photo_15, caption='Moxito sitrus\nNarxi: 18000 som ', reply_markup=buy_button)


@dp.message(F.text==("Sok Olmali"))
async def nolbesh(message: types.Message):
    sok_photo_11 = "https://images.uzum.uz/cegqq1avtie1lhbf82gg/original.jpg"
    lst.append("Sok Olmali")
    list.append("Сок яблочный")
    await message.answer_photo(photo=sok_photo_11, caption='Sok Ananasli\nNarxi: 12000 som ', reply_markup=buy_button)


@dp.message(F.text==("Sok Multifrukt"))
async def nolbesh(message: types.Message):
    sok_photo_15 = "https://images.uzum.uz/cegqt7ov1htd23ajan6g/t_product_540_high.jpg"
    lst.append("Sok Multifrukt")
    list.append("Сок мультифрукт")
    await message.answer_photo(photo=sok_photo_15, caption='Sok Multifrukt\nNarxi: 14000 som ', reply_markup=buy_button)


@dp.message(F.text==("Sok orikli"))
async def nolbesh(message: types.Message):
    sok_photo = "https://images.uzum.uz/cempqjqvtie1lhbg3bk0/original.jpg"
    lst.append("Sok orikli")
    list.append("Срк абрикосовый")
    await message.answer_photo(photo=sok_photo, caption='Sok orikli\nNarxi: 16000 som ', reply_markup=buy_button)


@dp.message(F.text==("Пепси 0.5Л"))
async def nolbesh(message: types.Message):
    pepsi_photo = "https://1119001045.rsc.cdn77.org/wa-data/public/shop/products/86/30/3086/images/2216/Napitok_Gazirovannyy_PEPSI_05_l.650@2x.jpg"
    lst.append("Pepsi 0.5L")
    list.append("Пепси 0.5Л")
    await message.answer_photo(photo=pepsi_photo, caption='Пепси 500мл\nЦена: 6000 сум  ', reply_markup=buy_button_ru)


@dp.message(F.text==("Пепси 1.5Л"))
async def nolbesh(message: types.Message):
    pepsi_photo_15 = "https://varus.ua/img/product/1140/1140/2637294"
    lst.append("Pepsi 1.5L")
    list.append("Пепси 1.5Л")
    await message.answer_photo(photo=pepsi_photo_15, caption='Пепси 1500мл\nЦена: 16000 сум  ', reply_markup=buy_button_ru)


@dp.message(F.text==("КокаКола 0.5Л"))
async def nolbesh(message: types.Message):
    cola_photo = "https://5.imimg.com/data5/TB/DD/MK/SELLER-107310956/500ml-coca-cola-cold-drink-500x500.jpg"
    lst.append("CocaCola 0.5L")
    list.append("КокаКола 0.5Л")
    await message.answer_photo(photo=cola_photo, caption='КокаКола 500мл\nЦена: 7000 сум ', reply_markup=buy_button_ru)


@dp.message(F.text==("КокаКола 1.5Л"))
async def nolbesh(message: types.Message):
    cola_photo_15 = "https://karvonmarket.uz/public/uploads/media/nfQsXlq9Oq9lELJErM2IARkUxtyfFZGukkSO9RV3.png"
    lst.append("CocaCola 1.5L")
    list.append("КокаКола 1.5Л")
    await message.answer_photo(photo=cola_photo_15, caption='CocaCola 1500мл \nЦена: 15000 сум ', reply_markup=buy_button_ru)


@dp.message(F.text==("Мохито малина"))
async def nolbesh(message: types.Message):
    moxito_photo = "https://img.freepik.com/premium-photo/raspberry-mojito-cocktail-white-background_690179-4725.jpg"
    lst.append("Moxito malina")
    list.append("Мохито малина")
    await message.answer_photo(photo=moxito_photo, caption='Мохито малина\nЦена: 17000 сум  ', reply_markup=buy_button_ru)


@dp.message(F.text==("Мохито цитрус"))
async def nolbesh(message: types.Message):
    moxito_photo_15 = "https://www.bpour.com/wp-content/uploads/2016/10/mojito.jpg"
    lst.append("Moxito sitrus")
    list.append("Мохито цитрус")
    await message.answer_photo(photo=moxito_photo_15, caption='Мохито цитрус\nЦена: 18000 сум ', reply_markup=buy_button_ru)


@dp.message(F.text==("Сок яблочный"))
async def nolbesh(message: types.Message):
    sok_photo_11 = "https://images.uzum.uz/cegqq1avtie1lhbf82gg/original.jpg"
    lst.append("Sok Olmali")
    list.append("Сок яблочный")
    await message.answer_photo(photo=sok_photo_11, caption='Сок ананасовый\nЦена: 12000 сум  ', reply_markup=buy_button_ru)


@dp.message(F.text==("Сок Мультифрукт"))
async def nolbesh(message: types.Message):
    sok_photo_15 = "https://images.uzum.uz/cegqt7ov1htd23ajan6g/t_product_540_high.jpg"
    lst.append("Sok Multifrukt")
    list.append("Сок мультифрукт")
    await message.answer_photo(photo=sok_photo_15, caption='Сок Мультифрукт\nЦена: 14000 сум ', reply_markup=buy_button_ru)


@dp.message(F.text==("Сок абрикосовый"))
async def nolbesh(message: types.Message):
    sok_photo = "https://images.uzum.uz/cempqjqvtie1lhbg3bk0/original.jpg"
    lst.append("Sok orikli")
    list.append("Срк абрикосовый")
    await message.answer_photo(photo=sok_photo, caption='Сок абрикосовый\nЦена: 16000 сум  ', reply_markup=buy_button_ru)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())(inline_keyboard=taom_menu)