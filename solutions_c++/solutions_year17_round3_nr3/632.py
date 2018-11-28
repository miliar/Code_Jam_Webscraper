//#include <bits/stdc++.h>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
#define openfile(s) freopen(s".in","r",stdin);freopen(s".out","w",stdout)
#define mpr std::make_pair
#define lg(x) (31-__builtin_clz(x))
#define lgll(x) (63-__builtin_clzll(x))
#define __count __builtin_popcount
#define __countll __builtin_popcountll
#define X first
#define Y second
#define mst(x) memset(x,0,sizeof(x))
#define mst1(x) memset(x,-1,sizeof(x))
#define ALL(c) (c).begin(),(c).end()
#define FOR(i,n) for(int i=0;i<n;i++)
#define FOR1(i,n) for(int i=1;i<=n;i++)
#define FORit(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define pb push_back
#define mp make_pair
#define RI(x) scanf("%d",&x)
#define RID(x) int x;RI(x)
using namespace std;
typedef long long LL;
typedef double LD;
typedef vector<int> VI;
typedef std::pair<int,int> PII;
template<class T>inline void maz(T &a,T b){if(a<b)a=b;}
template<class T>inline void miz(T &a,T b){if(a>b)a=b;}
template<class T>inline T abs(T a){return a>0?a:-a;}
const int N=100, INF=1e9;
const LD EPS=1e-9;

int n,k;
double u;
double P[N];
double usage(double level){
  double res = 0;
  FOR(i, n){
    if(P[i] < level) res += level - P[i];
  }
  return res;
}

int main(){
  int T, t=0;
  RI(T);
  while(t++ < T){
    printf("Case #%d: ", t);
    RI(n); RI(k);
    scanf("%lf", &u);
    FOR(i, n) scanf("%lf", &P[i]);
    double head = 0, end = 1;
    while(end-head>EPS){
      double mid = (end+head)/2;
      double res = usage(mid);
      if(res > u) end = mid;
      else head = mid;
    }
    double ans = 1;
    FOR(i,n){
      if(P[i]-EPS < head) ans *= head;
      else ans *= P[i];
    }
    printf("%.15lf\n", ans);
  }
  return 0;
}
