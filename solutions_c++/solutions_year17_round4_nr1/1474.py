#include <iostream>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 200;
int n, g[N], p;
int dist[N][4];
int cnt;

void gen(int d)
{
  static int st[4];
  if (d == p)
  {
    int sum = 0;
    int tot = 0;
    for (int i=0; i<p; ++i)
    {
      sum += st[i]*i;
      tot += st[i];
    }
    if (sum%p == 0 && tot <= p)
    {
      for (int i=0; i<p; ++i)
      {
        dist[cnt][i] = st[i];
        //printf("%d, ", st[i]);
      }
      //printf("\n");
      ++cnt;
    }
    return;
  }
  for (int i=0; i<=p; ++i)
  {
    st[d] = i;
    gen(d+1);
  }
}

void init()
{
  memset(g,0,sizeof(g));
  cin >> n >> p;
  for (int i=1; i<=n; ++i)
  {
    int x;
    cin >> x;
    g[x%p]++;
  }
  cnt = 0;
  gen(1);
}

int dfs(int i, int now)
{
  if (i == cnt)
  {
    int ex = 0;
    for (int i=1; i<p; ++i)
      if (g[i] > 0)
        ex = 1;
    return now + ex;
  }
  int ans = 0;
  for (int j=0; j<N; ++j)
  {
    bool ok = true;
    for (int k=0; k<p; ++k)
      if (dist[i][k]*j > g[k])
      {
        ok = false;
        break;
      }
    if (!ok) break;
    for (int k=0; k<p; ++k)
      g[k] -= dist[i][k]*j;
    ans = max(ans, dfs(i+1, now+j)); 
    for (int k=0; k<p; ++k)
      g[k] += dist[i][k]*j;
  }
  return ans;
}

int work()
{
  return dfs(1, 0)+g[0];
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
    init();
    cout << "Case #" << i << ": ";
    printf("%d\n", work());
  }
}
