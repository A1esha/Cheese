import tkinter


class Cheese:
    def __init__(self):
        self.now = 'white'
        self.now_figure = '0'
        self.GoClear = False
        self.game = []
        self.kol = 0
        self.click = 0
        self.canvas = tkinter.Canvas(width=500, height=700)
        self.canvas['background'] = '#D2B48C'
        self.canvas.create_text(250, 100, text='Cheese', font='Arial 50', fill='#F5DEB3')
        self.canvas.pack()
        self.start()
        self.desk()
        self.canvas.bind('<Button-1>', self.klik)
        self.desk()
        tkinter.mainloop()


    def desk(self):
        self.PBlack = tkinter.PhotoImage(file='images/P_black.png')
        self.PWhite = tkinter.PhotoImage(file='images/P_white.png')
        self.LBlack = tkinter.PhotoImage(file='images/LBlack.png')
        self.LWhite = tkinter.PhotoImage(file='images/LWhite.png')
        self.KWhite = tkinter.PhotoImage(file='images/KWhite.png')
        self.KBlack = tkinter.PhotoImage(file='images/KBlack.png')
        self.CBlack = tkinter.PhotoImage(file='images/CBlack.png')
        self.CWhite = tkinter.PhotoImage(file='images/CWhite.png')
        self.FWhite = tkinter.PhotoImage(file='images/FWhite.png')
        self.FBlack = tkinter.PhotoImage(file='images/FBlack.png')
        self.KrWhite = tkinter.PhotoImage(file='images/KrWhite.png')
        self.KrBlack = tkinter.PhotoImage(file='images/KrBlack.png')


        x = 50
        y = 200
        if self.kol == 0 or self.GoClear:
            self.kol += 1
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

    def start(self):

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

    def klik(self, event):
        if event.x < 50 + 50 * 8 and event.x >= 50 and event.y <= 200 + 8 * 50 and event.y >= 200:
            x = int((event.x-50)/50)
            y = int((event.y-200)/50)
            c = self.game[y][x][0]
            col = self.game[y][x][1]
            self.PBlack = tkinter.PhotoImage(file='images/P_black.png')
            self.PWhite = tkinter.PhotoImage(file='images/P_white.png')
            self.LBlack = tkinter.PhotoImage(file='images/LBlack.png')
            self.LWhite = tkinter.PhotoImage(file='images/LWhite.png')
            self.KWhite = tkinter.PhotoImage(file='images/KWhite.png')
            self.KBlack = tkinter.PhotoImage(file='images/KBlack.png')
            self.CBlack = tkinter.PhotoImage(file='images/CBlack.png')
            self.CWhite = tkinter.PhotoImage(file='images/CWhite.png')
            self.FWhite = tkinter.PhotoImage(file='images/FWhite.png')
            self.FBlack = tkinter.PhotoImage(file='images/FBlack.png')
            self.KrWhite = tkinter.PhotoImage(file='images/KrWhite.png')
            self.KrBlack = tkinter.PhotoImage(file='images/KrBlack.png')
            self.desk()

            if self.click == 1:
                self.click = 0
                if self.game[y][x][0] == '0' or (self.game[y][x][0] != '0' and self.game[y][x][1] != self.now):
                    if self.now == 'white' or self.now == 'black':
                        gox = 75 + x * 50
                        goy = y * 50 + 225

                        if self.game[y][x][0] == '0':
                            will = self.canvas.itemcget(self.canvas.find_overlapping(gox, goy, gox + 1, goy + 1)[-1], "fill")
                        else:
                            will = '#98FB98'
                        print(will)
                        if will == '#98FB98' or self.game[y][x][0] != '0':
                            colwill = '#FFF8DC'
                            if (x + y) % 2 == 1:
                                colwill = '#808080'

                            self.canvas.create_rectangle(self.now_figure[1][0] * 50 + 50, self.now_figure[1][1] * 50 + 200,
                                                         (self.now_figure[1][0] + 1) * 50 + 50, (self.now_figure[1][1] + 1)
                                                         * 50 + 200, fill=colwill)
                            print(x, y)
                            self.game[y][x][0] = self.now_figure[0]
                            self.game[y][x][1] = self.now
                            self.game[self.now_figure[1][1]][self.now_figure[1][0]][0] = '0'
                            self.game[self.now_figure[1][1]][self.now_figure[1][0]][1] = 'noooo'
                            self.GoClear = True
                            self.desk()
                            self.GoClear = False
                            if self.now == 'white':
                                self.now = 'black'
                            else:
                                self.now = 'white'
                        else:
                            self.GoClear = True
                            self.desk()
                            self.GoClear = False
            else:

                if c != '0':
                    self.click = 1
                    if col == 'white' and self.now == 'white':
                        self.canvas.create_rectangle(x * 50 + 50, y * 50 + 200, (x + 1) * 50 + 50, (y + 1) * 50 + 200,
                                                     fill='green')

                        if c == 'P':
                            self.canvas.create_image(75 + x * 50, 225 + y * 50, image=self.PWhite)
                            self.can(x, y)
                            self.now_figure = ['P', [x, y]]
                        elif c == 'L':
                            self.canvas.create_image(75 + x * 50, 225 + y * 50, image=self.LWhite)
                            self.can(x, y)
                            self.now_figure = ['L', (x, y)]
                        elif c == 'K':
                            self.canvas.create_image(75 + x * 50-2, 225 + y * 50, image=self.KWhite)
                            self.can(x, y)
                            self.now_figure = ['K', (x, y)]
                        elif c == 'C':
                            self.canvas.create_image(75 + x * 50, 225 + y * 50, image=self.CWhite)
                            self.can(x, y)
                            self.now_figure = ['C', (x, y)]
                        elif c == 'F':
                            self.canvas.create_image(75 + x * 50, 225 + y * 50, image=self.FWhite)
                            self.can(x, y)
                            self.now_figure = ['F', (x, y)]
                        elif c == 'Kr':
                            self.canvas.create_image(75 + x * 50, 225 + y * 50, image=self.KrWhite)
                            self.can(x, y)
                            self.now_figure = ['Kr', (x, y)]

                    if col == 'black' and self.now == 'black':
                        self.canvas.create_rectangle(x * 50 + 50, y * 50 + 200, (x + 1) * 50 + 50, (y + 1) * 50 + 200,
                                                     fill='green')

                        if c == 'P':
                            self.canvas.create_image(75 + x * 50, 225 + y * 50, image=self.PBlack)
                            self.can(x, y)
                            self.now_figure = ['P', (x, y)]
                        elif c == 'L':
                            self.canvas.create_image(75 + x * 50, 225 + y * 50, image=self.LBlack)
                            self.can(x, y)
                            self.now_figure = ['L', (x, y)]
                        elif c == 'K':
                            self.canvas.create_image(75 + x * 50, 225 + y * 50, image=self.KBlack)
                            self.can(x, y)
                            self.now_figure = ['K', (x, y)]
                        elif c == 'C':
                            self.canvas.create_image(75 + x * 50, 225 + y * 50, image=self.CBlack)
                            self.can(x, y)
                            self.now_figure = ['C', (x, y)]
                        elif c == 'F':
                            self.canvas.create_image(75 + x * 50, 225 + y * 50, image=self.FBlack)
                            self.can(x, y)
                            self.now_figure = ['F', (x, y)]
                        elif c == 'Kr':
                            self.canvas.create_image(75 + x * 50, 225 + y * 50, image=self.KrBlack)
                            self.can(x, y)
                            self.now_figure = ['Kr', (x, y)]
                else:
                    self.now_figure = '0'
                    self.GoClear = True
                    self.desk()
                    self.GoClear = False


    def clear(self, x, y):
        if self.game[y][x][1] == 'white':
            if y - 1 >= 0 and x - 1 >= 0 and self.game[y-1][x-1][0] == 'P':
                return -1
            if y - 1 >= 0 and x + 1 <= 7 and self.game[y-1][x+1][0] == 'P':
                return -1


            for i in range(1, 8):
                k_x = x - i
                k_y = y - i
                if k_x >= 0 and k_x <= 7 and k_y >=0 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            if self.game[k_y][k_x][0] == 'F' or self.game[k_y][k_x][0] == 'C':
                                return -1
                            else:
                                break
                        else:
                            break
            for i in range(1, 8):
                k_x = x - i
                k_y = y + i
                if k_x >= 0 and k_x <= 7 and k_y >= 0 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            if self.game[k_y][k_x][0] == 'F' or self.game[k_y][k_x][0] == 'C':
                                return -1
                            else:
                                break
                        else:
                            break
            for i in range(1, 8):
                k_x = x + i
                k_y = y - i
                if k_x >= 0 and k_x <= 7 and k_y >= 0 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            if self.game[k_y][k_x][0] == 'F' or self.game[k_y][k_x][0] == 'C':
                                return -1
                            else:
                                break
                        else:
                            break
            for i in range(1, 8):
                k_x = x + i
                k_y = y + i
                if k_x >= 0 and k_x <= 7 and k_y >= 0 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            if self.game[k_y][k_x][0] == 'F' or self.game[k_y][k_x][0] == 'C':
                                return -1
                            else:
                                break
                        else:
                            break

            #cheking horisontals
            for i in range(1, 8):
                k_x = x - i
                k_y = y
                if k_x >= 0 and k_x <= 7 and k_y >= 0 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            if self.game[k_y][k_x][0] == 'F' or self.game[k_y][k_x][0] == 'L':
                                return -1
                            break
                        break
            for i in range(1, 8):
                k_x = x
                k_y = y - i
                if k_x >= 0 and k_x <= 7 and k_y >= 0 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            if self.game[k_y][k_x][0] == 'F' or self.game[k_y][k_x][0] == 'L':
                                return -1
                            else:
                                break
                        else:
                            break
            for i in range(1, 8):
                k_x = x + i
                k_y = y
                if k_x >= 0 and k_x <= 7 and k_y >= 0 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            if self.game[k_y][k_x][0] == 'F' or self.game[k_y][k_x][0] == 'L':
                                return -1
                            else:
                                break
                        else:
                            break
            for i in range(1, 8):
                k_x = x
                k_y = y + i
                if k_x >= 0 and k_x <= 7 and k_y >= 0 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            if self.game[k_y][k_x][0] == 'F' or self.game[k_y][k_x][0] == 'L':
                                return -1
                            else:
                                break
                        else:
                            break

            #cheking horses
            for i in range(8):
                dx = [-2, -2, -1, -1, 1, 1, 2, 2]
                dy = [-1, 1, -2, 2, -2, 2, -1, 1]
                k_x = dx[i] + x
                k_y = dy[i] + y
                if k_x >= 0 and k_x <= 7 and k_y >=0 and k_y <= 7:
                    if self.game[k_y][k_x][0] == 'K' and self.game[k_y][k_x][1] != self.game[y][x][1]:
                        return -1

            return 0

    def shah(self, color):

        x = 0
        y = 0
        for i in range(8):
            for j in range(8):
                if self.game[j][i][0] == 'Kr' and self.game[j][i][1] == color:
                    x = i
                    y = j

        if color == 'white':
            if y - 1 >= 0 and x-1 >= 0 and self.game[y-1][x-1] == ['P', 'black']:
                return True
            if y - 1 >= 0 and x + 1 <= 7 and self.game[y-1][x+1] == ['P', 'black']:
                return True
        else:
            if y + 1 <= 7 and x - 1>=0 and self.game[y+1][x-1] == ['P', 'white']:
                return True
            if y + 1 <= 7 and x + 1 <= 7 and self.game[y+1][x+1] == ['P', 'white']:

        hlad = 'white'
        if color == 'white':
            hlad = 'black'

        dx = [-2, -2, -1, -1, 1, 1, 2, 2]
        dy = [-1, 1, -2, 2, -2, 2, -1, 1]
        for i in range(8):
            k_x = dx[i] + x
            k_y = dy[i] + y

            if k_x >= 0 and k_x <= 7 and k_y >= 0 and k_y <= 7:
                if self.game[k_y][k_x] == ['K', hlad]:
                    return True

        ##Нужно добавить ферзя слона и ладью






    def can(self, x, y):
        self.kol = 0
        self.desk()
        self.canvas.create_rectangle(x * 50 + 50, y * 50 + 200, (x + 1) * 50 + 50, (y + 1) * 50 + 200, fill='green')

        if self.game[y][x][0] == 'P' and self.game[y][x][1] == 'white':
            if y-1 >= 0 and self.game[y-1][x][0] == '0':
                self.canvas.create_rectangle(x * 50 + 50, (y - 1) * 50 + 200, (x+1)*50 + 50, y * 50 + 200,
                                             fill='#98FB98')
                if y == 6 and self.game[4][x][0] == '0':
                    self.canvas.create_rectangle(x * 50 + 50, (y - 2) * 50 + 200, (x + 1) * 50 + 50, (y - 1) * 50 + 200,
                                                 fill='#98FB98')
            if x-1 >= 0 and y-1 >=0 and  self.game[y-1][x-1][0] != '0' and self.game[y-1][x-1][1] != self.game[y][x][1]:
                self.canvas.create_rectangle((x - 1) * 50 + 50, (y - 1) * 50 + 200, x * 50 + 50, y * 50 + 200,
                                             fill='#FA8072')
            if x+1 <= 7 and y-1 >=0 and self.game[y-1][x+1][0] != '0' and self.game[y-1][x+1][1] != self.game[y][x][1]:
                self.canvas.create_rectangle((x+1) * 50 + 50, (y - 1) * 50 + 200, (x + 2) * 50 + 50, y * 50 + 200,
                                             fill='#FA8072')

        if self.game[y][x][0] == 'P' and self.game[y][x][1] == 'black':
            if y+1 <= 7 and self.game[y+1][x][0] == '0':
                self.canvas.create_rectangle(x * 50 + 50, (y + 1) * 50 + 200, (x + 1) * 50 + 50, (y + 2) * 50 + 200,
                                             fill='#98FB98')
                if y == 1 and self.game[3][x][0] == '0':
                    self.canvas.create_rectangle(x * 50 + 50, 3 * 50 + 200, (x + 1) * 50 + 50, 4 * 50 + 200,
                                                 fill='#98FB98')
                if x+1 <= 7 and y+1<=7 and self.game[y+1][x+1][0] != '0' and self.game[y+1][x+1][1] != self.game[y][x][1]:
                    self.canvas.create_rectangle((x + 1) * 50 + 50, (y + 1) * 50 + 200, (x + 2) * 50 + 50,
                                                 (y + 2) * 50 + 200, fill='#FA8072')
                if x-1 >= 0 and y+1<=7 and self.game[y+1][x-1][0] != '0' and self.game[y+1][x-1][1] != self.game[y][x][1]:
                    self.canvas.create_rectangle((x - 1) * 50 + 50, (y + 1) * 50 + 200, x * 50 + 50, (y + 2) * 50 + 200,
                                                 fill='#FA8072')

        if self.game[y][x][0] == 'K':
            dx = [-2, -2, -1, -1, 1, 1, 2, 2]
            dy = [-1, 1, -2, 2, -2, 2, -1, 1]
            for i in range(8):
                k_x = dx[i] + x
                k_y = dy[i] + y

                if k_x >= 0 and k_x <= 7 and k_y >=0 and k_y <= 7:
                    if self.game[k_y][k_x][0] == '0':
                        self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50, (k_y + 1) * 50 + 200, fill='#98FB98')
                    else:
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50, (k_y + 1) * 50 + 200, fill='#FA8072')

        if self.game[y][x][0] == 'C' or self.game[y][x][0] == 'F':

            for i in range(1, 8):
                k_x = x - i
                k_y = y - i
                if k_x >= 0 and k_y >= 0 and k_x <= 7 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                     (k_y + 1) * 50 + 200, fill='#FA8072')
                            break
                        else:
                            break
                    else:
                        self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                     (k_y + 1) * 50 + 200, fill='#98FB98')
                else:
                    break

            for i in range(1, 8):
                k_x = x - i
                k_y = y + i
                if k_x >= 0 and k_y >= 0 and k_x <= 7 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                         (k_y + 1) * 50 + 200, fill='#FA8072')
                            break
                        else:
                            break
                    else:
                        self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                     (k_y + 1) * 50 + 200, fill='#98FB98')
                else:
                    break

            for i in range(1, 8):
                k_x = x + i
                k_y = y - i
                if k_x >= 0 and k_y >= 0 and k_x <= 7 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                         (k_y + 1) * 50 + 200, fill='#FA8072')
                            break
                        else:
                            break
                    else:
                        self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                     (k_y + 1) * 50 + 200, fill='#98FB98')
                else:
                    break

            for i in range(1, 8):
                k_x = x + i
                k_y = y + i
                if k_x >= 0 and k_y >= 0 and k_x <= 7 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                         (k_y + 1) * 50 + 200, fill='#FA8072')
                            break
                        else:
                            break
                    else:
                        self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                     (k_y + 1) * 50 + 200, fill='#98FB98')
                else:
                    break

        if self.game[y][x][0] == 'L' or self.game[y][x][0] == 'F':

            for i in range(1, 8):
                k_x = x - i
                k_y = y
                if k_x >= 0 and k_x <= 7 and k_y >=0 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                         (k_y + 1) * 50 + 200, fill='#FA8072')
                            break
                        else:
                            break
                    else:
                        self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                     (k_y + 1) * 50 + 200, fill='#98FB98')
            for i in range(1, 8):
                k_x = x
                k_y = y - i
                if k_x >= 0 and k_x <= 7 and k_y >=0 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                         (k_y + 1) * 50 + 200, fill='#FA8072')
                            break
                        else:
                            break
                    else:
                        self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                     (k_y + 1) * 50 + 200, fill='#98FB98')
            for i in range(1, 8):
                k_x = x + i
                k_y = y
                if k_x >= 0 and k_x <= 7 and k_y >=0 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                         (k_y + 1) * 50 + 200, fill='#FA8072')
                            break
                        else:
                            break
                    else:
                        self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                     (k_y + 1) * 50 + 200, fill='#98FB98')
            for i in range(1, 8):
                k_x = x
                k_y = y + i
                if k_x >= 0 and k_x <= 7 and k_y >=0 and k_y <= 7:
                    if self.game[k_y][k_x][0] != '0':
                        if self.game[k_y][k_x][1] != self.game[y][x][1]:
                            self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                         (k_y + 1) * 50 + 200, fill='#FA8072')
                            break
                        else:
                            break
                    else:
                        self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                     (k_y + 1) * 50 + 200, fill='#98FB98')

        if self.game[y][x][0] == 'Kr':
            dx = [-1, -1, -1, 0, 0, 1, 1, 1]
            dy = [-1, 0, 1, -1, 1, -1, 0, 1]
            for i in range(8):
                k_x = dx[i] + x
                k_y = dy[i] + y
                if k_x >= 0 and k_x <= 7 and k_y >= 0 and k_y <= 7:
                    if self.game[k_y][k_x][1] == 'noooo':
                        self.game[k_y][k_x][1] = self.game[y][x][1]
                        if self.clear(k_x, k_y) == 0:
                            self.canvas.create_rectangle(k_x * 50 + 50, k_y * 50 + 200, (k_x + 1) * 50 + 50,
                                                         (k_y + 1) * 50 + 200, fill='#98FB98')
                        self.game[k_y][k_x][1] = 'noooo'

        self.desk()







app = Cheese()
