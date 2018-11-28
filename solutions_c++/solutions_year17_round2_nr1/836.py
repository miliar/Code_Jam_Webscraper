#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 2000;
const double eps = 1e-6;

int K[N], S[N], D, n;

void init()
{
  cin >> D >> n;
  for (int i=0; i<n; ++i)
    cin >> K[i] >> S[i];
}

bool ok(double s)
{
  for (int i=0; i<n; ++i)
  {
    if (S[i] >= s)
      continue;
    double rs = s-S[i];
    int dis = K[i];
    if (dis*s < D*rs)
      return false;
  }
  return true;
}

double work()
{
  /*
  double left = 0;
  double right = D;
  while (right-left>eps)
  {
    double mid = (right+left)*0.5;
    if (ok(mid))
      left = mid;
    else
      right = mid;
  }
  return left;
  */
  double mintime = 0;
  for (int i=0; i<n; ++i)
  {
    double time = 1.0*(D-K[i])/S[i];
    mintime = max(time, mintime);
  }
  return D/mintime;
}

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  //freopen("a.in", "r", stdin);
  //freopen("a.out", "w", stdout);
  int T;
  cin >> T;
  for (int i=1; i<=T; ++i)
  {
    cout << "Case #" << i << ": ";
    init();
    printf("%.6f\n", work());
  }
}
