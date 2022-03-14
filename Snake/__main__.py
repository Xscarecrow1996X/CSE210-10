import constants 

from Game.Casting.Cast import Cast
from Game.Casting.Snake import Snake
from Game.Scripting.Script import Script
from CSE210-10.Snake.game/scripting.control_actors_action import ControlActorsAction
from Game.Scripting.move_actors_action import MoveActorsAction
from Game.Scripting.handle_collisions_action import HandleCollisionsAction
from CSE210-10.Snake.game/scripting.draw_actors_action import DrawActorsAction
from Game.Directing.Director import Director
from Game.Services.Keyboard import KeyboardService
from Game.Services.video_service import VideoService
from Game.Shared.Color import Color
from Game.Shared.Point import Point


def main():
    # create the cast
    cast = Cast()
    cast.add_actor("snakes", Snake())

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService(caption='Snake', width=900, height=600, cell_size=15, frame_rate=15)

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()
