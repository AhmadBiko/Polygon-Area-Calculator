#[1] creatin the parent class
class Rectangle:
    #[2] initializing our attributes
    def __init__(self, width: int, height:int) -> None:
        self.width = width
        self.height = height
    #[3] creating the needed methods
    def set_width(self, new_width: int) -> None:
        self.width = new_width
    def set_height (self, new_height : int) -> None:
        self.height = new_height
    def get_area(self) -> float:
        return self.width * self.height
    def get_perimeter(self) -> int:
        half_perimeter = self.width + self.height 
        return 2 * half_perimeter  
    def get_diagonal(self) -> float:
        diagonal_pro_max = self.width ** 2 + self.height ** 2
        return diagonal_pro_max ** 0.5
    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        num_of_lines = self.height
        length_of_line = self.width
        picture = ''
        for line in range(num_of_lines):
            picture += length_of_line * '*' + '\n'
        return picture
    def get_amount_inside(self, shape) -> int:
        length_1 = int(self.width / shape.width)
        length_2 = int(self.height / shape.height)
        return length_1 * length_2
    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})' 
#[4] creating the child class    
class Square(Rectangle):
    #[5] intializing our attributes
    def __init__(self, length: int) -> None:
        super().__init__(length, length)
        self.length = length
    #[6] creating the needed methods
    def set_width(self, new_length: int) -> None:
        self.set_side(new_length)
    def set_height (self, new_length : int) -> None:
        self.set_side(new_length)
    def set_side(self, new_length: int) -> None:
        self.height = new_length
        self.width = new_length
        self.length = new_length
    def __str__(self) -> str:
        return f'Square(side={self.length})'
#[7] our testing data
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

print(Rectangle(15,10).get_amount_inside(Square(5)))
print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))
print(Rectangle(2,3).get_amount_inside(Rectangle(3, 6)))