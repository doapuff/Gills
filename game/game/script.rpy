define har = Character("Хариус", color="#5dade2")
define doc = Character("Доктор Осетр", color="#a569bd")
define nurse = Character("Сестра Треска", color="#f39c12")
define carp = Character("Карп", color="#e74c3c")
define pike = Character("Щука-лаборант", color="#27ae60")
define catfish = Character("Сом-знахарь", color="#8e44ad")
define algae = Character("Альга", color="#16a085")

# Изображения
image bg corridor = "images/backgrounds/hospital_corridor.png"
image bg room = "images/backgrounds/hospital_room.png"
image bg lab = "images/backgrounds/lab.png"
image bg office = "images/backgrounds/doctor_office.png"
image bg alley = "images/backgrounds/dark_alley.png"
image bg lake = "images/backgrounds/moon_lake.png"

image har normal = "images/characters/har_normal.png"
image har scared = "images/characters/har_scared.png"
image har panic = "images/characters/har_panic.png"
image har determined = "images/characters/har_determined.png"

image doctor = "images/characters/doctor.png"
image nurse = "images/characters/nurse.png"
image carp = "images/characters/carp.png"
image pike = "images/characters/pike.png"
image catfish = "images/characters/catfish.png"
image algae = "images/characters/algae.png"

# Звуки
define audio.ambience = "sounds/water_ambience.ogg"
define audio.heartbeat = "sounds/heartbeat.ogg"
define audio.dark_whisper = "sounds/dark_whisper.ogg"

# Жабры
image gills_normal = "images/gills_normal.png"
image gills_sick = "images/gills_sick.png"
image gills_fila = "images/gills_fila.png"
image gills_des = "images/gills_des.png"

label start:
    play music ambience loop

    # Пролог: Кошмар
    scene black
    har "{i}Я тону... но я же рыба?{/i}"
    play sound heartbeat
    har "{i}Жабры... не работают...{/i}"
    scene bg room with fade
    show har panic at center with vpunch
    har "А-а-а! Ч-что это было?!"
    hide har panic
    "..."

    # Сцена 1: Поступление в больницу
    scene bg corridor
    show har normal at left
    har "Как же здесь холодно... И пахнет формалином. Надеюсь, мой случай не слишком серьезный..."

    show nurse at right
    nurse "Фамилия, вид, диагноз при поступлении?"
    menu:
        "Назвать полные данные":
            har "Хариус сибирский (Thymallus arcticus). Меня направили с подозрением на «жаберные аномалии»."
            nurse "О, научный подход. Это понравится доктору Осетру."
        "Сказать кратко":
            har "Хариус... Сибирский. Проблемы с жабрами."
            nurse "М-да, лаконично. Палата №7."

    nurse "Палата №7. Соседка — карп с аневризмами. Не шумите, у нее давление."

    # Сцена 2: Знакомство с карпом
    scene bg room
    show carp at right
    carp "О, новенькая! Что у тебя?"

    show har normal at left
    har "Не знаю... Дышать тяжело, жабры будто горят."
    carp "У меня вот — аневризмы. Капилляры лопаются, как шарики. Но знаешь, что самое страшное?"

    menu:
        "Спросить что":
            har "Что?"
            carp "То, что мне вчера снилось... будто я превращаюсь в консервную банку."
        "Пошутить":
            har "Надеюсь, у тебя хотя бы икра в порядке?"
            carp "*фыркает* Ты хоть понимаешь, что в таком состоянии мне даже нереститься нельзя?!"

    # Сцена 3: В лаборатории
    scene bg lab
    show pike at right
    show har scared at left

    pike "Ламелли... Филаменты... Эпителий... О-о-о, интересненькое."
    har "Что «интересненькое»?!"
    pike "К главврачу. Немедленно."

    # Сцена 4: Диагноз
    scene bg office
    show doctor at right
    show har normal at left

    doc "Хариус... Ваши анализы... ужасны."
    show gills_normal at left with dissolve
    doc "Вот показатели нормы."
    show gills_sick at right with dissolve
    doc "А вот ваши жабры."
    pause 0.5

    show har scared at left with vpunch
    har "Это... Это МОИ жабры?!"

    doc "Во-первых, паразитарная деструкция. Видите этот круглый шарик?" 
    hide gills_normal
    hide gills_sick
    with dissolve
    doc "Они прогрызают ткани, образуют кисты."

    show har panic
    har "Но... Но это же..."

    doc "Во-вторых, слияние филаментов. Ваши жаберные нити склеились, как мокрая бумага."
    show gills_fila  with dissolve
    doc "Дыхательная поверхность сократилась на 40 процентов."
    pause 2.0
    hide gills_fila with dissolve

    show har panic at left with vpunch
    har "УЖАС! Как я могла довести до такого состояния?!"

    doc "И на десерт... десквамация. Эпителий отслаивается пластами."
    show gills_des with dissolve
    doc "Рассмотрите подробнее. Ваша аномалия кроется в кривизне и удлиненности ламелл в ваших жабрах. Местами они слиплись"
    pause 2.0
    hide gills_des with dissolve

    show har panic at left with vpunch
    har "КОМБО!!!"

    doc "Если начнется цитолиз... вас уже не спасти."

    menu treatment_choice:
        doc "Выбирайте лечение:"
        "Традиционная медицина":
            jump hospital_treatment
        "Народные методы":
            jump folk_treatment
        "Самостоятельно разобраться":
            jump self_research

