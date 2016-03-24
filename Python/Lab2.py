#!/usr/bin/env python

import sys
import pickle


class Connect4:	
	
	def __init__(self,cols,rows,win):
			self.cols = cols
			self.rows = rows
			self.win = win
			self.board = [[0] * int(rows) for _ in range(int(cols))]

	def boardprint(self):		
		for x in range(0,self.cols):
			for y in range(0,self.rows):
				print self.board[y][x],
			print
		
	def isColFull(self,col):
		answer = True;
		for i in self.board[int(self.cols)-1]:
			if self.board[int(i)][col] == 0:
				answer = False
				break
		return answer

	def availableRow(self,col):
		answer = 0
		if not self.isColFull(col):
			for x in reversed(self.board[col]):
				if self.board[int(x)] == 0:
					answer = i
					break
		return answer
	
	def aval(self,col):
		#for y in range(int(self.rows), -1):
		for x in range(int(self.rows),0):
			if self.board[x][col] == 0:
				return int(self.board[x][col])
		
		
	def place_token(self, column, player):
		row = self.board[column]
		if row[0] != 0:
			raise Exception('that row is full game crashed')
		i = -1
		while row[i] != 0:
			i -= 1
		row[i] = player
		
		
	def inARowV(self, r, c):
		answer = False
		i = 0
		i = r
		count = 0
		if self.board[c][r] != 0:
			if (r+self.win) < self.rows:
				while count< self.win:
					if self.board[c][i] != self.board[c][r]:
						count = 0
						break
					else:
						count = count + 1
						i = i + 1
				if count == self.win:
					answer = True
					
		return answer
	
	def vertical(self):
		answer = False
		for r in range(0,self.rows):
			for c in range(0,self.cols):
				if self.inARowV(r,c):
					answer = True
					break
			if answer == True:
				break
		return answer
	
	def inARowH(self,r,c):
		answer = False
		i = 0
		i = c
		count = 0
		if self.board[c][r] != 0:
			if (c+self.win) < self.cols:
				while count < self.win:
					if self.board[i][r] != self.board[c][r]:
						count = 0
						break
					else:
						count = count + 1
						i = i +1
				if count == self.win:
					answer = True
		return answer
	
	def hori(self):
		answer = False
		for r in range(0,self.rows):
			for c in range(0,self.cols):
				if self.inARowH(r,c):
					answer = True
					break
			if answer == True:
				break
		return answer
	
	def diagUR(self,r,c):
		answer = False
		i = 0
		j = 0
		#i = r - 1
		#j = c + 1
		i = r
		j = c
		count = 0
		flag = False
		if self.board[c][r] != 0:
			while i>=0 and j <= self.rows and count < self.win:
				if self.board[j][i] != self.board[c][r]:
					flag = True
					break
				else:
					count = count + 1
					i = i - 1
					j = j + 1
			if count == self.win:
				answer = True
		return answer
	
	
	
	def diagDR(self,r,c):
		try:
			answer = False
			i = 0
			j = 0
			#i = r + 1
			#j = c + 1
			i = r
			j = c
			count = 0
			flag = False
			if self.board[c][r] != 0:
				while i<= self.rows and j <= self.cols and count < self.win:
					if self.board[j][i] != self.board[c][r]:
						flag = True
						break
					else:
						count = count + 1
						i = i + 1
						j = j + 1
				if count == self.win:
					answer = True
			return answer
		except IndexError:
			return False
	def diag(self):
		answer = False
		for r in range(0,self.rows-1):
			for c in range(0,self.cols-1):
				if self.diagUR(r,c) or self.diagDR(r,c):
					answer = True
					break
			if answer == True:
				break
		return answer
	
	def save(self):
		file_name = "testfile"
		fileObject = open(file_name,'wb')
		pickle.dump(self.board,fileObject)
		fileObject.close()
		
	def open(self):
		fileObject = open(file_name,'r')
		self.board = pickle.load(fileObject)
		
	
				


if __name__ == "__main__":	
	
	if len(sys.argv) == 4:
				
		rows = int(sys.argv[1])
		cols = int(sys.argv[2])
		win = int(sys.argv[3])-1
		game = Connect4(cols,rows,win)
		game.board = [[0] * int(rows) for _ in range(int(cols))]
		
		game.place_token(0,2)
		game.place_token(1,1)
		game.place_token(2,2)
		game.place_token(3,1)
		game.place_token(4,2)
		game.place_token(1,2)
		
		
		game.place_token(0,2)
		game.place_token(2,1)
		game.place_token(3,1)
		game.place_token(2,2)
		game.place_token(3,1)
		game.place_token(4,2)
		game.place_token(3,2)
		
		if (game.vertical() is True) or (game.hori() is True) or (game.diag() is True):
			print('Winner')
		#game.board[1][3] = 1
		game.boardprint()
		
	elif len(sys.argv) != 4:
		print "Wrong number of command line arguements"

	