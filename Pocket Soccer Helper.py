# coding:utf-8
import xlrd
# coding:utf-8
import pygame
import copy
import time
import re
from pygame.locals import *
from sys import exit
background_image_filename = "game_resource/images/background.png"
use_image_filename = "game_resource/images/use.png"
back_image_filename = "game_resource/images/back.png"
white_image_filename = "game_resource/images/white.png"
toughness_image_filename = "game_resource/images/toughness.png"
willpower_image_filename = "game_resource/images/willpower.png"
DF_image_filename = "game_resource/images/DF.png"
FW_image_filename = "game_resource/images/FW.png"
MF_image_filename = "game_resource/images/MF.png"
GK_image_filename = "game_resource/images/GK.png"
shadow_image_filename = "game_resource/images/shadow.png"
DF_shadow_image_filename = "game_resource/images/DF_shadow.png"
willpower_shadow_image_filename = "game_resource/images/willpower_shadow.png"
number_image_filename = "game_resource/images/number.png"
kongbai_image_filename = "game_resource/images/kongbai.png"
info_image_filename = "game_resource/images/info.png"
tips_image_filename = "game_resource/images/tips.png"
enter_image_filename="game_resource/images/enter.png"
pygame.init()
pygame.mixer.init()
click_sound = pygame.mixer.Sound('game_resources/sounds/sound.wav')
screen=pygame.display.set_mode((1000,700),0,32)
pygame.display.set_caption('Pocket Soccer Helper')
background_image = pygame.image.load(background_image_filename).convert()
white_image = pygame.image.load(white_image_filename).convert()
info_image = pygame.image.load(info_image_filename).convert()
toughness_image = pygame.image.load(toughness_image_filename).convert_alpha()
willpower_image = pygame.image.load(willpower_image_filename).convert_alpha()
DF_image = pygame.image.load(DF_image_filename).convert_alpha()
GK_image = pygame.image.load(GK_image_filename).convert_alpha()
MF_image = pygame.image.load(MF_image_filename).convert_alpha()
tips_image = pygame.image.load(tips_image_filename).convert_alpha()
enter_image = pygame.image.load(enter_image_filename).convert_alpha()
kongbai_image = pygame.image.load(kongbai_image_filename).convert_alpha()
FW_image = pygame.image.load(FW_image_filename).convert_alpha()
use_image = pygame.image.load(use_image_filename).convert_alpha()
back_image = pygame.image.load(back_image_filename).convert_alpha()
shadow_image = pygame.image.load(shadow_image_filename).convert_alpha()
DF_shadow_image = pygame.image.load(DF_shadow_image_filename).convert_alpha()
willpower_shadow_image = pygame.image.load(willpower_shadow_image_filename).convert_alpha()
number_image = pygame.image.load(number_image_filename).convert_alpha()
font = pygame.font.Font('game_resource/font.ttc',28)
data = xlrd.open_workbook('game_resource/excel.xls')
table = data.sheets()[0]#table是这个表格的第一张
table3 = data.sheets()[3]
got_list=[]
number_image_list=[]
skill_list=[u'马赛回旋',u'大力手抛球',u'任意球大师',u'队长',u'传说的任意球射手',u'香蕉球射门',u'鱼跃头球',u'攻击参加',u'倒挂金钩',u'超级远射',u'大力抽射',u'脚后跟传球',u'剪刀假动作',u'无回旋射门']
for i in range(10):
    if i <=8:
        number_image_list.append(number_image.subsurface(i*22,0,21,30))

    else:number_image_list.append(number_image.subsurface(8*22+21,0,21,30))

