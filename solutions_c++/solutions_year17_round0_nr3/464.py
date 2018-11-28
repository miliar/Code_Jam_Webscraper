#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

typedef long long ll;

int log2floor(ll x) {
  int res = 0;
  x >>= 1;
  while(x > 0) {
    x >>= 1;
    ++res;
  }
  return res;
}

int main(void){
  int T;
  ll N, K;
  cin >> T;
  for(int tt = 0; tt < T; ++tt) {
    cin >> N >> K;
    int a = log2floor(K);

    ll rmax = (N - K + (1LL << a)) >> (a+1);
    ll rmin = (N - K) >> (a+1);
    cout << "Case #" << tt+1 << ": " << rmax << ' ' << rmin << endl;
  }

  return 0;
}
