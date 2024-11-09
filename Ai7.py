import random
class Ai7:
    @staticmethod
    def GenSeed(RangeSeed1, RangeSeed2, Range=10):
        alist = []
        for i in range(0, Range):
            random_number = random.randint(RangeSeed1, RangeSeed2)
            alist.append(random_number)
        return alist

    @staticmethod
    def PreGuess(Seed):
        for ss in Seed:
            ss = str(ss)

        for i in Seed:
            i += i
            average = i / int(len(ss))
        return average

    @staticmethod
    def Guess(Average, ActualNumber=None):
        if ActualNumber is None:
            return Average
        else:
            return Average, ActualNumber
