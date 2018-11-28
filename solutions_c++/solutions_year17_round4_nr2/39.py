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
VI b,p;
void dot(){
  in n,c,m;
  cin>>n>>c>>m;
  b=p=VI(m);
  forn(i,m)
    cin>>p[i]>>b[i];
  in mnnd=0;
  for(in i=1;i<=c;++i){
    in ct=0;
    forv(j,b)
      ct+=(b[j]==i);
    mnnd=max(mnnd,ct);
  }
  for(in i=1;i<=n;++i){
    in ct=0;
    forv(j,p)
      ct+=(p[j]<=i);
    mnnd=max(mnnd,(ct+i-1)/i);
  }
  cout<<mnnd<<" ";
  in f=0;
  for(in i=1;i<=n;++i){
    in ct=0;
    forv(j,p)
      ct+=(p[j]==i);
    f+=max(0LL,ct-mnnd);
  }
  cout<<f<<endl;
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
