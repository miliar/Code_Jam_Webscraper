#include<iostream>

using namespace std;

const long double INF = 1e15;
const int MAXN = 100 + 5;
long double e[MAXN] , s[MAXN] , d[MAXN][MAXN] , ans[MAXN][MAXN];
int v[MAXN] , u[MAXN];

int main()
{
  cout.precision(10);
  int T;
  cin >> T;
  for(int t = 0;t < T;t ++)
  {
    int n , Q;
    cin >> n >> Q;
    for(int i = 1;i <= n;i ++)
      cin >> e[i] >> s[i];

    for(int i = 1;i <= n;i ++)
      for(int j = 1;j <= n;j ++)
      {
        cin >> d[i][j];
        if(d[i][j] == -1)
          d[i][j] = INF;
      }

    for(int j = 1;j <= Q;j ++)
      cin >> v[j] >> u[j];

    for(int k = 1;k <= n;k ++)
      for(int i = 1;i <= n;i ++)
        for(int j = 1;j <= n;j ++)
          d[i][j] = min(d[i][j] , d[i][k] + d[k][j]);


    for(int i = 1;i <= n;i ++)
      for(int j = 1;j <= n;j ++)
      {
        if(d[i][j] <= e[i])
          ans[i][j] = (long double)d[i][j] / (long double)s[i];
        else
          ans[i][j] = INF;
      }
      

    for(int k = 1;k <= n;k ++)
      for(int i = 1;i <= n;i ++)
        for(int j = 1;j <= n;j ++)
            ans[i][j] = min(ans[i][j] , ans[i][k] + ans[k][j]);


    cout << "Case #" << t + 1 << ": ";
    for(int i = 1;i <= Q;i ++)
      if(i != Q)
        cout << fixed << ans[v[i]][u[i]] << " ";
      else
        cout << fixed << ans[v[i]][u[i]] << endl;
  }
  return 0;
}
