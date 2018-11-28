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

#define MAXL 105
#define MAXA (MAXL*MAXL)
#define MAXVN (MAXL*4+2) // define as needed: # of nodes in graph
const int dist_inf = MAXVN;
const int flow_inf = MAXA+1;

class Arc {
   public:
      int to,revind;
      int flow,cap;
      Arc(int _to,int _revind,int _cap):to(_to),revind(_revind),cap(_cap),flow(0) {}
};

class DinicFlow {
    public:
        /* initialize the following using constructor and append */
        int vn,src,sink;
        vector<Arc> adj[MAXVN];
        /* helper variables */
        int dist[MAXVN];
        int ql,qr,que[MAXVN];
        int iter[MAXVN];
        /* primary functions */
        DinicFlow(int _vn,int _src,int _sink):vn(_vn),src(_src),sink(_sink) {}
        void append(int v,int u,int c) {
            int vid=adj[v].size(),uid=adj[u].size();
            adj[v].push_back(Arc(u,uid,c));
            adj[u].push_back(Arc(v,vid,0));
        }
        void bfs_layer() {
            ql=qr=0;
            for(int i=0;i<vn;i++)
                dist[i]=dist_inf;
            que[qr++]=src;
            dist[src]=0;
            while(ql<qr) {
                int v=que[ql++];
                for(int i=0;i<adj[v].size();i++) {
                    int u=adj[v][i].to;
                    int res=adj[v][i].cap-adj[v][i].flow;
                    if(dist[u]<dist_inf) continue;
                    if(!res) continue;
                    que[qr++]=u;
                    dist[u]=dist[v]+1;
                }
            }
        }
        int dfs_push(int v,int a) {
            if(v==sink) return a;
            int pushed=0;
            for(int &i=iter[v];i<adj[v].size();i++) {
                int u=adj[v][i].to;
                int res=adj[v][i].cap-adj[v][i].flow;
                if(dist[u]!=dist[v]+1) continue;
                if(!res) continue;
                int ri=adj[v][i].revind;
                int pf=dfs_push(u,min(a-pushed,res));
                adj[v][i].flow+=pf;
                adj[u][ri].flow-=pf;
                pushed+=pf;
                if(pushed==a) break;
            }
            return pushed;
        }
        int push_flow() {
            bfs_layer();
            for(int i=0;i<vn;i++)
                iter[i]=0;
            return dfs_push(src,flow_inf);
        }
        int maxflow() {
            // O(mn^2) in general graph
            // good complexity in bipartite / unit-capcity graph
            int f=0;
            while(1) {
                int pf=push_flow();
                if(!pf) break;
                f+=pf;
            }
            return f;
        }
        vector<pii> get_midlinks() {
            vector<pii> lk;
            for(int v=0; v<vn; v++) {
                if (v==src) continue;
                for(auto arc: adj[v]) {
                    int u = arc.to;
                    int f = arc.flow;
                    if (u==sink) continue;
                    if (f>0) lk.PB(MP(v,u));
                }
            }
            return lk;
        }
};

class Placement {
    public:
        char ch;
        int r,c;
        Placement(int ch,int r,int c):ch(ch),r(r),c(c) {}
        void print() { printf("%c %d %d\n",ch,r+1,c+1); }
};

int n,npre;
bool g1[MAXL][MAXL];
bool g2[MAXL][MAXL];
bool zr[MAXL],zc[MAXL],zda[MAXL*2],zdm[MAXL*2];

int nd,score;
int vn1,src1,sink1;
int vn2,src2,sink2;
bool gg1[MAXL][MAXL],gg2[MAXL][MAXL];

inline int DM(int r,int c) { return r-c+n-1; }
inline int DA(int r,int c) { return r+c; }

inline int LV1(int i) {
    return i+1;
}
inline int RV1(int i) {
    return i+n+1;
}
inline int LV2(int i) {
    return i+1;
}
inline int RV2(int i) {
    return i+nd+1;
}

