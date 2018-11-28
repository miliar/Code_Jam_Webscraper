#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORN(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define BUG(x) cerr << #x << " = " << x << endl
#define PB push_back
#define MP make_pair

#define MAX 1511

int a[2][MAX];
int st[2][MAX], fn[2][MAX];
int f[MAX][MAX][2][2];

void op(int &a, int &b, int delta) {
  if (b == -1) return;
  if (a == -1 || b + delta < a) {
    a = b + delta;
  }
}

int main() {
  int ntest;
  cin >> ntest;
  
  FOR (test, 1, ntest) {
    int nActivity[2];
    cin >> nActivity[0] >> nActivity[1];
    REP (person, 2) REP (i, nActivity[person]) cin >> st[person][i] >> fn[person][i];

    memset(f, -1, sizeof(f));

    int res = 1e9;
    REP (i, 1440) {
      REP (startPerson, 2) {
        REP (person, 2) {
          bool busy = false;
          REP (k, nActivity[person]) if (st[person][k] <= i && i < fn[person][k]) {
            busy = true;
            break;
          }

          if (i == 0) {
            if (!busy && startPerson == person) {
              f[0][1][person][person] = 0;
            }
            continue;
          }

          FOR (keep, 1, i + 1) {
            int &cur = f[i][keep][startPerson][person];
            cur = -1;

            if (!busy) {
              int otherKeep = i + 1 - keep;
              int otherPerson = 1 - person;

              op(cur, f[i - 1][keep - 1][startPerson][person], 0);
              op(cur, f[i - 1][otherKeep][startPerson][otherPerson], 1);

              if (cur != -1 && i == 1439) {
                if (person != startPerson) cur++;

                if (keep == 720) {
                  res = min(res, cur);
                }
              }
            }
          }
        }
      }
    }
    cout << "Case #" << test << ": " << res << endl;
  }
}

