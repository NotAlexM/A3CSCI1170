import turtle, random, time, math

screenX = 1200
screenY = 700
mywindow = turtle.Screen()
mywindow.setup(screenX, screenY)
mywindow.bgcolor('green')
mywindow.title('Turtle Tower Tefense Twenty Twenty Two')
# --------------------------border turtle for testing------------------
borderMaker = turtle.Turtle()
borderMaker.speed(0)
borderMaker.penup()
borderMaker.hideturtle()
borderMaker.goto(9999, 9999)
borderMaker.pencolor('black')


def drawTestBorder():
 borderMaker.goto((screenX / 2), (screenY / 2))
 borderMaker.pendown()
 borderMaker.goto((screenX / 2), -(screenY / 2))
 borderMaker.goto(-(screenX / 2), -(screenY / 2))
 borderMaker.goto(-(screenX / 2), (screenY / 2))
 borderMaker.goto((screenX / 2), (screenY / 2))
 borderMaker.penup()
 borderMaker.goto(9999, 9999)
 return
drawTestBorder()
# ---------------------------random turtles i need-------------------------

pathMaker = turtle.Turtle()
pathMaker.penup()
pathMaker.pensize(5)
pathMaker.shape('circle')
pathMaker.pencolor('orange')
pathMaker.speed(0)
pathMaker.turtlesize(1.2, 1.2)

ranger = turtle.Turtle()
ranger.penup()
ranger.speed(0)
ranger.goto(-screenX/2 - 100,-screenY/2)
ranger.shape('circle')
ranger.color('grey')

rounder = turtle.Turtle()
rounder.penup()
rounder.speed(0)
rounder.goto(screenX/2-50,-150)
rounder.shape('triangle')
rounder.turtlesize(1.5)

banker = turtle.Turtle()
banker.penup()
banker.speed(0)
banker.goto(1000,1000)
banker.hideturtle()

healther = turtle.Turtle()
healther.penup()
healther.speed(0)
healther.goto(1000,1000)
healther.hideturtle()

shower = turtle.Turtle()
shower.penup()
shower.speed(0)
shower.goto(1000,1000)
shower.hideturtle()

grader = turtle.Turtle()
grader.penup()
grader.speed(0)
grader.goto(1000,-1000)
grader.turtlesize(2,5)
grader.shape('square')

seller = turtle.Turtle()
seller.penup()
seller.speed(0)
seller.goto(1000,-1000)
seller.turtlesize(2,3)
seller.shape('square')

w = turtle.Turtle()
w.penup()
w.hideturtle()
w.speed(0)
w.pencolor('black')
w.pensize(screenY/4)

winner = turtle.Turtle()
winner.penup()
winner.hideturtle()
winner.speed(0)
winner.pencolor('black')
winner.pensize(screenY/4)
winner.goto(1000,1000)



# speeder = turtle.Turtle()
# speeder.penup()
# speeder.speed(0)
# speeder.goto(screenX/2-100,-150)
# speeder.shape('triangle')
# speeder.turtlesize(1.5)
#
# speeder2 = turtle.Turtle()
# speeder2.penup()
# speeder2.speed(0)
# speeder2.goto(screenX/2-120,-150)
# speeder2.shape('triangle')
# speeder2.turtlesize(1.5)


# -----------------------functions-----------------------------------------
def generatePathPoint():
 global pointIndex
 pointIndex = pointIndex + 1
 pointList.append(turtle.Turtle())
 pointList[pointIndex].speed(0)
 pointList[pointIndex].penup()
 pointList[pointIndex].shape('circle')
 pointList[pointIndex].turtlesize(1, 1)
 # pointList[pointIndex].hideturtle()
 pointList[pointIndex].goto((-screenX / 2) - 100, (screenY / 2))
 return

def spawnEnemy():
 global enemyIndex
 enemyIndex = enemyIndex + 1
 enemyList.append(turtle.Turtle())
 enemySpeeds.append(1)
 enemyLocation.append(0)
 enemyHealths.append(1)
 enemyFrozen.append(0)
 enemyList[enemyIndex].speed(0)
 enemyList[enemyIndex].penup()
 enemyList[enemyIndex].shape('circle')
 enemyList[enemyIndex].turtlesize(1, 1)
 # pointList[pointIndex].hideturtle()
 enemyList[enemyIndex].goto(10000,10000)
 return

def showShop():
 w.clear()
 w.color('white')
 w.goto(-screenX / 2, -screenY / 4 - 100)
 w.pendown()
 w.goto(screenX / 2, -screenY / 4 - 100)
 w.penup()
 w.pencolor('black')
 for i in range(len(shopList)):
     shopList[i].goto((-450)+ 220*(i),-250)
     w.goto((-450)+ 220*(i),-300)
     w.write(monkeyNames[i], align='center', font=('Arial', 20))
 mywindow.update()
 return