class Cards(pygame.sprite.Sprite):
    def __init__(self,card_num):
        pygame.sprite.Sprite.__init__(self)
        self.image=kongbai_image

        if card_num ==0:
            self.rect = Rect(25,23,102, 120)
            self.cardname=(u'录像研究',u'ビデオ研究')
        elif card_num ==1:
            self.rect = Rect(147,23,102, 120)
            self.cardname=(u'盯人防守',u'マンツーマン')
        elif card_num ==2:
            self.rect = Rect(269,23,102, 120)
            self.cardname=((u'逼抢围',u'プレス'))
        elif card_num ==3:
            self.rect = Rect(391,23,102, 120)
            self.cardname=(u'防守反击',u'カウンター')
        elif card_num ==4:
            self.rect = Rect(513,23,102, 120)
            self.cardname=(u'运球',u'ドリブル')
        elif card_num ==5:
            self.rect = Rect(635,23,102, 120)
            self.cardname=(u'定点罚球',u'プレースキック')
        elif card_num ==6:
            self.rect = Rect(757,23,102, 120)
            self.cardname=(u'射门',u'シュート')
        elif card_num ==7:
            self.rect = Rect(879,23,102, 120)
            self.cardname=(u'传球',u'パス')
        elif card_num ==8:
            self.rect = Rect(87,156,102, 120)
            self.cardname=(u'小游戏',u'ミニゲーム')

        elif card_num ==9:
            self.rect = Rect(209,157,102, 120)
            self.cardname=(u'防线控制',u'ラインコントロール')
        elif card_num ==10:
            self.rect = Rect(331,157,102, 120)
            self.cardname=(u'任意球',u'セットプレー')

        elif card_num ==11:
            self.rect = Rect(575,156,102, 120)
            self.cardname=(u'颠球训练',u'リフティング')
        elif card_num ==12:
            self.rect =Rect(697,155,102, 120)
            self.cardname=(u'铲球',u'スライディング')

        elif card_num ==13:
            self.rect =Rect(819,156,102, 120)
            self.cardname=(u'头球',u'ヘディング')
        elif card_num ==14:
            self.rect =Rect(25,431,102, 120)
            self.cardname=(u'跑步',u'ランニング')
        elif card_num ==15:
            self.rect =Rect(147,431,102, 120)
            self.cardname=(u'肌肉力量',u'ウェイト')
        elif card_num ==16:
            self.rect =Rect(269,431,102, 120)
            self.cardname=(u'腿部力量',u'キック')
        elif card_num ==17:
            self.rect =Rect(391,431,102, 120)
            self.cardname=(u'冲刺',u'ダッシュ')
        elif card_num ==18:
            self.rect =Rect(513,431,102, 120)
            self.cardname=(u'点球训练',u'PK練習')
        elif card_num ==19:
            self.rect =Rect(635,431,102, 120)
            self.cardname=(u'合气道',u'合気道')
        elif card_num ==20:
            self.rect =Rect(757,431,102, 120)
            self.cardname=(u'意念训练',u'イメトレ')
        elif card_num ==21:
            self.rect =Rect(879,431,102, 120)
            self.cardname=(u'更衣室',u'ミーティング')
        elif card_num ==22:
            self.rect =Rect(87,565,102, 120)
            self.cardname=(u'梯子训练',u'アジリティー')
        elif card_num ==23:
            self.rect =Rect(209,565,102, 120)
            self.cardname=(u'有氧运动',u'エアロビクス')
        elif card_num ==24:
            self.rect =Rect(331,565,102, 120)
            self.cardname=(u'拉伸训练',u'ストレッチ')
        elif card_num ==25:
            self.rect =Rect(513,565,102, 120)
            self.cardname=(u'温泉',u'温泉')
        elif card_num ==26:
            self.rect =Rect(635,565,102, 120)
            self.cardname=(u'迷你训练营',u'ミニキャンプ')
        elif card_num ==27:
            self.rect =Rect(757,565,102, 120)
            self.cardname=(u'欢乐足球',u'カルチョビット')
        elif card_num ==28:
            self.rect =Rect(880,565,102, 120)
            self.cardname=(u'卡拉OK',u'カラオケ')
        elif card_num ==29:
            self.rect =Rect(635,297,102, 120)
            self.cardname=(u'香薰',u'アロマテラピー')
        elif card_num ==30:
            self.rect =Rect(757,297,102, 120)
            self.cardname=(u'坐禅',u'座禅')
        elif card_num == 31:
            self.rect =Rect(879, 297, 102, 120)
            self.cardname = (u'签名会', u'サイン会')
    def updates(self):
        self.number=got_list.count(self.cardname)
        if self.number !=0 and self.number <=9:
            screen.blit(number_image_list[self.number],(self.rect.left+75,self.rect.top+82))
        elif self.number ==0:
            screen.blit(shadow_image,(self.rect.left,self.rect.top))


