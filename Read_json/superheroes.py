import json

with open('all.json', 'r', encoding='utf-8') as file:
  text = json.load(file)

def top_intelligence(top_hero):
  print(f'Самый умный среди Халка, Капитана Америки и Таноса: {max(top_hero, key=top_hero.get)}\nГлуповат из них: {min(top_hero, key=top_hero.get)}')

list_intelligence = {}
free_list_intelligence = {}
for heroes in text:  
  list_intelligence[heroes['name']] = heroes['powerstats']['intelligence']
for hero, intelligence in list_intelligence.items():
  if hero == 'Hulk':
    free_list_intelligence[hero] = intelligence
  if hero == 'Captain America':
    free_list_intelligence[hero] = intelligence
  if hero == 'Thanos':
    free_list_intelligence[hero] = intelligence
if __name__ == '__main__':
  sortedDictWithValues = dict(sorted(free_list_intelligence.items(), key=lambda x: x[1], reverse=True))
  for key, value in sortedDictWithValues.items():  
    print("{0}: {1}".format(key,value))
top_intelligence(free_list_intelligence)
  
view_heroes = input('Хотите посмотреть ТОП самых умных супергероев? (Да/Нет): ').lower()  
if view_heroes == 'да':
  hero_intelligence = {}
  for heroes in text:
    hero_intelligence[heroes['name']] = heroes['powerstats']['intelligence']
  if __name__ == '__main__':
    sortedDictWithValues = dict(sorted(hero_intelligence.items(), key=lambda x: x[1], reverse=True))
  print('Топ супергероев по интелекту:')
  for key, value in sortedDictWithValues.items():  
    print('🥷 ' "{0}: {1}".format(key,value))
else:
  print('Печалька')