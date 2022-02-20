import pygame
import sys
import random
import numpy as np
import time

WIDTH = 600
HEIGHT = 600
BLACK_COLOR = (0,0,0,0)
WHITE_COLOR = (255,255,255,0)
GREEN_COLOR = (0,255,0,0)


pygame.init()
tileFont = pygame.font.SysFont('',100)
smallFont = pygame.font.SysFont('',50)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('NUMBER PUZZLE')
board = np.zeros((3,3), dtype=object)




class BoardTiles:
	tile_list = []
	move_counter = 0
	move_list =[]
	def __init__(self,name,x,y):
		self.name = name
		self.x = x
		self.y = y
		BoardTiles.tile_list.append(self)
		board[self.x,self.y] = self.name
		self.text = tileFont.render(f'{self.name}',False,(BLACK_COLOR))


	@staticmethod
	def draw_tiles():
		for tile in BoardTiles.tile_list:
			screen.blit(tile.text, (75+tile.y*200, 75+tile.x*200))


	@staticmethod
	def game_over_screen():
		pygame.draw.rect(screen,GREEN_COLOR,pygame.Rect(0,0,WIDTH,HEIGHT))	
		game_over_text = tileFont.render('YOU WIN!',False,(BLACK_COLOR))
		extra_text = smallFont.render('Press "R" to restart',False,(BLACK_COLOR))
		screen.blit(game_over_text,(WIDTH//2-200,HEIGHT//2-50))
		screen.blit(extra_text,(WIDTH//2-200,HEIGHT//2+50))


	def action_key(self,direction):
		original_x = self.x
		original_y = self.y
		if direction == 'up' and self.x != 2:
			self.x +=1
			BoardTiles.move_counter +=1
			BoardTiles.move_list.append(direction)
		elif direction == 'down' and self.x != 0:
			self.x -=1
			BoardTiles.move_counter +=1
			BoardTiles.move_list.append(direction)
		elif direction == 'left' and self.y != 2:
			self.y+=1
			BoardTiles.move_counter +=1
			BoardTiles.move_list.append(direction)
		elif direction == 'right' and self.y != 0:
			self.y-=1
			BoardTiles.move_counter +=1
			BoardTiles.move_list.append(direction)

		swapped_tile = board[self.x,self.y]
		board[self.x,self.y] = tile0.name
		board[original_x,original_y] = swapped_tile
		for tile in BoardTiles.tile_list:
			if swapped_tile == tile.name:
				tile.x = original_x
				tile.y = original_y

	@staticmethod
	def board_randomiser():
		direction_list = ['up','down','left','right']
		BoardTiles.move_counter = 0
		while BoardTiles.move_counter < 60:
			direction_choice = random.choice(direction_list)
			tile0.action_key(direction_choice)
		BoardTiles.move_counter = 0
		#print(BoardTiles.move_list)

	@staticmethod
	def auto_solve():
		solved_list = BoardTiles.move_list[::-1]

		for move in solved_list:
			if move == 'up':
				tile0.action_key('down')
			elif move == 'down':
				tile0.action_key('up')
			elif move == 'left':
				tile0.action_key('right')
			elif move == 'right':
				tile0.action_key('left')
			time.sleep(0.2)

			BoardTiles.draw_lines()
			BoardTiles.draw_tiles()
			pygame.draw.rect(screen,BLACK_COLOR,pygame.Rect(tile0.y*200,tile0.x*200,200,200))
			pygame.display.update()
			
		BoardTiles.move_list = []


	@staticmethod
	def draw_lines():
		screen.fill(WHITE_COLOR)
		pygame.draw.line(screen,BLACK_COLOR, (WIDTH//3,0),(WIDTH//3,HEIGHT),5)
		pygame.draw.line(screen,BLACK_COLOR, (WIDTH*2//3,0),(WIDTH*2//3,HEIGHT),5)
		pygame.draw.line(screen,BLACK_COLOR, (0,HEIGHT//3),(WIDTH,HEIGHT//3),5)
		pygame.draw.line(screen,BLACK_COLOR, (0,HEIGHT*2//3),(WIDTH,HEIGHT*2//3),5)
	


tile1 = BoardTiles(1,0,0)
tile2 = BoardTiles(2,0,1)
tile3 = BoardTiles(3,0,2)
tile4 = BoardTiles(4,1,0)
tile5 = BoardTiles(5,1,1)
tile6 = BoardTiles(6,1,2)
tile7 = BoardTiles(7,2,0)
tile8 = BoardTiles(8,2,1)
tile0 = BoardTiles(0,2,2)
winning_board = board.copy()
BoardTiles.board_randomiser()
game_over = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and not game_over:
				tile0.action_key('up')
			if event.key == pygame.K_DOWN and not game_over:
				tile0.action_key('down')
			if event.key == pygame.K_LEFT and not game_over:
				tile0.action_key('left')
			if event.key == pygame.K_RIGHT and not game_over:
				tile0.action_key('right')
			if event.key == pygame.K_s and not game_over:
				BoardTiles.auto_solve()
				

			if event.key == pygame.K_r:
				BoardTiles.board_randomiser()
				game_over = False

			if np.array_equal(winning_board,board):
				time.sleep(0.5)
				game_over = True

		BoardTiles.draw_lines()
		BoardTiles.draw_tiles()
		pygame.draw.rect(screen,BLACK_COLOR,pygame.Rect(tile0.y*200,tile0.x*200,200,200))
	if game_over:
		BoardTiles.game_over_screen()
	pygame.display.update()