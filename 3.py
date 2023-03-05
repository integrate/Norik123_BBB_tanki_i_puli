import time,wrap, random, math
from time import sleep
from wrap import sprite, actions, world, sprite_text
from random import randint, choice

world.create_world(600, 600, 680, 30)

hero = sprite.add("battle_city_tanks", 100, 100, "tank_player_size1_green1")
star=sprite.add("battle_city_items",1,1,costume="block_gift_star",visible=False)
life=sprite.add("battle_city_items",1,1,costume="block_gift_tank",visible=False)

level=0
heart=0
numberlevel=sprite.add_text(str(level), 570, 30,text_color=[249,255,80],font_size=38)
numberheart=sprite.add_text(str(heart), 550, 30,text_color=[255,114,10],font_size=38)

bullet=sprite.add("battle_city_items",1,1,costume="bullet",visible=False)
sprite.set_angle(bullet,90)
sprite.set_size_percent_of(bullet,500)

@wrap.on_key_always(wrap.K_RIGHT,wrap.K_d)
def move_right(key):
    a=sprite.get_angle(hero)
    sprite.set_angle(hero,a+5)

@wrap.on_key_always(wrap.K_LEFT,wrap.K_a)
def move_left(key):
    a=sprite.get_angle(hero)
    sprite.set_angle(hero,a-5)

@wrap.on_key_always(wrap.K_UP,wrap.K_w)
def go(key):
    sprite.move_at_angle_dir(hero,5)

@wrap.on_key_always(wrap.K_DOWN,wrap.K_s)
def back(key):
    sprite.move_at_angle_dir(hero,-3)

@wrap.always(5000)
def show_star_or_life():
    z=random.choice([star,life])
    x = randint(5, 590)
    y = randint(5, 590)
    sprite.move_to(z, x, y)

    if z==star:
        sprite.show(star)
        sprite.hide(life)
    else:
        sprite.show(life)
        sprite.hide(star)


@wrap.always(3000)
def show_bullet():
    y = randint(10, 590)
    sprite.move_to(bullet,1, y)
    sprite.show(bullet)

@wrap.always(50)
def bullet_move():
    sprite.move_at_angle_dir(bullet,10)



@wrap.always(1)
def level_up():
    global level,heart

    if sprite.is_collide_sprite(star,hero) and sprite.is_visible(star) and level<4:
        sprite.hide(star)
        level+=1
        updatelevel()


    elif sprite.is_collide_sprite(hero,life) and sprite.is_visible(life):
        sprite.hide(life)
        heart+=1
        updatelife()

    elif sprite.is_collide_sprite(hero,bullet) and sprite.is_visible(bullet):
        sprite.hide(bullet)

        if level>0:
            level-=1
            updatelevel()

        elif level==0 and heart>0:
            heart-= 1
            updatelife()

        elif level==0 and heart==0:
            sprite.hide(hero)
            x = sprite.get_x(hero)
            y = sprite.get_y(hero)
            end = sprite.add("battle_city_items", x, y, costume="effect_appearance1")
            sleep(0.5)
            sprite.set_costume_next(end)
            sleep(0.5)
            sprite.set_costume_next(end)
            sleep(0.5)
            sprite.set_costume_next(end)
            sleep(0.5)
            sprite.hide(end)
            sprite.move_to(hero, 300, 300)
            sleep(0.5)
            sprite.show(hero)


def updatelife():
    sprite_text.set_text(numberheart, str(heart))

def updatelevel():
    sprite_text.set_text(numberlevel, str(level))
    if level==0:
        sprite.set_costume(hero,costume="tank_enemy_size1_green1")
    elif level==1:
        sprite.set_costume(hero,costume="tank_enemy_size2_green1")
    elif level==2:
        sprite.set_costume(hero,costume="tank_enemy_size3_green1")
    elif level==3:
        sprite.set_costume(hero,costume="tank_enemy_size4_green1")
    elif level==4:
        sprite.set_costume(hero,costume="tank_enemy_size4_yellow1")

