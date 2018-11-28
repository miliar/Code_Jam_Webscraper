#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair
#define pii pair <int, int>
#define pll pair <ll,ll>
using namespace std;
const int ma = 1e5+5;
int lef[ma], rig[ma];
bool vis[ma];
pair <int, pair <int, int> > pr[1005], p1[1005];
int main()
{
  //freopen("in1.txt","r",stdin);
  //freopen("o.txt","w",stdout);
  int t;
  cin>>t;
  int p;
  for(p=1;p<=t;p++)
  {
    for(int i=1;i<=1005;i++)
    {
      vis[i] = false;
    }
    int n,k;
    cin>>n>>k;
    int ans1, ans2,id;
    vis[n%2 + n/2] = true;
    k--;
    if(k==0)
      cout<<"Case #"<<p<<": "<<max(n%2+n/2-1,n - (n%2 +n/2))<<" "<<min(n%2+n/2-1,n - (n%2 +n/2))<<endl;
    else
    {
      while(k)
      {
        int tp=0;
        for(int i=1;i<=n;i++)
        {
          if(!vis[i])
          {
            lef[i] = i-tp-1;
          }
          else
            tp = i;
        }
        tp = n+1;
        for(int i=n;i>=1;i--)
        {
          if(!vis[i])
          {
            rig[i] = tp-i-1;
          }
          else
            tp = i;
        }
        
        int ma = -1;
        bool f=false;
        int o=0;
        for(int i=1;i<=n;i++)
        {
          if(!vis[i] and ma < min(lef[i], rig[i]))
          {
            ma = min(lef[i], rig[i]);
          }
        }
        for(int i=1;i<=n;i++)
        {
          if(!vis[i] and ma == min(lef[i], rig[i]))
          {
              pr[o].first = i;
              pr[o].second.first = max(lef[i],rig[i]);
              pr[o].second.second = min(lef[i],rig[i]);
              o++;
              ans1 = max(lef[i],rig[i]);
              ans2 = min(lef[i],rig[i]);
              id=i;
          }
        }
        if(o>0)
        {
          ma = -1;
          for(int i=0;i<o;i++)
          {
            if(pr[i].second.first > ma)
            {
              ma = pr[i].second.first;
            }
          }
          int h=0;
          for(int i=0;i<o;i++)
          {
            if(pr[i].second.first == ma)
            {
              p1[h].first = pr[i].first;
              p1[h].second.first = pr[i].second.first;
              p1[h].second.second = pr[i].second.second;
              h++;
            }
          }
          sort(p1,p1+h);
          vis[p1[0].first] = true;
          ans1 = p1[0].second.first;
          ans2 = p1[0].second.second;
        }
        else
        {
          vis[id] = true;
        }
        k--;
      }
      cout<<"Case #"<<p<<": "<<ans1<<" "<<ans2<<endl;
    }
  }

  return 0;
}