
#include <iostream>
#include <vector>

typedef long long ll;

int R;
int C;

struct Cell {
    Cell(): laserH(-1), laserV(-1),state(0) {}
    int state;
    int laserH;
    int laserV;
};

struct Laser {
    std::vector<Cell*> h;
    std::vector<Cell*> v;
    int r;
    int c;
    bool done;
};

int f(int a, int b)
{
    return a*C + b;
}



void solve()
{
    std::cin >> R >> C;
    std::vector< std::vector<char> > dat( R , std::vector<char>( C ) );
    for ( int i = 0 ; i < R ; ++i )
        for ( int j = 0 ; j < C ; ++j ) {
            std::cin >> dat[ i ][ j ];
            if ( dat[i][j] == '|' || dat[i][j] == '-' )
                dat[i][j] = '?';
        }

    /*
      Strategy:
      - if a cell gets hit twice vertically or twice horizontally, that tells us those laser positions.
      - if a cell gets hit 0x vertically or 0x horizontally, that tells us a laser position since we must hit it from the other side.

      - if we figure out a laser position, we need to update our hit counts for all cells.

      - if ALL remaining cells have 1 from each side.......?
      is it safe to just put all remaining lasers vertically? Yes for small, no for large.
     */

    std::vector< std::vector<Cell> > cells( R , std::vector<Cell>( C ) );
    for ( int i = 0 ; i < R ; ++i )
        for ( int j = 0 ; j < C ; ++j )
            if ( dat[i][j] == '.' )
                cells[i][j].state = 1;

    std::vector<Laser> lasers;
    for ( int r = 0 ; r < R ; ++r )
        for ( int c = 0 ; c < C ; ++c )
            if ( dat[r][c] == '?' ) {
                // do I hit another laser horizontally?
                bool laserH = false;
                {
                int stepC = 1;
                while ( c + stepC < C && dat[ r ][ c+stepC ] != '#' ) {
                    if ( dat[ r ][ c+stepC ] != '.' ) {
                        laserH = true;
                        break;
                    }
                    ++stepC;
                }
                stepC = -1;
                while ( c + stepC >= 0 && dat[ r ][ c+stepC ] != '#' ) {
                    if ( dat[ r ][ c+stepC ] != '.' ) {
                        laserH = true;
                        break;
                    }
                    --stepC;
                }
                }
                // what about vertically?
                bool laserV = false;
                {
                int stepR = 1;
                while ( r + stepR < R && dat[ r+stepR ][ c ] != '#' ) {
                    if ( dat[ r+stepR ][ c ] != '.' ) {
                        laserV = true;
                        break;
                    }
                    ++stepR;
                }
                stepR = -1;
                while ( r + stepR >= 0 && dat[ r+stepR ][ c ] != '#' ) {
                    if ( dat[ r+stepR ][ c ] != '.' ) {
                        laserV = true;
                        break;
                    }
                    --stepR;
                }
                }

                if ( laserH && laserV ) {
                    std::cout << "IMPOSSIBLE\n";
                    return;
                }
                if ( laserH || laserV ) {
                    if ( laserH ) {
                        // this laser absolutely must be in '|' position.
                        dat[r][c] = '|';
                        // set those cells as seen.
                        int stepR = 1;
                        while ( r + stepR < R && dat[ r+stepR ][ c ] != '#' ) {
                            cells[ r+stepR ][ c ].state = 2;
                            ++stepR;
                        }
                        stepR = -1;
                        while ( r + stepR >= 0 && dat[ r+stepR ][ c ] != '#' ) {
                            cells[ r+stepR ][ c ].state = 2;
                            --stepR;
                        }
                    } else {
                        // laserV.
                        dat[r][c] = '-';
                        
                        int stepC = 1;
                        while ( c + stepC < C && dat[ r ][ c+stepC ] != '#' ) {
                            cells[ r ][ c+stepC ].state = 2;
                            ++stepC;
                        }
                        stepC = -1;
                        while ( c + stepC >= 0 && dat[ r ][ c+stepC ] != '#' ) {
                            cells[ r ][ c+stepC ].state = 2;
                            --stepC;
                        }
                    }
                } else {
                    // this laser doesn't see other lasers,
                    // so either position could be possible.
                    lasers.emplace_back();
                    int lid = lasers.size()-1; // "laser ID"
                    Laser& L = lasers.back();
                    L.r = r; L.c = c;
                    {
                    int stepC = 1;
                    while ( c + stepC < C && dat[ r ][ c+stepC ] != '#' ) {
                        cells[ r ][ c+stepC ].laserH = lid;
                        L.h.push_back( &cells[ r ][ c+stepC ] );
                        ++stepC;
                    }
                    stepC = -1;
                    while ( c + stepC >= 0 && dat[ r ][ c+stepC ] != '#' ) {
                        cells[ r ][ c+stepC ].laserH = lid;
                        L.h.push_back( &cells[ r ][ c+stepC ] );
                        --stepC;
                    }
                    }
                    {
                    int stepR = 1;
                    while ( r + stepR < R && dat[ r+stepR ][ c ] != '#' ) {
                        cells[ r+stepR ][ c ].laserV = lid;
                        L.v.push_back( &cells[ r+stepR ][ c ] );
                        ++stepR;
                    }
                    stepR = -1;
                    while ( r + stepR >= 0 && dat[ r+stepR ][ c ] != '#' ) {
                        cells[ r+stepR ][ c ].laserV = lid;
                        L.v.push_back( &cells[ r+stepR ][ c ] );
                        --stepR;
                    }
                    }
                }
            }

    // now start solving.
    // if a cell with state == 1 gets hit by 0 lasers from a direction,
    // that forces the other laser.
    bool done = false;
    while ( !done ) {
        done = true;
        // any new cells to be adjusted?
        for ( int r = 0 ; r < R && done ; ++r )
            for ( int c = 0 ; c < C && done ; ++c ) {
                if ( cells[r][c].state == 1 &&
                    (cells[r][c].laserH == -1 && cells[r][c].laserV == -1) ) {
                    // this cell can no longer be hit at all.
                    std::cout << "IMPOSSIBLE\n";
                    return;
                }
                if ( cells[r][c].state == 1 &&
                    (cells[r][c].laserH == -1 || cells[r][c].laserV == -1) ) {
                    if ( cells[r][c].laserH == -1 ) {
                        // that VERTICAL laser definitely needs to point this way.
                        int lid = cells[r][c].laserV;
                        Laser& L = lasers[ lid ];
                        dat[ L.r ][ L.c ] = '|';
                        // now update cells.
                        // cells that are now definitely hit should be set to state 2.
                        
                        {
                            int stepR = 1;
                            while ( L.r + stepR < R && dat[ L.r+stepR ][ L.c ] != '#' ) {
                                cells[ L.r+stepR ][ L.c ].state = 2;
                                ++stepR;
                            }
                            stepR = -1;
                            while ( L.r + stepR >= 0 && dat[ L.r+stepR ][ L.c ] != '#' ) {
                                cells[ L.r+stepR ][ L.c ].state = 2;
                            --stepR;
                            }
                        }
                        // cells that are now definitely not hit should be set to
                        // laserH = -1.
                        {
                            int stepC = 1;
                            while ( L.c + stepC < C && dat[ L.r ][ L.c+stepC ] != '#' ) {
                                cells[ L.r ][ L.c+stepC ].laserH = -1;
                                ++stepC;
                            }
                            stepC = -1;
                            while ( L.c + stepC >= 0 && dat[ L.r ][ L.c+stepC ] != '#' ) {
                                cells[ L.r ][ L.c+stepC ].laserH = -1;
                                --stepC;
                            }
                        }
                        lasers[lid].done = true;
                    } else {
                        // that HORIZONTAL laser definitely needs to point this way.
                        int lid = cells[r][c].laserH;
                        Laser& L = lasers[ lid ];
                        dat[ L.r ][ L.c ] = '-';
                        // now update cells.
                        // cells that are now definitely hit should be set to state 2.
                        {
                        int stepC = 1;
                        while ( L.c + stepC < C && dat[ L.r ][ L.c+stepC ] != '#' ) {
                            cells[ L.r ][ L.c+stepC ].state = 2;
                            ++stepC;
                        }
                        stepC = -1;
                        while ( L.c + stepC >= 0 && dat[ L.r ][ L.c+stepC ] != '#' ) {
                            cells[ L.r ][ L.c+stepC ].state = 2;
                            --stepC;
                        }
                        }
                        // cells that are now definitely not hit should be set to
                        // laserV = -1.
                        {
                        int stepR = 1;
                        while ( L.r + stepR < R && dat[ L.r+stepR ][ L.c ] != '#' ) {
                            cells[ L.r+stepR ][ L.c ].laserV = -1;
                            ++stepR;
                        }
                        stepR = -1;
                        while ( L.r + stepR >= 0 && dat[ L.r+stepR ][ L.c ] != '#' ) {
                            cells[ L.r+stepR ][ L.c ].laserV = -1;
                            --stepR;
                        }
                        }
                        lasers[lid].done = true;
                    }
                    // done updating this laser's position.
                    done = false;
                    continue;
                }
                // if we're here, this cell can't currently be deduced.
            }
    }
    // all remaining cells are hit from both sides.
    // just set remaining lasers to |.
    for ( int i = 0 ; i < lasers.size() ; ++i ) {
        if ( lasers[i].done == true )
            continue;
        Laser& L = lasers[ i ];
        dat[ L.r ][ L.c ] = '|';
    }

    // now print the result.

    std::cout << "POSSIBLE\n";
    for ( int r = 0 ; r < R ; ++r ) {
        for ( int c = 0 ; c < C ; ++c ) {
            std::cout << dat[r][c];
        }
        std::cout << '\n';
    }
    return;
}

int main()
{
    int T;
    std::cin >> T;
    for ( int testID = 1 ; testID <= T ; ++testID ) {

        std::cout << "Case #" << testID << ": ";
        
        solve();
    }

    return 0;
}
