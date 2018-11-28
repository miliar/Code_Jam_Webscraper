
#include <iostream>
#include <memory>
#include <algorithm>
#include <unordered_map>
using namespace std;

void main() {
  int T;
  cin >> T;
  for( int iT = 1; iT <= T; ++iT ) {
    long long K, N;
    cin >> N >> K;
    //cout << "orig: " << N << " " << K << ", ";
    
    
    long long minS = ( N - 1 ) / 2;
    long long maxS = minS + ( N - 1 ) % 2;
    
    unordered_map<long long, long long> arrBig;
    arrBig.insert( make_pair( minS, 1 ) );
    if( arrBig.find( maxS ) == arrBig.end() ) arrBig[maxS] = 0;
    arrBig[maxS]++;

    long long curMax = maxS;
    for( long long iK = 1; iK < K; ) {
      if( arrBig[curMax] == 0 ) {
        curMax = 0;
        for( auto iter : arrBig ) {
          if( iter.second > 0 ) curMax = max( curMax, iter.first );
        }
      }

      minS = ( curMax - 1 ) / 2;
      maxS = minS + ( curMax - 1 ) % 2;
      if( maxS == 0 ) break;

      if( arrBig.find( minS ) == arrBig.end() ) arrBig[minS] = 0;
      arrBig[minS] += arrBig[curMax];
      if( arrBig.find( maxS ) == arrBig.end() ) arrBig[maxS] = 0;
      arrBig[maxS] += arrBig[curMax];

      iK += arrBig[curMax];
      arrBig[curMax] = 0;
    }

    cout << "Case #" << iT << ": " << maxS << " " << minS << endl;
  }

}

