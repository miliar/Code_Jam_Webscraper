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

bool tidy(ll x){
  int l = 9;
  while(x > 0) {
    if(l < x%10) return false;
    l = x%10;
    x /= 10;
  }
  return true;
}

int main(void){
  int T;
  ll N;
  cin >> T;
  for(int tt = 0; tt < T; ++tt) {
    cin >> N;
    ll res = 0;
    while(!tidy(N)) {
      while(N%10 != 9) {
        --N;
      }
      res *= 10;
      res += 9;
      N /= 10;
    }
    while(N > 0) {
      res *= 10;
      res += N % 10;
      N /= 10;
    }

    cout << "Case #" << tt+1 << ": ";
    while(res > 0) {
      cout << res % 10;
      res /= 10;
    }
    cout << endl;
  }

  return 0;
}
