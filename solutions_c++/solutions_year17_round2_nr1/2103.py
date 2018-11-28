#include <iostream>
#include <vector>
#include <assert.h>
#include <algorithm>
#include <float.h>

using namespace std;

int main()
{
  int t;
  cin >> t;
  for( int i = 0; i < t; ++i ) {
    int D, N;
    cin >> D >> N;

    double maxTime = 0;
    for( int j = 0; j < N; ++j ) {
      int K, S;
      cin >> K >> S;
      maxTime = max( maxTime, 1.0 * ( D - K ) / S );
    }
    assert( maxTime > 0 );
    const double maxSpeed = D / maxTime;
    printf( "Case #%d: %f\n", (i+1), maxSpeed );
    //cout << "Case #" << (i+1) << ": " << maxSpeed << endl;
  }

  return 0;
}