import random
import itertools
import json


class c_64gua:
        def __init__(self, num, name, icon, bin_str, dec):
                self.num = num
                self.name = name
                self.icon = icon
                self.bin_str = bin_str
                self.dec = dec


buf_64gua = [c_64gua(2, '坤', '䷁', '000000', 0), c_64gua(23, '剥', '䷖', '000001', 1), c_64gua(8, '比', '䷇', '000010', 2), c_64gua(20, '观', '䷓', '000011', 3),
c_64gua(16, '豫', '䷏', '000100', 4), c_64gua(35, '晋', '䷢', '000101', 5), c_64gua(45, '萃', '䷬', '000110', 6), c_64gua(12, '否', '䷋', '000111', 7),
c_64gua(15, '谦', '䷎', '001000', 8), c_64gua(52, '艮', '䷳', '001001', 9), c_64gua(39, '蹇', '䷦', '001010', 10), c_64gua(53, '渐', '䷴', '001011', 11),
c_64gua(62, '小过', '䷽', '001100', 12), c_64gua(56, '旅', '䷷', '001101', 13), c_64gua(31, '咸', '䷞', '001110', 14), c_64gua(33, '遁', '䷠', '001111', 15),
c_64gua(7, '师', '䷆', '010000', 16), c_64gua(4, '蒙', '䷃', '010001', 17), c_64gua(29, '坎', '䷜', '010010', 18), c_64gua(59, '涣', '䷺', '010011', 19),
c_64gua(40, '解', '䷧', '010100', 20), c_64gua(64, '未济', '䷿', '010101', 21), c_64gua(47, '困', '䷮', '010110', 22), c_64gua(6, '讼', '䷅', '010111', 23),
c_64gua(46, '升', '䷭', '011000', 24), c_64gua(18, '蛊', '䷑', '011001', 25), c_64gua(48, '井', '䷯', '011010', 26), c_64gua(57, '巽', '䷸', '011011', 27),
c_64gua(32, '恒', '䷟', '011100', 28), c_64gua(50, '鼎', '䷱', '011101', 29), c_64gua(28, '大过', '䷛', '011110', 30), c_64gua(44, '姤', '䷫', '011111', 31),
c_64gua(24, '复', '䷗', '100000', 32), c_64gua(27, '颐', '䷚', '100001', 33), c_64gua(3, '屯', '䷂', '100010', 34), c_64gua(42, '益', '䷩', '100011', 35),
c_64gua(51, '震', '䷲', '100100', 36), c_64gua(21, '噬嗑', '䷔', '100101', 37), c_64gua(17, '随', '䷐', '100110', 38), c_64gua(25, '无妄', '䷘', '100111', 39),
c_64gua(36, '明夷', '䷣', '101000', 40), c_64gua(22, '贲', '䷕', '101001', 41), c_64gua(63, '既济', '䷾', '101010', 42), c_64gua(37, '家人', '䷤', '101011', 43),
c_64gua(55, '丰', '䷶', '101100', 44), c_64gua(30, '离', '䷝', '101101', 45), c_64gua(49, '革', '䷰', '101110', 46), c_64gua(13, '同人', '䷌', '101111', 47),
c_64gua(19, '临', '䷒', '110000', 48), c_64gua(41, '损', '䷨', '110001', 49), c_64gua(60, '节', '䷻', '110010', 50), c_64gua(61, '中孚', '䷼', '110011', 51),
c_64gua(54, '归妹', '䷵', '110100', 52), c_64gua(38, '睽', '䷥', '110101', 53), c_64gua(58, '兑', '䷹', '110110', 54), c_64gua(10, '履', '䷉', '110111', 55),
c_64gua(11, '泰', '䷊', '111000', 56), c_64gua(26, '大畜', '䷙', '111001', 57), c_64gua(5, '需', '䷄', '111010', 58), c_64gua(9, '小畜', '䷈', '111011', 59),
c_64gua(34, '大壮', '䷡', '111100', 60), c_64gua(14, '大有', '䷍', '111101', 61), c_64gua(43, '夬', '䷪', '111110', 62), c_64gua(1, '乾', '䷀', '111111', 63),
]


# 生成包含6个随机数的数组
random_numbers = [random.randint(0, 3) for _ in range(6)]
print(random_numbers)
for i in range(0, len(random_numbers)):
    if random_numbers[i] == 0 or random_numbers[i] == 2: # 0 2 为阳爻
        random_numbers[i] = 1
    elif random_numbers[i] == 3:
        random_numbers[i] = 0
print(random_numbers)

# 创建一个字典，键是三位字符，值是八卦字符
bagua_map = {'000': '坤', '001': '艮', '010': '坎', 
             '011': '兑', '100': '震', '101': '离', 
             '110': '巽', '111': '乾'} 


# 取random_numbers前三位组成字符串
first_part = ''.join(map(str, random_numbers[:3]))

# 取后三位组成字符串
second_part = ''.join(map(str, random_numbers[3:]))

# 示例输出
print(first_part, bagua_map[first_part])
print(second_part, bagua_map[second_part])

target_gua = ''.join(map(str, random_numbers[0:]))

# 载入 gua.json 文件
with open('gua.json', 'r', encoding='utf-8') as f:
    gua_data = json.load(f).get('gua')
    # print(gua_data)
 
    for gua in buf_64gua:
        if gua.bin_str == target_gua:
            # print(f"{gua.num}  {gua.name} {gua.icon} {gua.bin_str} {gua.dec}")

            # 通过 gua.name 进行搜索匹配
            for g in gua_data:
                if g['gua-name'] == gua.name:
                    # for detail in g.get('yao-detail'):
                        # print(detail)
                    print(g.get('gua-summary'))
                    print(g.get('gua-level'))
                    print(g.get('gua-description'))
                    print(g.get('gua-explain'))
