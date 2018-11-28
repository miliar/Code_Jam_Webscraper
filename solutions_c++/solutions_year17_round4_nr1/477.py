// @author kelvin
// #includes {{{
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <algorithm>
#include <sstream>
using namespace std;
// }}}
// #defines {{{
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define POP() pop_back()
#define F first
#define S second
#define PR printf
void RI() {}
template<typename... T>
void RI(int& head,T&... tail) {
    scanf("%d",&head);
    RI(tail...);
}
void PRI(int x) {
    printf("%d\n",x);
}
template<typename... Args>
void PRI(int head,Args... tail) {
    printf("%d ",head);
    PRI(tail...);
}
#define RF(x) scanf("%lf",&(x))
#define RS(x) scanf("%s",x)
#define DPRI(x) fprintf(stderr,"<"#x"=%d>\n",x)
#define DPRII(x,y) fprintf(stderr,"<"#x"=%d, "#y"=%d>\n",x,y)
#define DPRIII(x,y,z) fprintf(stderr,"<"#x"=%d, "#y"=%d, "#z"=%d>\n",x,y,z)
#define DPRIIII(x,y,z,w) fprintf(stderr,"<"#x"=%d, "#y"=%d, "#z"=%d "#w"=%d>\n",x,y,z,w)
#define DPRF(x) fprintf(stderr,"<"#x"=%lf>\n",x)
#define DPRS(x) fprintf(stderr,"<"#x"=%s>\n",x)
#define DPRMSG(x) fprintf(stderr,#x"\n")
#define DPRPII(x) fprintf(stderr,"<"#x"=(%d,%d)>\n",x.F,x.S)
typedef pair<int,int> pii;
// }}}
// #functions {{{
pii operator+(const pii &a,const pii &b) { return MP(a.F+b.F,a.S+b.S); }
pii operator-(const pii &a,const pii &b) { return MP(a.F-b.F,a.S-b.S); }
pii& operator+=(pii &a,const pii &b) { a.F+=b.F; a.S+=b.S; return a; }
pii& operator-=(pii &a,const pii &b) { a.F-=b.F; a.S-=b.S; return a; }
template <class T,class U>
bool cmp_second(const pair<T,U> &a,const pair<T,U> &b) { return a.second<b.second; }
template <class T>
T gcd(T a,T b) { a=abs(a); b=abs(b); while(b) { T t=b; b=a%b; a=t; } return a; }
template <class T>
pair<T,T> ext_gcd(T a,T b) {
   T a0=1,a1=0,b0=0,b1=1;
   if(a<0) { a=-a; a0=-1; }
   if(b<0) { b=-b; b1=-1; }
   while(b) {
      T t,q=a/b;
      t=b; b=a-b*q; a=t;
      t=b0; b0=a0-b0*q; a0=t;
      t=b1; b1=a1-b1*q; a1=t;
   }
   return MP(a0,a1);
}
inline int sg(int x) { return x?(x>0?1:-1):0; }
inline string concatenate_strings(vector<string> ss) {
   string s;
   for(int i=0;i<ss.size();i++)
      s+=ss[i];
   return s;
}
template <class T>
inline vector<T> read_from_string(string s) {
   vector<T> ret; stringstream ss(s,stringstream::in);
   while(1) { T x; ss>>x; ret.push_back(x); if(ss.eof()) break; }
   return ret;
}
// }}}

#define MAXN 105

int n,mod;
int s[4];

int solve2() {
    int sol = s[1]/2;
    return sol;
}

int solve3() {
    int sol = 0;
    int w1 = min(s[1],s[2]);
    sol += w1;
    s[1] -= w1;
    s[2] -= w1;
    sol += s[1]/3 + (s[1]+1)/3;
    sol += s[2]/3 + (s[2]+1)/3;
    return sol;
}

int solve4() {
    int sol = 0;
    int w13 = min(s[1],s[3]);
    sol += w13;
    s[1] -= w13;
    s[3] -= w13;
    int w22 = s[2]/2;
    sol += w22;
    s[2] -= 2*w22;
    int w112 = min(s[1]/2, s[2]);
    sol += w112*2;
    s[1] -= w112*2;
    s[2] -= w112;
    int w233 = min(s[3]/2, s[2]);
    sol += w233*2;
    s[3] -= w233*2;
    s[2] -= w233;
    int w1 = s[1]/4;
    sol += w1*3;
    s[1] -= w1*4;
    int w3 = s[3]/4;
    sol += w3*3;
    s[3] -= w3*4;
    //
    sol += max(s[1]+s[2]+s[3]-1, 0);
    return sol;
}

int solve() {
    switch(mod) {
        case 2:
            return solve2();
        case 3:
            return solve3();
        case 4:
            return solve4();
    }
    return 0;
}

int main(void)
{
    int t;
    RI(t);
    for(int cas=1; cas<=t; cas++) {
        RI(n,mod);
        memset(s,0,sizeof(s));
        for (int i=0; i<n; i++) {
            int x;
            RI(x);
            s[x%mod]++;
        }
        int sol = n-solve();
        printf("Case #%d: %d\n",cas,sol);
    }
    return 0;
}

// vim: fdm=marker:commentstring=//\ %s:nowrap:autoread
