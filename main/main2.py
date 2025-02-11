from child.child import Smart_samurai
class hagakure(Smart_samurai):
    community_name = 'HAGAKUREPGM塾'
    def __init__(self, name: str, period: int, python_level: int, web_level: int):
        super().__init__(name, period, python_level)
        self.web_level = web_level
    def make_pgm_level(self):
        return self.python_level + self.web_level
    def introduce(self):
        return f"{self.community_name}の{self.name}です。SAGA_SMART_SAMURAI{self.period}期生です。pgmレベルは{self.make_pgm_level()}です..。"
if __name__ == '__main__':
    hagakure1 = hagakure('hagakure', 3, 1, 100)
    print(hagakure1.introduce())
    samurai1 = Smart_samurai('samurai', 3, 100)
    print(samurai1.introduce())
    print(samurai1+hagakure1)
    #
    # print(samurai1 - hagakure1)
    # print(samurai1 * hagakure1)
    # print(samurai1 / hagakure1)
    # print(samurai1 == hagakure1)
    #
    # print(Smart_samurai.fun_of_community_by_staticmethod())
    # print(Smart_samurai.fun_of_community_by_classmethod())
    # print(hagakure.fun_of_community_by_staticmethod())
    # print(hagakure.fun_of_community_by_classmethod())
