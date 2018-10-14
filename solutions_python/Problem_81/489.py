'''
Created on 21.05.2011

@author: pavlo
'''


import os

class TeamStats( ):
    wp = 0;
    owp = 0;
    oowp = 0;
    oponents = [ ];
    
    def __init__( self, wp = 0, owp = 0, oowp = 0, oponents = [ ] ):
        self.wp = wp;
        self.owp = owp;
        self.oowp = oowp;
        self.oponents = oponents;

def countRPI( wp, owp, oowp ):
    return ( 0.25 * wp ) + ( 0.5 * owp ) + ( 0.25 * oowp );

inputFile = open( os.path.join( os.path.dirname( __file__ ), 'A-large.in' ) );
outputFile = open( os.path.join( os.path.dirname( __file__ ), 'output.txt' ), 'w' );

numCases = int( inputFile.readline( ) );

for case in range( numCases ):
    numOfTeams = int( inputFile.readline( ) );
    schedule = [ ];
    teams = [ ];
    for t in range( numOfTeams ):
        teamInput = inputFile.readline( );
        numOfGames = 0;
        numOfWons = 0;
        wp = 0;
        oponents = [ ];
        schedule.append( teamInput );
        for i in range( numOfTeams ):
            if teamInput[ i ] == '.':
                continue;
            if teamInput[ i ] == '1':
                numOfWons += 1;
                numOfGames += 1;
                oponents.append( i );
                continue;
            if teamInput[ i ] == '0':
                numOfGames += 1;
                oponents.append( i );
        if not numOfGames == 0:
            wp = float( numOfWons ) / float( numOfGames );
        teams.append( TeamStats( wp = wp, oponents = oponents ) );
    for i in range( numOfTeams ):
        owp = 0;
        for j in range( numOfTeams ):
            if not j in teams[ i ].oponents:
                continue;
            if j == i:
                continue;
            wp = 0;
            gamesWon = 0;
            gamesPalyed = 0;
            for r in range( numOfTeams ): 
                if r == i:
                    continue;
                else:
                    if schedule[ j ][ r ] == '.':
                        continue;
                    if schedule[ j ][ r ] == '1':
                        gamesWon += 1;
                        gamesPalyed += 1;
                    if schedule[ j ][ r ] == '0':
                        gamesPalyed += 1;
            if not gamesPalyed == 0:
                wp = float( gamesWon ) / float( gamesPalyed );
            owp += wp;
        teams[ i ].owp = float( owp ) / float( len( teams[ i ].oponents ) );
    for i in range( numOfTeams ):
        oowp = 0;
        for opp in teams[ i ].oponents:
            oowp += teams[ opp ].owp;
        if not len( teams[ i ].oponents ) == 0:
            teams[ i ].oowp = float( oowp ) / len( teams[ i ].oponents );
    outputFile.write( 'Case #%s:\n' % str( case + 1 ) );
    for team in teams:
        outputFile.write( '%s\n' % str( countRPI( team.wp, team.owp, team.oowp ) ) );
print 'All Done';