def whereClick(x,y):
 print(x,y)
 dist = 99999
 selected = 'none'
 for i in range(len(monkeyList)):
     if activeMonkeys[i] == 1:
         if monkeyList[i].distance(x,y) < dist:
             dist = monkeyList[i].distance(x,y)
             selected = i
 if selected != 'none' and dist <= 20:
     showUpgrade(selected)
 elif y > -190:
     showShop()
     ranger.goto(-screenX / 2 - 100, -screenY / 2)
     ranger.turtlesize(1)
     grader.goto(1000,-1000)
     seller.goto(1000,-1000)
     seller.clear()
 for i in range(len(projectileList)):
     if projectileList[i].distance(x,y) < 20:
         moneyCollect(i)
 mywindow.update()
 return

def showUpgrade(index):
 global upgradingMonkey
 upgradingMonkey = index
 ranger.turtlesize(monkeyRanges[index] / 10)
 ranger.goto(monkeyList[index].pos())
 seller.clear()
 w.clear()
 w.color('white')
 w.goto(-screenX / 2, -screenY / 4 - 100)
 w.pendown()
 w.goto(screenX / 2, -screenY / 4 - 100)
 w.penup()
 w.pencolor('black')
 for i in range(len(shopList)):
     shopList[i].goto(-screenX/2 - 200, -screenY/2)
     w.goto((-450)+ 220*(i),-300)
     if i <= monkeyUpgrade[index] - 1:
         w.color('green')
     else:
         w.color('red')
     w.write(upgradeTexts[monkeyTypes[index] - 1][i], align='center', font=('Arial', 20))
     w.setheading(240)
     w.forward(40)
     w.write(upgradePrices[monkeyTypes[index] - 1][i], align='center', font=('Arial', 20))
 if monkeyUpgrade[index] <= 4:
     grader.color('green')
 else:
     grader.color('red')
 grader.goto(0,-screenY/4 - 50)
 seller.color('orange')
 seller.pencolor('black')
 seller.goto(-screenX / 2 + 40, -screenY / 4 - 100)
 seller.write('sell', align='center', font=('Arial', 20))
 seller.goto(-screenX / 2 + 40, -screenY / 4 - 50)
 w.goto(grader.xcor(),grader.ycor() - 45)
 w.color('black')
 w.write('upgrade', align='center', font=('Arial', 15))
 mywindow.update()
 return

def sellMonkey(x,y):
   global upgradingMonkey, money
   money = money + monkeyPrices[monkeyTypes[upgradingMonkey] - 1] // 2
   projectileList[upgradingMonkey].clear()
   projectileList[upgradingMonkey].speed(0)
   projectileList[upgradingMonkey].penup()
   projectileList[upgradingMonkey].shape('circle')
   projectileList[upgradingMonkey].turtlesize(1, 1)
   projectileList[upgradingMonkey].goto((-screenX / 2) - 100, (screenY / 2) - 300)
   activeMonkeys[upgradingMonkey] = 0
   monkeyTypes[upgradingMonkey] = 0
   monkeyRanges[upgradingMonkey] = 0
   monkeyDamages[upgradingMonkey] = 0
   monkeyAttackSpd[upgradingMonkey] = 0
   monkeyUpgrade[upgradingMonkey] = 0
   monkeyCooldown[upgradingMonkey] = 0
   monkeyEarnings[upgradingMonkey] = 3
   lavaHealth[upgradingMonkey] = 0
   lavaDamage[upgradingMonkey] = 0
   monkeyReload[upgradingMonkey] = False
   monkeyList[upgradingMonkey].speed(0)
   monkeyList[upgradingMonkey].penup()
   monkeyList[upgradingMonkey].shape('turtle')
   monkeyList[upgradingMonkey].turtlesize(1.5, 1.5)
   # pointList[upgradingMonkey].hideturtle()
   monkeyList[upgradingMonkey].goto((-screenX / 2) - 100, (screenY / 2) - 200)
   showShop()
   ranger.goto(-screenX / 2 - 100, -screenY / 2)
   ranger.turtlesize(1)
   grader.goto(1000, -1000)
   seller.goto(1000, -1000)
   seller.clear()
   showShop()
   showMoney()
   mywindow.update()
   return

def upgradeMonkey(x,y):
 global upgradingMonkey,money
 if monkeyUpgrade[upgradingMonkey] < 5 and upgradePrices[monkeyTypes[upgradingMonkey] - 1][monkeyUpgrade[upgradingMonkey]] <= money:
     print(upgradePrices[monkeyTypes[upgradingMonkey] - 1][monkeyUpgrade[upgradingMonkey]])
     money = money - upgradePrices[monkeyTypes[upgradingMonkey] - 1][monkeyUpgrade[upgradingMonkey]]
     monkeyUpgrade[upgradingMonkey] = monkeyUpgrade[upgradingMonkey] + 1
 showMoney()
 evaluateUpgrade()
 showUpgrade(upgradingMonkey)
 return

