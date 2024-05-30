hat = 50 * '_'
MSG_FAVORITE_DISH = 'Enter name of your favorite dish: '
MSG_FAVORITE_RECIPE = 'Enter recipe of your favorite dish: '

user_favorite_dish = input(MSG_FAVORITE_DISH).title().strip()
user_favorite_recipe = input(MSG_FAVORITE_RECIPE).lower().strip()

result_01 = f'~~~~~~~~~~, {user_favorite_dish} ,~~~~~~~~~~'
result_02 = f'{user_favorite_recipe},😋'

print(hat)
print(result_01)
print(result_02)
print(user_favorite_recipe.count('meat'))
print(hat)
