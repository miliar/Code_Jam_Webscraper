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
  int n=gi(), c=gi(), m=gi(), mxc=0;
  vi cc(c,0), nc(n,0);
  vector<vi> ncc(n,vi(c,0));
  for(int i=0;i<m;i++){
    int ni=gi()-1, ci=gi()-1;
    nc[ni]++, cc[ci]++;
    ncc[ni][ci]++;
    domax(mxc,cc[ci]);
  }
  for(int ans=mxc;;ans++){
    int req=0;
    int can=0;
    bool ok=true;
    for(int i=0;i<n;i++) {
      if(nc[i]<ans)can+=(ans-nc[i]);
      else if(nc[i]>ans){
        int need = nc[i]-ans;
        if(need>can)ok=false;
        else {
          req+=need;
          can-=need;
        }
      }
    }
    if(ok) {
      cout<<ans<<" "<<req;
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
