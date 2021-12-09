class Parser:

    def __init__(self):
        self._p = False

    @staticmethod
    def parse_grid(lines, delim=","):
        grid = []
        for line in lines:
            if delim == "":
                k = line.strip()
                grid.append([x for x in k if x != "\\n"])
            else:
                grid.append(line.strip().split(delim))
        return grid
    
    @staticmethod
    def parse_int_grid(lines, delim=","):
        grid = []
        for line in lines:
            if delim == "":
                k = line.strip()
                grid.append([int(x) for x in k if x != "\\n"])
            else:
                grid.append(line.strip().split(delim))
        return grid