class Usingcards(pygame.sprite.Sprite):
    def __init__(self,position,cards_list):
        pygame.sprite.Sprite.__init__(self)
        self.image=use_image
        self.rect=Rect(position,(48,48))
        self.basic_rect=copy.copy(self.rect)
        self.cards_list=cards_list
    def usecard(self):
        global got_list

        for i in self.cards_list:
            got_list.remove(i)



        prints()
        for sort in sorts:
            if sort.selected==True:
                Fangxiang(sort.name)

class Sortway(pygame.sprite.Sprite):
    def __init__(self,whatsort):
        pygame.sprite.Sprite.__init__(self)
        if whatsort=='FW':
            self.rect =Rect(80,56,64,35)
            self.image =FW_image
            self.shadow_image = DF_shadow_image
        if whatsort=='MF':
            self.rect =Rect(233,56,64,35)
            self.image =MF_image
            self.shadow_image = DF_shadow_image
        if whatsort=='DF':
            self.rect =Rect(408,56,64,35)
            self.image =DF_image
            self.shadow_image = DF_shadow_image
        if whatsort=='GK':
            self.rect =Rect(572,56,64,35)
            self.image=GK_image
            self.shadow_image = DF_shadow_image
        if whatsort=='toughness':
            self.rect =Rect(736,42,49,49)
            self.image =toughness_image
            self.shadow_image = willpower_shadow_image
        if whatsort=='willpower':
            self.rect =Rect(885,42,49,49)
            self.image =willpower_image
            self.shadow_image = willpower_shadow_image
        self.name = whatsort
        self.selected=False
        self.basic_rect = copy.copy(self.rect)
    def updates(self):
        if self.selected==True:
            pass
        else:
            screen.blit(self.shadow_image,self.rect)



