import os

class VPG:
    def __init__(self, filesrc):
        if os.path.splitext(filesrc)[1].lower() != ".vpg": return
        
        self.list = []
        self.filesrc = ""

        with open(filesrc, "r", encoding='UTF8') as file:
            while True:
                line = file.readline()
                if not line: break
                self.filesrc = filesrc
                self.list.append(line)
    
    def read(self, key):
        for i in self.list:
            if str(i).startswith("%"): continue
            if i.split(":")[0] == key: return i.split(":")[1]
        
    def write(self, key, value):
        for i in self.list:
            if i.split(":")[0] == key:
                self.list[self.list.index(i)] = f"{key}:{value}"
                
                filevalue = ""

                for i in self.list:
                    filevalue += f"{i}\n"

                with open(self.filesrc, "w", encoding='UTF8') as file:
                    file.write(filevalue)
                    
                return
                
        self.list.append(f"{key}:{value}")
        
        filevalue = ""

        for i in self.list:
            if self.list.index(i) + 1 != len(self.list): filevalue += f"{i}\n"
            else: filevalue += f"{i}"

        with open(self.filesrc, "w", encoding='UTF8') as file:
            file.write(filevalue)