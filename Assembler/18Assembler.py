def convertBinToHex(bin_str):
    hex = ""
    if bin_str == "0000":
        hex = "0"
    elif bin_str == "0001":
        hex = "1"
    elif bin_str == "0010":
        hex = "2"
    elif bin_str == "0011":
        hex = "3"
    elif bin_str == "0100":
        hex = "4"
    elif bin_str == "0101":
        hex = "5"
    elif bin_str == "0110":
        hex = "6"
    elif bin_str == "0111":
        hex = "7"
    elif bin_str == "1000":
        hex = "8"
    elif bin_str == "1001":
        hex = "9"
    elif bin_str == "1010":
        hex = "A"
    elif bin_str == "1011":
        hex = "B"
    elif bin_str == "1100":
        hex = "C"
    elif bin_str == "1101":
        hex = "D"
    elif bin_str == "1110":
        hex = "E"
    elif bin_str == "1111":
        hex = "F"
    return hex


# Updated for  instruction set (18-bit)
def checkInstruction(inst):
    convertInstruction = ""
    if inst == "or":
        convertInstruction = "0000"
    elif inst == "subi":
        convertInstruction = "0001"
    elif inst == "sw":
        convertInstruction = "0011"
    elif inst == "beq":
        convertInstruction = "0100"
    elif inst == "andi":
        convertInstruction = "0110"
    elif inst == "sll":
        convertInstruction = "0000"  # opcode is same for R-type SLL
    elif inst == "jmp":
        convertInstruction = "1000"
    elif inst == "lw":
        convertInstruction = "1001"
    elif inst == "add":
        convertInstruction = "0000"
    elif inst == "nop":
        convertInstruction = "0000"  # same opcode for R-type NOP
    else:
        convertInstruction = "Invalid"
    return convertInstruction

# Added function bit lookup for R-type
def checkFunction(inst):
    func = ""
    if inst == "or":
        func = "0010"
    elif inst == "nop":
        func = "0101"
    elif inst == "sll":
        func = "0111"
    elif inst == "add":
        func = "1010"
    else:
        func = "0000"
    return func

def checkRegister(reg):
    convertReg = ""
    if reg == "$zero":
        convertReg = "000"
    elif reg == "$t0":
        convertReg = "001"
    elif reg == "$t1":
        convertReg = "010"
    elif reg == "$t2":
        convertReg = "011"
    elif reg == "$s0":
        convertReg = "100"
    elif reg == "$s1":
        convertReg = "101"
    elif reg == "$s2":
        convertReg = "110"
    elif reg == "$ra":
        convertReg = "111"
    else:
        convertReg = "Invalid"
    return convertReg

# Modified to allow variable bit size conversion
def decimalToBinary(num, bits):
    if num < 0:
        num = (1 << bits) + num
    result = bin(num)[2:]
    return result.zfill(bits)

readf = open("inputs", "r")
writef = open("outputs", "w")
writef.write("v2.0 raw\n")

for i in readf:
    splitted = i.strip().split()
    inst = splitted[0]

    # R-Type: Opcode (4) | rs (3) | rt (3) | rd (3) | shift (1) | func (4)
    if inst in ["or", "sll", "add", "nop"]:
        opcode = checkInstruction(inst)
        rs = checkRegister(splitted[1]) if inst != "nop" else "000"
        rt = checkRegister(splitted[2]) if inst != "nop" else "000"
        rd = checkRegister(splitted[3]) if inst != "nop" else "000"
        shift = "1" if inst == "sll" else "0"
        func = checkFunction(inst)

        full_bin = opcode + rs + rt + rd + shift + func  # total 18 bits
        hex_out = hex(int(full_bin, 2))[2:].zfill(5).upper()
        print(hex_out)
        writef.write(hex_out + "\n")

    # I-Type: Opcode (4) | rs (3) | rd (3) | immediate (8)
    elif inst in ["subi", "sw", "lw", "beq", "andi"]:
        opcode = checkInstruction(inst)
        rs = checkRegister(splitted[1])
        rd = checkRegister(splitted[2])
        imm = decimalToBinary(int(splitted[3]), 8)

        full_bin = opcode + rs + rd + imm
        hex_out = hex(int(full_bin, 2))[2:].zfill(5).upper()
        print(hex_out)
        writef.write(hex_out + "\n")

    # J-Type: Opcode (4) | address (14)
    elif inst == "jmp":
        opcode = checkInstruction(inst)
        address = decimalToBinary(int(splitted[1]), 14)

        full_bin = opcode + address
        hex_out = hex(int(full_bin, 2))[2:].zfill(5).upper()
        print(hex_out)
        writef.write(hex_out + "\n")
