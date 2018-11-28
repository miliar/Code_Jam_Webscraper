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

pair<int, int> arr[1005];

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    int d, n;
    scanf("%d %d", &d, &n);
    for(int i=0;i<n;i++)
      scanf("%d %d", &arr[i].f, &arr[i].s);
    sort(arr ,arr + n);
    double t = 0;
    for(int i=n-1;i>=0;i--)
    {
      bool bad = false;
      for(int j=i+1;j<n && !bad;j++)
      {
        if(arr[j].s >= arr[i].s) continue;
        int diff = arr[j].f - arr[i].f;
        double dist = (1 / arr[j].s - 1 / arr[i].s);
        dist = diff / (arr[j].s * dist);
        if(dist + arr[i].f <= d) bad = true;
      }
      if(!bad) t = max(t, (d - arr[i].f) * 1.0 / arr[i].s);
    }
    printf("Case #%d: %.10lf\n", tt++, d * 1.0 / t);
  }
  return 0;
}
