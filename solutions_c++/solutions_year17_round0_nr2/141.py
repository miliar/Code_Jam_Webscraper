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
bool isok(VI dgs, VI rdg){
  assert(sz(dgs)==sz(rdg));
  for(in i=sz(dgs)-1;i>=0;--i){
    if(dgs[i]<rdg[i])
      return 0;
    if(rdg[i]<dgs[i])
      return 1;
  }
  return 1;
}
void dot(){
  in n;
  cin>>n;
  VI dgs;
  while(n){
    dgs.PB(n%10);
    n/=10;
  }
  VI rdg(sz(dgs));
  for(in i=sz(dgs)-1;i>=0;--i){
    for(in dg=9;dg>=0;--dg){
      for(in j=i;j>=0;--j)
	rdg[j]=dg;
      if(isok(dgs,rdg)){
	break;
      }
    }
  }
  in ans=0;
  for(in i=sz(rdg)-1;i>=0;--i){
    ans=10*ans+rdg[i];
  }
  cout<<ans<<endl;
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
