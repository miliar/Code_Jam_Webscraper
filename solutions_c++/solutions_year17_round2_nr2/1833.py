#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <queue>

using namespace std;

#define TRACE(x) cerr << #x << " " << x << endl
#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define _ << " " <<

#define fst first
#define snd second

typedef long long llint;
typedef pair<int, int> pii;

int T, N;
int R, O, Y, G, B, V;

vector <string> r, b, y;

void solve_small(int t) {
  vector<pair<int, string> > v;
  string sol = "";

  v.emplace_back(R, "R");
  v.emplace_back(B, "B");
  v.emplace_back(Y, "Y");

  for (int i = 0; i < N; ++i) {
    sort(v.begin(), v.end());
    if (i == 0 || sol[i - 1] != v[2].second[0]) {
      if (i != 0 && v[1].first == v[2].first && v[1].second[0] == sol[0] && v[1].second[0] != sol[i - 1]) {
        sol += v[1].second;
        v[1].first--;
        continue;
      }
      if (i != 0 && v[0].first == v[2].first && v[0].second[0] == sol[0] && v[0].second[0] != sol[i - 1]) {
        sol += v[0].second;
        v[0].first--;
        continue;
      }
      sol += v[2].second;
      v[2].first--;
    } else {
      if (v[1].first == v[0].first && v[0].second[0] == sol[0]) {
        sol += v[0].second;
        v[0].first--;
      } else {
        sol += v[1].second;
        v[1].first--;
      }
    }
  }

  sort(v.begin(), v.end());
  if (v[0].first < 0 || sol[0] == sol[sol.size() - 1])
    printf("Case #%d: IMPOSSIBLE\n", t);
  else
    cout << "Case #" << t << ": " << sol << endl;
}

void solve(int t) {
  scanf("%d", &N);
  scanf("%d%d%d%d%d%d", &R, &O, &Y, &G, &B, &V);

  solve_small(t);

//  if (O == 
//  if (R <= G || B <= O || Y <= V) {
//    printf("Case #%d: IMPOSSIBLE\n", t);
//    return;
//  }
//
//  r.clear();
//  b.clear();
//  y.clear();
//
//  for (

}

int main(void) {
  scanf("%d", &T);
  for (int i = 0; i < T; ++i)
    solve(i + 1);

  return 0;
}
