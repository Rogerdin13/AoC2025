
class Data:
    direction:str = ''
    distance:int = 0

    # ctor (constructor)
    def __init__(self, direction:str, distance:int):
        self.direction = direction
        self.distance = distance

    # toString overwrite
    def __str__(self):
        return f"{{{self.direction}, {self.distance}}}"

def extract_data() -> list[Data]:
    result = []
    with open(r"input") as inp_file:
    #with open(r"test_input") as inp_file:
        for l in inp_file:
            result.append(Data(l[0], int(l[1:len(l)-1])))
    return result

    
def solve(instruction_list:list[Data])->int:
    value = 50
    zero_counter = 0
    for instruction in instruction_list:
        if instruction.direction == "L":
            value = (value-instruction.distance) % 100
        else :
            value = (value+instruction.distance) % 100

        if value == 0:
            zero_counter += 1
    return zero_counter


##
# test input solution is '3' (number of times dial points at 0)
if __name__ == '__main__':
    print(solve(extract_data()))