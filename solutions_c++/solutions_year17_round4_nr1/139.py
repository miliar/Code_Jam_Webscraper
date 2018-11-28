/* Written by Filip Hlasek 2017 */
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>

#define FOR(i, a, b)   for (int i = (a); i <= (b); i++)
#define FORD(i, a, b)  for (int i = (a); i >= (b); i--)
#define REP(i, b)      for (int i =  0 ; i <  (b); i++)

using namespace std;

int P;

map<vector<int>, int> dp;

int solve(vector<int> cnt) {
  if (dp.count(cnt)) return dp[cnt];
  int best = 0;
  REP(i, cnt.size()) if (cnt[i]) {
    if (cnt[i] > 1) {
      vector<int> ncnt = cnt;
      ncnt[i] -= 2;
      int nval = ((i + 1) + (i + 1)) % P;
      int ans = 0;
      if (nval) ncnt[nval - 1]++;
      else ans++;
      best = max(best, ans + solve(ncnt));
    }
    REP(j, i) if (cnt[j]) {
      vector<int> ncnt = cnt;
      ncnt[i]--;
      ncnt[j]--;
      int nval = ((i + 1) + (j + 1)) % P;
      int ans = 0;
      if (nval) ncnt[nval - 1]++;
      else ans++;
      best = max(best, ans + solve(ncnt));
    }
  }
  return dp[cnt] = best;
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    int N;
    scanf("%d%d", &N, &P);
    vector<int> cnt;
    REP(i, P) cnt.push_back(0);
    int ans = 0;
    int total = 0;
    REP(i, N) {
      int a;
      scanf("%d", &a);
      a %= P;
      total = (total + a) % P;
      if (!a) ans++;
      else cnt[a - 1]++;
    }
    printf("Case #%d: %d\n", t, ans + solve(cnt) + (total != 0));
  }
  return 0;
}
