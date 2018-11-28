#include<cstdio>
#include<algorithm>
#include<map>
#include<vector>
using namespace std;
typedef long long ll;
typedef vector<ll> V;
const int N=100000;
int T,C,i;
ll n,m,cnt,q[N];
map<ll,int>id;
map<ll,bool>vis;
map<ll,V>f;
V g;
struct P{
  ll a,b;
  P(){}
  P(ll _a,ll _b){a=_a,b=_b;}
}a[N];
inline bool cmp(const P&a,const P&b){return a.a>b.a;}
void dfs0(ll n){
  if(n<1)return;
  if(id[n])return;
  id[n]=cnt;
  q[cnt++]=n;
  if(n&1)dfs0(n/2);
  else{
    dfs0(n/2-1);
    dfs0(n/2);
  }
}
V dfs1(ll n){
  if(n<1){
    V t;
    for(int i=0;i<cnt;i++)t.push_back(0);
    return t;
  }
  if(vis[n])return f[n];
  vis[n]=1;
  V t=dfs1(n/2);
  if(n&1){
    for(int i=0;i<cnt;i++)t[i]*=2;
  }else{
    V o=dfs1(n/2-1);
    for(int i=0;i<cnt;i++)t[i]+=o[i];
  }
  t[id[n]]++;
  return f[n]=t;
}
int main(){
  scanf("%d",&T);
  for(C=1;C<=T;C++){
    printf("Case #%d: ",C);
    scanf("%I64d%I64d",&n,&m);
    id.clear();
    vis.clear();
    f.clear();
    cnt=0;
    dfs0(n);
    g=dfs1(n);
    for(i=0;i<cnt;i++)a[i]=P(q[i],g[i]);
    sort(a,a+cnt,cmp);
    for(i=0;i<cnt;i++)if(m<=a[i].b){
      ll t=a[i].a;
      if(t&1)printf("%I64d %I64d\n",t/2,t/2);
      else printf("%I64d %I64d\n",t/2,t/2-1);
      break;
    }else m-=a[i].b;
  }
}