import pytest

from RoverMars.Rover import Rover
from RoverMars.Rover import Position


def test_rovermars_haspositionandfacing():
    initial_position = Position(1, 1)
    our_rover = Rover(initial_position, "N")

    assert our_rover.position == initial_position and our_rover.face_direction == "N"


@pytest.fixture
def cardinal_face_directions():
    return ['N', 'S', 'E', 'W']


def test_rovermars_getfacing(cardinal_face_directions):
    for face_position in cardinal_face_directions:
        initial_position = Position(1, 1)
        our_rover = Rover(initial_position, face_position)
        assert our_rover.get_face_direction() == face_position


def test_rovermars_setfacing(cardinal_face_directions):
    for face_direction in cardinal_face_directions:
        initial_position = Position(1, 1)
        our_rover = Rover(initial_position, face_direction)
        our_rover.set_face_direction(face_direction)
        assert our_rover.face_direction == face_direction


def test_rovermars_moveforwardfacingSouth():
    initial_position = Position(5, 5)
    our_rover = Rover(initial_position, "S")
    our_rover.state.move_forward()
    assert our_rover.position.y == 4
