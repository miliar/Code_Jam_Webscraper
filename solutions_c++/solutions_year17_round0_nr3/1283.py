#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<utility>
#include<iomanip>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(12);

  int64_t T;
  cin >> T;

  for (int64_t t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    int64_t N, K;
    cin >> N >> K;
    map<int64_t,int64_t> ivals;
    ivals[N]=1;
    while (K > 0) {
      auto iter = ivals.rbegin();
      int64_t l = iter->first;
      int64_t cnt = iter->second;
      int64_t a, b;
      if (l%2) {
        a = (l-1)/2;
        b = (l-1)/2;
      } else {
        a = (l-2)/2;
        b = l/2;
      }
      if (K <= cnt) {
        cout << max(a,b) << " " << min(a,b) << '\n';
        break;
      }
      K -= cnt;
      ivals.erase(l);
      if (a != 0) ivals[a]+=cnt;
      ivals[b]+=cnt;
    }
  }
  return 0;
} 

