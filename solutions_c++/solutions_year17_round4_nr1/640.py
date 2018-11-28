#include <bits/stdc++.h>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 2000000000000000000LL
#define INF 1000000000
#define EPS 1e-8
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

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    int n, p, c = 0, x;
    scanf("%d %d", &n, &p);
    vector<int> v;
    v.resize(p);
    for(int i=0;i<n;i++)
    {
      scanf("%d", &x);
      if(x % p) v[x%p]++;
      else c++;
    }
    if(p == 2) c += (v[1] + 1) / 2;
    else if(p == 3)
    {
      int tmp = min(v[1], v[2]);
      c += tmp;
      v[1] -= tmp;
      v[2] -= tmp;
      c += (v[2] + 2) / 3;
      c += (v[1] + 2) / 3;
    }
    else
    {
      int tmp = min(v[1], v[3]);
      c += tmp;
      v[1] -= tmp;
      v[3] -= tmp;

      c += v[2] / 2;
      v[2] %= 2;

      if(v[2])
      {
        if(v[1])
        {
          c += (v[1] + 5) / 4;
        }
        else if(v[3])
        {
          c += (v[3] + 5) / 4;
        }
        else c++;
      }
      else
      {
        c += (v[1] + 3) / 4;
        c += (v[3] + 3) / 4;
      }
    }
    printf("Case #%d: %d\n", tt++, c);
  }
  return 0;
}
