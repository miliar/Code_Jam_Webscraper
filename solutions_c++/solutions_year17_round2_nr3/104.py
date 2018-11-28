#include <bits/stdc++.h>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 2000000000000000000LL
#define INF 1000000000
#define EPS 1e-7
#define LL long long
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define setzero(a) memset(a,0,sizeof(a))
#define setdp(a) memset(a,-1,sizeof(a))
#define bits(a) __builtin_popcount(a)

using namespace std;

int speed[105], maxd[105];
LL dist[105][105];
double cost[105];
bool done[105];

int main()
{
  freopen("C-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    int n, q, x, y;
    scanf("%d %d", &n, &q);
    for(int i=0;i<n;i++)
      scanf("%d %d", &maxd[i], &speed[i]);
    for(int i=0;i<n;i++)
    {
      for(int j=0;j<n;j++)
      {
        scanf("%I64d", &dist[i][j]);
        if(dist[i][j] == -1) dist[i][j] = (1LL << 55);
      }
    }
    for(int k=0;k<n;k++)
      for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
          dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
    printf("Case #%d:", tt++);
    while(q--)
    {
      scanf("%d %d", &x, &y);
      x--, y--;
      for(int i=0;i<n;i++) cost[i] = 1e15, done[i] = false;
      cost[x] = 0;
      priority_queue<pair<double, int> > pq;
      pq.push(mp(0, x));
      while(!pq.empty())
      {
        int node = pq.top().s;
        pq.pop();
        if(done[node]) continue;
        if(node == y) break;
        done[node] = true;
        for(int i=0;i<n;i++)
        {
          if(done[i] || dist[node][i] > maxd[node]) continue;
          double nxtcost = cost[node] + dist[node][i] * 1.0 / speed[node];
          if(nxtcost < cost[i])
          {
            cost[i] = nxtcost;
            pq.push(mp(-nxtcost, i));
          }
        }
      }
      printf(" %.10lf", cost[y]);
    }
    printf("\n");
  }
  return 0;
}
