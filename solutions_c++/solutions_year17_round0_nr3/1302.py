#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <cstring>
#include <queue>
#include <map>
using namespace std;
typedef long long ll;
const int maxn = 105;

/*ll dfs(ll x, ll y) {
  if(x<y)return 0;
  if(x==y)return 1;
  return dfs((x-1)>>1, y)+dfs(x>>1, y);
}*/

int main() {
  //freopen("in.cpp","r",stdin);
  freopen("C-large.in","r",stdin);
  freopen("C.l.out","w",stdout);

  /*int tt=999999;
  for(int i=1;i<=tt;i++)
  if(dfs(tt,i))
  cout<<i<<": "<<dfs(tt,i)<<endl;*/

  int T,ncase=0;
  cin>>T;
  while(T--) {
    ll n,m;
    cin>>n>>m;
    vector<pair<ll,ll>>v{make_pair(n,1)};
    int pos0=0,pos1=-1;
    while(v[pos0].first!=1) {
      if(v[pos0].first==2) {
        if(pos1==-1) {
          v.push_back(make_pair(1,v[pos0].second));
          pos0++;
        } else {
          v[pos1].second+=v[pos0].second;
          pos0=pos1;
          pos1=-1;
        }
      } else {
        vector<ll>tmp;
        if(v[pos0].first>>1)tmp.push_back(v[pos0].first>>1);
        if((v[pos0].first-1)>>1)tmp.push_back((v[pos0].first-1)>>1);
        if(pos1!=-1) {
          if(v[pos1].first>>1)tmp.push_back(v[pos1].first>>1);
          if((v[pos1].first-1)>>1)tmp.push_back((v[pos1].first-1)>>1);
        }
        sort(tmp.begin(),tmp.end());
        tmp.erase(unique(tmp.begin(),tmp.end()),tmp.end());
        reverse(tmp.begin(),tmp.end());
        //cout<<tmp.size()<<endl;
        //for(int i=0; i<tmp.size(); i++)cout<<tmp[i]<<" ";
        //cout<<endl;
        v.push_back(make_pair(tmp[0],0));
        if(tmp.size()==2)v.push_back(make_pair(tmp[1],0));
        int add=(pos1!=-1);

        ll tt=v[pos0].first>>1;
        if(tt) {
          if(tmp[0]==tt)v[pos0+1+add].second+=v[pos0].second;
          else v[pos0+2+add].second+=v[pos0].second;
        }
        tt=(v[pos0].first-1)>>1;
        if(tt) {
          if(tmp[0]==tt)v[pos0+1+add].second+=v[pos0].second;
          else v[pos0+2+add].second+=v[pos0].second;
        }

        if(pos1!=-1) {
          tt=(v[pos1].first-1)>>1;
          if(tt) {
            if(tmp[0]==tt)v[pos1+1].second+=v[pos1].second;
            else v[pos1+2].second+=v[pos1].second;
          }
          tt=v[pos1].first>>1;
          if(tt) {
            if(tmp[0]==tt)v[pos1+1].second+=v[pos1].second;
            else v[pos1+2].second+=v[pos1].second;
          }
        }

        pos0+=add+1;
        if(tmp.size()==2)pos1=pos0+1;
        else pos1=-1;
      }
    }
    //for(int i=v.size()-1; i>=0; i--)
      //cout<<v[i].first<<": "<<v[i].second<<endl;
    ll sum=0,ret=n;
    for(int i=0;i<v.size();i++){
      ret=v[i].first;
      sum+=v[i].second;
      if(sum>=m)break;
    }
    cout<<"Case #"<<++ncase<<": "<<(ret>>1)<<" "<<((ret-1)>>1)<<endl;
  }
  return 0;
}