def addCard(card):
    shuru=card
    if shuru=='任意球':
        got_list.append((u'任意球',u'セットプレー'))
    elif shuru=='防守反击':
        got_list.append((u'防守反击',u'カウンター'))
    elif shuru=='盯人防守':
        got_list.append((u'盯人防守',u'マンツーマン'))
    elif shuru=='防线控制':
        got_list.append((u'防线控制',u'ラインコントロール'))
    elif shuru=='录像研究':
        got_list.append((u'录像研究',u'ビデオ研究'))
    elif shuru=='逼抢围':
        got_list.append((u'逼抢围',u'プレス'))
    elif shuru=='小游戏':
        got_list.append((u'小游戏',u'ミニゲーム'))
    #################################
    elif shuru=='传球':
        got_list.append((u'传球',u'パス'))
    elif shuru=='铲球':
        got_list.append((u'铲球',u'スライディング'))
    elif shuru=='运球':
        got_list.append((u'运球',u'ドリブル'))
    elif shuru=='头球':
        got_list.append((u'头球',u'ヘディング'))
    elif shuru=='颠球训练':
        got_list.append((u'颠球训练',u'リフティング'))
    elif shuru=='定点罚球':
        got_list.append((u'定点罚球',u'プレースキック'))
    elif shuru=='射门':
        got_list.append((u'射门',u'シュート'))
    #################################
    elif shuru == '拉伸训练':
        got_list.append((u'拉伸训练',u'ストレッチ'))
    elif shuru == '梯子训练':
        got_list.append((u'梯子训练',u'アジリティー'))
    elif shuru == '有氧运动':
        got_list.append((u'有氧运动',u'エアロビクス'))
    elif shuru == '跑步':
        got_list.append((u'跑步',u'ランニング'))
    elif shuru == '冲刺':
        got_list.append((u'冲刺',u'ダッシュ'))
    elif shuru == '肌肉力量':
        got_list.append((u'肌肉力量',u'ウェイト'))
    elif shuru == '腿部力量':
        got_list.append((u'腿部力量',u'キック'))
    #################################
    elif shuru == '合气道':
        got_list.append((u'合气道',u'合気道'))
    elif shuru == '卡拉OK':
        got_list.append((u'卡拉OK',u'カラオケ'))
    elif shuru == '签名会':
        got_list.append((u'签名会',u'サイン会'))
    elif shuru == '点球训练':
        got_list.append((u'点球训练',u'PK練習'))
    elif shuru == '欢乐足球':
        got_list.append((u'欢乐足球',u'カルチョビット'))
    elif shuru == '迷你训练营':
        got_list.append((u'迷你训练营',u'ミニキャンプ'))
    elif shuru == '意念训练':
        got_list.append((u'意念训练',u'イメトレ'))
    elif shuru == '坐禅':
        got_list.append((u'坐禅',u'座禅'))
    elif shuru == '温泉':
        got_list.append((u'温泉',u'温泉'))
    elif shuru == '更衣室':
        got_list.append((u'更衣室',u'ミーティング'))
    elif shuru == '香薰':
        got_list.append((u'香薰',u'アロマテラピー'))
    elif shuru=='结束':
        got_list.append((u'欢乐足球', u'カルチョビット'))
        got_list.append((u'迷你训练营', u'ミニキャンプ'))

        got_list.append((u'颠球训练', u'リフティング'))
        got_list.append((u'有氧运动', u'エアロビクス'))
        got_list.append((u'香薰', u'アロマテラピー'))
        got_list.append((u'意念训练', u'イメトレ'))
        got_list.append((u'合气道', u'合気道'))
        got_list.append((u'坐禅', u'座禅'))
        got_list.append((u'更衣室', u'ミーティング'))
        got_list.append((u'温泉', u'温泉'))


        got_list.append((u'卡拉OK', u'カラオケ'))

        got_list.append((u'签名会', u'サイン会'))

        got_list.append((u'点球训练', u'PK練習'))
        got_list.append((u'任意球', u'セットプレー'))
        got_list.append((u'防守反击', u'カウンター'))
        got_list.append((u'盯人防守', u'マンツーマン'))
        got_list.append((u'防线控制', u'ラインコントロール'))
        got_list.append((u'录像研究', u'ビデオ研究'))
        got_list.append((u'逼抢围', u'プレス'))
        got_list.append((u'小游戏', u'ミニゲーム'))
    #################################
        got_list.append((u'传球', u'パス'))
        got_list.append((u'铲球', u'スライディング'))
        got_list.append((u'运球', u'ドリブル'))
        got_list.append((u'头球', u'ヘディング'))

        got_list.append((u'定点罚球', u'プレースキック'))
        got_list.append((u'射门', u'シュート'))
    #################################
        got_list.append((u'拉伸训练', u'ストレッチ'))
        got_list.append((u'梯子训练', u'アジリティー'))
        got_list.append((u'有氧运动', u'エアロビクス'))
        got_list.append((u'跑步', u'ランニング'))
        got_list.append((u'冲刺', u'ダッシュ'))

        got_list.append((u'肌肉力量', u'ウェイト'))

        got_list.append((u'腿部力量', u'キック'))

        #print u'#################################'

    else:print u'输入错误，请重新输入'





