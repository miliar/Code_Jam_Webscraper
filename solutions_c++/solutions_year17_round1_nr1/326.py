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
  int r=gi(), c=gi();
  vector<char[55]> vs(r);
  for(int i=0;i<r;i++){
    scanf(" %s",vs[i]);
  }
  for(int ri=0;ri<r;ri++){
    for(int ci=0;ci<c;ci++)
      if(vs[ri][ci]=='?' && ci>0 && vs[ri][ci-1]!='?'){
        vs[ri][ci]=vs[ri][ci-1];
      }
    for(int ci=c-1;ci>=0;ci--)
      if(vs[ri][ci]=='?' && ci<(c-1) && vs[ri][ci+1]!='?'){
        vs[ri][ci]=vs[ri][ci+1];
      }
  }
  for(int ci=0;ci<c;ci++){
    for(int ri=0;ri<r;ri++)
    if(vs[ri][ci]=='?' && ri>0 && vs[ri-1][ci]!='?'){
      vs[ri][ci]=vs[ri-1][ci];
    }
    for(int ri=r-1;ri>=0;ri--)
    if(vs[ri][ci]=='?' && ri<(r-1) && vs[ri+1][ci]!='?'){
      vs[ri][ci]=vs[ri+1][ci];
    }
  }
  printf("\n");
  for(int ri=0;ri<r;ri++)
    printf("%s\n",vs[ri]);
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
