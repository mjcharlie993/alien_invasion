import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image, and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
#        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ship's center.
        self.centerx0 = float(self.rect.centerx)
        self.centery0 = float(self.rect.centery)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx0 += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx0 -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery0 -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery0 += self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.centerx0
        self.rect.centery = self.centery0

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """Center the ship on the screen."""
        self.centerx0 = self.screen_rect.centerx
        self.centery0 = 780