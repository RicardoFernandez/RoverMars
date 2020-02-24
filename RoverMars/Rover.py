class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rover:

    def __init__(self, position, face_direction):
        self.position = position
        self.set_face_direction(face_direction)

    def set_face_direction(self, face_direction):
        self.state = self.set_face_state(face_direction)
        self.face_direction = face_direction

    def get_face_direction(self):
        return self.face_direction

    def set_face_state(self, face_direction):
        directions = {
            'N': RoverFaceNorth(self),
            'W': RoverFaceWest(self),
            'S': RoverFaceSouth(self),
            'E': RoverFaceEast(self)
        }
        return directions[face_direction]

    def move_forward(self):
        self.state.move_forward()

    def move_backward(self):
        self.state.move_backward()


class RoverFaceSouth:

    def __init__(self, rover):
        self.rover = rover

    def move_forward(self):
        self.rover.position.y -= 1

    def move_backward(self):
        self.rover.position.y += 1


class RoverFaceNorth:

    def __init__(self, rover):
        self.rover = rover

    def move_forward(self):
        self.rover.position.y += 1

    def move_backward(self):
        self.rover.position.y -= 1


class RoverFaceWest:

    def __init__(self, rover):
        self.rover = rover

    def move_forward(self):
        self.rover.position.x -= 1

    def move_backward(self):
        self.rover.position.x += 1


class RoverFaceEast:

    def __init__(self, rover):
        self.rover = rover

    def move_forward(self):
        self.rover.position.x += 1

    def move_backward(self):
        self.rover.position.x -= 1
