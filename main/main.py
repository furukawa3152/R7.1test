from child.child import Smart_samurai,Hagakure
samurai1 = Smart_samurai("itaru", 1, 3)
print(samurai1.name)
print(samurai1.introduce())
samurai1.python_level_up(3)
print(samurai1.introduce())

samurai2 = Smart_samurai.create_with_default_level("tarou", 1)
print(samurai2.introduce())
samurai3 = Smart_samurai("kokoto", 2, 99)
print(samurai3.name)
print(Smart_samurai.get_total_samurais())

del samurai2
print(Smart_samurai.get_total_samurais())
hagakure1 = Hagakure("sora", 2, 5, 4)
# 子メンバ
print(hagakure1.introduce())

# クラスメソッドを呼び出し
print(Smart_samurai.get_total_samurais())
# # 子メンバ
# print(sora.weight)
# # 子メソッド
# print(sora.get_bmi())
# # 親メソッド
# print(sora.introduce())