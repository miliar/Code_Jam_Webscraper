#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

struct Rect
{
    int i;
    int j;
    int w;
    int h;
};

bool spread( vector<string>& cake, int i, int j, char c, bool isRow ) {
    bool res = false;
    if ( !isRow && i < cake.size() && cake[ i + 1 ][ j ] == '?' ) {
        cake[ i + 1 ][ j ] = c;
        spread( cake, i + 1, j, c, isRow );
        res = true;
    }
    if ( !isRow && i > 0 && cake[ i - 1 ][ j ] == '?' ) {
        cake[ i - 1 ][ j ] = c;
        spread( cake, i - 1, j, c, isRow );
        res = true;
    }
    if ( isRow && j < cake[ 0 ].size() && cake[ i ][ j + 1 ] == '?' ) {
        cake[ i ][ j + 1 ] = c;
        spread( cake, i, j + 1, c, isRow );
        res = true;
    }
    if ( isRow && j > 0 && cake[ i ][ j - 1 ] == '?' ) {
        cake[ i ][ j - 1 ] = c;
        spread( cake, i, j - 1, c, isRow );
        res = true;
    }
    return res;
}

bool checkRect( vector<string>& cake, char c, Rect r ) {
    for ( int i = r.i; i < r.i + r.h; ++i ) {
        for ( int j = r.j; j < r.j + r.w; ++j ) {
            if ( cake[ i ][ j ] == '?' || cake[ i ][ j ] == c ) {
                //cake[ i ][ j ] = c;
            }
            else
            {
                return false;
            }
        }
    }
    return true;
}

void maximizeRect( vector<string>& cake, char c, Rect rect ) {
    // try up
    while ( rect.i > 0 ) {
        Rect newRect = rect;
        newRect.i--;
        newRect.h++;
        if ( !checkRect( cake, c, newRect ) ) {
            break;
        } else {
            rect = newRect;
        }
    }
    // try right
    while ( rect.j + rect.w < cake[ 0 ].size() ) {
        Rect newRect = rect;
        newRect.w++;
        if ( !checkRect( cake, c, newRect ) ) {
            break;
        } else {
            rect = newRect;
        }
    }
    //try bot
    while ( rect.i + rect.h < cake.size() ) {
        Rect newRect = rect;
        newRect.h++;
        if ( !checkRect( cake, c, newRect ) ) {
            break;
        } else {
            rect = newRect;
        }
    }
    // Try left
    while ( rect.j > 0 ) {
        Rect newRect = rect;
        newRect.j--;
        newRect.w++;
        if ( !checkRect( cake, c, newRect ) ) {
            break;
        } else {
            rect = newRect;
        }
    }

    for ( int i = rect.i; i < rect.i + rect.h; ++i ) {
        for ( int j = rect.j; j < rect.j + rect.w; ++j ) {
            cake[ i ][ j ] = c;
        }
    }
}

int main( int argc, char** argv )
{
    if ( argc < 2 ) {
        cout << "NG." << endl;
        return 0;
    }

    ifstream fin( argv[ 1 ] );
    ofstream fout( "A.out" );

    int T;
    fin >> T;
    for ( int testNum = 1; testNum <= T; ++testNum ) {
        int r, c;
        fin >> r >> c;
        vector<string> cake( r );
        for ( int i = 0; i < r; ++i ) {
            fin >> cake[ i ];
        }

        std::set<char> maximized;

        for ( int i = 0; i < r; ++i ) {
            for ( int j = 0; j < c; ++j ) {
                if ( cake[ i ][ j ] != '?' && !maximized.count( cake[ i ][ j ] ) ) {
                    maximizeRect( cake, cake[ i ][ j ], Rect { i, j, 1, 1 } );
                    maximized.insert( cake[ i ][ j ] );
                    /*if ( spread( cake, i, j, cake[ i ][ j ], true ) ) {
                        spread( cake, i, j, cake[ i ][ j ], false );
                    }*/
                }
            }
        }

        fout << "Case #" << testNum << ":\n";
        for ( int i = 0; i < r; ++i ) {
            fout << cake[ i ] << "\n";
        }
    }

    return 0;
}
