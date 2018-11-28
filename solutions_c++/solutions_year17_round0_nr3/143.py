#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cassert>
#define PB push_back
#define MP make_pair
#define sz(v) (in((v).size()))
#define forn(i,n) for(in i=0;i<(n);++i)
#define forv(i,v) forn(i,sz(v))
#define fors(i,s) for(auto i=(s).begin();i!=(s).end();++i)
#define all(v) (v).begin(),(v).end()
using namespace std;
typedef long long in;
typedef vector<in> VI;
typedef vector<VI> VVI;
map<pair<in,in>,in> tt;
in usd(in n, in pr){
  if(n==0)
    return 0;
  auto it=tt.find(MP(n,pr));
  if(it!=tt.end())
    return it->second;
  in mn=pr/2;
  in mx=pr-mn;
  in c1=(n-1)/2;
  in c2=(n-1)-c1;
  if(MP(mn,mx)>MP(c1,c2))
    return 0;
  in rs=1+usd(c1,pr)+usd(c2,pr);
  return tt[MP(n,pr)]=rs;
}
void dot(){
  in n,k;
  cin>>n>>k;
  in mn=0;
  in mx=3e18;
  in md;
  while(mx-mn>1){
    md=(mx+mn)/2;
    if(usd(n,md)>=k)
      mn=md;
    else
      mx=md;
  }
  in c1=mn/2;
  in c2=mn-c1;
  cout<<c2<<" "<<c1<<endl;
}
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  in t;
  cin>>t;
  forn(z,t){
    cout<<"Case #"<<(z+1)<<": ";
    dot();
  }
  return 0;
}
