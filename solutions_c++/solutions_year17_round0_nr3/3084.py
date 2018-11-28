#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using std::cin;  using std::cout;  using std::endl;
using std::vector; using std::string;

int main() {

  int T;
  cin >> T;

  long N, K;

  for (int i=1; i<=T; ++i) {

    cin >> N;
    cin >> K;

    long k;
    long max_p, min_p;

    long num_longs, num_shorts;
    bool long_is_odd = 0;
    
    // place first guy
    
    // if N is odd, then the two halves are equal-length
    // otherwise, placing a guy in the stall leaves one half shorter
    max_p = N/2;
    min_p = N/2 + ( N%2==1 ? 0 : -1);
    // The number of empty intervals that are long or short
    // (if N is odd, placing a guy in the middle, we've two "long" intervals,
    //  otherwise, one interval is "long" and the other is 1 stall shorter
    num_longs = 1 + ( N%2==1 ? 1 : 0);
    num_shorts = ( N%2==1 ? 0 : 1);
    --K;

    k = 2;  // number of guys we can place in next logarithmic round
    while (K > 0  &&  K > k) {
      // if the "long" interval is odd, then it will make two longs
      // otherwise, it will make one long, and one short
      // (vice versa for short intervals)
      num_longs = max_p%2==0 ? num_longs : num_longs * 2 + num_shorts;
      num_shorts = max_p%2==0 ? num_longs + num_shorts * 2 : num_shorts;
      max_p = max_p / 2;
      min_p = min_p / 2 + (min_p%2==1 ? 0 : -1);
      K -= k;
      k *= 2;
    }
    if (K > 0) {
      if (K<=num_longs) {
	min_p = max_p / 2 + (max_p%2==1 ? 0 : -1);
	max_p = max_p / 2;
      }
      else {
	max_p = min_p / 2;
	min_p = min_p / 2 + (min_p%2==1 ? 0 : -1);
      }
    }
    
    cout << "case #" << i << ": " << max_p << " " << min_p << endl;

  }

  return 0;
}