def prints():
    global  find_list
    global y_max
    local_time=time.time()
    set_list=set(got_list)
    set_list=[i for i in set_list]
    uses.empty()
    find_list=[]
    y_max=0
    for a in range(133):
        got=False

        if table.row_values(a)[5] ==u'':
            b = table.row_values(a)[3]+table.row_values(a)[4]
            for q in set_list:
                if q[1] in b:
                    if q[1]==u'キック' and u'プレースキック' in b:
                        continue

                    for w in set_list:
                        if q==w:
                            continue
                        elif w[1] in b:
                            if w[1] == u'キック' and u'プレースキック' in b:
                                continue
                            print w[1]
                            print q[1]
                            print b
                            got=True
                            xiaohao1=q[0]
                            xiaohao11=q
                            xiaohao2=w[0]
                            xiaohao22=w
                            xiaohao3=0
                            break

        else:
            b=table.row_values(a)[3]+table.row_values(a)[4]+table.row_values(a)[5]
            for q in set_list:
                if q[1] in b:
                    if q[1]==u'キック' and u'プレースキック' in b:
                        continue


                    for w in set_list:
                        if q==w:
                            continue
                        elif w[1] in b:
                            if w[1] == u'キック' and u'プレースキック' in b:
                                continue
                            for e in set_list:
                                if q==e or w==e:
                                    continue
                                elif e[1] in b:
                                    if e[1] == u'キック' and u'プレースキック' in b:
                                        continue


                                    got=True
                                    xiaohao1 = q[0]
                                    xiaohao11=q
                                    xiaohao2 = w[0]
                                    xiaohao22=w
                                    xiaohao3 = e[0]
                                    xiaohao33=e
                                    break
        if got==True:
            fazhanqiantu=0
            for l in range(86):
                if table.row_values(a)[1] in table3.row_values(l)[0]:

                    fazhanqiantu = u'发展前途:'
                    qiantu_list=re.findall('[0-9]+/...',table3.row_values(l)[0])
                    for f in qiantu_list:


                        fazhanqiantu=fazhanqiantu+u'训练%s次:%s'%(f[:-4],f[-3]+f[-2]+f[-1])+u' '
                else:
                    if l ==85 and fazhanqiantu==0:
                        fazhanqiantu = u'发展前途:'+u'无'



            mingcheng= u'名称:'+table.row_values(a)[2]
            if xiaohao3== 0:
                xiaohaokapai= u'消耗卡牌:%s+%s'%(xiaohao1,xiaohao2)
                xiaohao_list = [xiaohao11, xiaohao22]
            else:
                xiaohaokapai=u'消耗卡牌:%s+%s+%s' % (xiaohao1, xiaohao2,xiaohao3)
                xiaohao_list = [xiaohao11, xiaohao22,xiaohao33]
            xunlianfangxiang= u'训练方向:%s'%(table.row_values(a)[0])
            zongheshouyi= u'综合收益:'+str(int(table.row_values(a)[13]))
            shuzhibianhua= u'数值变化:'
            shuzhibianhua1=u''
            shuzhibianhua2=u''

            for j in range(30):
                if table.row_values(a)[j]!=u''and j>5 and j!=13 and j!=14 and j!=15 and j<16 :

                    try:
                        if '-' in str(int(table.row_values(a)[j])):
                            haha=table.row_values(0)[j]+str(int(table.row_values(a)[j]))
                        else:
                            haha = table.row_values(0)[j] + u'+'+str(int(table.row_values(a)[j]))
                    except:pass




                    shuzhibianhua = shuzhibianhua + haha
                elif table.row_values(a)[j]!=u''and j >=16 and j<23:
                    if '-' in str(int(table.row_values(a)[j])):
                        haha1=table.row_values(0)[j]+str(int(table.row_values(a)[j]))
                    else:
                        haha1 = table.row_values(0)[j] + u'+'+str(int(table.row_values(a)[j]))


                    shuzhibianhua1=shuzhibianhua1+haha1
                elif table.row_values(a)[j]!=u''and j >=23 :
                    if '-' in str(int(table.row_values(a)[j])):
                        haha2=table.row_values(0)[j]+str(int(table.row_values(a)[j]))
                    else:
                        haha2 = table.row_values(0)[j] + u'+'+str(int(table.row_values(a)[j]))


                    shuzhibianhua2=shuzhibianhua2+haha2



            text_surface = font.render(xunlianfangxiang, True, (0, 0, 0))
            text_surface1 = font.render(mingcheng, True, (0, 0, 0))
            for skill in skill_list:
                if skill in mingcheng:
                    text_surface1 = font.render(mingcheng, True, (255, 0, 0))
            text_surface2 = font.render(zongheshouyi, True, (0, 0, 0))
            text_surface3 = font.render(xiaohaokapai, True, (0, 0, 0))
            #try:
            text_surface4 = font.render(fazhanqiantu, True, (0, 0, 0))
            text_surface5 = font.render(shuzhibianhua, True, (0, 0, 0))
            text_surface6 = font.render(shuzhibianhua1, True, (0, 0, 0))
            text_surface7 = font.render(shuzhibianhua2, True, (0, 0, 0))
            use1=Usingcards((320,0),xiaohao_list)
            uses.add(use1)
            print_dict = dict(use=use1,created=False,xiaohao=xiaohao_list,sort=0, zonghe=int(table.row_values(a)[13]), fangxiang=table.row_values(a)[0],
                              wenzi=[text_surface, text_surface1, text_surface2, text_surface3, text_surface4,
                                     text_surface5,text_surface6,text_surface7])

            find_list.append(print_dict)
    find_list=sorted(find_list,key=lambda x:x['zonghe'],reverse=True)
    print 'time'+str(time.time()-local_time)

