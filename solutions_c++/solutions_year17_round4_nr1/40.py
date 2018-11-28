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
const in mx=109;
VI hv;
VI bst,lft;
void dot(){
  in n,p,g;
  cin>>n>>p;
  hv=VI(p,0);
  in hp=0;
  forn(z,n){
    cin>>g;
    if(g%p==0){
      ++hp;
    }
    else{
      ++hv[g%p];
    }
  }
  const in inf=1e9;
  VI pw={1,mx,mx*mx,mx*mx*mx};
  bst.clear();
  bst.resize(pw[3],-inf);
  lft.clear();
  lft.resize(pw[3],0);
  bst[0]=0;
  VI vl;
  in a;
  in ttb=0;
  forv(z,bst){
    if(bst[z]==-inf)
      continue;
    ttb=max(ttb,bst[z]);
    vl.clear();
    a=z;
    forn(zz,3){
      vl.PB(a%mx);
      a/=mx;
    }
    for(in i=1;i<p;++i){
      if(vl[i-1]<hv[i]){
	bst[z+pw[i-1]]=max(bst[z+pw[i-1]],bst[z]+(lft[z]==0));
	lft[z+pw[i-1]]=(lft[z]+(p-i))%p;
      }
    }
  }
  cout<<ttb+hp<<endl;
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
