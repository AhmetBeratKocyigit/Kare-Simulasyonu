import pygame
import sys
import random
import math

# Parkur ve kare renkleri
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Kare boyutları
SIDE_LENGTH = 50

# Parkur boyutları
WIDTH = 600
HEIGHT = 400

# Kare hızı
SPEED = 10  

# Parkur oluşturma
def draw_course(screen):
    screen.fill(WHITE)  # Arka planı beyaz yap
    pygame.draw.rect(screen, BLACK, (50, 50, WIDTH - 100, HEIGHT - 100), 2)  # Parkuru çiz

# Kareyi oluşturma
def draw_square(screen, x, y):
    pygame.draw.rect(screen, BLACK, (x, y, SIDE_LENGTH, SIDE_LENGTH))

# Kareyi hareket ettirme
def move_square(x, y, angle):
    angle %= 360  # Açıyı 0 ile 360 arasında sınırla
    rad = math.radians(angle)  # Dereceyi radyana çevir
    x += SPEED * math.cos(rad)  # X koordinatını güncelle
    y -= SPEED * math.sin(rad)  # Y koordinatını güncelle
    return x, y

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kare Simülasyonu")
    clock = pygame.time.Clock()

    # Kareyi rastgele bir konuma yerleştir
    x = random.randint(50, WIDTH - SIDE_LENGTH - 50)
    y = random.randint(50, HEIGHT - SIDE_LENGTH - 50)

    # Başlangıçta rastgele bir açıda hareket ettir
    angle = random.randint(0, 359)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Kareyi hareket ettir
        x, y = move_square(x, y, angle)

        # Kenarlara geldiğinde yönü değiştir
        if x <= 50 or x >= WIDTH - SIDE_LENGTH - 50 or y <= 50 or y >= HEIGHT - SIDE_LENGTH - 50:
            if x <= 50:  # Sol kenara çarpma
                if 180 <= angle <= 270:
                    angle = 180 - angle
                else:
                    angle = 540 - angle
            elif x >= WIDTH - SIDE_LENGTH - 50:  # Sağ kenara çarpma
                if 0 <= angle <= 90:
                    angle = 180 - angle
                else:
                    angle = 540 - angle
            elif y <= 50:  # Üst kenara çarpma
                angle = 360 - angle
            elif y >= HEIGHT - SIDE_LENGTH - 50:  # Alt kenara çarpma
                angle = 360 - angle

        screen.fill(WHITE)
        draw_course(screen)
        draw_square(screen, x, y)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
