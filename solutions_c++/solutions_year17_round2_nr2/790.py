#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORN(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define BUG(x) cerr << #x << " = " << x << endl

#define SIZE(a) ((int) a.size())

typedef pair<int, int> pii;

int n, r, o, y, g, b, v;

int c[6][6];
int degin[6], degout[6];
bool ok[6][6];
string label = "RYBOGV";

bool isDone(int u) {
  FOR (i, 0, 5)
    if (c[u][i] > 0) {
      return false;
    }

  return true;
}

vector<int> findCycle(int u) {
  vector<int> vt;

  vt.push_back(u);

  int prv = u;
  while(true) {
    int v = -1;

    FOR (i, 0, 5)
      if (c[prv][i] > 0) {
        v = i;
        break;
      }

    vt.push_back(v);
    c[prv][v]--;
    prv = v;
    if (v == u) {
      break;
    }
  }

  return vt;

}

vector<int> find(int u) {
  vector<int> vt = findCycle(u);

  while(true) {
    int pos = -1;

    REP(i, SIZE(vt)) {
      if (!isDone(vt[i])) {
        pos = i;
        break;
      }
    }

    if (pos == -1) {
      return vt;
    }

    vector<int> t = findCycle(vt[pos]);
    vt.erase(vt.begin() + pos);
    vt.insert(vt.begin() + pos, t.begin(), t.end());
  }

  return vt;
}

string check() {
  FOR (i, 0, 5)
    FOR (j, 0, 5)
      if (c[i][j] < 0) {
        return "";
      }

  FOR (i, 0, 5) {
    degin[i] = degout[i] = 0;
  }

  FOR (i, 0, 5)
    FOR (j, 0, 5) {
      degin[i] += c[j][i];
      degout[i] += c[i][j];
    }

  FOR (i, 0, 5) {
    if (degin[i] != degout[i]) {
      return "";
    }
  }

  FOR (i, 0, 5)
    FOR (j, 0, 5) {
      ok[i][j] = (i == j || c[i][j] > 0);
    }

  FOR (i, 0, 5)
    FOR (j, 0, 5)
      FOR (k, 0, 5) {
        ok[i][j] |= ok[i][k] && ok[k][j];
      }

  FOR (i, 0, 5)
    FOR (j, 0, 5)
      if (degin[i] > 0 && degin[j] > 0 && !ok[i][j]) {
        return "";
      }

  int start = 0;
  FOR (i, 0, 5) {
    if (degin[i] > 0) {
      start = i;
      break;
    }
  }

  vector<int> vt = find(start);

  string res = "";
  FOR (i, 0, SIZE(vt) - 2) {
    res += label[vt[i]];
  }

  return res;
}

string solve() {
  FOR (rb, 0, min(r, b))
      FOR (br, 0, min(r, b)) {
        FOR (i, 0, 5)
          FOR (j, 0, 5)
            c[i][j] = 0;

        c[4][0] = c[0][4] = g;
        c[3][2] = c[2][3] = o;
        c[1][5] = c[5][1] = v;

        c[0][2] = rb;
        c[2][0] = br;

        c[0][1] = r - g - c[0][2];

        c[2][1] = b - c[2][0] - o;
        c[1][2] = b - c[0][2] - o;

        c[1][0] = y - v - c[1][2];

        string res = check();
        if (res != "") {
          return res;
        }
      }

  return "IMPOSSIBLE";
}

int main() {
  int t;
  cin >> t;

  FOR (i, 1, t) {
    cin >> n >> r >> o >> y >> g >> b >> v;

    string res = solve();

    cout << "Case #" << i << ": " << res << endl;
  }

  return 0;
}
