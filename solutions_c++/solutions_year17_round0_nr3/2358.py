#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define MODV 1000000007

typedef long long ll;
typedef double dbl;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pi;
void addmod(int &a, ll b){a=(a+b); if(a>=MODV)a-=MODV;}
void mulmod(int &a, ll b){a=(a*b)%MODV;}
template<class T>bool domin(T &a, const T &b){return a>b?a=b,1:0;}
template<class T>bool domax(T &a, const T &b){return a<b?a=b,1:0;}
int gi(){int a;scanf("%d",&a);return a;}
ll gll(){ll a;scanf("%lld",&a);return a;}

void doit() {
  ll n=gll(), k=gll(), ck=0, cnt;
  map<ll,ll,greater<ll>> ma[2];
  ma[0][n]=1;
  int ix=0;
  ll nxa, nxb;
  while(true){
    ix=!ix;
    int pix=!ix;
    ma[ix].clear();
    for(auto it=ma[pix].begin(); it!=ma[pix].end();it++){
      if(it==ma[pix].begin()){
        ck+=(cnt=(*it).se);
        ll num=(*it).fi;
        nxa=num/2, nxb=(num-1)/2;
        ma[ix][nxa]+=cnt;
        ma[ix][nxb]+=cnt;
      }else{
        ma[ix][(*it).fi]+=(*it).se;
      }
    }
    if(ck>=k){
      if(nxa<nxb)swap(nxa,nxb);
      cout<<nxa<<" "<<nxb;
      return;
    }
  }

}

int main() {
  int tc=gi();
  for(int i=1;i<=tc;i++){
    printf("Case #%d: ",i);
    doit();
    puts("");
  }
  return 0;
}
