from abc import ABC,abstractmethod

# Abstract class with all methods each language should implement. Functionalities of the app.
class Commands(ABC):
    def __init__(self, axis_speeds: dict = None):
        self.speeds = axis_speeds
    
    @abstractmethod
    def stopCmd(self):
        pass

    @abstractmethod
    def moveCmd(self, axis_values: dict):
        pass

class CSeries(Commands):
    def __init__(self, axis_speeds: dict = None):
        super().__init__(axis_speeds)

    def stopCmd(self):
        return "@0R3\n\r".encode(encoding="ascii")
    
    def moveCmd(self, axis_values: dict, axis_speeds: dict = None):
        # maybe add axis definition command in return
        if axis_speeds:
            self.speeds = axis_speeds
        axisStr = ""
        for axis,dist in axis_values.items():
            axisStr+=f"{int(dist)},{int(self.speeds[axis])}," 
        return f"@0a {axisStr[:-1]}\n\r".encode("ascii")
    
if __name__ == "__main__":
    print("start")
    cs = CSeries({'X':500, 'Y':300, 'Z':100})

    print(cs.moveCmd({'X': 300, 'Y':200, 'Z':100}))