def evaluateUpgrade(): #imma leave comments here so i dont forget
 global upgradingMonkey
 if monkeyTypes[upgradingMonkey] == 1: #gun monkey
     if monkeyUpgrade[upgradingMonkey] == 2: #faster
         monkeyAttackSpd[upgradingMonkey] = 0.5
     if monkeyUpgrade[upgradingMonkey] == 3: #bigger range
         monkeyRanges[upgradingMonkey] = 100
         monkeyDamages[upgradingMonkey] = 2
     if monkeyUpgrade[upgradingMonkey] == 4: #even faster
         monkeyAttackSpd[upgradingMonkey] = 0.2
     if monkeyUpgrade[upgradingMonkey] == 5: # huge range
         monkeyRanges[upgradingMonkey] = 200
         monkeyDamages[upgradingMonkey] == 3
 if monkeyTypes[upgradingMonkey] == 2: #ice monkey
     # if monkeyUpgrade[upgradingMonkey] == 2: #freeze attack
     #     monkeyAttackSpd[upgradingMonkey] = 0.5
     if monkeyUpgrade[upgradingMonkey] == 3: #bigger range
         monkeyRanges[upgradingMonkey] = 100
     # if monkeyUpgrade[upgradingMonkey] == 4: #even freezier
     #     monkeyAttackSpd[upgradingMonkey] = 0.2
     if monkeyUpgrade[upgradingMonkey] == 5: # faster attack range
         monkeyAttackSpd[upgradingMonkey] = 0.5
 if monkeyTypes[upgradingMonkey] == 3: #lava monkey
     if monkeyUpgrade[upgradingMonkey] == 2: #hotter lava stronger too
         lavaHealth[upgradingMonkey] = 10
         monkeyDamages[upgradingMonkey] = 2
     if monkeyUpgrade[upgradingMonkey] == 3: #double money
         monkeyEarnings[upgradingMonkey] = 6
     if monkeyUpgrade[upgradingMonkey] == 4: #even freezier
         monkeyAttackSpd[upgradingMonkey] = 1.5
     if monkeyUpgrade[upgradingMonkey] == 5: # faster attack range
         monkeyDamages[upgradingMonkey] = 7
         lavaHealth[upgradingMonkey] = 20
 if monkeyTypes[upgradingMonkey] == 4:  # money monkey
     if monkeyUpgrade[upgradingMonkey] == 2: # mo moola
         monkeyDamages[upgradingMonkey] = 50
     if monkeyUpgrade[upgradingMonkey] == 3: # fasta moola
         monkeyAttackSpd[upgradingMonkey] = 7
     if monkeyUpgrade[upgradingMonkey] == 5: # even mo moola
         monkeyDamages[upgradingMonkey] = 100
 if monkeyTypes[upgradingMonkey] == 5:  # supa monkey
     if monkeyUpgrade[upgradingMonkey] == 2: # supa range
         monkeyRanges[upgradingMonkey] = 200
     if monkeyUpgrade[upgradingMonkey] == 3: # supa speed
         monkeyAttackSpd[upgradingMonkey] = 0.1
     if monkeyUpgrade[upgradingMonkey] == 3: # supa damage
         monkeyDamages[upgradingMonkey] = 2
     if monkeyUpgrade[upgradingMonkey] == 5: # supa dupa damage
         monkeyDamages[upgradingMonkey] = 4
 return

def shopFirstTimeSetup():
 global shopIndex
 for i in range(5):
     shopIndex = shopIndex + 1
     shopList.append(turtle.Turtle())
     shopList[shopIndex].speed(0)
     shopList[shopIndex].penup()
     shopList[shopIndex].shape('turtle')
     shopList[shopIndex].turtlesize(2, 2)
     # shopList[pointIndex].hideturtle()
     shopList[shopIndex].goto((-screenX / 2) - 100, (screenY / 2) - 300)
 return

def spawnMonkey():
 global monkeyIndex, projectileIndex, matthewIndex
 projectileIndex = projectileIndex + 1
 projectileList.append(turtle.Turtle())
 projectileList[projectileIndex].speed(0)
 projectileList[projectileIndex].penup()
 projectileList[projectileIndex].shape('circle')
 projectileList[projectileIndex].turtlesize(1, 1)
 projectileList[projectileIndex].goto((-screenX / 2) - 100, (screenY / 2) - 300)
 monkeyIndex = monkeyIndex + 1
 monkeyList.append(turtle.Turtle())
 activeMonkeys.append(0)
 monkeyTypes.append(0)
 monkeyRanges.append(0)
 monkeyDamages.append(0)
 monkeyAttackSpd.append(0)
 monkeyUpgrade.append(0)
 monkeyCooldown.append(0)
 monkeyEarnings.append(3)
 lavaHealth.append(0)
 lavaDamage.append(0)
 monkeyReload.append(False)
 monkeyList[monkeyIndex].speed(0)
 monkeyList[monkeyIndex].penup()
 monkeyList[monkeyIndex].shape('turtle')
 monkeyList[monkeyIndex].turtlesize(1.5, 1.5)
 # pointList[pointIndex].hideturtle()
 monkeyList[monkeyIndex].goto((-screenX / 2) - 100, (screenY / 2) - 200)
 # matthewIndex = matthewIndex + 1
 # matthewList.append(turtle.Turtle())
 # matthewList[monkeyIndex].speed(0)
 # matthewList[monkeyIndex].penup()
 # matthewList[monkeyIndex].hideturtle()
 return

