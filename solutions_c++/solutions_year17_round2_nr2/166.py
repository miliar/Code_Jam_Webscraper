#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define ROF(i, n) for (int i = (n) - 1; i >= 0; --i)
#define REP(i, n) for (int i = 1; i <= (n); ++i)
#define REP3(i, s, n) for (int i = (s); i <= (n); ++i)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

string solve(int N, int R, int O, int Y, int G, int B, int V) {
  string ans = "";
  if (N == 1) {
    assert(false);
    if (R == 1) return "R";
    else if (O == 1) return "O";
    else if (Y == 1) return "Y";
    else if (G == 1) return "G";
    else if (B == 1) return "B";
    else if (V == 1) return "V";
  }

  if (R - G < 0 || Y - V < 0 || B - O < 0) {
    return "";
  } else {
    if (G != 0 && R - G == 0) {
      if (R + G != N) {
        return "";
      } else {
        FOR (i, R) ans += "RG";
        return ans;
      }
    }
    if (V != 0 && Y - V == 0) {
      if (Y + V != N) {
        return "";
      } else {
        FOR (i, Y) ans += "YV";
        return ans;
      }
    }
    if (O != 0 && B - O == 0) {
      if (B + O != N) {
        return "";
      } else {
        FOR (i, B) ans += "BO";
        return ans;
      }
    }
    R -= G;
    Y -= V;
    B -= O;

    int cols[3] = {R, Y, B};
    int other[3] = {G, V, O};
    bool up[3] = {false, false, false};
    int M = max(max(R, Y), B), mi = 0;
    if (R + Y + B - M < M) return "";

    if (R == M) mi = 0;
    else if (Y == M) mi = 1;
    else mi = 2;

    bool first[3] = {true, true, true};
    FOR (i, M) {
      FOR (k, 3) {
        int col = (k + mi) % 3;
        if ((k != 2 && i < cols[col]) ||
            (k == 2 && M - i - 1 < cols[col])) {
          ans += "RYB"[col];
          if (first[col]) {
            first[col] = false;
            FOR (j, other[col]) {
              ans += "GVO"[col];
              ans += "RYB"[col];
            }
          }
        }
      }
    }

    return ans;
  }
}

  set<pair<char, char>> bad;
bool ok(char x, char y) {
  return !bad.count(make_pair(x, y)) && !bad.count(make_pair(y, x)) && x != y;
}

int main() {
  bad.insert(make_pair('R', 'O'));
  bad.insert(make_pair('Y', 'O'));
  bad.insert(make_pair('Y', 'G'));
  bad.insert(make_pair('B', 'G'));
  bad.insert(make_pair('B', 'V'));
  bad.insert(make_pair('R', 'V'));

  int T;
  cin >> T;
  REP (tc, T) {
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;

    string ans = solve(N, R, O, Y, G, B, V);
    cout << "Case #" << tc << ": ";
    if (ans == "") cout << "IMPOSSIBLE" << endl;
    else {
      assert(ans.size() == N);
      FOR (i, N) {
        assert(ok(ans[i], ans[(i + 1) % N]));
      }
      cout << ans << endl;
    }
  }
  return 0;
}
