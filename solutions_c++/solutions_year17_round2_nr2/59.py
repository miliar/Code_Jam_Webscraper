// CONTEST SOURCE
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <climits>
//#include <priority_queue>
using namespace std;
#define ll long long
#define x first
#define y second
#define pii pair<int, int>
#define pdd pair<double, double>
#define L(s) (int)(s).size()
#define VI vector<int>
#define all(s) (s).begin(), (s).end()
#define pb push_back
#define mp make_pair
#define inf 1000000000
int t, n, p, q, r, pq, qr, rp;
int e[6][6];
char path[1111];
int ptr;
void dfs(int v) {
  for(int j = 0; j < 6; ++j) {
    while(e[v][j]) {
      --e[v][j];
      dfs(j);
    }
  }
  if (v == 0) path[ptr++] = 'R'; else
    if (v == 1) path[ptr++] = 'Y'; else
      if (v == 2) path[ptr++] = 'B'; else
        if (v == 3) path[ptr++] = 'G'; else
          if (v == 4) path[ptr++] = 'V'; else
            if (v == 5) path[ptr++] = 'O';
}
bool solve() {
    if (p < qr || q < rp || r < pq) return 0;
    for(int p2q = 0; p2q <= p - qr && p2q <= q - rp; ++p2q) {
      e[0][3] = qr;
      e[3][0] = qr;
      e[1][4] = rp;
      e[4][1] = rp;
      e[2][5] = pq;
      e[5][2] = pq;

      e[0][1] = p2q;
      e[0][2] = p - e[0][3] - e[0][1];
      e[2][1] = q - e[0][1] - e[4][1];
      e[2][0] = r - e[2][5] - e[2][1];
      e[1][2] = r - e[0][2] - e[5][2];
      e[1][0] = p - e[3][0] - e[2][0];

      if (e[0][2] < 0 || e[2][1] < 0 || e[2][0] < 0 || e[1][2] < 0 || e[1][0] < 0) continue;
      if (e[0][1] + e[0][2] + e[0][3] != p) continue;
      if (e[1][0] + e[2][0] + e[3][0] != p) continue;
      if (e[1][0] + e[1][2] + e[1][4] != q) continue;
      if (e[0][1] + e[2][1] + e[4][1] != q) continue;
      if (e[2][0] + e[2][1] + e[2][5] != r) continue;
      if (e[0][2] + e[1][2] + e[5][2] != r) continue;

      int idx = 0; while(e[idx][0] + e[idx][1] + e[idx][2] == 0) ++idx;

      ptr = 0;
      dfs(idx);

      if (ptr != n + 1) continue;
      path[n] = 0;
      return 1;
    }
    return 0;
}
bool naive() {
  int ord[111];
  int cnt = 0;
  for(int i = 0; i < p; ++i) ord[cnt++] = 0;
  for(int i = 0; i < q; ++i) ord[cnt++] = 1;
  for(int i = 0; i < r; ++i) ord[cnt++] = 2;
  for(int i = 0; i < qr; ++i) ord[cnt++] = 3;
  for(int i = 0; i < rp; ++i) ord[cnt++] = 4;
  for(int i = 0; i < pq; ++i) ord[cnt++] = 5;
  do {
    ord[n] = ord[0];
    bool ok = 1;
    for(int i = 0; i < n; ++i) {
      if (ord[i] == 0 && ord[i + 1] == 0) { ok = 0; break; }
      if (ord[i] == 0 && ord[i + 1] == 4) { ok = 0; break; }
      if (ord[i] == 0 && ord[i + 1] == 5) { ok = 0; break; }
      if (ord[i] == 1 && ord[i + 1] == 1) { ok = 0; break; }
      if (ord[i] == 1 && ord[i + 1] == 3) { ok = 0; break; }
      if (ord[i] == 1 && ord[i + 1] == 5) { ok = 0; break; }
      if (ord[i] == 2 && ord[i + 1] == 2) { ok = 0; break; }
      if (ord[i] == 2 && ord[i + 1] == 3) { ok = 0; break; }
      if (ord[i] == 2 && ord[i + 1] == 4) { ok = 0; break; }
      if (ord[i] == 3 && ord[i + 1] != 0) { ok = 0; break; }
      if (ord[i] == 4 && ord[i + 1] != 1) { ok = 0; break; }
      if (ord[i] == 5 && ord[i + 1] != 2) { ok = 0; break; }
    }
    if (ok) {
      //for(int i = 0; i < n; ++i) cerr << ord[i] << " "; cerr << endl;
      return 1;
    }
  } while(next_permutation(ord, ord + n));
  return 0;
}
int main() {
  freopen("B-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> t;
  //t = 100000;
  for(int tc = 1; tc <= t; ++tc) {
    cerr << tc << endl;
    cin >> n;
    cin >> p >> pq >> q >> qr >> r >> rp;
    cout << "Case #" << tc << ": ";
    if (!solve()) cout << "IMPOSSIBLE\n";
    else cout << path << endl;
    /*
    n = 1 + rand() % 13;
    p = q = r = pq = qr = rp = 0;
    for(int i = 0; i < n; ++i) {
      int val = rand() % 6;
      if (val == 0) ++p; else
        if (val == 1) ++q; else
          if (val == 2) ++r; else
            if (val == 3) ++qr; else
              if (val == 4) ++rp; else
                if (val == 5) ++pq;
    }

    //  cerr << p << " " << q << " " << r << " " << qr << " " << rp << " " << pq << endl;


    if (solve() != naive()) {
      cerr << "ERROR\n";
      cerr << solve() << endl;
      cerr << naive() << endl;
      exit(0);
    }
    cerr << "OK " << tc << endl;
    */

  }
}
