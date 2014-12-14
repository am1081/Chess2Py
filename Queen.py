from Piece import Piece 

class Queen(Piece):

	def __init__(self,team):
		self.name = "Q" + str(team)
		Piece.__init__(self,team)

	#for pawn and king make sure to include the special moves
	def validMove(self,move):

		anyDiagonal = abs(move[0]) == abs(move[1])
		anyVertical = move[0] == 0 and abs(move[1]) > 0
		anyHorizontal = move[1] == 0 and abs(move[0]) > 0

		if anyDiagonal or anyVertical or anyHorizontal:
			return True