def Fangxiang(fangxiang):
    global  find_list
    if fangxiang =='FW':
        for i in find_list:
            if i['fangxiang'] == u'进攻':
                i['sort'] = 1
            elif i['fangxiang'] == u'控制':
                i['sort'] = 2
            elif i['fangxiang'] == u'身体素质':
                i['sort'] = 3
            elif i['fangxiang'] == u'心里素质':
                i['sort'] = 4
            elif i['fangxiang'] == u'庆祝':
                i['sort'] = 5
            elif i['fangxiang'] == u'防守':
                i['sort'] = 6
            elif i['fangxiang'] == u'守门':
                i['sort'] = 7
            else:
                i['sort'] = 8
    elif fangxiang =='DF':
        for i in find_list:
            if i['fangxiang'] == u'防守':
                i['sort'] = 1
            elif i['fangxiang'] == u'控制':
                i['sort'] = 2
            elif i['fangxiang'] == u'身体素质':
                i['sort'] = 3
            elif i['fangxiang'] == u'心里素质':
                i['sort'] = 4
            elif i['fangxiang'] == u'庆祝':
                i['sort'] = 5
            elif i['fangxiang'] == u'进攻':
                i['sort'] = 6
            elif i['fangxiang'] == u'守门':
                i['sort'] = 7
            else:
                i['sort'] = 8
    elif fangxiang =='GK':
        for i in find_list:
            if i['fangxiang'] == u'进攻':
                i['sort'] = 6
            elif i['fangxiang'] == u'控制':
                i['sort'] = 5
            elif i['fangxiang'] == u'身体素质':
                i['sort'] = 4
            elif i['fangxiang'] == u'心里素质':
                i['sort'] = 2
            elif i['fangxiang'] == u'庆祝':
                i['sort'] = 7
            elif i['fangxiang'] == u'防守':
                i['sort'] = 3
            elif i['fangxiang'] == u'守门':
                i['sort'] = 1
            else:
                i['sort'] = 8
    elif fangxiang =='willpower':
        for i in find_list:
            if i['fangxiang'] == u'进攻':
                i['sort'] = 3
            elif i['fangxiang'] == u'控制':
                i['sort'] = 2
            elif i['fangxiang'] == u'身体素质':
                i['sort'] =5
            elif i['fangxiang'] == u'心里素质':
                i['sort'] = 1
            elif i['fangxiang'] == u'庆祝':
                i['sort'] = 7
            elif i['fangxiang'] == u'防守':
                i['sort'] = 4
            elif i['fangxiang'] == u'守门':
                i['sort'] = 6
            else:
                i['sort'] = 8
    elif fangxiang =='toughness':
        for i in find_list:
            if i['fangxiang'] == u'进攻':
                i['sort'] = 2
            elif i['fangxiang'] == u'控制':
                i['sort'] = 3
            elif i['fangxiang'] == u'身体素质':
                i['sort'] = 1
            elif i['fangxiang'] == u'心里素质':
                i['sort'] = 6
            elif i['fangxiang'] == u'庆祝':
                i['sort'] = 7
            elif i['fangxiang'] == u'防守':
                i['sort'] = 4
            elif i['fangxiang'] == u'守门':
                i['sort'] = 5
            else:
                i['sort'] = 8
    elif fangxiang ==u'庆祝':
        for i in find_list:
            if i['fangxiang'] == u'进攻':
                i['sort'] = 2
            elif i['fangxiang'] == u'控制':
                i['sort'] = 3
            elif i['fangxiang'] == u'身体素质':
                i['sort'] = 4
            elif i['fangxiang'] == u'心里素质':
                i['sort'] = 4
            elif i['fangxiang'] == u'庆祝':
                i['sort'] = 1
            elif i['fangxiang'] == u'防守':
                i['sort'] = 6
            elif i['fangxiang'] == u'守门':
                i['sort'] = 7
            else:
                i['sort'] = 8

    elif fangxiang =='MF':
        for i in find_list:
            if i['fangxiang'] == u'进攻':
                i['sort'] = 2
            elif i['fangxiang'] == u'控制':
                i['sort'] = 1
            elif i['fangxiang'] == u'身体素质':
                i['sort'] = 5
            elif i['fangxiang'] == u'心里素质':
                i['sort'] = 4
            elif i['fangxiang'] == u'庆祝':
                i['sort'] = 7
            elif i['fangxiang'] == u'防守':
                i['sort'] = 3
            elif i['fangxiang'] == u'守门':
                i['sort'] = 6
            else:
                i['sort'] = 8
    find_list = sorted(find_list, key=lambda x: x['sort'], reverse=False)
