#include <iostream>
#include <set>
using namespace std;

int main() {

  long long int in_t;
  cin >> in_t;
  for ( long long int for_t = 0; for_t < in_t; for_t++ ) {
    cout << "Case #" << for_t + 1 << ": ";


    long long int n, k;
    cin >> n >> k;

    multiset< long long int > s;
    s.insert( -n );

    long long int ans_max, ans_min;

    for ( long long int i = 0; i < k; i++ ) {

      long long int p = *s.begin();
      s.erase( s.begin() );
      p *= -1;
      p--;
      ans_max = p / 2 + ( p % 2 );
      ans_min = p / 2;
      s.insert( -ans_max );
      s.insert( -ans_min );

    }

    cout << ans_max << " " << ans_min << endl;

  }

  return 0;

}
