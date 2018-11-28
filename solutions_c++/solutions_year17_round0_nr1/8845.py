/*
 * Name: Serena Shi
 * Date: 4/7/2017
 */

#include <iostream>
#include <string>

using namespace std;

bool ifFlipped( const string & s ) {
  for( int i = 0; i < s.size(); i++ ) {
    if( s.at(i) == '-' )
      return false;
  }

  return true;
}

int main() {
  int t, k;
  string s;

  // get the number of test cases
  cin >> t;

  // iterate through test cases
  for( int i = 1; i <= t; i++ ) {
    // get input for string and for number of pancakes
    cin >> s >> k;

    int flips = 0;

    // do all the flipping
    for( int j = 0; j <= s.size() - k; j++ ) {
      if( s.at(j) == '-' ) {
        for( int l = 0; l < k; l++ ) {
          if( s.at( j + l ) == '-' )
            s.at( j + l ) = '+';
          else
            s.at( j + l ) = '-';
        }
        flips++;
      }
    }

    // check if all flipped
    if( ifFlipped(s) )
      cout << "Case #" << i << ": " << flips << endl;
    else
      cout << "Case #" << i << ": IMPOSSIBLE" << endl;
  }

  return 0;
}
