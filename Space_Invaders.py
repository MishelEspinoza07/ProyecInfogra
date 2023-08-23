
import arcade

# Constantes para la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Invaders"

# Constantes para la nave y los invasores
SHIP_SPEED = 5
INVADER_SPEED = 2
BULLET_SPEED = 5

class SpaceInvadersGame(arcade.Window):
    def _init_(self):
        super()._init_(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.ship = None
        self.bullets = []
        self.invaders = []
        self.score = 0
        self.invader_speed = INVADER_SPEED

    def setup(self):
        self.ship = arcade.Sprite("imagenes/player0.png")
        self.ship.center_x = SCREEN_WIDTH // 2
        self.ship.bottom = 0

        for row in range(5):
            for col in range(10):
                invader = arcade.Sprite("imagenes/player0.png", 0.5)
                invader.center_x = col * 80 + 40
                invader.top = SCREEN_HEIGHT - row * 50 - 10
                self.invaders.append(invader)

    def on_draw(self):
        arcade.start_render()
        self.ship.draw()
        for invader in self.invaders:
            invader.draw()
        for bullet in self.bullets:
            bullet.draw()
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ship.change_x = -SHIP_SPEED
        elif key == arcade.key.RIGHT:
            self.ship.change_x = SHIP_SPEED
        elif key == arcade.key.SPACE:
            bullet = arcade.Sprite("imagenes/laser1.png")
            bullet.center_x = self.ship.center_x
            bullet.top = self.ship.top
            self.bullets.append(bullet)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ship.change_x = 0

    def update(self, delta_time):
        self.ship.update()

        for bullet in self.bullets:
            bullet.top += BULLET_SPEED
            if bullet.top > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

            for invader in self.invaders:
                    if arcade.check_for_collision(bullet, invader):
                        invader.remove_from_sprite_lists()
                        bullet.remove_from_sprite_lists()
                        self.score += 10
                        break 

        for invader in self.invaders:
            invader.center_x += self.invader_speed
            if invader.right > SCREEN_WIDTH or invader.left < 0:
                self.invader_speed *= -1

            

def main():
    game = SpaceInvadersGame()
    game.setup()
    arcade.run()

if _name_ == "_main_": 
    main()
