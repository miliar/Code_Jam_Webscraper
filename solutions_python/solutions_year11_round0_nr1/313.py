import os
import sys

class Bot:
    def __init__( self ):        
        self.position = 1

    def act( self, goal, wait ):
        if goal is None:
            return -2
        
        if self.position == goal:
            return self.position if not wait else -1
        else:
            if self.position < goal:
                self.position += 1
            else:
                self.position -= 1

            return 0
            
        
def main():
    totalCaseCount = int( sys.stdin.readline().strip( '\r\n' ) )

    for index in range( totalCaseCount ):
        case = sys.stdin.readline().strip( '\r\n' ).split()
        
        cmdList = list()        
        cmdCount = int( case[ 0 ] )

        for i in range( cmdCount ):
            botColor = case[ 2 * i + 1 ]
            botPosition = int( case[ 2 * i + 2 ] )
            
            cmdList.append( ( botColor, botPosition ) )

        botOrange = Bot()
        botBlue = Bot()        

        tick = 0

        while True:
            tick += 1

            botOrangeGoal = None
            botOrangeWait = None
            botBlueGoal = None
            botBlueWait = None

            for i, cmd in enumerate( cmdList ):
                color, button = cmd

                if botOrangeGoal is None and color == 'O':
                    botOrangeGoal = button
                    botOrangeWait = ( i > 0 )

                if botBlueGoal is None and color == 'B':
                    botBlueGoal = button
                    botBlueWait = ( i > 0 )

                if botOrangeGoal is None or botBlueGoal is None: continue
                break

            botOrangeRet = botOrange.act( botOrangeGoal, botOrangeWait )
            botBlueRet = botBlue.act( botBlueGoal, botBlueWait )

            if botOrangeRet > 0 or botBlueRet > 0:
                cmdList.pop( 0 )
                
            if len( cmdList ) == 0:
                break

        print( 'Case #{}: {}'.format( index + 1, tick ) )

if __name__ == '__main__':
    main()
