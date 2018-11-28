#include <iostream>
#include <assert.h>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

typedef map<char, int> CColorCounts;

static bool chooseNextColor( char lastColor, CColorCounts& initialCounts, CColorCounts& counts, char& color )
{
  if( lastColor == 'G' ) {
    color = 'R';
  } else if( lastColor == 'O' ) {
    color = 'B';
  } else if( lastColor == 'V' ) {
    color = 'Y';
  } else if( lastColor == 'R' ) {
    if( counts['G'] > 0 ) {
      color = 'G';
    } else {
      if( make_pair( counts['Y'], initialCounts['Y'] ) >= make_pair( counts['B'], initialCounts['B'] ) ) {
        color = 'Y';
      } else {
        color = 'B';
      }
    }
  } else if( lastColor == 'Y' ) {
    if( counts['V'] > 0 ) {
      color = 'V';
    } else {
      if( make_pair( counts['R'], initialCounts['R'] ) >= make_pair( counts['B'], initialCounts['B'] ) ) {
        color = 'R';
      } else {
        color = 'B';
      }
    }
  } else if( lastColor == 'B' ) {
    if( counts['O'] > 0 ) {
      color = 'O';
    } else {
      if( make_pair( counts['R'], initialCounts['R'] ) >= make_pair( counts['Y'], initialCounts['Y'] ) ) {
        color = 'R';
      } else {
        color = 'Y';
      }
    }
  } else {
    if( counts['R'] >= max( counts['Y'], counts['B'] ) ) {
      color = 'R';
    } else if( counts['Y'] >= max( counts['R'], counts['B'] ) ) {
      color = 'Y';
    } else {
      color = 'B';
    }
  }
  if( counts[ color ] == 0 ) {
    return false;
  }
  counts[color]--;
  return true;
}

static bool solve( int N, CColorCounts counts, string& result )
{
  CColorCounts initCounts = counts;
  char lastColor = ' ';
  for( int i = 0; i < N; ++i ) {
    char color;
    if( !chooseNextColor( lastColor, initCounts, counts, color ) ) {
      return false;
    }
    result += color;
    lastColor = color;
  }
  assert( result.size() == N );
  if( result[0] == result[ N - 1 ] ) {
    return false;
  }
  return true;
}

int main()
{
  int t;
  cin >> t;
  for( int i = 0; i < t; ++i ) {
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    CColorCounts counts;
    counts['R'] = R;
    counts['O'] = O;
    counts['Y'] = Y;
    counts['G'] = G;
    counts['B'] = B;
    counts['V'] = V;
    
    cout << "Case #" << (i+1) << ": ";
    string s;
    if( !solve( N, counts, s ) ) {
      cout << "IMPOSSIBLE";
    } else {
      cout << s;
    }
    cout << endl;
  }

  return 0;
}