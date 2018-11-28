// pre-written code {{{
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
#include <set>
#include <sys/resource.h>
#define FOR(i,n) for(int _n=n,i=0;i<_n;++i)
#define FR(i,a,b) for(int _b=b,i=a;i<_b;++i)
#define CL(x) memset(x,0,sizeof(x))
#define PN printf("\n");
#define MP make_pair
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define FORSZ(i,v) FOR(i,v.size())
#define FORIT(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
void stackSizeUnlimited() { struct rlimit rl; getrlimit(RLIMIT_STACK, &rl); rl.rlim_cur = RLIM_INFINITY; setrlimit(RLIMIT_STACK, &rl); }
///////////////////////////////////////////////////////////////////////////////////
// }}}

int n,p;

int r[5][101][101][101];

int ries(int a, int b, int c, int p ) {
  // int z[4]; CL(z); 
  //z[1]=a; z[2]=b; z[3]=c;
  int &ret = r[p][a][b][c];
  //printf("v: %d %d %d: %d\n",a,b,c,ret-1);
  if(ret>0) return ret-1;
  ret = 0;
  if(a+b+c>=0) ret=1;
  if(a==b && b==c && c==0) {
    return 0;
  }
  FOR(i,min(a+1,4+1)) 
    FOR(j,min(b+1,3+1))
      FOR(k, min(c+1, 4+1)) if(i+j+k>0) if( (i*1+j*2+k*3)%p==0) {    
        ret = max(ret, 1 + ries(a-i,b-j,c-k, p));
      }
  ret++;
  //printf("%d %d %d: %d\n",a,b,c,ret-1);
  return ret-1;
}

void solve(){
  scanf("%d %d\n",&n,&p);
  int z[4]; CL(z);
  FOR(i,n) { 
    int x; scanf("%d",&x);
    z[x%p]++;
  }  
  //FOR(i,p) printf(" %d",z[i]); PN;  
  printf("%d\n",ries(z[1],z[2],z[3],p)+z[0]);
}

int main(){
  CL(r);
  stackSizeUnlimited();
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