label hospital_treatment:
    scene bg office
    show doctor at right
    show har determined at left

    doc "Разумный выбор. Начнем с противопаразитарных ванн."
    scene black with fade
    "..."
    "Неделю спустя..."

    scene bg room
    show har normal at left
    show carp at right

    carp "Как результаты?"
    har "Паразиты исчезли, но... появилось новое."
    play sound dark_whisper
    "{i}*шёпот* Приди к омуту...*шёпот*{/i}"
    har "Ты слышала?!"
    carp "Что? У меня опять в глазах темнеет..."

    jump mysterious_ending

label folk_treatment:
    scene bg alley
    show catfish at right
    show har scared at left

    play music dark_whisper
    catfish "А-а-а, больная душа чувствует мой киоск..."
    har "Я слышала, вы можете помочь с жаберными..."
    catfish "*Перебив*"
    catfish "За 500 ракушек сделаю тебя как новую! Но... нужна твоя чешуя для обряда."
    menu:
        "Согласиться":
            jump catfish_deal
        "Отказаться":
            jump run_away

label catfish_deal:
    scene bg lake
    show catfish at right
    show har panic at left

    catfish "*бормочет* Чешуя на восток, хвост на запад..."
    har "А-а-а! Что вы делаете?!"
    catfish "Теперь ты моя! Хе-хе-хе!"

    scene black
    "..."
    "Ваше сознание медленно растворяется в темноте..."
    return

label run_away:
    scene bg alley
    show har determined at left
    show catfish at right

    har "Нет! Я лучше умру, чем стану вашим экспериментом!"
    catfish "Как глупо... ты уже обречена."

    scene bg room
    show har panic at center
    "Вы вернулись в больницу, но состояние быстро ухудшается..."
    play sound heartbeat
    scene black
    "..."
    "КОНЕЦ: ОДИНОКАЯ ГИБЕЛЬ"
    return

label self_research:
    scene bg lab
    show pike at right
    show har determined at left

    har "Я должна сама разобраться в своих анализах!"
    pike "О-о-о, научный интерес! Вот микроскоп и мои заметки."

    scene black with fade
    "..."
    "3 дня спустя..."

    scene bg lab
    show algae at right
    show har normal at left

    algae "Я слышала, ты ищешь лекарство? Мой вид производит природный антибиотик."
    har "Правда?! Но почему ты хочешь помочь?"
    algae "Потому что... я тоже когда-то была пациенткой."

    jump hopeful_ending

label mysterious_ending:
    scene bg lake
    show har panic at center

    har "Этот шёпот... он ведёт меня сюда!"
    "Из глубины появляются тысячи паразитов..."
    scene black
    play sound heartbeat
    "..."
    "КОНЕЦ. ИЛИ НАЧАЛО?"
    return

label hopeful_ending:
    scene bg room
    show har normal at left
    show algae at right

    har "Спасибо! Я чувствую, как жабры постепенно восстанавливаются."
    algae "Помни — экосистема взаимосвязана. Помоги и ты когда-нибудь другому."

    scene black
    "..."
    "СПАСЕНИЕ НАЙДЕНО"
    return