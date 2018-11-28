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

int N, R, O, Y, G, B, V;

string repe(string x, int n){
  string ret = "";
  FOR(i,n) ret+=x;
  return ret;
}

void solve(){
  scanf("%d %d %d %d %d %d %d\n",&N, &R, &O, &Y, &G, &B, &V);
  string ret = ""; 

  if( R>0 && G>0 && B==0 && O==0 && Y==0 && V==0) {
    if(R==G) {
      printf("%s\n",repe("RG",R).c_str());
      return;
    } else {
      printf("IMPOSSIBLE\n"); 
      return;
    }
  }
  if( R==0 && G==0 && B>0 && O>0 && Y==0 && V==0) {
    if(R==G) {
      printf("%s\n",repe("BO",B).c_str());
      return;
    } else {
      printf("IMPOSSIBLE\n"); 
      return;
    }
  }
  if( R==0 && G==0 && B==0 && O==0 && Y>0 && V>0) {
    if(R==G) {
      printf("%s\n",repe("YV",V).c_str());
      return;
    } else {
      printf("IMPOSSIBLE\n"); 
      return;      
    }
  }

  if( (R>=G-1) && (B>=O-1) && (Y>=V-1) ) {
    string ret = "";
    string subR = "";
    map<char,string> sub;
    sub['R'] = "";
    sub['B'] = "";
    sub['Y'] = "";
    if(G>0) { sub['R']=repe("GR",G); R-=G; }
    if(O>0) { sub['B']=repe("OB",O); B-=O; }
    if(V>0) { sub['Y']=repe("VY",V); Y-=V; }
    //FORIT(it, sub) printf("%c %s\n",it->first, (it->second).c_str());
    map<char, int> p;
    p['R'] = R;
    p['B'] = B;
    p['Y'] = Y;
    while(p['R']+p['B']+p['Y']>0) {      
      //printf("%s\n",ret.c_str());
      //printf("%d %d %d",p['R'], p['B'], p['Y']);
      VI poc = VI(3);      
      poc[0] = p['R']; poc[1] = p['B']; poc[2] = p['Y']; sort(ALL(poc)); reverse(ALL(poc));

      // najst najpocetnejsieho, ak je to mozne tak ret[0]
      char naj = ' ';
      FORIT(it,p) {
        if( (it->second>0) && (it->second == poc[0]) && ( (ret.SZ==0) || (it->first != ret[ret.SZ-1] ) ) ) {
          naj = it->first;
        }
      }
      if(ret.SZ>0) {
        char v = ret[0];
        if( (p[v]>0) && (p[v] == poc[0]) && ( (ret.SZ==0) || (v != ret[ret.SZ-1] ) ) ) {
          naj = v;
        }
      }
      if(naj!=' ') {
        ret+=naj;
        ret+=sub[naj]; sub[naj]="";        
        p[naj]--;
        continue;
      }

      FORIT(it,p) {
        if( (it->second>0) && (it->second == poc[1]) && ( (ret.SZ==0) || (it->first != ret[ret.SZ-1] ) ) ) {
          naj = it->first;
        }
      }
      if(ret.SZ>0) {
        char v = ret[0];
        if( (p[v]>0) && (p[v] == poc[1]) && ( (ret.SZ==0) || (v != ret[ret.SZ-1] ) ) ) {
          naj = v;
        }
      }
      if(naj!=' ') {
        ret+=naj;
        ret+=sub[naj]; sub[naj]="";        
        p[naj]--;
        continue;
      }
      printf("IMPOSSIBLE\n"); return;
    }
    if(ret[0] == ret[ret.SZ-1]) {
      printf("IMPOSSIBLE\n"); return;
    } else { 
      printf("%s\n",ret.c_str());
      return;
    }
  }
  if(ret[0] == ret[ret.SZ-1]) {
    printf("IMPOSSIBLE\n"); return;
  } else { 
    printf("%s\n",ret.c_str());
    return;
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
