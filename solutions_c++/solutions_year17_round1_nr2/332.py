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
typedef pair<ll, ll> pll;
void addmod(int &a, ll b){a=(a+b); if(a>=MODV)a-=MODV;}
void mulmod(int &a, ll b){a=(a*b)%MODV;}
template<class T>bool domin(T &a, const T &b){return a>b?a=b,1:0;}
template<class T>bool domax(T &a, const T &b){return a<b?a=b,1:0;}
int gi(){int a;scanf("%d",&a);return a;}
ll gll(){ll a;scanf("%lld",&a);return a;}

pll getr(ll bs, ll av){
  ll mn=-1, mx=-1;
  ll tbs=av/bs;
  ll tn=(tbs*bs*9)/(bs*10)-2;
  ll tx=(tbs*bs*12)/(bs*10)+2;
  for(ll v=tn;v<=tx;v++){
    if(v*bs*9<=av*10 && v*bs*11>=av*10){
      if(mn==-1)mn=v;
      mx=v;
    }
  }
  return {mn,mx};
}

void doit() {
  int n=gi(), p=gi(), ans=0;
  vector<ll> bs(n);
  vector<vector<ll>> av(n, vector<ll>(p));
  vector<vector<pll>> mnx(n, vector<pll>(p));
  vector<vector<bool>> tk(n,vector<bool>(p,false));
  for(int i=0;i<n;i++){
    bs[i]=gi();
  }
  for(int i=0;i<n;i++){
    for(int j=0;j<p;j++){
      av[i][j]=gi();
    }
    sort(av[i].begin(), av[i].end());
    for(int j=0;j<p;j++){
      mnx[i][j]=getr(bs[i],av[i][j]);
      ll mn=mnx[i][j].fi;
      ll mx=mnx[i][j].se;
      if(mn==-1 || mx==-1)tk[i][j]=true;
    }
  }
  vector<int> sel(n);

  for(int j=0;j<p;j++)
  if(!tk[0][j]){
    bool nf=true;
    fill(sel.begin(),sel.end(),-1);
    sel[0]=j;

    for(ll v=mnx[0][j].fi;v<=mnx[0][j].se && nf;v++){
      bool vok=true;
      for(int i=1;i<n && vok;i++){
        for(int jj=0;jj<p && sel[i]==-1;jj++)
        if(!tk[i][jj] && v>=mnx[i][jj].fi && v<=mnx[i][jj].se){
          sel[i]=jj;
        }

        if(sel[i]==-1)vok=false;
      }
      if(vok){
        nf=false;
        for(int i=0;i<n;i++)tk[i][sel[i]]=true;
        ans++;
      }
    }
  }
  cout<<ans;
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
