import turtle

ekran = turtle.Screen()
ekran.title("Pong - Seviye Sistemi")
ekran.bgcolor("black")
ekran.setup(width=800, height=600)
ekran.tracer(0)


basladi_mi = False
carpma_kac = 0  # burayı yapana kadar bittim hala anlamaya çalışıyom
seviyeNo = 1

# raket yapıyoz
class Raket(turtle.Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, 0)

    def yukari(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 30)

    def asagi(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 30)

# topun hareketleri (sıkıldım) 
class Top(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 2.0
        self.dy = 2.0

    def hareket(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        if self.ycor() > 290 or self.ycor() < -290:
            self.dy = -self.dy  # böyle daha net

    def sifirla(self):
        self.goto(0, 0)
        self.dx = -self.dx

    def hiz_arttir(self, levelx):
        hizlar = {2: 3.5, 3: 5, 4: 8}
        hiz = hizlar.get(levelx, 2.0)
        self.dx = hiz if self.dx > 0 else -hiz
        self.dy = hiz if self.dy > 0 else -hiz

# skor (zaten nerdeyse chat gbt yaptı olmuyooooooooo ama yapçam sorun var ama yok eğlenceli olcak)
class Skor(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.sol = 0
        self.sag = 0
        self.guncelle()

    def guncelle(self):
        self.clear()
        self.write(f"{self.sol} : {self.sag}", align="center", font=("Arial", 24, "normal"))

# seviye yazisi
seviye_yazi = turtle.Turtle()
seviye_yazi.color("yellow")
seviye_yazi.penup()
seviye_yazi.hideturtle()
seviye_yazi.goto(0, -250)

def seviye_goster(s):
    seviye_yazi.clear()
    seviye_yazi.write(f"SEVİYE {s}", align="center", font=("Arial", 16, "bold"))

# başlangıç ekranı
baslat= turtle.Turtle()
baslat.color("white")
baslat.penup()
baslat.hideturtle()
baslat.goto(0, 0)
baslat.write("BAŞLAMAK İÇİN BOŞLUK TUŞUNA BAS", align="center", font=("Arial", 20, "bold"))

def baslat():
    global oyun_basladi, seviyeNo
    oyun_basladi = True
    baslangic_yazi.clear()
    seviye_goster(seviyeNo)
   
sol = Raket(-350)
sag = Raket(350)
top = Top()
skor = Skor()
ekran.listen()
ekran.onkeypress(sol.yukari, "w")
ekran.onkeypress(sol.asagi, "s")
ekran.onkeypress(sag.yukari, "Up")
ekran.onkeypress(sag.asagi, "Down")
ekran.onkeypress(baslat, "space")

oyun_basladi = False
carpma_kac = 0
seviyeNo = 1

def oyun_dongusu():
    global carpma_kac, seviyeNo

    if not oyun_basladi:
        ekran.ontimer(oyun_dongusu, 10)
        return

    top.hareket()

    if top.xcor() > 330 and top.distance(sag) < 50:
        top.dx = -top.dx
        carpma_kac += 1

    if top.xcor() < -330 and top.distance(sol) < 50:
        top.dx = -top.dx
        carpma_kac += 1

    if top.xcor() > 390:
        skor.sol += 1
        skor.guncelle()
        top.sifirla()

    if top.xcor() < -390:
        skor.sag += 1
        skor.guncelle()
        top.sifirla()

    if carpma_kac >= 1000 and seviyeNo == 3:
        seviyeNo = 4
        top.hiz_arttir(seviyeNo)
        seviye_goster(seviyeNo)
    elif carpma_kac >= 100 and seviyeNo == 2:
        seviyeNo = 3
        top.hiz_arttir(seviyeNo)
        seviye_goster(seviyeNo)
    elif carpma_kac >= 10 and seviyeNo == 1:
        seviyeNo = 2
        top.hiz_arttir(seviyeNo)
        seviye_goster(seviyeNo)

    ekran.update()
    ekran.ontimer(oyun_dongusu, 10)

oyun_dongusu()
ekran.mainloop()

