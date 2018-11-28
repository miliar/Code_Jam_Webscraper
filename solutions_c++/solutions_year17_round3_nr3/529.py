#include <iostream>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 60;
int n, k;
double p[N], U;

void init()
{
  cin >> n >> k >> U;
  for (int i=1; i<=n; ++i)
    cin >> p[i];
}

double work()
{
  sort(p+1, p+1+n);
  while (U>0)
  {
    double small = p[1];
    double second = -1;
    for (int i=1; i<=n; ++i)
      if (p[i] > small)
      {
        second = p[i];
        break;
      }
    if (second < 0)
    {
      for (int i=1; i<=n; ++i)
        p[i] += U/n;
      U = 0;
      break;
    }
    int k = 0;
    for (int i=1; i<=n; ++i)
      if (p[i] < second)
        ++k;
    if ((second-small) * k <= U)
    {
      U -= (second-small) * k;
      for (int i=1; i<=k; ++i)
        p[i] = second;
    }
    else
    {
      for (int i=1; i<=k; ++i)
        p[i] += U/k;
      U = 0;
    }
  }
  double ans = 1;
  for (int i=1; i<=n; ++i)
    ans *= p[i];
  return ans;
}

int main()
{
  freopen("C-small-1-attempt1.in", "r", stdin);
  freopen("C.out", "w", stdout);
  //freopen("B-large.in", "r", stdin);
  //freopen("B-large.out", "w", stdout);
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
