#Class dengan constructor
class rumusMatematika_construct():
    """
    Ini kelas yang berisi rumus-rumus geometri matermatika
    """

    #Constructor
    def __init__(self, s, a, t, r, p, l):
        """
        :param s: variable untuk sisi luasPersegi
        :param a: alas
        :param t: tinggi
        :param r: jari-jari
        :param p: panjang
        :param l: lebar
        """

        #Attribute
        self.s = s
        self.a = a
        self.t = t
        self.r = r
        self.p = p
        self.l = l

    #Function di dalam class --> Method
    def luasLingkaran(self):
        return 3.14 * self.r**2

    def luasPersegi(self):
        return self.s*self.s

    def luasJajarGenjang(self):
        return self.a * self.t

    def luasSegitiga(self):
        return (1/2) * self.a * self.t

    def luasPersegiPanjang(self):
        return self.p * self.l

if __name__ == '__main__':
    matematikaCons = rumusMatematika_construct(4, 5, 6, 9, 7, 2)
    print(matematikaCons.luasLingkaran())

    #Untuk print dokumentasi
    print(help(rumusMatematika_construct))