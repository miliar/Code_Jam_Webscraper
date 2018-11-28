#include <vector>
#include <string>
#include <iostream>
#include <assert.h>

using namespace std;

typedef vector<string> CGrid;

static void fill( int x0, int x1, int y0, int y1, char c, CGrid& g )
{
  for( int i = y0; i <= y1; ++i ) {
    for( int j = x0; j <= x1; ++j ) {
      g[i][j] = c;
    }
  }
}

static char findFirstChar( int x0, int y0, const CGrid& g, int& x1, int&y1 )
{
  for( y1 = y0; y1 < g.size(); ++y1 ) {
    for( x1 = x0; x1 < g[0].size(); ++x1 ) {
      if( g[y1][x1] != '?' ) {
        return g[y1][x1];
      }
    }
  }
  assert( false );
  return ' ';
}

static bool hasEmptyCell( int x0, int y0, const CGrid& g )
{
  for( int y1 = y0; y1 < g.size(); ++y1 ) {
    for( int x1 = x0; x1 < g[0].size(); ++x1 ) {
      if( g[y1][x1] == '?' ) {
        return true;
      }
    }
  }
  return false;
}

static bool hasEmptyColumn( int x, int y0, int y1, const CGrid& g )
{
  for( int y = y0; y <= y1; ++y ) {
    if( g[y][x] != '?' ) {
      return false;
    }
  }
  return true;
}

static bool hasEmptyRow( int x0, int x1, int y, const CGrid& g )
{
  for( int x = x0; x <= x1; ++x ) {
    if( g[y][x] != '?' ) {
      return false;
    }
  }
  return true;
}

static void solve( int x0, int y0, CGrid& grid )
{
  const int r = grid.size();
  const int c = grid[0].size();
  if( x0 == c || y0 == r ) {
    return;
  }
  if( !hasEmptyCell( x0, y0, grid ) ) {
    return;
  }

  int x1, y1;
  const char letter = findFirstChar( x0, y0, grid, x1, y1 );
  while( x1 + 1 < c && hasEmptyColumn( x1 + 1, y0, y1, grid ) ) {
    x1++;
  }
  while( y1 + 1 < r && hasEmptyRow( x0, x1, y1 + 1, grid ) ) {
    y1++;
  }
  fill( x0, x1, y0, y1, letter, grid );

  solve( x1+1, y0, grid );
  solve( x0, y1+1, grid );
}

int main()
{
  int t;
  cin >> t;
  for( int i = 0; i < t; ++i ) {
    int r, c;
    cin >> r >> c;
    vector<string> grid( r );
    for( int j = 0; j < r; ++j ) {
      cin >> grid[j];
    }
    solve( 0, 0, grid );
    assert( !hasEmptyCell( 0, 0, grid ) );

    cout << "Case #" << (i+1) << ":" << endl;
    for( int j = 0; j < r; ++j ) {
      cout << grid[j] << endl;
    }
  }

  return 0;
}