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

int main()
{
  freopen("C-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    LL n, k;
    scanf("%I64d %I64d", &n, &k);
    vector<pair<LL, LL> > v;
    v.pb(mp(n, 1));
    LL mini = -1;
    LL maxi = -1;
    bool done = false;
    while(!v.empty())
    {
      map<LL, LL> nxt;
      for(pair<LL, LL> x : v)
      {
        k -= x.s;
        if(k <= 0)
        {
          maxi = x.f / 2;
          mini = (x.f - 1) / 2;
          done = true;
          break;
        }
        nxt[x.f / 2] += x.s;
        nxt[(x.f - 1) / 2] += x.s;
      }
      if(done) break;
      v.clear();
      for(pair<LL, LL> x : nxt)
      {
        if(!x.f) continue;
        v.pb(x);
      }
      assert(v.size() < 3);
      if(v.size() == 2)
      {
        swap(v[0], v[1]);
        assert(v[0].f > v[1].f);
      }
    }
    assert(maxi != -1);
    assert(maxi >= mini);
    printf("Case #%d: %I64d %I64d\n", tt++, maxi, mini);
  }
  return 0;
}
