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

const int N = 1111;

int main()
{
  freopen("/Users/antonl/Dropbox (Facebook)/!My programs/GoogleCodeJam/2017/Round2/B/B/2.in","r",stdin);
  freopen("/Users/antonl/Dropbox (Facebook)/!My programs/GoogleCodeJam/2017/Round2/B/B/2.out","w",stdout);
  int TST,tst=0;
  for(scanf("%d",&TST);TST--;)
  {
    printf("Case #%d: ",++tst);
    fprintf(stderr,"Case #%d:\n",tst);
    int n,c,m;
    scanf("%d%d%d",&n,&c,&m);
    int cnt[N]={0};
    int a[N]={0},b[N];
    for(int i=0;i<m;i++) {
      int p,b;
      scanf("%d%d",&p,&b);
      a[p]++;
      cnt[b]++;
    }
    int L=0;
    for(int i=1;i<=c;i++)
      MAX(L,cnt[i]);
    L--;
    int R=m;
    while(L+1<R) {
      int M=(L+R)/2;
      for(int i=1;i<=n;i++) b[i]=a[i];
      for(int i=n;i>1;i--)
        if(b[i]>M) {
          b[i-1]+=b[i]-M;
        }
      if(b[1]>M) L=M; else R=M;
    }
    int res=0;
    for(int i=1;i<=n;i++)
      res+=max(a[i]-R,0);
    printf("%d %d\n",R,res);
  }
  fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
  return 0;
}















