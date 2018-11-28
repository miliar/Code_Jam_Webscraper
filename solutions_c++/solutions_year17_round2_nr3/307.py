#include <bits/stdc++.h>

#define MOD 1000000007

using namespace std;

typedef long long int lld;
typedef pair<int, int> pii;
typedef pair<pii, pii> line;

#define F first
#define S second

vector<double> ans;
int n, q;
int horseE[105];
int horseS[105];
lld dist[105][105];
double sol[105];

int main()
{
  int T;
  scanf("%d", &T);
  
  for (int t = 1; t <= T; t++)
  {
    ans.clear();
    scanf("%d %d", &n, &q);

    for (int i = 0; i < n; i++)
      scanf("%d %d", &horseE[i], &horseS[i]);

    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        scanf("%lld", &dist[i][j]);

    for (int k = 0; k < n; k++)
      for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
        {
          if (dist[i][k] == -1 || dist[k][j] == -1)
            continue;

          if (dist[i][j] > dist[i][k] + dist[k][j] || dist[i][j] == -1)
            dist[i][j] = dist[i][k] + dist[k][j];
        }

    for (int Q = 0; Q < q; Q++)
    {
      int u, v;
      scanf("%d %d", &u, &v);
      u--, v--;

      for (int i = 0; i < n; i++)
        sol[i] = -100;
      sol[v] = 0;

      for (int k = 0; k < 2 * n; k++)
        for (int i = 0; i < n; i++)
          for (int j = 0; j < n; j++)
          {
            if (sol[j] < -1)
              continue;

            if (dist[i][j] <= horseE[i] && dist[i][j] >= 0)
            {
              double cur = sol[j] + (1.0 * dist[i][j]) / horseS[i];
              if (sol[i] < -1 || sol[i] > cur)
                sol[i] = cur;
            }
          }

      ans.push_back(sol[u]);
    }

    printf("Case #%d:", t);
    for (int i = 0; i < q; i++)
      printf(" %0.7lf", ans[i]);
    printf("\n");
  }

  return 0;
}
