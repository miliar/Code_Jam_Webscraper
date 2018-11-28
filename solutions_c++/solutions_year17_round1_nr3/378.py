#include <bits/stdc++.h>
using namespace std;

const int MAXN = 101;


int opt[MAXN][MAXN][MAXN][MAXN];

int origin = 10000;
void clear()
{
  memset(opt, -1, sizeof opt);
  origin = 10000;
}


int dfs(int Hd, int Ad, int Hk, int Ak, int B, int D) {
  if (Hk <= 0) {
    return 0;
  }
  if (Hd <= 0) {
    return -1;
  }
  if (opt[Hd][Ad][Hk][Ak] != -1) {
    return opt[Hd][Ad][Hk][Ak];
  }
  int ret = -1;
  int temp = dfs(Hd - Ak, Ad, Hk - Ad, Ak, B, D);
  if (temp != -1) {
    if (ret == -1 || ret > temp) {
      ret = temp;
    }
  }
  temp = dfs(Hd - Ak, Ad + B, Hk, Ak, B, D);
  if (temp != -1) {
    if (ret == -1 || ret > temp) {
      ret = temp;
    }
  }
  temp = dfs(origin - Ak, Ad, Hk, Ak, B, D);
  if (temp != -1) {
    if (ret == -1 || ret > temp) {
      ret = temp;
    }
  }
  temp = dfs(Hd - Ak, Ad, Hk, max(Ak -D, 0) , B, D);
  if (temp != -1) {
    if (ret == -1 || ret > temp) {
      ret = temp;
    }
  }
  return opt[Hd][Ad][Hk][Ak] = ret;
}

int main()
{
  freopen("input", "r", stdin);
  // freopen("output", "w", stdout);
  int T;
  cin >> T;
  for (int kase = 1; kase <= T; kase++)
  {
    clear();
    int Hd, Ad, Hk, Ak, B, D;
    cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
    origin = Hd;
    for (int i = 0; i <= Hd; i++) {
      for (int j = 0; j <= Ad; j++) {
        for (int k = 0; k <= Ak; k++) {
          opt[i][j][0][k] = 0;
        }
      }
    }
    int ret = dfs(Hd, Ad, Hk, Ak, B, D);
    if (ret == -1) {
      cout << "Case #" << kase << ": " << "IMPOSSIBLE" << endl;
    } else {
      cout << "Case #" << kase << ": " << ret << endl;
    }
  }
  return 0;
}