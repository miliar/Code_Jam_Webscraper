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
  char c[1005];
  int k, l, ans=0;
  bool ok=true;
  scanf("%s %d", c, &k);
  l=strlen(c);
  for(int i=0;i<=(l-k);i++)
  if(c[i]=='-'){
    ans++;
    for(int j=i;j<(i+k);j++){
      if(c[j]=='-')c[j]='+';
      else c[j]='-';
    }
  }
  for(int i=0;i<l;i++)
  if(c[i]=='-'){
    ok=false;
  }
  if(!ok){
    cout<<"IMPOSSIBLE";
    return;
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
