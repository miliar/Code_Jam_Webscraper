#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <ctime>
#include <cassert>
#include <functional>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 55

int R[MAXN], N, P, Q[MAXN][MAXN], v[MAXN][MAXN];
PII range[MAXN][MAXN];
int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  int cs;
  cin >> cs;
  REP(csn, 1, cs + 1) {
    printf("Case #%d: ", csn);
    //cerr << csn << endl;
    cin >> N >> P;
    REP(i,0,N) cin >> R[i];
    int minK = INF, maxK = -1;
    REP(i,0,N) {
      REP(j,0,P) cin >> Q[i][j];
      sort(Q[i], Q[i] + P);
      REP(j,0,P) {
        int a = Q[i][j];
        int low = (10*a + 11*R[i] - 1) / (11*R[i]);
        int high = (10*a) / (9*R[i]);
        minK = min(low, minK);
        maxK = max(high, maxK);
        range[i][j] = PII(low, high);
      }
    }
    FILL(v,0);
    int ans = 0;
    REP(k,minK,maxK+1) {
      VI choices;
      REP(i,0,N) {
        bool rowFound = 0;
        REP(j,0,P) {
          if (v[i][j]) continue;
          if (range[i][j].first <= k && range[i][j].second >= k) {
            rowFound = 1;
            choices.push_back(j);
            break;
          }
        }
        if (!rowFound) break;
      }
      if (choices.size() != N) continue;
      REP(i,0,N) v[i][choices[i]] = 1;
      ans++;
      k -= 1;
    }
    cout << ans << endl;
  }
  return 0;
}
