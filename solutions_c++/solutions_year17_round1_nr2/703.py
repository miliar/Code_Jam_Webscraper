#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#pragma comment(linker, "/STACK:266777216")
using namespace std;

#define assert(f) { if(!(f)) { fprintf(stderr,"Assertion failed: "); fprintf(stderr,#f); fprintf(stderr,"\n"); exit(1); } }

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<double> VD;
typedef pair<double,double> PDD;

const int inf=1000000000;
const LL INF=LL(inf)*inf;
const double eps=1e-9;
const double PI=2*acos(0.0);
#define bit(n) (1<<(n))
#define bit64(n) ((LL(1))<<(n))
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) (a).begin(),(a).end()
#define fill(ar,val) memset((ar),(val),sizeof (ar))
#define MIN(a,b) {if((a)>(b)) (a)=(b);}
#define MAX(a,b) {if((a)<(b)) (a)=(b);}
#define sqr(x) ((x)*(x))
#define X first
#define Y second

clock_t start=clock();

struct SegmEnd {
  int x;
  int y;
  // -1 start, 1 end
  int state;
  int type;
  int ind;
  SegmEnd(){}
  SegmEnd(int x_,int y_,int s,int t,int i):x(x_),y(y_),state(s),type(t),ind(i){}
  bool operator<(const SegmEnd& s) const {
    if(x!=s.x) return x<s.x;
    if(state != s.state) return state < s.state;
    return y<s.y;
  }
};

const int N = 55;

int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d: ",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
    if(tst==61)
      tst=tst;
    int n,m;
    scanf("%d%d",&n,&m);
    int a[N];
    for(int i=0;i<n;i++) scanf("%d",a+i);
    int L[N][N], R[N][N];
    vector<SegmEnd> s;
    for(int i=0;i<n;i++) {
      for(int j=0;j<m;j++) {
        int x;
        scanf("%d",&x);
        L[i][j] = (10*x+11*a[i]-1)/(11*a[i]);
        R[i][j] = (10*x)/(9*a[i]);
        if(L[i][j]<=R[i][j]) {
          s.pb(SegmEnd(L[i][j],R[i][j],-1,i,j));
          s.pb(SegmEnd(R[i][j],0,1,i,j));
        }
      }
    }

    /*int cor=0;
    if(n==1) cor=s.sz/2; else {
      int p[N];
      for(int i=0;i<m;i++) p[i]=i;
      do {
        int i;
        for(i=0;i<m;i++) {
          int L1=L[0][i],R1=R[0][i];
          int L2=L[1][p[i]],R2=R[1][p[i]];
          if(!(L1<=R1 && L1<=R2 && L2<=R1 && L2<=R2)) break;
        }
        MAX(cor,i);
      } while(next_permutation(p,p+m));
    }
    printf("%d ",cor);*/

    sort(all(s));
    set<PII> opened[N];
    for(int i=0;i<n;i++) opened[i].cl;
    int res=0;
    for(int k=0;k<s.sz;k++) {
      int i=s[k].type;
      int j=s[k].ind;
      if(s[k].state == -1) {
        opened[i].insert(mp(R[i][j],j));
        int h;
        for(h=0;h<n;h++)
          if(opened[h].empty()) break;
        if(h==n) {
          res++;
          for(int h=0;h<n;h++) {
            opened[h].erase(opened[h].begin());
          }
        }
      } else {
        opened[i].erase(mp(R[i][j],j));
      }
    }
    printf("%d\n",res);
    //assert(res==cor);
	}
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