def enemyMaker(round):
 for i in range(len(enemyList)):
     enemyHealths[i] = round[i]
 return

def idleEnemies():
 for i in range(len(enemyList)):
     enemyList[i].color('black')
     enemyHealths[i] = 1
     enemySpeeds[i] = 1
     mywindow.update()
 return

def monkeyDefend():
 global movingList
 for i in range(len(monkeyList)):
     if activeMonkeys[i] == 1 and monkeyTypes[i] == 1:
         gunMonkey(i)
     if activeMonkeys[i] == 1 and monkeyTypes[i] == 2:
         iceMonkey(i)
     if activeMonkeys[i] == 1 and monkeyTypes[i] == 3:
         lavaMonkey(i)
     if activeMonkeys[i] == 1 and monkeyTypes[i] == 4:
         moneyMonkey(i)
     if activeMonkeys[i] == 1 and monkeyTypes[i] == 5:
         gunMonkey(i)
 return

def gunMonkey(i): #(and supa monkey)
 global movingList,money
 dist = 9999
 coolDown = monkeyAttackSpd[i]
 if len(movingList) > 0:
     for j in range(len(movingList)):
         if monkeyList[i].distance(enemyList[j].xcor(), enemyList[j].ycor()) < dist:
             target = j
             dist = monkeyList[i].distance(enemyList[j].xcor(), enemyList[j].ycor())
     if dist < monkeyRanges[i]:
         monkeyList[i].setheading(monkeyList[i].towards(enemyList[target].xcor(), enemyList[target].ycor()))
     if monkeyReload[i] == True and dist < monkeyRanges[i]:
         projectileList[i].pensize(1)
         projectileList[i].color('black')
         projectileList[i].pencolor('orange')
         projectileList[i].turtlesize(0.5)
         if monkeyUpgrade[i] >= 5:
             projectileList[i].pencolor('purple')
             projectileList[i].pensize(5)
         if monkeyTypes[i] == 5:
             projectileList[i].color('purple')
             projectileList[i].pencolor('blue')
             projectileList[i].pensize(10)
             if monkeyUpgrade[i] >= 5:
                 projectileList[i].color('blue')
                 projectileList[i].pencolor('black')
                 projectileList[i].pensize(20)
                 projectileList[i].turtlesize(3)
         projectileList[i].goto(monkeyList[i].pos())
         projectileList[i].pendown()
         projectileList[i].goto(enemyList[target].xcor(), enemyList[target].ycor())
         projectileList[i].penup()
         monkeyReload[i] = False
         monkeyCooldown[i] = time.time()
         if enemyHealths[target] > 0:
             enemyHealths[target] = enemyHealths[target] - monkeyDamages[i]
             money = money + monkeyEarnings[i] * monkeyDamages[i]
     else:
         if time.time() - monkeyCooldown[i] >= monkeyAttackSpd[i]:
             monkeyReload[i] = True
     if time.time() - monkeyCooldown[i] >= monkeyAttackSpd[i]/4:
         projectileList[i].goto((-screenX / 2) - 100, (screenY / 2) - 300)
         projectileList[i].turtlesize(1)
         projectileList[i].color('black')
         projectileList[i].clear()
 return

def iceMonkey(i):
 global movingList, money,monkeyUpgrade, enemyFrozen
 coolDown = monkeyAttackSpd[i]
 freeze = []
 if len(movingList) > 0:
     for j in range(len(movingList)):
         if enemyList[j].distance(monkeyList[i].xcor(), monkeyList[i].ycor()) < monkeyRanges[i]:
             freeze.append(j)
     if len(freeze) > 0:
         if monkeyReload[i] == True:
             monkeyReload[i] = False
             projectileList[i].turtlesize(monkeyRanges[i]/10)
             projectileList[i].color('blue')
             projectileList[i].goto(monkeyList[i].pos())
             monkeyCooldown[i] = time.time()
             for j in range(len(movingList)):
                 if j in freeze and enemyHealths[j] > 0:
                     enemyHealths[j] = enemyHealths[j] - monkeyDamages[i]
                     if monkeyUpgrade[i] >= 4:
                         enemyFrozen[j] = 2
                     elif monkeyUpgrade[i] >= 2 and enemyFrozen[j] !=2:
                         enemyFrozen[j] = 1
             for j in range(len(freeze)):
                 money = money + monkeyEarnings[i] * monkeyDamages[i]
     if time.time() - monkeyCooldown[i] >= monkeyAttackSpd[i]/2:
         projectileList[i].goto((-screenX / 2) - 100, (screenY / 2) - 300)
         projectileList[i].turtlesize(1)
         projectileList[i].color('black')
     if time.time() - monkeyCooldown[i] >= monkeyAttackSpd[i]:
         monkeyReload[i] = True
 return

