#include <iostream>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 1010;
struct Cake
{
  double r, h;
} c[N];

bool operator<(const Cake&c1, const Cake&c2)
{
  return c1.r > c2.r;
}

int n, K;
void init()
{
  cin >> n >> K;
  for (int i=1; i<=n; ++i)
    cin >> c[i].r >> c[i].h;
  sort(c+1, c+n+1);
}

double f[N][N];
const double pi = acos(-1);

double work()
{
  f[0][0] = 0;
  for (int i=1; i<=K; ++i)
    f[0][i] = -1e100;
  for (int i=1; i<=n; ++i)
  {
    for (int u=0; u<=K; ++u)
      f[i][u] = 0;
    for (int j=0; j<i; ++j)
      for (int u=0; u<K; ++u)
      {
        double s = 0;
        if (u == 0)
          s = pi * c[i].r * c[i].r;
        double h = 2 * pi * c[i].r * c[i].h;
        f[i][u+1] = max(f[i][u+1], f[j][u] + s + h);
      }
  }
  double ans = 0;
  for (int i=K; i<=n; ++i)
    if (f[i][K] > ans)
      ans = f[i][K];
  return ans;
}

int main()
{
  //freopen("A-small-attempt0.in", "r", stdin);
  //freopen("A.out", "w", stdout);
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  //freopen("in", "r", stdin);
  //freopen("out", "w", stdout);
  int T;
  cin >> T;
  for (int i=1; i<=T; ++i)
  {
    cout << "Case #" << i << ": ";
    init();
    printf("%.7f\n", work());
  }
}
