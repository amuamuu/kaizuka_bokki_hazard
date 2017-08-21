from itertools import permutations, combinations
original_menu = ["カレー", "チキン", "パスタ", "ラーメン", "キムチ", "カツ", "チーズ",]
print("\n".join(["%s%s%s" % (t[0], t[1], t[2]) for t in permutations(original_menu, 3)]))

#　　　 　　　 ,一-、
#　　　　　　 /￣　l
#　　　　　　■■-っ　ｺﾉﾌﾟﾛｸﾞﾗﾑｲｲｶﾝｼﾞﾀﾞﾃﾞ! ﾀﾞﾃﾞｯ!
#　　　　　　 *　 /
#　　　　 　(~つ┬と
#   　　≡ ◎-ヽJ┴◎ 　ｷｺｷｺ
