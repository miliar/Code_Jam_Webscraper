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
  ll ans=0;
  ll n=gll();
  int nd[20], nlen=0;
  ll tn=n;
  while(tn){
    nd[nlen++]=tn%10;
    tn/=10;
  }
  for(int kk=0;kk<20;kk++){
    bool ok=true;
    for(int i=nlen-2;i>=0 && ok;i--){
      if(nd[i]<nd[i+1]){
        int j;
        for(j=i;j>=0;j--)nd[j]=9;
        for(j=i+1;j<(nlen-1) && nd[j]==1;j++){
          nd[j]=9;
        }
        nd[j]--;
        ok=false;
      }
    }
  }
  for(int i=nlen-1;i>=0;i--){
    ans = ans*10 + nd[i];
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
