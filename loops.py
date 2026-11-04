monster_health = 150
player_damage = 25

attack_count = 0

while monster_health > 0:
    monster_health -= player_damage
    attack_count += 1

    if monster_health < 0:
        monster_health = 0

    print("Monster health:", monster_health)
  
print("Total attacks:", attack_count)
