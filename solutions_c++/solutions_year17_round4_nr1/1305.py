#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
using namespace std;

//typedef pair<int, int> P;
#define rep(i, n) for (int i=0; i<(n); i++)
#define all(c) (c).begin(), (c).end()
#define uniq(c) c.erase(unique(all(c)), (c).end())
#define _1 first
#define _2 second
#define pb push_back
#define INF 1145141919
#define MOD 1000000007

int T, N, P;
int C[4];
int memo3[101][101];
int memo4[101][101][101];

int gcd(int a, int b) {
  if (a > b) swap(a, b);
  if (a == 0) return b;
  return gcd(b%a, a);
}

int f2(int a) {
  return (a+1)/2;
}

int f3(int a, int b) {
  if (a<0||b<0) return -INF;
  if (a==0&&b==0) return 0;
  if (memo3[a][b] != -1) return memo3[a][b];
  int s = 1;
  s = max(s, f3(a-3, b) + 1);
  s = max(s, f3(a, b-3) + 1);
  s = max(s, f3(a-1, b-1) + 1);
  /*
  for (int i=0; i<4; i++) {
    for (int j=0; j<4; j++) {
      if (i == 0 && j == 0) continue;
      if ((1*i+2*j) % 3 != 0) continue;
        s = max(s, f3(a-i, b-j) + 1);
    }
  }
  */
  return memo3[a][b] = s;
}

int f4(int a, int b, int c) {
  if (a<0||b<0||c<0) return -INF;
  if (a==0&&b==0&&c==0) return 0;
  if (memo4[a][b][c] != -1) return memo4[a][b][c];
  int s = 1;
  //s = max(s, f4(a-4, b, c) + 1);
  //s = max(s, f4(a, b-4, c) + 1);
  //s = max(s, f4(a, b, c-4) + 1);
  for (int i=0; i<5; i++) {
    for (int j=0; j<5; j++) {
      for (int k=0; k<5; k++) {
        if (i == 0 && j == 0 && k == 0) continue;
        if ((1*i+2*j+3*k) % 4 != 0) continue;
        s = max(s, f4(a-i, b-j, c-k) + 1);
      }
    }
  }
  return memo4[a][b][c] = s;
}

signed main() {
  ios::sync_with_stdio(false); cin.tie(0);
  cin >> T;
  rep(i, 101) {
    rep(j, 101) {
      memo3[i][j] = -1;
      rep(k, 101) {
        memo4[i][j][k] = -1;
      }
    }
  }
  rep(i, T) {
    cin >> N >> P;
    rep(i, 4) C[i] = 0;
    rep(i, N) {
      int g;
      cin >> g;
      C[g%P]++;
    }
    int x = C[0];
    if (P == 2) x += f2(C[1]);
    else if (P == 3) x += f3(C[1], C[2]);
    else x += f4(C[1], C[2], C[3]);
    cout << "Case #"<<i+1<<": "<<x<<"\n";
  }
  return 0;
}
