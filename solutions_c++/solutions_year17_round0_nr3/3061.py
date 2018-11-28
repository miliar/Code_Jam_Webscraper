#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<pair<int, int>, int> iii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define I18F 1000000000000000000 // 10^18
#define INF 2139062143
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B

int T;

int main(){
  scanf("%d", &T);
  for(int _t = 1; _t <= T; ++_t){
    printf("Case #%d: ", _t);
    ll N, K;
    scanf("%lld %lld", &N, &K);
    ll big, small, ct, big_ct, size, res;
    big = small = N;
    ct = 0;
    big_ct = size = 1;
    while(ct + size < K){
      ll new_ct = big_ct;

      if(big % 2 == 1) new_ct += big_ct;
      if(small % 2 == 0) new_ct += (size-big_ct);
      big_ct = new_ct;

      big = big/2; small = (small-1)/2;
      ct += size;
      size <<= 1;
      //printf("%lld %lld %lld %lld\n", ct, big, small, big_ct);
    }
    res = (ct + big_ct < K) ? small : big;
    printf("%lld %lld\n", res/2, (res-1)/2); 
  }
}
