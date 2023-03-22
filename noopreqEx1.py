import requests
import json
import operator

heroes_list = ['Hulk', 'Captain america', 'Thanos']
#создадим словарь, в котором будет находиться информация об интеллекте каждого героя (изначально 0)
intelligence_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'

for hero in heroes_list:
    hero_dict = json.loads(requests.get(url + hero).content)
    intelligence_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])
    x = max(intelligence_dict.items(), key=operator.itemgetter(1))

print(intelligence_dict)
print(f'Герой с наибольшим интеллектом: ', x[0])