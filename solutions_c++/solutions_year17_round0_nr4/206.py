#include <bits/stdc++.h>
using namespace std;

#define int long long
#define inf 1000000007LL

#define rep(i, n) for(int i = 0; i < (n); i++)
#define rrep(i, n) for(int i = (n) - 1; i >= 0; i--)
#define trep(i, n) for(int i = 0; i <= (n); i++)
#define rep1(i, n) for(int i = 1; i <= (n); i++)
#define mfor(i, s, t) for(int i = (s); i < (t); i++)
#define tfor(i, s, t) for(int i = (s); i <= (t); i++)

int n;
int ans;
bool okv[114][114];
bool okd[114][114];

int in[114][114];
int flg[114][114];

void addv(int y, int x) {
  ans++;
  flg[y][x] |= 1;
  tfor(i, -n, n) {
    if(0 <= y + i && y + i < n && 0 <= x + i && x + i < n) {
      okv[y + i][x + i] = false;
    }
    if(0 <= y + i && y + i < n && 0 <= x - i && x - i < n) {
      okv[y + i][x - i] = false;
    }
  }
}
void addd(int y, int x) {
  ans++;
  flg[y][x] |= 2;
  rep(i, n) {
    okd[y][i] = false;
    okd[i][x] = false;
  }
}

signed main() {
  int t;
  cin >> t;
  rep1(_, t) {
    int m;
    ans = 0;
    cin >> n >> m;
    rep(i, n) {
      rep(j, n) {
        in[i][j] = 0;
        flg[i][j] = 0;
        okv[i][j] = true;
        okd[i][j] = true;
      }
    }
    rep(i, m) {
      string s;
      int y, x;
      cin >> s >> y >> x;
      y--;
      x--;
      if(s == "+") {
        in[y][x] = 1;
        addv(y, x);
      }
      else if(s == "x") {
        in[y][x] = 2;
        addd(y, x);
      }
      else {
        in[y][x] = 3;
        addv(y, x);
        addd(y, x);
      }
    }
    rep(i, n) {
      rep(j, n) {
        if(okv[i][j]) {
          addv(i, j);
        }
        if(okv[n - 1 - i][j]) {
          addv(n - 1 - i, j);
        }
        if(okv[j][i]) {
          addv(j, i);
        }
        if(okv[j][n - 1 - i]) {
          addv(j, n - 1 - i);
        }
      }
    }
    rep(i, n) {
      rep(j, n) {
        if(okd[i][j]) {
          addd(i, j);
        }
      }
    }
    int k = 0;
    rep(i, n) {
      rep(j, n) {
        if(in[i][j] != flg[i][j]) {
          k++;
        }
      }
    }
    cout << "Case #" << _ << ": " << ans << " " << k << endl;
    rep(i, n) {
      rep(j, n) {
        if(in[i][j] != flg[i][j]) {
          if(flg[i][j] == 1) {
            cout << "+" << " " << i + 1 << " " << j + 1 << endl;
          }
          else if(flg[i][j] == 2) {
            cout << "x" << " " << i + 1 << " " << j + 1 << endl;
          }
          else if(flg[i][j] == 3) {
            cout << "o" << " " << i + 1 << " " << j + 1 << endl;
          }
        }
      }
    }
  }
}
