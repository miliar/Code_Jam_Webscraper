//#include <bits/stdc++.h>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
#include <cmath>
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
const int N=100100, INF=1e9;
const LD EPS=1e-7;

int n,k;
double PI = acos(-1);

double two_rhpi(PII p){
  return 2*PI*p.X*p.Y;
}

int main(){
  //openfile("A");
  int T, t=0;
  RI(T);
  while(t++<T){
    vector<PII> lists;
    printf("Case #%d: ", t);
    RI(n); RI(k);
    FOR(i,n){
      RID(R); RID(H);
      lists.pb(mp(R,H));
    }
    sort(lists.begin(), lists.end());
    double ans = 0;
    for(int i=n-1;i>=0;i--){
      double res = 0;
      res += PI * lists[i].X * lists[i].X;
      res += two_rhpi(lists[i]);
      vector<double> tmp;
      if(i<k-1) break;
      for(int j=0;j<i;j++) tmp.pb(two_rhpi(lists[j]));
      sort(tmp.begin(), tmp.end());
      FOR(j, k-1){
        int idx = (int) tmp.size() -1 -j;
        //assert(idx>=0);
        res += tmp[idx];
      }
      if(res > ans) ans = res;
    }
    printf("%.10lf\n", ans);
  }
  return 0;
}
