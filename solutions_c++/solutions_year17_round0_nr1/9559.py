#include <cstdio>
#include <climits>
#include <cassert>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <numeric>
#include <functional>
#include <tuple>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <vector>

#define REP(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define FOR(x,xs) for(auto &x: xs)

using namespace std;
typedef long long ll;
typedef pair<int,int> PI;
typedef pair<ll,ll> PL;
typedef vector<int> VI;
typedef vector<ll> VL;

int main() {
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  REP(i,0,T) {
    string S;
    int K;
    cin >> S >> K;
    vector<bool> p(S.size());
    REP(j,0,S.size()) {
      p[j] = S[j] == '+';
    }
    int ans = 0;
    REP(j,0,S.size() - K + 1) {
      if(!p[j]) {
        REP(k,0,K) {
          p[j+k] = !p[j+k];
        }
        ans++;
      }
    }
    bool pos = true;
    REP(j,0,p.size()) {
      if(!p[j]) {
        pos = false;
        break;
      }
    }
    cout << "Case #" << i + 1 << ": ";
    if(pos) {
      cout << ans;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << endl;
  }
  return 0;
}
