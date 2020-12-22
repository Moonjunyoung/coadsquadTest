from collections import deque

def List_to_CorrectCommandlist(Command_list): # 들어오는 명령어를 올바른 명령어로 바꾸어주는 함수
    Command_List_Index = 0
    Change_Command_list=[] # 제대로 된 명령어를 만들기위한 저장소
    while Command_List_Index < len(Command_list):
        if Command_list[Command_List_Index] == "'":
            Change_Command_list[-1] += "'"
        else:
            Change_Command_list.append(Command_list[Command_List_Index])
        Command_List_Index += 1

    return Change_Command_list

class Cube:
    def __init__(self):
        self.cube=[['R','R','W'],['G','C','W'],['G','B','B']] # 0. 3x3 초기큐브 값 설정

    def Set_Cube_Upper(self,upper_cube): # 1-1. upper_cube의값으로 최상단 큐브값 설정
        for i in range(len(upper_cube)):
            self.cube[0][i]=upper_cube[i]
    def Set_Cube_Lower(self,lower_cube): # 1-2. lower_cube의값으로 최하단 큐브값 설정
        for i in range(len(lower_cube)):
            self.cube[2][i]=lower_cube[i]
    def Set_Cube_Left(self, left_cube): # 1-3  left_cube의 값으로 맨 왼쪽 큐브값 설정
        for i in range(len(left_cube)):
            self.cube[i][0] = left_cube[i]
    def Set_Cube_Right(self,right_cube): # 1-4 right_cube의 값으로 맨 오른쪽 큐브값 설정
        for i in range(len(right_cube)):
            self.cube[i][2] = right_cube[i]

    def Get_Cube_Right(self): # 2-1.현재 맨 오른쪽의 큐브값을 가져온다
          tmp_list=[]
          for i in range(len(self.cube)):tmp_list.append(self.cube[i][2])
          return tmp_list

    def Get_Cube_Left(self): # 2-2. 현재 맨 왼쪽의 큐브값을 가져온다.
        tmp_list = []
        for i in range(len(self.cube)): tmp_list.append(self.cube[i][0])
        return tmp_list

    def Get_Cube_Upper(self): # 2-3. 현재 맨 위쪽의 큐브값을 가져온다.
        return self.cube[0]

    def Get_Cube_Lower(self): # 2-4. 현재 맨 아래의 큐브값을 가져온다.
        return self.cube[2]

    def Print(self): # 3.현재 큐브 상태를 출력하는 함수
        for i in range(3):
            for j in range(3):
                print(self.cube[i][j],end=' ')
            print()
        print()

    def Upper_Push_to_Left(self): # 4.1.1 큐브의 가장 윗줄을 왼쪽으로 한칸밀기
        upper_cube=deque(self.Get_Cube_Upper())
        upper_cube.rotate(-1)
        self.Set_Cube_Upper(upper_cube)
    def Upper_Push_to_Right(self):  # 4.1.2 큐브의 가장 윗줄을 오른쪽으로 한칸밀기
        upper_cube = deque(self.Get_Cube_Upper())
        upper_cube.rotate(1)
        self.Set_Cube_Upper(upper_cube)
    def Lower_Push_to_Left(self): # 4.2.1 큐브의 가장 아랫줄을 왼쪽으로 한칸 밀기
        lower_cube= deque(self.Get_Cube_Lower())
        lower_cube.rotate(-1)
        self.Set_Cube_Lower(lower_cube)
    def Lower_Push_to_Right(self): # 4.2.2 큐브의 가장 아랫줄을 오른쪽으로 한칸 밀기
        lower_cube = deque(self.Get_Cube_Lower())
        lower_cube.rotate(1)
        self.Set_Cube_Lower(lower_cube)

    def Right_Push_to_Up(self): # 4.3.1 큐브의 가장 오른쪽을 위로 한칸밀기
        right_cube=deque(self.Get_Cube_Right())
        right_cube.rotate(-1)
        self.Set_Cube_Right(right_cube)

    def Right_Push_to_Down(self): # 4.3.2 큐브의 가장 오른쪽을 아래로 한칸밀기
        right_cube=deque(self.Get_Cube_Right())
        right_cube.rotate(1)
        self.Set_Cube_Right(right_cube)

    def Left_Push_to_Down(self): # 4.4.1 큐브의 가장 왼쪽을 아래로 한칸 밀기
        left_cube=deque(self.Get_Cube_Left())
        left_cube.rotate(1)
        self.Set_Cube_Left(left_cube)

    def Left_Push_to_Up(self): # 4.4.2 큐브의 가장 왼쪽을 아래로 위로 한칸 밀기
        left_cube=deque(self.Get_Cube_Left())
        left_cube.rotate(-1)
        self.Set_Cube_Left(left_cube)


    def Command_Input_List(self):
        Command_List = list(input("CUBE>").strip())
        Command_List = List_to_CorrectCommandlist(Command_List)
        return Command_List

    def Command_Print(self,command):
        if command=='Q':
            print('Bye~')
            exit(0)
        else:
            print(command)
        return

    def Command_Cube(self,command):
        if command=='U':
            self.Upper_Push_to_Left()
        elif command=="U'":
            self.Upper_Push_to_Right()
        elif command=='R':
             self.Right_Push_to_Up()
        elif command=="R'":
             self.Right_Push_to_Down()
        elif command=='L':
            self.Left_Push_to_Down()
        elif command=="L'":
             self.Left_Push_to_Up()
        elif command=='B':
            self.Lower_Push_to_Right()
        elif command=="B'":
            self.Lower_Push_to_Left()
        else:
            return False

        return True



cube=Cube() # 큐브 객체생성
cube.Print()

# 명령어에 따라 큐브에 맞는 기능을 실행시켜주는 메인 함수
while True:
      #Command_List=list(input("CUBE>").strip())
      #Command_List=List_to_CorrectCommandlist(Command_List)
      Command_Input_List=cube.Command_Input_List()
      for command in Command_Input_List:
          if cube.Command_Cube(command):
              cube.Command_Print(command)
              cube.Print()
          else:
              continue

          # if command=='Q':
          #     print('Bye~')
          #     exit(0)
          # elif command=='U':
          #      print('U')
          #      cube.Upper_Push_to_Left()
          # elif command=="U'":
          #      print("U'")
          #      cube.Upper_Push_to_Right()
          # elif command=='R':
          #      print('R')
          #      cube.Right_Push_to_Up()
          # elif command=="R'":
          #      print("R'")
          #      cube.Right_Push_to_Down()
          # elif command=='L':
          #      print('L')
          #      cube.Left_Push_to_Down()
          # elif command=="L'":
          #      print("L'")
          #      cube.Left_Push_to_Up()
          # elif command=='B':
          #      print('B')
          #      cube.Lower_Push_to_Right()
          # elif command=="B'":
          #      print("B'")
          #      cube.Lower_Push_to_Left()
          # else: # 잘못된 명령어 인경우
          #     continue

          #cube.Print() # 현재 큐브상태출력