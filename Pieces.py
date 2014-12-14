from collections import namedtuple

class Piece:

	name = None

	def __init__(self,team):
		self.team = team
		self.moved = False

	def validMove(self,move):
		raise NotImplementedError("This needs to be implemented!")

	def isPathClear(self,move,currentSquare,toSquare,pieceDict):

		print move
		#calculate the range of squares to be checked
		if move[0] > 0:
			xRange = range(currentSquare[0]+1,toSquare[0]+1)
		else:
			xRange = range(currentSquare[0]-1,toSquare[0]-1,-1)
		print xRange 
		if move[1] > 0:
			yRange = range(currentSquare[1]+1,toSquare[1]+1)
		else:
			yRange = range(currentSquare[1]-1,toSquare[1]-1,-1)
		print yRange

		if abs(move[0]) == abs(move[1]):
			for i in range(0,len(xRange)):
				if not self.squareEmpty(xRange[i],yRange[i],currentSquare,toSquare,pieceDict):
					return False
		else:
			for x in xRange:
				for y in yRange:
					if not self.squareEmpty(x,y,currentSquare,toSquare,pieceDict):
						return False
		return True

	def squareEmpty(self,x,y,currentSquare,toSquare,pieceDict):
		#if the board square isn't blank
		print (x,y)
		if (x,y) in pieceDict:

			#if this isn't the final move or the piece is friendly 
			if not (x == toSquare[0] and y == toSquare[1]) or pieceDict[(x,y)].team == pieceDict[currentSquare].team:
				return False
		return True
			
class Queen(Piece):

	def __init__(self,team):
		self.name = "Q" + str(team)
		Piece.__init__(self,team)

	#for pawn and king make sure to include the special moves
	def validMove(self,move,currentSquare,toSquare,pieceDict):

		anyDiagonal = abs(move[0]) == abs(move[1])
		anyVertical = move[0] == 0 and abs(move[1]) > 0
		anyHorizontal = move[1] == 0 and abs(move[0]) > 0
		pathClear = self.isPathClear(move,currentSquare,toSquare,pieceDict)

		if (anyDiagonal or anyVertical or anyHorizontal) and pathClear:
			return True
		else: 
			return False

class Pawn(Piece):

	def __init__(self,team):
		self.name = "p" + str(team)	
		Piece.__init__(self,team)


	#for pawn and king make sure to include the special moves
	def validMove(self,move,currentSquare,toSquare,pieceDict):
		if self.team == 1:
			multiplier = 1
		else: 
			multiplier = -1

		diagonalUp = abs(move[0]) == 1 and multiplier*move[1] == 1 and toSquare in pieceDict #this makes sure the pawn can only move diagonaly if there is a piece to take
		vertical_1 = move[0] == 0 and multiplier*move[1] == 1 and not toSquare in pieceDict
		vertical_2 = move[0] == 0 and multiplier*move[1] == 2 and self.moved == False and not toSquare in pieceDict

		pathClear = self.isPathClear(move,currentSquare,toSquare,pieceDict)

		if (diagonalUp or vertical_1 or vertical_2) and pathClear:
			self.moved = True
			return True
		else: 
			return False

class Rook(Piece):

	def __init__(self,team):
		self.name = "R" + str(team)
		Piece.__init__(self,team)

	#for pawn and king make sure to include the special moves
	def validMove(self,move,currentSquare,toSquare,pieceDict):

		anyVertical = move[0] == 0 and abs(move[1]) > 0
		anyHorizontal = move[1] == 0 and abs(move[0]) > 0
		pathClear = self.isPathClear(move,currentSquare,toSquare,pieceDict)

		if (anyVertical or anyHorizontal) and pathClear:
			return True
		else: 
			return False

class Bishop(Piece):

	def __init__(self,team):
		self.name = "B" + str(team)
		Piece.__init__(self,team)

	#for pawn and king make sure to include the special moves
	def validMove(self,move,currentSquare,toSquare,pieceDict):

		anyDiagonal = abs(move[0]) == abs(move[1])
		pathClear = self.isPathClear(move,currentSquare,toSquare,pieceDict)

		if anyDiagonal and pathClear:
			return True
		else: 
			return False

class King(Piece):

	def __init__(self,team):
		self.name = "K" + str(team)	
		Piece.__init__(self,team)


	#for pawn and king make sure to include the special moves
	def validMove(self,move,currentSquare,toSquare,pieceDict):
		diagonal_1 = abs(move[0]) == abs(move[1]) == 1
		vertical_1 = move[0] == 0 and abs(move[1]) == 1
		horizontal_1 = move[1] == 0 and abs(move[0]) == 1
		pathClear = self.isPathClear(move,currentSquare,toSquare,pieceDict)

		if (anyDiagonal or anyVertical or anyHorizontal) and pathClear:
			return True
		else: 
			return False

class Knight(Piece):

	def __init__(self,team):
		self.name = "k" + str(team)	
		Piece.__init__(self,team)


	#for pawn and king make sure to include the special moves
	def validMove(self,move,currentSquare,toSquare,pieceDict):
		horizontal_L = abs(move[0]) == 2 and abs(move[1]) == 1
		vertical_L = abs(move[0]) == 1 and abs(move[1]) == 2
		pathClear = self.squareEmpty(toSquare[0],toSquare[1],currentSquare,toSquare,pieceDict) #knights can jump over things so we dont need to check if the route is clear

		if (horizontal_L or vertical_L) and pathClear:
			return True
		else: 
			return False


