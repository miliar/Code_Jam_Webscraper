
#include <iostream>
#include <string>
using namespace std;

void flip( string& S, int pos, int K ) {
  for( int i = 0; i < K; ++i ) {
    if( S[pos + i] == '-' ) S[pos + i] = '+';
    else S[pos + i] = '-';
  }
}

void main() {
  int T, K;
  string S;
  cin >> T;
  for( int iT = 1; iT <= T; ++iT ) {
    cin >> S >> K;
    int flips = 0;
    int lastK = S.size() - K;
    //cout << "\norig: " << S << K;
    for( int iS = 0; iS < lastK; ++iS ) {
      if( S[iS] == '-' ) {
        flip( S, iS, K );
        flips++;
        //cout << ", " << S;
      }
    }
    if( S[lastK] == '-' ) flips++;
    bool isGood = true;
    for( int iS = lastK + 1; iS < S.size(); ++iS ) {
      if( S[iS] != S[lastK] ) {
        isGood = false;
        break;
      }
    }
    if( isGood ) {
      cout << "Case #" << iT << ": " << flips << endl;
    }
    else {
      cout << "Case #" << iT << ": IMPOSSIBLE" << endl;
    }
  }

}

