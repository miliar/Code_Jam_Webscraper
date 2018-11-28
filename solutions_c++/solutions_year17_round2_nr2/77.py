#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define ALL(a) begin(a), end(a)
#define SZ(a) ((int)(a).size())

#ifdef __DEBUG
#define debug if (true)
#else
#define debug if (false)
#endif

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

enum Color {
  R, O, Y, G, B, V
};

void answer(const string &ans) {
  static int caseNo = 1;
  printf("Case #%d: %s\n", caseNo++, ans.c_str());
}

string solve(vector<pair<int, char>> v) {
  assert(SZ(v) == 3);
  debug printf("%c%c%c\n", v[0].se, v[1].se, v[2].se);
  if (v[0].fi == 0 || v[1].fi + v[2].fi < v[0].fi) {
    return "IMPOSSIBLE";
  }
  vector<string> poss(v[0].fi);
  int curPos = 0;
  for (int i = 1; v[1].fi + v[2].fi > 0; i ^= 3) {
    for (int j = 0; j < v[0].fi && v[i].fi > 0; j++, v[i].fi--) {
      if (!poss[curPos].empty() && poss[curPos].back() == v[i].se) {
        return "IMPOSSIBLE";
      }
      poss[curPos] += v[i].se;
      curPos = (curPos + 1) % v[0].fi;
    }
  }
  string ret = "";
  for (int i = 0; i < v[0].fi; i++) {
    ret += v[0].se;
    ret += poss[i];
  }
  assert(ret[0] != ret.back());
  return ret;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
  cin >> T;
  while (T--) {
    int n;
    cin >> n;
    vi c(6);
    for (int i = 0; i < 6; i++) {
      cin >> c[i];
    }
    if (c[B] < c[O] || c[R] < c[G] || c[Y] < c[V]) {
      answer("IMPOSSIBLE");
      continue;
    }
    c[B] -= c[O];
    c[R] -= c[G];
    c[Y] -= c[V];
    if ((c[O] > 0 && c[B] == 0) ||
        (c[G] > 0 && c[R] == 0) ||
        (c[V] > 0 && c[Y] == 0)) {
      if (accumulate(ALL(c), 0) == c[O]) {
        // OBOBOBOB...
        const string pattern = "OB";
        string ret = "";
        for (int i = 0; i < c[O]; i++) {
          ret += pattern;
        }
        answer(ret);
      } else if (accumulate(ALL(c), 0) == c[G]) {
        // GRGRGR...
        const string pattern = "GR";
        string ret = "";
        for (int i = 0; i < c[G]; i++) {
          ret += pattern;
        }
        answer(ret);
      } else if (accumulate(ALL(c), 0) == c[V]) {
        // VYVYVY...
        const string pattern = "VY";
        string ret = "";
        for (int i = 0; i < c[V]; i++) {
          ret += pattern;
        }
        answer(ret);
      } else {
        answer("IMPOSSIBLE");
      }
      continue;
    }
    string ans = "IMPOSSIBLE";
    vector<pair<int, char>> t {{c[B], 'B'}, {c[R], 'R'}, {c[Y], 'Y'}};
    sort(ALL(t));
    do {
      string ret = solve(t);
      if (ret != "IMPOSSIBLE") {
        ans = "";
        int last = -1;
        for (char ch : ret) {
          ans += ch;
          last = ch;
          if (last == 'B') {
            while (c[O] > 0) {
              ans += "OB";
              c[O]--;
            }
          } else if (last == 'Y') {
            while (c[V] > 0) {
              ans += "VY";
              c[V]--;
            }
          } else if (last == 'R') {
            while (c[G] > 0) {
              ans += "GR";
              c[G]--;
            }
          }
        }
        break;
      }
    } while (next_permutation(ALL(t)));
    answer(ans);
  }
  return 0;
}

