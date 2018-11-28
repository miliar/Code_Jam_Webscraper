#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF=1e18+7;
const int MX=1e3+3;
map<ll, ll> ans;
map<ll, bool> vis;
vector<pair<ll,ll> > shit;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
  int t;
  cin>>t;
  for(int ii=1;ii<=t;++ii)
  {
      vis.clear();
      ans.clear();
      shit.clear();
      ll n , k;
      cin>>n>>k;
      ll v1=n,v2=0;
      queue<ll> q;
      q.push(n);
      vis[n] = 1;
      ans[n] = 1;
      while(!q.empty())
      {
          ll cur = q.front();
          q.pop();
          ll tmp;
          if(cur != n)
          {
              if(ans.count(cur*2))
                ans[cur] += ans[cur*2];
            if(ans.count(cur*2+2))
                ans[cur] += ans[cur*2+2];
              if(ans.count(cur*2+1))
                ans[cur] += ans[cur*2+1]*2;
          }
          cur--;
          tmp = cur/2;
          ll tmp2 = cur - tmp;
          if(tmp2 > 0 && !vis[tmp2])
            vis[tmp2] = 1,q.push(tmp2);
          if(tmp > 0 && !vis[tmp])
            vis[tmp] = 1,q.push(tmp);
      }

      for(auto u: ans)
          shit.push_back(u);

        for(int i=shit.size()-1;i>=0;--i)
        {
            if(k <= shit[i].second)
            {
                ll tmp1,tmp2;
                ll cc = shit[i].first;
                cc--;
                tmp1 = cc/2;
                cc -= tmp1;
                tmp2 = cc;
                printf("Case #%d: %lld %lld\n",ii,tmp2,tmp1);
                break;
            }
            k -= shit[i].second;
        }

  }
    return 0;
}


