import re


class Range(object):
    def __init__(self, *args):
        if len(args) == 1:
            self.start_col, self.start_row, self.end_col, self.end_row = self._split_to_num(args[0])
        else:
            self.start_col, self.start_row, self.end_col, self.end_row = args
            
        self.col_num = self._list_range(self.start_col, self.end_col)
        self.row_num = self._list_range(self.start_row, self.end_row)
        self.col_name = [self._num_to_chr(i) for i in self.col_num]

    @staticmethod
    def _chr_to_num(chars):
        sum_ = 0
        for c in chars:
            sum_ *= 26
            sum_ += ord(c) - ord('A') + 1
        return sum_

    @staticmethod
    def _list_range(s, e):
        return list(range(s, e+1))

    @staticmethod
    def _num_to_chr(num):
        col = ""
        while num > 0:
            num, modulo = divmod(num - 1, 26)
            col = chr(ord('A') + modulo) + col
        return col

    def _split_to_num(self, r):
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
        return [c + str(r) for r in self.row_num for c in self.col_name]

    def col_names(self):
        return self.col_name
        
    def col_numbers(self):
        return self.col_num

    def move_top(self, n):
        new_sr = self.start_row + n
        if new_sr > 0:
            return Range(self.start_col, new_sr, self.end_col, self.end_row)
        else:
            raise ZeroRowException("Cannot move to Row 0")

    def row_numbers(self):
        return self.row_num

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class ZeroRowException(Exception):
    pass
