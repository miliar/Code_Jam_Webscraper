#include <iostream>
#include <cstring>
using namespace std;

#define MAXN 64
#define MAXP 64
#define mp make_pair

int n, p;
int r[MAXN];
pair<int, int> q[MAXN][MAXP];
int l[MAXN];

void solve() {
  memset(l, 0, sizeof(l));
  cin >> n >> p;

  for(int i = 0; i < n; i++) {
    cin >> r[i];
  }

  //1000 000 * n*p <= 1000

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < p; j++) {
      int temp;
      cin >> temp;
      int lb = (temp*10) / (9*r[i]);
      int ub = (temp*10 + 11*r[i] - 1) / (11*r[i]);
      q[i][j] = mp(ub, lb);
      //cout << i << " " << j << "-> (" << ub << " " << ub << ")\n";
    }
  }

  for(int i = 0; i < n; i++) {
    sort(q[i], q[i] + p);
  }
  int res = 0;
  for(int cans = 1 ; cans <= 1000100; cans++) {
    int ok = true;
    while(ok) {
      ok = true;
      for(int i = 0; i < n; i++) {
        while(l[i] < p && q[i][l[i]].second < cans) {
          l[i]++;
        }

        if(l[i] == p || q[i][l[i]].first > cans) {
          ok = false;
          break;
        }
      }
      if(ok) {
        for(int i = 0; i < n; i++) {
          l[i] += l[i] < p;
        }
      }
      res += ok;
    }
  }

  cout << res << endl;
}

int main () {
  int t;
  cin >> t;
  for(int i = 1; i <=t; i++) {
    printf("Case #%d: ", i);
    solve();
  }
}
