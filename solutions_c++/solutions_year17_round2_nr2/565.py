#include <bits/stdc++.h>

using namespace std;

using ll = long long;

const string IMP = "IMPOSSIBLE";

int next(const string& s, int p) {
  const int n = s.size();
  for (int i = 0; i < n; i++) {
    if (s[(p + i) % n] == '#') return (p + i) % n;
  }
  return p;
}


string solveSmall(int n, int r, int y, int b) {
  if (r > n / 2) return IMP;
  if (y > n / 2) return IMP;
  if (b > n / 2) return IMP;

  int cands[3] = {r, y, b};
  char add[3] = {'R', 'Y', 'B'};

  string ans;
  int start = 0;
  int last = -1;
  for (int i = 0; i < n; i++) {
    int best = start == last ? (start + 1) % 3 : start;
    for (int j = 0; j < 3; j++) {
      if (cands[j] > cands[best] and j != last) {
        best = j;
      }
    }

    last = best;
    if (not i) start = best;
    cands[best]--;

    ans += add[best];

  }

  return ans;
}

string solve(int n, int r, int o, int y, int g, int b, int v) {
  int sr = r;
  int sy = y;
  int sb = b;

  if ((v + o + g) and (y + v == n or b + o == n or r + g == n)) {
    if (y + b + r != v + o + g) return IMP;
    string ans;
    for (int i = 0; i < n; i++) {
      if (i % 2) {
        if (o) ans += 'O';
        if (v) ans += 'V';
        if (g) ans += 'G';
      } else {
        if (r) ans += 'R';
        if (y) ans += 'Y';
        if (b) ans += 'B';
      }
    }
    return ans;
  } 

  
  for (int i = 0; i < o; i++) {
    if (sb < 2) return IMP;
    sb--;
  }

  for (int i = 0; i < g; i++) {
    if (sr < 2) return IMP;
    sr--;
  }

  for (int i = 0; i < v; i++) {
    if (sy < 2) return IMP;
    sy--;
  }

  int sn = sr + sy + sb;
  string sans = solveSmall(sn, sr, sy, sb);


  if (sans == IMP) return IMP;

  string ans;
  for (int i = 0; i < sn; i++) {
    if (sans[i] == 'B' and o) {
      ans += "BO"; 
    } else if (sans[i] == 'Y' and v) {
      ans += "YV";
    } else if (sans[i] == 'R' and g) {
      ans += "RG";
    }
    ans += sans[i];
  }

  return ans;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    string ans = solve(n, r, o, y, g, b, v);
    cout << "Case #" << tc << ": " << ans << '\n';
  }

}