def FindingDraw(ifdraw,ifinfo):
    global y_max
    if ifdraw==True:

        screen.blit(white_image,(0,0))
        sorts.draw(screen)
        screen.blit(back_image,(0,y))
        screen.blit(use_image,info)
        position1 = 0
        for i in find_list:
            position = 0
            for text_surface in i['wenzi']:


                i['use'].rect.top=100+50-20+y+position1*300


                screen.blit(text_surface, (0, 100 + position * 30 + y + position1 * 300))
                position += 1
            position1 += 1
        uses.draw(screen)
        for sort in sorts:
            sort.updates()
        for use in uses:
            if use.rect.top-400>y_max:
                y_max=use.rect.top -400
        draw_info(ifinfo)
    else:pass
addCard('结束')
y=0
position1=1
find_list=[]
count=0
sorts=pygame.sprite.Group()
uses=pygame.sprite.Group()
cards=pygame.sprite.Group()
sort_list=['DF','MF','GK','FW','willpower','toughness']
if_finding=False
clock=pygame.time.Clock()
dianji=30
fanhui=Rect(0,0,48,48)
jinru =Rect(463,322,87,53)
info=Rect(957,0,43,48)
tips=Rect(0,660,50,40)
if_tips=False
y_max=0
if_info=False
for i in sort_list:
    sort=Sortway(i)
    sorts.add(sort)
for i in range(32):
    card=Cards(i)
    cards.add(card)
def mainboard(if_finding):
    if if_finding==False:
        screen.blit(background_image, (0, 0))
        screen.blit(tips_image, (0, 660))
        screen.blit(enter_image, (463, 322))


        for card in cards:
            card.updates()
