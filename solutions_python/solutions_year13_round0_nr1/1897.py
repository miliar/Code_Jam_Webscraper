#!/usr/bin/python
"""Problem A. Tic-Tac-Toe-Tomek
   author: hkpeprah"""

class TomekBoard:
    """A tomek board for playing the Tic-Tac-Toe Tomek game"""
    def __init__( this, plays ):
        """Copies over the plays already made."""
        full = True
        for p in plays: full = ( False if p == "." else full )
        """Assign variables."""
        this.plays = plays
        this.boardFull = full
        this.players = [ "X", "O" ]
        this.wildcard = "T"
        this.winningPlays = [ [[0, 4, 8, 12], 1], [[0, 1, 2, 3], 4], [[0], 5], [[12], -3]]

    def determineWinner(this):
        """Determines who has won, if it is a draw or if the game has yet to finish."""
        for player in this.players:
            """Chech horizontals, vertical and diagonal possibilities."""
            for row in this.winningPlays:
                for initial in row[0]:
                    won = True
                    for square in xrange(initial, initial + 4 * row[1], row[1]):
                        if not( this.plays[square] == this.wildcard or this.plays[square] == player ):
                            won = False
                            break
                    if won: return player + " won"
        if this.boardFull: return "Draw"
        else: return "Game has not completed"


if __name__ == "__main__":
    """Read in the number of test cases, then solve them one-by-one."""
    T = int(raw_input())
    cases = 1
    while ( cases <= T ):
        blocks = []
        for x in xrange(0, 4): 
            token = raw_input()
            for ch in token: blocks.append(ch)
        board = TomekBoard(blocks)
        print "Case #%s: %s"%(str(cases), board.determineWinner())
        cases = cases + 1
        if ( cases <= T ): raw_input()
