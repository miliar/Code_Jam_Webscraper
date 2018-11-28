
#include <iostream>
#include <memory>
#include <vector>
#include <map>
#include <array>
#include <sstream>
#include <algorithm>
using namespace std;


void main() {
  int T;
  cin >> T;
  for( int iT = 1; iT <= T; ++iT ) {
    cout << "Case #" << iT << ": ";
    stringstream msg;
    msg.precision( 16 );
    cout.precision( 16 );
    
    int N, K;
    cin >> N >> K;

    double U;
    cin >> U;

    vector<double> P( N );
    for( int i = 0; i < N; ++i ) {
      double Pi;
      cin >> Pi;
      P[i] = Pi;
    }

    sort( P.begin(), P.end() );

    double tol = 1e-7;
    while( U > tol ) {
      int difPos = 0;
      while( P[difPos] - P[0] < tol ) {
        difPos++;
        if( difPos == P.size() ) break;
      }
      
      double difOne = 0.;
      double dif = 0.;
      if( difPos < P.size() ) {
        difOne = P[difPos] - P[0];
        dif = difOne * difPos;
      }

      if( dif > U || difPos == P.size() ) {
        dif = U;
        difOne = dif / difPos;
      }
      
      for( int i = 0; i < difPos; ++i ) {
        P[i] += difOne;
      }
      U -= dif;
    }

    double res = 1.;
    for( double Pi : P ) {
      res *= Pi;
    }
    if( res > 1. ) res = 1.;

    cout << res << endl;
  }

}

