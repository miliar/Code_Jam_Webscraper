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
  int n=gi(), p=gi(), ans=0;
  vi a(p+2,0);
  for(int i=0;i<n;i++){
    int g=gi()%p;
    a[g]++;
  }
  ans+=a[0];
  if(p==4){
    int v=min(a[1],a[3]);
    ans+=v;
    a[1]-=v, a[3]-=v;
    ans+=a[2]/2;
    int np=0;
    if(a[2]&1)np=2, ans++;
    while(a[1]>0 || a[3]>0){
      if(np==0)ans++;
      if(a[1])np++, a[1]--;
      if(a[3])np+=3, a[3]--;
      np %= 4;
    }
  }else if(p==3){
    int v=min(a[1],a[2]);
    ans+=v;
    a[1]-=v, a[2]-=v;
    int np=0;
    while(a[1]>0 || a[2]>0){
      if(np==0)ans++;
      if(a[1])np++, a[1]--;
      if(a[2])np+=2, a[2]--;
      np %= 3;
    }
  }else{
    ans+=a[1]/2;
    if(a[1]&1)ans++;
  }
  cout<<ans<<endl;

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
