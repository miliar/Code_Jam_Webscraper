#include <iostream>
#include <string>
using namespace std;

string str;
string S;
int K;

int firstMinusFromStartIndex( int aStartInd ) {
  for( int i = aStartInd; i < S.size(); i++ ) {
    if( S[i] == '-' ) {
      return i;
    }
  }
  return -1;
}

bool flip( int aStartInd ) {
  int stopInd = aStartInd + K;
  if( stopInd > S.size() ) return false;
  for( int i = aStartInd; i < stopInd; i++ ) {
    char c = '-';
    if( S[i] == '-' ) c = '+';
    S[i] = c;
  }
  return true;
}

int solve(const string& aStr) {
  int numOfFlips = 0;
  int i = firstMinusFromStartIndex( 0 );
  while( i != -1 ) {
    bool ok = flip( i );
    if( !ok ) {
      return -1;
    }
    numOfFlips++;
    i = firstMinusFromStartIndex( i + 1 );
  }
  return numOfFlips;
}

void main() {
  int t;
  cin >> t;
  const int NumOfCases = t + 1;

  for( int i = 1; i < NumOfCases; i++ ) {
    cin >> S;
    cin >> K;
    int numOfFlips = solve( str );
    cout << "\nCase #" << i << ": ";
    if( numOfFlips == -1 ) {
      cout << "IMPOSSIBLE";
    }
    else {
      cout << numOfFlips;
    }
  }
}