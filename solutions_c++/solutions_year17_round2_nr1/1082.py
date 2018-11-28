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

pair<ll, int> KS[1000];

int main(void){
  int T;
  cin >> T;
  for (int tt = 0; tt < T; ++tt) {
    ll D; int N;
    cin >> D >> N;
    for(int i = 0; i < N; ++i)
      cin >> KS[i].first >> KS[i].second;
    sort(KS, KS+N);

    int target = -1;
    for(int j = 0; j < N; ++j) {
      bool ok = true;
      for(int k = j + 1; k < N; ++k) {
        if(KS[k].second * (D - KS[j].first) <= KS[j].second * (D - KS[k].first)) {
          ok = false;
          break;
        }
      }
      if (ok) {
        target = j;
        break;
      }
    }

    printf("Case #%d: %.6lf\n", tt+1, KS[target].second * D / (double)(D - KS[target].first));
  }

  return 0;
}
