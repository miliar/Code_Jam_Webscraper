#include <bits/stdc++.h>
using namespace std;
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
template<class T>inline void check_min(T&a,T b){if(b<a)a=b;}
template<class T>inline void check_max(T&a,T b){if(a<b)a=b;}
typedef long long int64;
typedef pair<int, int> PII;

const int N = 32;

int R, C;
char a[N][N];

void add(PII& a, const PII& b) {
  a.first += b.first;
  a.second += b.second;
}

bool check(PII a, PII b, PII d) {
  if (a.first <= 0 || a.first > R || a.second <= 0 || a.second > C) return false;
  add(b, d);
  for (; a != b; add(a, d)) {
    if (::a[a.first][a.second] != '?') {
      return false;
    }
  }
  return true;
}

void solve() {
  scanf("%d%d", &R, &C);
  map<char, pair<PII, PII>> mp;
  for (int i = 1; i <= R; ++i) {
    scanf("%s", &a[i][1]);
    for (int j = 1; j <= C; ++j) {
      char c = a[i][j];
      if (c == '?') continue;
      PII p = make_pair(i, j);
      if (!mp.count(c)) {
        mp[c] = make_pair(p, p);
      } else {
        check_min(mp[c].first.first, p.first);
        check_min(mp[c].first.second, p.second);
        check_max(mp[c].second.first, p.first);
        check_max(mp[c].second.second, p.second);
      }
    }
  }
  for (auto& pr : mp) {
    PII& lt = pr.second.first;
    PII& rt = pr.second.second;
    for (int i = lt.first; i <= rt.first; ++i) {
      for (int j = lt.second; j <= rt.second; ++j) {
        a[i][j] = pr.first;
      }
    }
    bool flag = true;
    while (flag) {
      flag = false;
      if (check(make_pair(lt.first - 1, lt.second), make_pair(lt.first - 1, rt.second), make_pair(0, 1))) {
        for (int j = lt.second; j <= rt.second; ++j) a[lt.first - 1][j] = pr.first;
        --lt.first;
        flag = true;
      }
      if (check(make_pair(rt.first + 1, lt.second), make_pair(rt.first + 1, rt.second), make_pair(0, 1))) {
        for (int j = lt.second; j <= rt.second; ++j) a[rt.first + 1][j] = pr.first;
        ++rt.first;
        flag = true;
      }
      if (check(make_pair(lt.first, lt.second - 1), make_pair(rt.first, lt.second - 1), make_pair(1, 0))) {
        for (int i = lt.first; i <= rt.first; ++i) a[i][lt.second - 1] = pr.first;
        --lt.second;
        flag = true;
      }
      if (check(make_pair(lt.first, rt.second + 1), make_pair(rt.first, rt.second + 1), make_pair(1, 0))) {
        for (int i = lt.first; i <= rt.first; ++i) a[i][rt.second + 1] = pr.first;
        ++rt.second;
        flag = true;
      }
    }
  }
  for (int i = 1; i <= R; ++i) {
    printf("%s\n", &a[i][1]);
  }
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d:\n", index);
    solve();
  }
  return 0;
}