def draw_info(ifinfo):
    if ifinfo == True:
        screen.blit(info_image, (225, -1))
def tipsboard(iftips):
    if iftips==True:
        screen.blit(white_image,(0,0))
        tips_list=[u'Tips：',u'1.左键点击卡片增加卡片个数，右键点击减少卡片个数，上限为9张。',u'2.增加卡片后点击屏幕中心按钮进入统计界面，上方的DF,WF等为训练方向，点击',u'后训练会依据选择的训练方向进行排序。',u'3.所有训练默认依据综合收益排序，综合收益高的训练排名靠前。',u'4.点击训练右边的按钮可以直接扣除此训练花费的卡片，与主界面卡片数量同步。',u'5.统计界面右上角按钮可显示一些球员类型的中日文对照，方便查询。',u'其他:',u'本人是编程新手，也是欢乐足球爱好者，便借此作为练手项目。',u'如果运行过程中发现BUG或有什么好的建议，可以联系我qq605753520。',u'版本号:0.1']
        position=0
        for i in tips_list:

            text_surface = font.render(i, True, (0, 0, 0))
            if u'版本号'in i:
                screen.blit(text_surface, (850, 670))

            else:
                screen.blit(text_surface, (0, 60 + position * 32))
            position+=1
        screen.blit(back_image, (0, 0))








while 1:
    clock.tick(30)
    screen.blit(background_image,(0,0))

    for event in pygame.event.get():
        if event.type ==QUIT:
            exit()





        if if_finding==True:


            if event.type == MOUSEBUTTONDOWN and (event.button==4 or event.button==5):
                if event.button ==4:

                    if y==0:
                        pass
                    else:
                        y+=80

                elif event.button==5:
                    if y<=-y_max:
                        pass
                    else:

                        y-=80
                for sort in sorts:
                    sort.rect.top = sort.basic_rect.top+y


            if event.type == MOUSEBUTTONUP and event.button==1 :


                mouse = event.pos
                if info.collidepoint(mouse):
                    click_sound.play()
                    if if_info==True:
                        if_info=False
                    else:
                        if_info=True


                if fanhui.collidepoint(mouse):
                    if_finding=False
                    click_sound.play()
                    for sort in sorts:
                        sort.selected=False

                for sort in sorts:
                    if sort.rect.collidepoint(mouse):
                        click_sound.play()

                        sort.selected=True
                        for sort1 in sorts:
                            if sort1 ==sort:
                                pass
                            else:
                                sort1.selected=False
                    if sort.selected==True:
                        Fangxiang(sort.name)
                if dianji>=15:
                    dianji =0

                    for use in uses:
                        if use.rect.collidepoint(mouse):
                            use.usecard()
                            click_sound.play()
        elif if_tips==True:
            if event.type == MOUSEBUTTONUP and event.button == 1:
                mouse = event.pos
                if fanhui.collidepoint(mouse):
                    if_tips=False
                    click_sound.play()









        else:
            if event.type == MOUSEBUTTONUP and event.button == 1:
                mouse = event.pos
                for card in cards:
                    if card.rect.collidepoint(mouse):
                        if got_list.count(card.cardname) >= 9:
                            pass
                        else:
                            got_list.append(card.cardname)
                if jinru.collidepoint(mouse):
                    click_sound.play()
                    prints()
                    if_finding=True
                if tips.collidepoint(mouse):
                    click_sound.play()
                    if_tips = True

            if event.type == MOUSEBUTTONUP and event.button == 3:
                mouse = event.pos
                for card in cards:
                    if card.rect.collidepoint(mouse):
                        if got_list.count(card.cardname) == 0:
                            pass
                        else:
                            got_list.remove(card.cardname)

    dianji +=1




    mainboard(if_finding)
    
    FindingDraw(if_finding,if_info)
    tipsboard(if_tips)

    pygame.display.update()








