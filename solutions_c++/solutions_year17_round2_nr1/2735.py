
#include <iostream>
#include <memory>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;


void main() {
  int T;
  cin >> T;
  for( int iT = 1; iT <= T; ++iT ) {
    cout << "Case #" << iT << ": ";
    stringstream msg;
    

    int D, N;
    cin >> D >> N;
    vector<int> K( N, 0 ), S( N, 0 );
    for( int i = 0; i < N; ++i ) {
      cin >> K[i] >> S[i];
    }

    double worstTime = -1.;
    for( int i = 0; i < N; ++i ) {
      double thisTime = ( double )( D - K[i] ) / ( double )S[i];
      if( worstTime < 0 || thisTime > worstTime ) {
        worstTime = thisTime;
      }
    }

    double result = ( double )D / worstTime;
    
    //msg.precision( 6 );
    cout.precision( 16 );
    cout << result << endl;
  }

}

