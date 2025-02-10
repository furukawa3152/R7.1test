# class宣言
class Smart_samurai:
    # クラス変数 後で追加
    total_samurais = 0
    default_python_level = 3
    community_name = '佐賀スマートサムライ'
    # コンストラクタ
    def __init__(self, name: str, period: int, python_level: int):
        self.name = name
        self.period = period
        self.python_level = python_level
        #クラスメソッドの際追加
        Smart_samurai.total_samurais += 1

    # デストラクタ
    def __del__(self):
        Smart_samurai.total_samurais -= 1
        print(f"{self.name} が削除されました。現在の総人数: {Smart_samurai.total_samurais}")

    # 自己紹介メソッド
    def introduce(self):
        return f"{self.community_name}の{self.name}です。SAGA_SMART_SAMURAI{self.period}期生です。Pythonレベルは{self.python_level}です。"
    # レベルアップメソッド
    def python_level_up(self, increment: int):
        self.python_level += increment
    # クラスメソッド: デフォルト値でインスタンスを作成　クラスメソッド:クラス全体に関する操作や情報の提供を行う
    @classmethod
    def create_with_default_level(cls, name: str, period: int):
        return cls(name, period, cls.default_python_level)
    # クラスメソッド: 現在の総人数を取得
    @classmethod
    def get_total_samurais(cls):
        return f"SAGA_SMART_SAMURAIの総人数は{cls.total_samurais}人です。"
    @classmethod
    def fun_of_community_by_classmethod(cls):
        return f"{cls.community_name}最高です！"
    @staticmethod
    def fun_of_community_staticmethod():
        return f"{Smart_samurai.community_name}最高やで！"
    # __add__(self, other)を使うことで「＋」演算時を使った際の挙動を指定。
    def __add__(self, other):
        return f"{self.name}と{other.name}が融合するとpythonレベルは{self.python_level + other.python_level}になるよ。"

    def __sub__(self, other):
        return f"{self.name}から{other.name}を引くとpythonレベルは{self.python_level - other.python_level}になるよ。"
    def __mul__(self, other):
        return f"{self.name}に{other.name}をかけ合わせるとpythonレベルは{self.python_level * other.python_level}になるよ。"
    def __truediv__(self, other):
        return f"{self.name}割る{other.name}でpythonレベルは{self.python_level / other.python_level}になるよ。"

    def __eq__(self, other):
        if self.python_level == other.python_level:
            return f"{self.name}と{other.name}は同じpythonレベルです。"
        elif self.python_level > other.python_level:
            return f"{self.name}の方がpythonレベルが高いです。"
        else:
            return f"{other.name}の方がpythonレベルが高いです。"
# Smart_samuraiクラスを継承して、hagakureクラスを定義
class Hagakure(Smart_samurai):
    # コンストラクタ
    def __init__(self, name: str, period: int, python_level: int, web_level: int):

        #親クラスのコンストラクタを呼び出す
        super().__init__(name, period, python_level)

        self.web_level = web_level

    # total_pgm_levelメソッド
    def total_pgm_level(self):
        return self.python_level + self.web_level

    # 自己紹介メソッドをオーバーライド
    def introduce(self):
        return f"私の名前は、{self.name}です。SAGA_SMART_SAMURAI{self.period}期生です。Pythonレベルは{self.python_level}、プログラミングレベルは{self.total_pgm_level()}です。"