def lavaMonkey(i):
 global movingList,money
 coolDown = monkeyAttackSpd[i]
 dist = 9999
 if len(movingList) > 0:
     for j in range(len(movingList)):
         if monkeyList[i].distance(enemyList[j].xcor(), enemyList[j].ycor()) < dist:
             target = j
             dist = monkeyList[i].distance(enemyList[j].xcor(), enemyList[j].ycor())
     if dist < monkeyRanges[i] and monkeyReload[i] == True:
         monkeyList[i].setheading(monkeyList[i].towards(enemyList[target].xcor(), enemyList[target].ycor()))
     if monkeyReload[i] == True and dist < monkeyRanges[i]:
         projectileList[i].goto(enemyList[target].xcor(), enemyList[target].ycor())
         projectileList[i].penup()
         projectileList[i].turtlesize(1.5)
         projectileList[i].color('orange')
         monkeyReload[i] = False
     for j in range(len(movingList)):
         if enemyList[j].distance(projectileList[i].pos()) <= 15:
             if lavaDamage[i] < lavaHealth[i]:
                 print(monkeyDamages[i])
                 enemyHealths[j] = enemyHealths[j] - monkeyDamages[i]
                 money = money + monkeyEarnings[i] * monkeyDamages[i]
                 lavaDamage[i] = lavaDamage[i] + 1
     if lavaDamage[i] == lavaHealth[i]:
         monkeyCooldown[i] = time.time()
         projectileList[i].goto((-screenX / 2) - 100, (screenY / 2) - 300)
         projectileList[i].turtlesize(1)
         projectileList[i].color('black')
         projectileList[i].clear()
         lavaDamage[i] = 0
     if monkeyReload[i] == False and lavaDamage[i] == 0:
         if time.time() - monkeyCooldown[i] >= monkeyAttackSpd[i]:
             monkeyReload[i] = True
 return

def moneyMonkey(i):
 global movingList, money
 if monkeyReload[i] == True:
     if projectileList[i].distance(monkeyList[i].pos()) > 10:
         projectileList[i].goto(monkeyList[i].pos())
         projectileList[i].color('dark green')
         projectileList[i].turtlesize(2)
         mywindow.update()
     if monkeyUpgrade[i] >= 4:
         moneyCollect(i)
 if monkeyReload[i] == False:
     monkeyList[i].left(1)
     if time.time() - monkeyCooldown[i] >= monkeyAttackSpd[i]:
         monkeyReload[i] = True
 return

def moneyCollect(i):
 global money
 if monkeyReload[i] == True:
     monkeyCooldown[i] = time.time()
     projectileList[i].goto((-screenX / 2) - 100, (screenY / 2) - 300)
     projectileList[i].turtlesize(1)
     projectileList[i].color('black')
     projectileList[i].clear()
     money = money + monkeyDamages[i]
     monkeyReload[i] = False
 return

def rounded(x,y):
   global currentRound,money
   rounder.turtlesize(2)
   mywindow.update()
   time.sleep(0.01)
   mywindow.update()
   if playing == False:
       rounder.turtlesize(1.5)
       currentRound = currentRound + 1
       healthPool()
       print(roundList[currentRound])
       showRound()
       runRound(roundList[currentRound])
       money = money + roundEarnings[currentRound]
   if health <= 0:
       lose()
   if currentRound == 39:
       win()
   showMoney()
   mywindow.update()
   return

def win():
   winner.goto(0,0)
   winner.write('YOU WIN', align='center', font=('Arial', 100))
   time.sleep(1000000)
   return

def lose():
   winner.goto(0, 0)
   winner.write('HAHA LOSER', align='center', font=('Arial', 100))
   time.sleep(1000000)
   return

def healthPool():
   global currentRound
   multiplyer = currentRound
   if currentRound < 10:
       for i in range(10 * multiplyer):
           indexer = random.randint(0,29)
           roundList[currentRound][indexer] = roundList[currentRound][indexer] + 1
   elif currentRound < 20:
       for i in range(25 * multiplyer):
           indexer = random.randint(0,29)
           roundList[currentRound][indexer] = roundList[currentRound][indexer] + 1
   elif currentRound < 29:
       for i in range(50 * multiplyer):
           indexer = random.randint(0,29)
           roundList[currentRound][indexer] = roundList[currentRound][indexer] + 1
   elif currentRound < 34:
       for i in range(100 * multiplyer):
           indexer = random.randint(0,29)
           roundList[currentRound][indexer] = roundList[currentRound][indexer] + 1
   elif currentRound < 38:
       for i in range(200 * multiplyer):
           indexer = random.randint(0,29)
           roundList[currentRound][indexer] = roundList[currentRound][indexer] + 1
   else:
       for i in range(300 * multiplyer):
           indexer = random.randint(0,29)
           roundList[currentRound][indexer] = roundList[currentRound][indexer] + 1
   return

def matthew():
   for i in range(len(enemyList)):
       matthewList[i].clear()
       matthewList[i].goto(enemyList[i].pos())
       matthewList[i].setheading(270)
       matthewList[i].forward(10)
       matthewList[i].write(enemyHealths[i], align='center', font=('Arial', 10))
   return

