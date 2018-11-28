#include <bits/stdc++.h>
#define ll long long

using namespace std ;

int main(int argc, char const *argv[])
{
  ll count;
  cin >> count ;
  for (ll j = 0; j < count; ++j) {
    cout << "Case #" << j + 1 << ": " ;
    ll N, K;
    cin >> K >> N;
    long double max = LDBL_MIN;
    for(int i = 0; i < N; ++i) {
      ll pos, speed;
      cin >> pos >> speed;
      if(max < (K - pos)/(speed*1.0)) {
        max = (K - pos)/(speed*1.0);
      }
    }
    std::cout << std::fixed;
    std::cout << std::setprecision(6) << (K/max) << endl;
  }
  return 0;
}
 
