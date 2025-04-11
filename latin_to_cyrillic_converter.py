print("1.Lotindan Krillga")
print("1.Krilldan Lotinga")
a = int(input("Xizmatni tanlang"))

if a == 1:
    lotin = input("Lotincha so'zni kiriting: ")
    krill = lotin.replace("a", "а").replace("b", "б").replace("d", "д").replace("e", "е").replace("f", "ф").replace("g", "г").replace("h", "х").replace("i", "и").replace("j", "ж").replace("k", "к").replace("l", "л").replace("m", "м").replace("n", "н").replace("o", "о").replace("p", "п").replace("q", "қ").replace("r", "р").replace("s", "с").replace("t", "т").replace("u", "у").replace("v", "в").replace("x", "х").replace("y", "й").replace("z", "з")
    print(krill)
elif a == 2:
    krill = input("Krillcha so'zni kiriting: ")
    lotin = krill.replace("а", "a").replace("б", "b").replace("д", "d").replace("е", "e").replace("ф", "f").replace("г", "g").replace("х", "h").replace("и", "i").replace("ж", "j").replace("к", "k").replace("л", "l").replace("м", "m").replace("н", "n").replace("о", "o").replace("п", "p").replace("қ", "q").replace("р", "r").replace("с", "s").replace("т", "t").replace("у", "u").replace("в", "v").replace("х", "x").replace("й", "y").replace("з", "z")
    print(lotin)
else:
    print("Son kiritmang")