import re

class Range(object):
    def __init__(self, *args):
        if len(args) == 1:
            self.sc, self.sr, self.ec, self.er = self._split_to_num(args[0])
        else:
            self.sc, self.sr, self.ec, self.er = args
            
        self.cnum = list_range(self.sc, self.ec)
        self.rnum = list_range(self.sr, self.er)
        self.cname = [self._num_to_chr(i) for i in self.cnum]

    def _chr_to_num(chars):
        sum = 0
        for c in chars:
            sum *= 26
            sum += ord(c) - ord('A') + 1
        return sum

    def _list_range(s, e):
        return list(range(s, e+1))

    def _num_to_chr(num):
        col = ""
        while num > 0:
            num, modulo = divmod(num-1, 26)
            col = chr(ord('A') + modulo) + col
        return col

    def _split_to_num(r):
        m = re.match(r'([A-Z]+)(\d+):([A-Z]+)(\d+)', r)
        start_column = m.group(1)
        end_column = m.group(3)
        start_row = m.group(2)
        end_row = m.group(4)
        return (self._chr_to_num(start_column),
                int(start_row),
                self._chr_to_num(end_column),
                int(end_row))

    def cells(self):
        return [c + str(r) for r in self.rnum for c in self.cname]

    def col_names(self):
        return self.cname
        
    def col_numbers(self):
        return self.cnum

    def move_top(self, n):
        new_sr = self.sr + n
        if  new_sr > 0:
            return Range(self.sc, new_sr, self.ec, self.er)
        else:
            raise ZeroRowException("Cannot move to Row 0")

    def row_numbers(self):
        return self.rnum

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class ZeroRowException(Exception):
    pass