def runRound(round):
 global spawnTime, spawnTick,movingList,playing,enemyFrozen
 playing = True
 enemyMaker(round)
 movingList = []
 played = 0
 tickCount = 0
 spawnTick = 50
 enemyFrozen = []
 rounder.color('white')
 for i in range(len(enemyList)):
     enemyFrozen.append(0)
 while len(deadEnemies) <= len(enemyList) - 1:
     time.sleep(0.00001)
     tickCount = tickCount + 1
     if len(movingList) == len(enemyList):
         doneCheck = 0
         for i in range(len(movingList)):
             if movingList[i] == 'done':
                 doneCheck = doneCheck + 1
             elif movingList[i] == 'dead':
                 doneCheck = doneCheck + 1
         if doneCheck == len(movingList):
             for i in range(len(movingList)):
                 enemyLocation[i] = 0
             idleEnemies()
             playing = False
             updatePlayerHealth()
             rounder.color('black')
             for k in range(len(projectileList)):
                 if monkeyTypes[k] != 3 and monkeyTypes[k] != 4:
                     projectileList[k].goto((-screenX / 2) - 100, (screenY / 2) - 300)
                     projectileList[k].turtlesize(1)
                     projectileList[k].color('black')
                     projectileList[k].clear()
             mywindow.update()
             return
     if tickCount == spawnTick and len(movingList) != len(enemyList):
         enemyList[played].goto(pointList[0].xcor(), pointList[0].ycor())
         # enemyList[played].goto(0,0)
         downTime = time.time()
         enemyLocation[played] = 0
         movingList.append(played)
         played = played + 1
         mywindow.update()
         tickCount = 0
     if len(movingList) > 0:
         for i in range(len(movingList)):
             # enemyList[i].setheading(90)
             # if enemyLocation[i] == len(pointList):
             if enemyLocation[i] != len(pointList) - 1:
                 if enemyList[i].distance((pointList[enemyLocation[i] + 1]).xcor(),
                                          (pointList[enemyLocation[i] + 1]).ycor()) > enemySpeeds[i] + 1 and enemyLocation[i] != len(pointList) and i in movingList:
                     enemyList[i].setheading((enemyList[i].towards((pointList[enemyLocation[i] + 1]).xcor(),
                                                                   (pointList[enemyLocation[i] + 1]).ycor())))
                     # print(((pointList[enemyLocation[i]+1]).xcor(),(pointList[enemyLocation[i]+1]).ycor()))
                     if enemyFrozen[i] == 1:
                         enemyList[i].forward(((enemySpeeds[i]) / 4)* 3)
                     elif enemyFrozen[i] == 2:
                         enemyList[i].forward(((enemySpeeds[i]) / 2)*1)
                     else:
                         enemyList[i].forward(enemySpeeds[i])
                 else:
                     enemyLocation[i] = enemyLocation[i] + 1
             else:
                 movingList[i] = 'done'
                 enemyList[i].goto(10000,10000)
             # print(movingList)
         monkeyDefend()
         if len(movingList) > 0:
             for i in range(len(movingList)):
                 if enemyHealths[i] <= 0:
                     movingList[i] = 'dead'
                     enemyList[i].goto(10000,10000)
         # matthew()
         healthCheck()
         showMoney()
         showHealth()
         #print(movingList)
         mywindow.update()
 return

def updatePlayerHealth():
 global health, movingList
 for i in range(len(movingList)):
     if movingList[i] == 'done':
         health = health - 1
 showHealth()
 mywindow.update()
 return


def healthCheck():
 for i in range(len(enemyList)):
     if enemyHealths[i] >= 201:
         enemyList[i].color('purple')
         enemySpeeds[i] = 0.5
         enemyList[i].turtlesize(6,7)
     elif enemyHealths[i] >= 101:
         enemyList[i].color('black')
         enemySpeeds[i] = 0.5
         enemyList[i].turtlesize(5,6)
     elif enemyHealths[i] >= 51:
         enemyList[i].color('dark red')
         enemySpeeds[i] = 2
         enemyList[i].turtlesize(4,5)
     elif enemyHealths[i] >= 21:
         enemyList[i].color('light blue')
         enemySpeeds[i] = 4
         enemyList[i].turtlesize(3,4)
     elif enemyHealths[i] >= 11:
         enemyList[i].color('brown')
         enemySpeeds[i] = 3.5
         enemyList[i].turtlesize(1.2)
     elif enemyHealths[i] >= 7:
         enemyList[i].color('black')
         enemySpeeds[i] = 3.5
         enemyList[i].turtlesize(1)
     elif enemyHealths[i] >= 6:
         enemyList[i].color('purple')
         enemySpeeds[i] = 4
         enemyList[i].turtlesize(1)
     elif enemyHealths[i] >= 5:
         enemyList[i].color('pink')
         enemySpeeds[i] = 3
         enemyList[i].turtlesize(1)
     elif enemyHealths[i] >= 4:
         enemyList[i].color('yellow')
         enemySpeeds[i] = 2.5
         enemyList[i].turtlesize(1)
     elif enemyHealths[i] >= 3:
         enemyList[i].color('dark green')
         enemySpeeds[i] = 2
         enemyList[i].turtlesize(1)
     elif enemyHealths[i] >= 2:
         enemyList[i].color('blue')
         enemySpeeds[i] = 1.5
         enemyList[i].turtlesize(1)
     elif enemyHealths[i] >= 1:
         enemyList[i].color('red')
         enemySpeeds[i] = 1
         enemyList[i].turtlesize(1)
 return
