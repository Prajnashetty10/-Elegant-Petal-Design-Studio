import turtle
import random
import time
from datetime import datetime

class PetalDesigner:
    def __init__(self):
        # Setup the screen
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=800)
        self.screen.bgcolor("black")
        self.screen.title("Advanced Petal Design Studio")
        
        # Create the main turtle
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        
        # Create text display turtle
        self.text_display = turtle.Turtle()
        self.text_display.hideturtle()
        self.text_display.penup()
        self.text_display.color("white")
        
        # Color schemes
        self.color_schemes = {
            "rainbow": ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
            "sunset": ["#FF7F50", "#FF6B6B", "#FFA07A", "#FFD700", "#FF4500"],
            "ocean": ["#00FFFF", "#00CED1", "#20B2AA", "#48D1CC", "#40E0D0"],
            "forest": ["#228B22", "#32CD32", "#90EE90", "#98FB98", "#3CB371"]
        }
        
        # Petal patterns
        self.patterns = {
            "classic": self.draw_classic_petal,
            "curved": self.draw_curved_petal,
            "pointed": self.draw_pointed_petal,
            "spiral": self.draw_spiral_petal
        }
        
        self.current_scheme = "rainbow"
        self.animation_speed = 0
        self.size = 100
        self.petals = 36
        
    def show_message(self, message, duration=1):
        """Display a temporary message on screen"""
        self.text_display.clear()
        self.text_display.goto(0, 350)
        self.text_display.write(message, align="center", font=("Arial", 16, "normal"))
        self.screen.update()
        time.sleep(duration)
        
    def draw_classic_petal(self):
        # Elegant curved petal with smooth edges
        self.pen.pensize(2)
        for i in range(2):
            self.pen.circle(self.size, 60)
            self.pen.left(120)
        # Add detail lines inside
        pos = self.pen.position()
        head = self.pen.heading()
        self.pen.pensize(1)
        self.pen.forward(self.size/2)
        self.pen.backward(self.size/2)
        self.pen.left(30)
        self.pen.forward(self.size/3)
        self.pen.backward(self.size/3)
        self.pen.right(60)
        self.pen.forward(self.size/3)
        self.pen.backward(self.size/3)
        self.pen.goto(pos)
        self.pen.setheading(head)
        
    def draw_curved_petal(self):
        # Flowing, nature-inspired petal
        self.pen.pensize(2)
        self.pen.circle(self.size, 60)
        pos1 = self.pen.position()
        head1 = self.pen.heading()
        self.pen.left(30)
        self.pen.circle(self.size * 0.7, 60)
        self.pen.left(120)
        self.pen.circle(self.size * 0.7, 60)
        self.pen.goto(pos1)
        self.pen.setheading(head1)
        self.pen.left(120)
        self.pen.circle(self.size, 60)
        
    def draw_pointed_petal(self):
        # Elegant pointed petal with curves
        self.pen.pensize(2)
        self.pen.circle(self.size, 45)
        self.pen.left(90)
        self.pen.forward(self.size * 1.2)
        self.pen.left(135)
        self.pen.circle(-self.size/2, 90)
        self.pen.left(135)
        self.pen.forward(self.size * 1.2)
        self.pen.left(90)
        self.pen.circle(self.size, 45)
        
    def draw_spiral_petal(self):
        # Intricate spiral design with varying thickness
        base_size = self.size * 0.8
        self.pen.pensize(2)
        for i in range(15):
            ratio = (15 - i) / 15
            self.pen.pensize(2 * ratio)
            self.pen.circle(base_size * ratio, 30)
            self.pen.left(15)
        self.pen.pensize(1)
        # Add decorative lines
        pos = self.pen.position()
        head = self.pen.heading()
        for _ in range(3):
            self.pen.circle(self.size/4, 120)
        self.pen.goto(pos)
        self.pen.setheading(head)
            
    def create_design(self, pattern="classic", add_glitter=False):
        """Create the main petal design"""
        self.pen.clear()
        self.pen.penup()
        self.pen.goto(0, -100)  # Start position
        self.pen.pendown()
        self.pen.speed(self.animation_speed)
        
        colors = self.color_schemes[self.current_scheme]
        
        for i in range(self.petals):
            # Set color with opacity
            self.pen.pencolor(colors[i % len(colors)])
            
            # Draw the petal
            self.patterns[pattern]()
            
            # Add glitter effect
            if add_glitter and i % 3 == 0:
                self.add_glitter_effect()
                
            # Rotate for next petal
            self.pen.right(360 / self.petals)
            
    def add_glitter_effect(self):
        """Add sparkle points around the current position"""
        current_pos = self.pen.position()
        current_heading = self.pen.heading()
        
        self.pen.penup()
        for _ in range(3):
            offset_x = random.randint(-10, 10)
            offset_y = random.randint(-10, 10)
            self.pen.goto(current_pos[0] + offset_x, current_pos[1] + offset_y)
            self.pen.dot(2, "white")
        
        self.pen.goto(current_pos)
        self.pen.setheading(current_heading)
        self.pen.pendown()
        
    def save_design(self):
        """Save the current design as an image"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"petal_design_{timestamp}.ps"
        self.screen.getcanvas().postscript(file=filename)
        self.show_message(f"Design saved as {filename}")
        
    def interactive_mode(self):
        """Start interactive mode with keyboard controls"""
        self.show_message("Welcome to Petal Designer! Press 'h' for help", 2)
        
        def help_menu():
            help_text = """
            Controls:
            1-4: Change color scheme
            a-d: Change pattern
            +/-: Change size
            </>/: Change petal count
            s: Save design
            g: Toggle glitter
            q: Quit
            """
            self.show_message(help_text, 4)
            
        def change_color_scheme(scheme_num):
            schemes = list(self.color_schemes.keys())
            if 0 <= scheme_num < len(schemes):
                self.current_scheme = schemes[scheme_num]
                self.create_design()
                
        def change_pattern(pattern_num):
            patterns = list(self.patterns.keys())
            if 0 <= pattern_num < len(patterns):
                self.create_design(patterns[pattern_num])
                
        # Keyboard bindings
        self.screen.onkey(help_menu, 'h')
        self.screen.onkey(lambda: change_color_scheme(0), '1')
        self.screen.onkey(lambda: change_color_scheme(1), '2')
        self.screen.onkey(lambda: change_color_scheme(2), '3')
        self.screen.onkey(lambda: change_color_scheme(3), '4')
        self.screen.onkey(lambda: change_pattern(0), 'a')
        self.screen.onkey(lambda: change_pattern(1), 'b')
        self.screen.onkey(lambda: change_pattern(2), 'c')
        self.screen.onkey(lambda: change_pattern(3), 'd')
        self.screen.onkey(lambda: setattr(self, 'size', self.size + 10), 'plus')
        self.screen.onkey(lambda: setattr(self, 'size', max(10, self.size - 10)), 'minus')
        self.screen.onkey(lambda: setattr(self, 'petals', self.petals + 2), 'period')
        self.screen.onkey(lambda: setattr(self, 'petals', max(4, self.petals - 2)), 'comma')
        self.screen.onkey(self.save_design, 's')
        self.screen.onkey(lambda: self.create_design(add_glitter=True), 'g')
        self.screen.onkey(self.screen.bye, 'q')
        
        self.screen.listen()
        
# Create and run the application
if __name__ == "__main__":
    designer = PetalDesigner()
    designer.create_design()  # Create initial design
    designer.interactive_mode()  # Start interactive mode
    turtle.done()