inline int ILV1(int v) {
    return v-1;
}
inline int IRV1(int v) {
    return v-n-1;
}
inline int ILV2(int v) {
    return v-1;
}
inline int IRV2(int v) {
    return v-nd-1;
}

void input() {
    RI(n,npre);
    nd = n*2-1;
    score = 0;
    for (int i=0; i<n; i++)
        for (int j=0; j<n; j++)
            g1[i][j] = g2[i][j] = 0;
    for (int i=0; i<n; i++)
        zr[i] = zc[i] = 0;
    for (int i=0; i<nd; i++)
        zda[i] = zdm[i] = 0;
    for(int i=0; i<npre; i++) {
        char ss[10],ch;
        int r,c;
        RS(ss); ch=ss[0];
        RI(r,c); r--; c--;
        if (ch == 'x' || ch == 'o') {
            g1[r][c] = 1;
            zr[r] = 1;
            zc[c] = 1;
            score++;
        }
        if (ch == '+' || ch == 'o') {
            g2[r][c] = 1;
            zda[DA(r,c)] = 1;
            zdm[DM(r,c)] = 1;
            score++;
        }
    }
}

void solve() {
    // 1
    vn1 = 2*n+2;
    src1 = 0;
    sink1 = vn1-1;
    DinicFlow df1(vn1,src1,sink1);
    for (int i=0; i<n; i++)
        if(!zr[i]) df1.append(src1, LV1(i), 1);
    for (int i=0; i<n; i++)
        if(!zc[i]) df1.append(RV1(i), sink1, 1);
    for (int r=0; r<n; r++)
        for (int c=0; c<n; c++)
            df1.append(LV1(r), RV1(c), 1);
    // 2
    vn2 = 2*nd+2;
    src2 = 0;
    sink2 = vn2-1;
    DinicFlow df2(vn2,src2,sink2);
    for (int i=0; i<nd; i++)
        if(!zda[i]) df2.append(src2, LV2(i), 1);
    for (int i=0; i<nd; i++)
        if(!zdm[i]) df2.append(RV2(i), sink2, 1);
    for (int r=0; r<n; r++)
        for (int c=0; c<n; c++)
            df2.append(LV2(DA(r,c)), RV2(DM(r,c)), 1);
    // solve
    int f1 = df1.maxflow();
    int f2 = df2.maxflow();
    score += f1+f2;
    vector<pii> lk1 = df1.get_midlinks();
    vector<pii> lk2 = df2.get_midlinks();
    for (int r=0; r<n; r++) {
        for (int c=0; c<n; c++) {
            gg1[r][c] = g1[r][c];
            gg2[r][c] = g2[r][c];
        }
    }
    for (auto lk: lk1) {
        int v = lk.F, u = lk.S;
        int r = ILV1(v);
        int c = IRV1(u);
        gg1[r][c] = 1;
    }
    for (auto lk: lk2) {
        int v = lk.F, u = lk.S;
        int da = ILV2(v);
        int dm = IRV2(u);
        int r = (da+dm-n+1)/2;
        int c = da-r;
        gg2[r][c] = 1;
    }
    vector<Placement> pl;
    for (int r=0; r<n; r++) {
        for(int c=0; c<n; c++) {
            if (gg1[r][c]==g1[r][c] && gg2[r][c]==g2[r][c]) continue;
            if (gg1[r][c] && gg2[r][c]) {
                pl.PB(Placement('o',r,c));
            } else if (gg1[r][c]) {
                pl.PB(Placement('x',r,c));
            } else if (gg2[r][c]) {
                pl.PB(Placement('+',r,c));
            }
        }
    }
    // output
    printf("%d %d\n",score, (int)pl.size());
    for (auto p: pl) {
        p.print();
    }
}

int main(void)
{
    int t;
    RI(t);
    for(int cas=1; cas<=t; cas++) {
        input();
        printf("Case #%d: ",cas);
        solve();
    }
    return 0;
}

// vim: fdm=marker:commentstring=//\ %s:nowrap:autoread
