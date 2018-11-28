#include <string>
#include <iostream>

using namespace std;

static bool flip( int k, string s, int& flipsCount )
{
  flipsCount = 0;
  for( int i = 0; i < s.length(); ++i ) {
    if( s[i] == '-' ) {
      if( i + k > s.size() ) {
        return false;
      }
      for( int j = i; j < i + k; ++j ) {
        if( s[j] == '+' ) {
          s[j] = '-';
        } else {
          s[j] = '+';
        }
      }
      flipsCount++;
    }
  }
  return true;
}

int main()
{
  int t;
  cin >> t;
  for( int i = 0; i < t; ++i ) {
    string s;
    int k;
    cin >> s >> k;

    cout << "Case #" << i+1 << ": "; 
    int flipsCount = 0;
    if( flip( k, s, flipsCount ) ) {
      cout << flipsCount << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}