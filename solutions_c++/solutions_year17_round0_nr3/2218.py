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


void solve(){
  LL n,k;  
  scanf("%lld %lld\n",&n,&k);
  map<LL,LL> poc;
  priority_queue<LL> Q;
  poc[n]=1;
  Q.push(n); 
  while(k>0) {
   LL d = Q.top();   
   Q.pop();
   LL da = (d-1)/2;
   LL db = (d-1)-da;
   if(poc[d]==0) continue;
   if(poc[d]<k) {
      if(poc[da]==0) Q.push(da);
      if(poc[db]==0 && da!=db) Q.push(db);
      poc[da]+=poc[d];
      poc[db]+=poc[d];      
      k-=poc[d];
      poc[d]=0;      
   } else {
      printf("%lld %lld\n",db,da);
      return;
   }
  }
}

int main(){
  stackSizeUnlimited();
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