#lol

#lol

def monkeyDrag(x,y):
 global clicked, refreshDrag,playing
 dist = 1000000
 for i in range(len(shopList)):
     if shopList[i].distance(x, y) < dist:
         dist = shopList[i].distance(x, y)
         clicked = i
 for i in range(len(shopList)):
     if i != clicked:
         shopList[i].goto(-screenX/2 - 200, -screenY/2)
         w.goto((-450)+ 220*(i),-300)
 refreshDrag = refreshDrag + 1
 shopList[clicked].goto(x,y)
 ranger.turtlesize(defaultRanges[clicked]/10)
 ranger.goto(x,y)
 if playing == False and refreshDrag > 5:
     refreshDrag = 0
     mywindow.update()
 if playing == True and refreshDrag > 100:
     refreshDrag = 0
     mywindow.update()
 return

def monkeyPlace(x,y):
 global clicked, refreshDrag
 for i in range(len(shopList)):
     shopList[i].goto((-450) + 220 * (i), -250)
 counter = 0
 if 0 in activeMonkeys:
     summonMonkey(clicked,x,y)
 mywindow.update()
 return

def summonMonkey(typeIndex,x,y):
 global money
 if monkeyPrices[typeIndex] <= money and y > -170:
     i = -1
     found = False
     while found == False:
         i = i + 1
         if activeMonkeys[i] == 0:
             found = True
     activeMonkeys[i] = 1
     monkeyList[i].goto(x,y)
     print(typeIndex)
     monkeyTypeCheck(typeIndex + 1,i)
     monkeyTypes[i] = typeIndex + 1
     money = money - monkeyPrices[typeIndex]
 ranger.goto(-screenX / 2 - 100, -screenY / 2)
 ranger.turtlesize(1)
 showMoney()
 mywindow.update()
 return

def monkeyTypeCheck(typeMonkey,index):
 if typeMonkey == 1:
     monkeyList[index].color('dark green')
     monkeyRanges[index] = 50
     monkeyAttackSpd[index] = 1
     monkeyDamages[index] = 1
     monkeyUpgrade[index] = 1
     monkeyReload[index] = True
     projectileList[index].turtlesize(0.5)
 if typeMonkey == 2:
     monkeyList[index].color('light blue')
     monkeyRanges[index] = 50
     monkeyAttackSpd[index] = 1.5
     monkeyDamages[index] = 1
     monkeyUpgrade[index] = 1
     monkeyReload[index] = True
     projectileList[index].turtlesize(0.5)
 if typeMonkey == 3:
     monkeyList[index].color('red')
     monkeyRanges[index] = 50
     monkeyAttackSpd[index] = 2
     monkeyDamages[index] = 1
     monkeyUpgrade[index] = 1
     monkeyReload[index] = True
     projectileList[index].turtlesize(0.5)
     lavaHealth[index] = 5
 if typeMonkey == 4:
     monkeyList[index].color('yellow')
     monkeyRanges[index] = 20
     monkeyAttackSpd[index] = 10
     monkeyDamages[index] = 25
     monkeyUpgrade[index] = 1
     monkeyReload[index] = True
     projectileList[index].turtlesize(0.5)
 if typeMonkey == 5:
     monkeyList[index].color('purple')
     monkeyRanges[index] = 100
     monkeyAttackSpd[index] = 0.25
     monkeyDamages[index] = 1
     monkeyUpgrade[index] = 1
     monkeyReload[index] = True
     projectileList[index].turtlesize(0.5)
 return

def showMoney():
 global money
 banker.goto(screenX/2 - 70, screenY/2 - 50)
 banker.clear()
 banker.write(money, align='center', font=('Arial', 20))
 banker.goto(screenX / 2 - 15, screenY / 2 - 50)
 banker.write('$', align='center', font=('Arial', 20))
 return

def showHealth():
 global health
 healther.goto(-screenX/2 + 110, screenY/2 - 50)
 healther.clear()
 healther.write(health, align='center', font=('Arial', 20))
 healther.goto(-screenX / 2 + 50, screenY / 2 - 50)
 healther.write('Health:', align='center', font=('Arial', 20))
 return

def showRound():
 global health
 shower.goto(-screenX/2 + 110, screenY/2 - 100)
 shower.clear()
 shower.write(currentRound + 1, align='center', font=('Arial', 20))
 shower.goto(-screenX / 2 + 50, screenY / 2 - 100)
 shower.write('Round:', align='center', font=('Arial', 20))
 return

