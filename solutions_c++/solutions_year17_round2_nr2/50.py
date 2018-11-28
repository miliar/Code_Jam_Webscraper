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

#define MAXN 1050

int n;
int s[3],s2[3];
const char* str[] = {
    "R",
    "Y",
    "B"
};
const char* str2[] = {
    "GR",
    "VY",
    "OB"
};

inline int max(int a,int b, int c) { return max(a,max(b,c)); }

bool solve() {
    for (int i=0; i<3; i++) {
        if (!s2[i]) continue;
        if (s[i]<s2[i]) return false;
        if (s[i]==s2[i]) {
            if(s[i]+s2[i] != n) return false;
            for (int t=0; t<s[i]; t++)
                printf("%s", str2[i]);
            puts("");
            return true;
        }
    }
    for (int i=0; i<3; i++)
        s[i] -= s2[i];
    int ss = s[0]+s[1]+s[2];
    for (int i=0; i<3; i++) {
        if (s[i] > ss-s[i]) return false;
    }
    //
    int xx, prev = -1;
    int sm = max(s[0],s[1],s[2]);
    for (xx=0; s[xx]!=sm; xx++);
    while(ss) {
        //printf("%d %d %d %d %d %d\n",s[0],s[1],s[2],s2[0],s2[1],s2[2]);
        int x;
        sm = -1;
        for (int i=0; i<3; i++) {
            int t = (xx+i)%3;
            if (t==prev) continue;
            if (s[t] > sm) {
                x = t;
                sm = s[t];
            }
        }
        printf("%s", str[x]);
        for (;s2[x]>0; s2[x]--)
            printf("%s", str2[x]);
        s[x]--;
        ss--;
        prev = x;
    }
    puts("");
    return true;
}

int main(void)
{
    int t;
    RI(t);
    for(int cas=1; cas<=t; cas++) {
        RI(n);
        /* R O Y G B V */
        RI(s[0],s2[2],s[1],s2[0],s[2],s2[1]);
        printf("Case #%d: ",cas);
        if (!solve()) puts("IMPOSSIBLE");
    }
    return 0;
}

// vim: fdm=marker:commentstring=//\ %s:nowrap:autoread
