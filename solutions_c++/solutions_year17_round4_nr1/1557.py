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
#include <cassert>

using namespace std;

typedef long long ll;

int G[100];
int cnt[4];

int main(void){
  int T;
  cin >> T;
  for (int tt = 0; tt < T; ++tt) {
    cout << "Case #" << tt+1 << ": ";

    int N, P;
    cin >> N >> P;
    fill_n(cnt, P, 0);
    for(int i = 0; i < N; ++i) {
      cin >> G[i];
      G[i] %= P;
      ++cnt[G[i]];
    }

    for(int p = P - 1; p > 0; --p) {
      if(p <= P-p) break;
      int n = min(cnt[p], cnt[P-p]);
      cnt[p] -= n;
      cnt[P-p] -= n;
      cnt[0] += n;
    }
    int t = -1;
    for(int p = 1; p < P; ++p) {
      if(cnt[p] > 0){
        assert(t == -1);
        t = p;
      }
    }
    int cur = 0;
    while(cnt[t] > 0) {
      --cnt[t];
      cur += t;
      if(cur % P == 0) {
        cur = 0;
        ++cnt[0];
      }
    }
    cout << cnt[0] + (cur == 0 ? 0 : 1) << endl;
  }

  return 0;
}
