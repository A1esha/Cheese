import tkinter


class Cheese:
    def __init__(self):
        self.game = []
        self.canvas = tkinter.Canvas(width=500, height=700)
        self.canvas['background'] = '#D2B48C'
        self.canvas.create_text(250, 100, text='Cheese', font='Arial 50', fill='#F5DEB3')
        self.canvas.pack()
        self.start()
        self.desk()
        tkinter.mainloop()
    def desk(self):

        self.PBlack = tkinter.PhotoImage(file='images/P_black.png')
        self.PWhite = tkinter.PhotoImage(file='images/P_white.png')
        self.LBlack = tkinter.PhotoImage(file='images/LBlack.png')
        self.LWhite = tkinter.PhotoImage(file='images/Lwhite.png')
        self.KWhite = tkinter.PhotoImage(file='images/KWhite.png')
        self.KBlack = tkinter.PhotoImage(file='images/KBlack.png')
        self.CBlack = tkinter.PhotoImage(file='images/CBlack.png')
        self.CWhite = tkinter.PhotoImage(file='images/CWhite.png')
        self.FWhite = tkinter.PhotoImage(file='images/FWhite.png')
        self.FBlack = tkinter.PhotoImage(file='images/FBlack.png')
        self.KrWhite = tkinter.PhotoImage(file='images/KrWhite.png')
        self.KrBlack = tkinter.PhotoImage(file='images/KrBlack.png')

        x = 30
        y = 225
        for i in range(8):
            self.canvas.create_text(x, y, fill='black', text=str(8 - i), font='Arial 18')
            y += 50

        x = 75
        y = 615
        for i in range(97, 105):
            self.canvas.create_text(x, y, fill='black', font='Arial 18', text=chr(i))
            x += 50

        x = 50
        y = 200
        for i in range(8):
            for j in range(8):
                color = '#FFF8DC'
                if (i + j) % 2 == 1:
                    color = '#808080'
                self.canvas.create_rectangle(x + i * 50, y + j * 50, x + (i + 1) * 50, y + (j + 1) * 50, fill=color)

        x = 75
        y = 225
        for i in range(8):
            for j in range(8):
                col = self.game[j][i][1]
                if col == 'white':
                    if self.game[j][i][0] == 'P':
                        self.canvas.create_image(x + i * 50, y + j * 50, image=self.PWhite)
                    elif self.game[j][i][0] == 'L':
                        self.canvas.create_image(x + i * 50, y + j * 50, image=self.LWhite)
                    elif self.game[j][i][0] == 'K':
                        self.canvas.create_image(x + i * 50-2, y + j * 50, image=self.KWhite)
                    elif self.game[j][i][0] == 'C':
                        self.canvas.create_image(x + i * 50, y + j * 50, image=self.CWhite)
                    elif self.game[j][i][0] == 'F':
                        self.canvas.create_image(x + i * 50, y + j * 50, image=self.FWhite)
                    elif self.game[j][i][0] == 'Kr':
                        self.canvas.create_image(x + i * 50, y + j * 50, image=self.KrWhite)
                    else:
                        self.canvas.create_text(x + i * 50, y + j * 50, text=self.game[j][i][0], fill='red')
                if col == 'black':
                    if self.game[j][i][0] == 'P':
                        self.canvas.create_image(x + i * 50, y + j * 50, image=self.PBlack)
                    elif self.game[j][i][0] == 'L':
                        self.canvas.create_image(x + i * 50, y + j * 50, image=self.LBlack)
                    elif self.game[j][i][0] == 'K':
                        self.canvas.create_image(x + i * 50, y + j * 50, image=self.KBlack)
                    elif self.game[j][i][0] == 'C':
                        self.canvas.create_image(x + i * 50, y + j * 50, image=self.CBlack)
                    elif self.game[j][i][0] == 'F':
                        self.canvas.create_image(x + i * 50, y + j * 50, image=self.FBlack)
                    elif self.game[j][i][0] == 'Kr':
                        self.canvas.create_image(x + i * 50, y + j * 50, image=self.KrBlack)
                    else:
                        self.canvas.create_text(x + i * 50, y + j * 50, text=self.game[j][i][0], fill='green')


    def start(self):
        for j in range(8):
            mas = []
            for i in range(8):
                mas.append(['0', 'noooo'])
            self.game.append(mas)
        self.game[0][0] = ['L', 'black']
        self.game[0][7] = ['L', 'black']
        self.game[7][0] = ['L', 'white']
        self.game[7][7] = ['L', 'white']  # Ладьи на доске

        self.game[0][1] = ['K', 'black']
        self.game[0][6] = ['K', 'black']
        self.game[7][1] = ['K', 'white']
        self.game[7][6] = ['K', 'white']  # Кони на доске

        self.game[0][2] = ['C', 'black']
        self.game[0][5] = ['C', 'black']
        self.game[7][2] = ['C', 'white']
        self.game[7][5] = ['C', 'white']  # Слоны на доске

        self.game[0][3] = ['F', 'black']
        self.game[0][4] = ['Kr', 'black']# Черные король и ферзь

        self.game[7][3] = ['F', 'white']
        self.game[7][4] = ['Kr', 'white']# Белые король и ферзь

        for i in range(8):
            self.game[1][i] = ['P', 'black']
            self.game[6][i] = ['P', 'white']


app = Cheese()

