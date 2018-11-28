#include <iostream>
#include <string>
#include <vector>
#include <limits>
#include <cassert>

using namespace std;

int R, C;
char CAKE[25][25];
bool initialIsUsed[256];

int fillCakeR( char in, int r, int c, int dj ) {
  int j = c + dj;
  for( ; j >= 0 && j < C; j += dj ) {
    if( CAKE[r][j] == '?' ) {
      CAKE[r][j] = in;
    }
    else {
      return j - dj;
    }
  }
  return j - dj;
}

void fillCakeC( char initial, int r, int di, int j1, int j2 ) {
  int i = r + di;
  for( ; i >= 0 && i < R; i += di ) {
    bool lineIsEmpty = true;
    for( int j = j1; j <= j2; j++ ) {
      if( CAKE[i][j] != '?' ) {
        lineIsEmpty = false;
      }
    }
    if( lineIsEmpty ) {
      for( int j = j1; j <= j2; j++ ) {
        CAKE[i][j] = initial;
      }
    }
    else {
      return;
    }
  }
}

void print( int t ) {
  cout << "Case #" << t << ":";
  for( int i = 0; i < R; i++ ) {
    cout << "\n";
    for( int j = 0; j < C; j++ ) {
      cout << CAKE[i][j];
    }
  }
  cout << "\n";
}

void main() {
  int T;
  cin >> T;

  for( int t = 1; t <= T; t++ ) {
    for( int i = 0; i < 256; i++ ) initialIsUsed[i] = false;

    cin >> R >> C;
    for( int i = 0; i < R; i++ ) {
      for( int j = 0; j < C; j++ ) {
        cin >> CAKE[i][j];
      }
    }

    for( int i = 0; i < R; i++ ) {
      for( int j = 0; j < C; j++ ) {
        char initial = CAKE[i][j];
        if( initial != '?' && initialIsUsed[initial] == false ) {
          int j1 = fillCakeR( initial, i, j, -1 );
          int j2 = fillCakeR( initial, i, j, +1 );
          //print(t);
          fillCakeC( initial, i, -1, j1, j2 );
          fillCakeC( initial, i, +1, j1, j2 );
          initialIsUsed[initial] = true;
          //print( t );
          //cout << "\n";
          j = j2;
        }
      }
    }
    print( t );
  }
}
