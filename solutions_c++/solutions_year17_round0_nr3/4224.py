#include <iostream>
#include <string>
#include <vector>
#include <limits>
#include <cassert>

using namespace std;

long long N;
long long K;
const long long ONE = 1;

pair< long long, long long > solve() {
  if( N == K ) {
    return pair< long long, long long >( 0, 0 );
  }
  int L = static_cast<int>( log2( K ) );
  long long KL = K - ( ONE << L ) + 1;
  long long even_count = 0;
  long long odd_count = 0;
  long long even = -1;
  long long odd = -1;
  bool isEven = ( ( N & 1 ) == 0 );
  if( isEven ) {
    even_count = 1;
    even = N;
  }
  else {
    odd_count = 1;
    odd = N;
  }
  for( int l = 1; l <= L; l++ ) {
    long long new_even_count = 0;
    long long new_odd_count = 0;
    long long new_even = -1;
    long long new_odd = -1;
    if( even_count > 0 ) {
      new_even_count = even_count;
      new_odd_count = even_count;
      long long half = even >> 1;
      bool isHalfEven = ( ( half & 1 ) == 0 );
      if( isHalfEven ) {
        new_even = half;
        new_odd = half - 1;
      }
      else {
        new_odd = half;
        new_even = half - 1;
      }
    }
    if( odd_count > 0 ) {
      long long half = odd >> 1;
      bool isHalfEven = ( ( half & 1 ) == 0 );
      if( isHalfEven ) {
        new_even_count += 2 * odd_count;
        new_even = half;
      }
      else {
        new_odd_count += 2 * odd_count;
        new_odd = half;
      }
    }
    even_count = new_even_count;
    odd_count = new_odd_count;
    even = new_even;
    odd = new_odd;
  }
  long long min_n = -1;
  long long max_n = -1;
  long long min_count = 0;
  long long max_count = 0;
  if( even > odd ) {
    min_n = odd;
    max_n = even;
    min_count = odd_count;
    max_count = even_count;
  }
  else {
    min_n = even;
    max_n = odd;
    min_count = even_count;
    max_count = odd_count;
  }

  assert( min_count + max_count == ( ONE << L ) );

  long long rest = KL - max_count;
  long long s = -1;
  if( rest <= 0 ) {
    s = max_n;
  }
  else {
    s = min_n;
  }
  long long half = s >> 1;
  bool isHalfEven = ( ( s & 1 ) == 0 );
  if( isHalfEven ) {
    pair< long long, long long > nn( half, half - 1 );
    return nn;
  }
  else {
    pair< long long, long long > nn( half, half );
    return nn;
  }
}

void main() {
  int t;
  cin >> t;
  const int NumOfCases = t + 1;

  for( int i = 1; i < NumOfCases; i++ ) {
    cin >> N;
    cin >> K;
    pair< long long, long long > nn = solve();
    cout << "\nCase #" << i << ": " << nn.first << " " << nn.second << endl;
  }
}
