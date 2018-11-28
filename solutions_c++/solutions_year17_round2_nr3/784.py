#include <bits/stdc++.h>
using namespace std;
const double oo = 1e18;

int n, e[111], s[111], d[111][111];
double a[111][111];

void init()
{
  for (int x = 0; x < n; x++)
  {
    a[x][x] = 0;
    vector <int> done(n, 0);
    while (1)
    {
      int u = -1;
      double minTime = oo / 2;
      for (int i = 0; i < n; i++)
        if (!done[i] && a[x][i] < minTime)
        {
          minTime = a[x][i];
          u = i;
        }

      if (u < 0)
        break;
      done[u] = 1;

      for (int v = 0; v < n; v++)
      {
        if (d[u][v] < 0)
          continue;
        double curTime = a[x][u] + 1. * d[u][v] / s[x];
        if (curTime * s[x] <= e[x])
          a[x][v] = min(a[x][v], curTime);
      }
    }
  }

  for (int k = 0; k < n; k++)
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
}

int main()
{
  int test, from, to, q;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  {
    cerr << "Running test " << iTest << endl;
    cin >> n >> q;
    for (int i = 0; i < n; i++)
      cin >> e[i] >> s[i];
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
      {
        cin >> d[i][j];
        a[i][j] = oo;
      }
    init();

    cout << "Case #" << iTest << ": ";
    while (q--)
    {
      cin >> from >> to;
      cout << fixed << setprecision(9) << a[from - 1][to - 1] << ' ';
    }
    cout << endl;
  }
}