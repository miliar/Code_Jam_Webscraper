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

int main()
{
  freopen("/Users/antonl/Dropbox (Facebook)/!My programs/GoogleCodeJam/2017/Round2/A/2.in","r",stdin);
  freopen("/Users/antonl/Dropbox (Facebook)/!My programs/GoogleCodeJam/2017/Round2/A/A/2.out","w",stdout);
  int TST,tst=0;
  for(scanf("%d",&TST);TST--;)
  {
    printf("Case #%d: ",++tst);
    fprintf(stderr,"Case #%d:\n",tst);
    int n,p;
    scanf("%d%d",&n,&p);
    int a[4]={0};
    for(int i=0;i<n;i++) {
      int x;
      scanf("%d",&x);
      a[x%p]++;
    }
    int res=a[0];
    if(p==2) {
      res+=(a[1]+1)/2;
    } else if(p==3) {
      int d=min(a[1],a[2]);
      res+=d;
      a[1]-=d;
      a[2]-=d;
      res+=(a[1]+2)/3 + (a[2]+2)/3;
    } else if(p==4) {
      int d=min(a[1],a[3]);
      res+=d;
      a[1]-=d;
      a[3]-=d;
      res+=a[2]/2;
      a[2]%=2;
      if(a[2]) {
        int cur=1;
        if(a[1]>=2) {
          int cur1 = 1 + (a[1]+1)/4 + (a[3]+3)/4;
          MAX(cur, cur1);
        }
        if(a[3]>=2) {
          int cur1 = 1 + (a[1]+3)/4 + (a[3]+1)/4;
          MAX(cur, cur1);
        }
        res+=cur;
      } else {
        res+=(a[1]+3)/4 + (a[3]+3)/4;
      }
    }
    printf("%d\n",res);
  }
  fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
  return 0;
}