# def speeded(x,y):
#     global gameSpeed
#     if gameSpeed == 'normal':
#         speeder.color('grey')
#         speeder2.color('grey')
#         gameSpeed = 'fast as frick boiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'
#         for i in range(len(monkeyList)):
#
#
#     else:
#         speeder.color('black')
#         speeder2.color('black')
#         gameSpeed = 'normal'
#     mywindow.update()
#     return
# ----------------------------variables setup---------------------------
pointIndex = -1
pointList = []
enemyIndex = -1
enemyList = []
monkeyIndex = -1
monkeyList = []
shopIndex = -1
shopList = []
projectileIndex = -1
projectileList = []
matthewIndex = -1
matthewList = []
spawnTime = 0.5
deadEnemies = []
enemySpeeds = []
enemyLocation = []
mywindow.tracer(0, 0)
spawnTick = 10
enemyHealths = []
monkeyTypes = []
activeMonkeys = []
monkeyRanges = []
monkeyDamages = []
monkeyAttackSpd = []
monkeyUpgrade = []
monkeyCooldown = []
monkeyReload =[]
movingList = []
refreshDrag = 0
monkeyNames = ['gun turtle 200$', 'ice turtle 300$','lava turtle 400$','money turtle 500$','supaturtle1000$']
clicked = 'lol'
currentRound = -1
playing = False
money = 650
monkeyPrices = [200,300,400,500,1000]
monkeyEarnings = []
roundEarnings = [100,100,100,100,100,150,150,150,150,150,200,200,200,200,200,250,250,250,250,250,300,300,300,300,300,350,350,350,350,350,400,400,400,400,400,450,450,450,450,450]
health = 10
upgradeTexts = [['default','faster','turtle training','supa fast','super gunner'],['default','ball slower','bigger range','even slower balls','faster attack'],['default','better lava','more money','faster cooldown','even BETTER lava'],['default (click for money)','mo moola','fasta moola','autocollect','even mo moola'],['default','supa range','supa speed','supa damage','supa dupa damage']]
upgradePrices = [[200,100,200,500,1000],[300,250,300,300,700],[400,450,1000,350,2000],[400,450,400,650,1100],[1000,700,2000,10000,20000]]
upgradingMonkey = 'hehehehehah'
enemyFrozen = []
defaultRanges = [50,50,50,20,100]
lavaHealth = []
lavaDamage = []
# gameSpeed = 'normal'
# roundList = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1],[3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,3,4,4,4,1,1,1,1,1,4,4,1,1,1],[5,5,5,5,5,2,2,2,2,2,2,2,2,2,2,2,3,4,4,4,5,5,5,5,5,4,4,5,6,6],[5,5,5,5,5,2,2,2,2,2,2,2,2,2,2,2,3,4,4,4,5,5,5,5,5,4,4,5,6,6],[5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,3,4,4,4,5,5,5,5,5,4,4,5,6,6],[50, 400, 200, 50, 100, 50, 200, 50, 50, 50, 50, 400, 200, 50, 100, 50, 200, 50, 50, 50, 50, 400, 200, 50, 100, 50, 200, 50, 50, 50]]
roundList = []
for i in range(40):
   roundList.append([])
   for j in range(30):
       roundList[i].append(1)
print(roundList)

# ---------------------------round settings-----------------------------

# ------------------------------path setup-----------------------------
for i in range(5):
 generatePathPoint()
pointList[0].goto((-screenX / 2) , random.randint(-150,150))
pointList[1].goto((-screenX / 4) , random.randint(-150,screenY / 2))
pointList[2].goto(0, random.randint(-150,screenY / 2))
pointList[3].goto(screenX/4, random.randint(-150,screenY / 2))
pointList[4].goto(screenX/2, random.randint(-150,screenY / 2))

for i in range(len(pointList)):
 pathMaker.goto(pointList[i].xcor(), pointList[i].ycor())
 pathMaker.pendown()
 pathMaker.stamp()
 pointList[i].stamp()

# ------------------------------spawning enemies and stuff-----------------------


shopFirstTimeSetup()
shopList[0].color('dark green')
shopList[1].color('light blue')
shopList[2].color('red')
shopList[3].color('yellow')
shopList[4].color('purple')
showShop()

showMoney()
showHealth()

for i in range(30):
 spawnEnemy()




for i in range(50):
 spawnMonkey()

showRound()
showHealth()
# ----------------------------random stuff for testing---------------------------




# monkeyList[0].goto(-screenX / 2 + 150, -screenY / 2 + 50)
# monkeyTypes[0] = 1
# activeMonkeys[0] = 1
#
# monkeyList[1].goto(-screenX / 2 + 250, -screenY / 2 + 200)
# monkeyTypes[1] = 1
# activeMonkeys[1] = 1
# --------------------------------loop---------------------------------
mywindow.update()
mywindow.listen()

# runRound(roundOne)
# runRound(roundTwo)
rounder.onclick(rounded)

# speeder.onclick(speeded)
# speeder2.onclick(speeded)

shopList[0].ondrag(monkeyDrag)
shopList[1].ondrag(monkeyDrag)
shopList[2].ondrag(monkeyDrag)
shopList[3].ondrag(monkeyDrag)
shopList[4].ondrag(monkeyDrag)

shopList[0].onrelease(monkeyPlace)
shopList[1].onrelease(monkeyPlace)
shopList[2].onrelease(monkeyPlace)
shopList[3].onrelease(monkeyPlace)
shopList[4].onrelease(monkeyPlace)

grader.onclick(upgradeMonkey)
seller.onclick(sellMonkey)
mywindow.onclick(whereClick)

mywindow.mainloop()