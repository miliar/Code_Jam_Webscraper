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

int len,cn,sn;
int cnt[MAXN];
//pii s[MAXN];
int s[MAXN];

inline bool sub(int k) {
    int i = 0;
    int t = len;
    for (int si=0; si<sn; si++) {
        int x = s[si];
        while (x<t || i==k) {
            t--;
            i = 0;
        }
        //printf("[%d %d %d]\n",x,t,i);
        if (t < 1) return false;
        i++;
    }
    return true;
}

inline int gao(int k) {
    int i = 0;
    int t = len;
    int pro = 0;
    for (int si=0; si<sn; si++) {
        int x = s[si];
        while (x<t || i==k) {
            t--;
            i = 0;
        }
        //printf("[%d %d %d]\n",x,t,i);
        if (t < x) pro++;
        else i++;
    }
    return pro;
}

void solve() {
    int mi=0;
    //sort(s,s+sn,std::greater<pii>());
    sort(s,s+sn,std::greater<int>());
    for (int i=0; i<=cn; i++)
        mi = max(mi, cnt[i]);
    int l = mi-1;
    int r = sn;
    int m;
    while (l+1 < r) {
        //printf("<%d %d>\n",l,r);
        int m = (l+r)/2;
        if (sub(m)) r=m;
        else l=m;
    }
    int pro = gao(r);
    printf("%d %d\n",r,pro);
}

int main(void)
{
    int t;
    RI(t);
    for(int cas=1; cas<=t; cas++) {
        RI(len,cn,sn);
        memset(cnt,0,sizeof(cnt));
        for (int i=0; i<sn; i++) {
            //RI(s[i].F,s[i].S);
            //cnt[s[i].F]++;
            int x, c;
            RI(x,c);
            cnt[c]++;
            s[i] = x;
        }
        printf("Case #%d: ",cas);
        solve();
    }
    return 0;
}

// vim: fdm=marker:commentstring=//\ %s:nowrap:autoread
