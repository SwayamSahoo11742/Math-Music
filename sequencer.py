class Sequencer:
    @classmethod
    def fibonacci_series(self, n):
        series = []
        a, b = 0, 1

        while len(series) < n:
            series.append(a)
            a, b = b, a + b

        return series
    
    @classmethod
    def create_hailstones(self, start):
        n = start
        hailstones = []
        hailstones.append(n)
        while True:
            if n % 2 == 1:
                n = ((n*3)+1)
            else:
                n = (n/2)
            hailstones.append(n)
            if n == 1:
                break
        return hailstones