from Pieces import *

class Chess2Py:

	pieceDict = {}
	currentTeam = 0

	def __init__(self):
		self.addChessPieces()
		self.playerTurn(True)
		
	def printBoard(self):
		boardString = "  0  1  2  3  4  5  6  7"
		for y in range(0,8):
			boardString += "|\n" + str(y)
			for x in range(0,8):
				content = "XX"
				if (x,y) in self.pieceDict:
					content = self.pieceDict[(x,y)].name
				elif (y+x)%2 == 0:
					content = "  "
				boardString += "|" + str(content)

		print boardString + "|"

	def playerTurn(self,newTurn):
		
		if newTurn:
			self.printBoard()
			print("player %s's turn" % self.currentTeam)

		playerInput = raw_input("move string [xyxy]: ")

		fromSquare = (int(playerInput[0]),int(playerInput[1]))
		toSquare = (int(playerInput[2]),int(playerInput[3]))

		self.evaluateMove(fromSquare,toSquare)
		
	def evaluateMove(self,fromSquare,toSquare):

		#calculate the move relative to the current position on the board
		move = (toSquare[0] - fromSquare[0], toSquare[1] - fromSquare[1])
		piece = None
		#if the space is blank
		if (fromSquare[0],fromSquare[1]) in self.pieceDict:
			piece = self.pieceDict[(fromSquare[0],fromSquare[1])]

			if not piece.team == self.currentTeam: 
				print "not your piece"
				self.playerTurn(False)

			#check that moving the peice to the square is a valid move 
			elif not piece.validMove(move,fromSquare,toSquare,self.pieceDict):
				print "invalid move"
				self.playerTurn(False)

			else:
				#move the piece
				self.pieceDict[(toSquare[0],toSquare[1])] = piece
				#set moved to true (used for pawns first move and castling)
				self.pieceDict[(toSquare[0],toSquare[1])].moved = True
				#delete the old piece
				del self.pieceDict[(fromSquare[0],fromSquare[1])]

				#change the current team
				self.currentTeam = abs(self.currentTeam - 1)

			self.playerTurn(True)

		else:
			print "No piece there!"
			self.playerTurn(False)

	


	def addPiece(self,square,piece):
		self.pieceDict[square] = piece

	def addChessPieces(self):
		for i in range(0,9):
			self.addPiece((i,1),Pawn(1))
			self.addPiece((i,6),Pawn(0))

		#white	
		self.addPiece((0,7),Rook(0))
		self.addPiece((1,7),Knight(0))
		self.addPiece((2,7),Bishop(0))
		self.addPiece((3,7),Queen(0))
		self.addPiece((4,7),King(0))
		self.addPiece((5,7),Bishop(0))
		self.addPiece((6,7),Knight(0))
		self.addPiece((7,7),Rook(0))

		#black
		self.addPiece((0,0),Rook(1))
		self.addPiece((1,0),Knight(1))
		self.addPiece((2,0),Bishop(1))
		self.addPiece((3,0),King(1))
		self.addPiece((4,0),Queen(1))
		self.addPiece((5,0),Bishop(1))
		self.addPiece((6,0),Knight(1))
		self.addPiece((7,0),Rook(1))


if __name__ == '__main__':
	Chess2Py()
