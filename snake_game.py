import pygame
import random
from enum import Enum
from collections import deque
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 139, 34)  # Dark green
LIGHT_GREEN = (50, 205, 50)  # Light green for body
YELLOW = (255, 255, 0)
DARK_GREEN = (0, 100, 0)  # Very dark for tail

# Direction Enum
class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

# Snake Game Class
class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        
        # Initialize snake in the middle
        self.snake = deque([(GRID_WIDTH // 2, GRID_HEIGHT // 2)])
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.food = self.spawn_food()
        self.score = 0
        self.running = True
        self.game_over = False
    
    def spawn_food(self):
        """Spawn food at random location"""
        while True:
            food_x = random.randint(0, GRID_WIDTH - 1)
            food_y = random.randint(0, GRID_HEIGHT - 1)
            if (food_x, food_y) not in self.snake:
                return (food_x, food_y)
    
    def handle_events(self):
        """Handle user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                # Change direction based on arrow keys or WASD
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.direction != Direction.DOWN:
                        self.next_direction = Direction.UP
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if self.direction != Direction.UP:
                        self.next_direction = Direction.DOWN
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if self.direction != Direction.RIGHT:
                        self.next_direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if self.direction != Direction.LEFT:
                        self.next_direction = Direction.RIGHT
                
                # Restart game on SPACE if game over
                if event.key == pygame.K_SPACE and self.game_over:
                    self.__init__()
    
    def update(self):
        """Update game logic"""
        if self.game_over:
            return
        
        self.direction = self.next_direction
        
        # Calculate new head position
        head_x, head_y = self.snake[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            self.game_over = True
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Add new head
        self.snake.appendleft(new_head)
        
        # Check food collision
        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
    
    def draw_snake_head(self, x, y):
        """Draw snake head with eyes looking in direction of movement"""
        # Draw head circle
        center_x = x * GRID_SIZE + GRID_SIZE // 2
        center_y = y * GRID_SIZE + GRID_SIZE // 2
        pygame.draw.circle(self.screen, GREEN, (center_x, center_y), GRID_SIZE // 2 - 2)
        
        # Draw eyes based on direction
        eye_offset = GRID_SIZE // 4
        eye_radius = 3
        
        if self.direction == Direction.RIGHT:
            # Eyes on right side
            pygame.draw.circle(self.screen, WHITE, (center_x + eye_offset, center_y - 3), eye_radius)
            pygame.draw.circle(self.screen, WHITE, (center_x + eye_offset, center_y + 3), eye_radius)
            pygame.draw.circle(self.screen, BLACK, (center_x + eye_offset, center_y - 3), 2)
            pygame.draw.circle(self.screen, BLACK, (center_x + eye_offset, center_y + 3), 2)
        elif self.direction == Direction.LEFT:
            # Eyes on left side
            pygame.draw.circle(self.screen, WHITE, (center_x - eye_offset, center_y - 3), eye_radius)
            pygame.draw.circle(self.screen, WHITE, (center_x - eye_offset, center_y + 3), eye_radius)
            pygame.draw.circle(self.screen, BLACK, (center_x - eye_offset, center_y - 3), 2)
            pygame.draw.circle(self.screen, BLACK, (center_x - eye_offset, center_y + 3), 2)
        elif self.direction == Direction.UP:
            # Eyes on top
            pygame.draw.circle(self.screen, WHITE, (center_x - 3, center_y - eye_offset), eye_radius)
            pygame.draw.circle(self.screen, WHITE, (center_x + 3, center_y - eye_offset), eye_radius)
            pygame.draw.circle(self.screen, BLACK, (center_x - 3, center_y - eye_offset), 2)
            pygame.draw.circle(self.screen, BLACK, (center_x + 3, center_y - eye_offset), 2)
        elif self.direction == Direction.DOWN:
            # Eyes on bottom
            pygame.draw.circle(self.screen, WHITE, (center_x - 3, center_y + eye_offset), eye_radius)
            pygame.draw.circle(self.screen, WHITE, (center_x + 3, center_y + eye_offset), eye_radius)
            pygame.draw.circle(self.screen, BLACK, (center_x - 3, center_y + eye_offset), 2)
            pygame.draw.circle(self.screen, BLACK, (center_x + 3, center_y + eye_offset), 2)
    
    def draw_snake_body(self, x, y, is_tail=False):
        """Draw snake body segment"""
        rect = pygame.Rect(x * GRID_SIZE + 2, y * GRID_SIZE + 2, GRID_SIZE - 4, GRID_SIZE - 4)
        
        # Tail is darker
        if is_tail:
            pygame.draw.rect(self.screen, DARK_GREEN, rect, border_radius=4)
            pygame.draw.rect(self.screen, GREEN, rect, 1, border_radius=4)
        else:
            # Body segments are lighter
            pygame.draw.rect(self.screen, LIGHT_GREEN, rect, border_radius=4)
            pygame.draw.rect(self.screen, GREEN, rect, 2, border_radius=4)
    
    def draw(self):
        """Draw game elements"""
        self.screen.fill(BLACK)
        
        # Draw snake body and head
        for i, (x, y) in enumerate(self.snake):
            if i == 0:
                # Draw head with eyes
                self.draw_snake_head(x, y)
            elif i == len(self.snake) - 1:
                # Draw tail (darker)
                self.draw_snake_body(x, y, is_tail=True)
            else:
                # Draw body
                self.draw_snake_body(x, y, is_tail=False)
        
        # Draw food (apple-like)
        food_x = self.food[0] * GRID_SIZE + GRID_SIZE // 2
        food_y = self.food[1] * GRID_SIZE + GRID_SIZE // 2
        pygame.draw.circle(self.screen, RED, (food_x, food_y), GRID_SIZE // 2 - 3)
        # Draw stem
        pygame.draw.line(self.screen, (34, 139, 34), (food_x, food_y - GRID_SIZE // 2 + 3), (food_x, food_y - 8), 2)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw game over message
        if self.game_over:
            game_over_text = self.font.render("GAME OVER! Press SPACE to restart", True, RED)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            # Draw background for text
            bg_rect = text_rect.inflate(20, 20)
            pygame.draw.rect(self.screen, BLACK, bg_rect)
            pygame.draw.rect(self.screen, RED, bg_rect, 2)
            self.screen.blit(game_over_text, text_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()

# Run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.run()
