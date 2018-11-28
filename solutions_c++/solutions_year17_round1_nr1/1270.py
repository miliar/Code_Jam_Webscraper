// {{{
#include <bits/stdc++.h>
#define MP make_pair
#define PB push_back
#define ALL(x) begin(x),end(x)
#define SZ(x) ((int)x.size())
#define FOR(i,n) for(int i=0;i<n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
using LL=long long;
using PII=pair<int,int>;
using VI=vector<int>;

#ifdef FEI
template<typename T>
void _dump(const char* s, T&& head) { cerr<<s<<"="<<head<<endl; }
template<typename T, typename... Args>
void _dump(const char* s, T&& head, Args&&... tail) {
    int c=0;
    while (*s!=',' || c!=0) {
        if (*s=='(' || *s=='[' || *s=='{') c++;
        if (*s==')' || *s==']' || *s=='}') c--;
        cerr<<*s++;
    }
    cerr<<"="<<head<<", ";
    _dump(s+1, tail...);
}

#define dump(...) do { \
    fprintf(stderr, "%s:%d - ", __PRETTY_FUNCTION__, __LINE__); \
    _dump(#__VA_ARGS__, ##__VA_ARGS__); \
} while(0);

template<typename Iter>
ostream& _out(ostream &s, Iter b, Iter e) {
    s<<'[';
    for (auto it=b; it!=e; it++) s<<(it==b?"":",")<<*it;
    s<<']';
    return s;
}

template<typename A, typename B>
ostream& operator <<(ostream &s, const pair<A,B> &p) { return s<<"("<<p.first<<","<<p.second<<")";}
template<typename T>
ostream& operator <<(ostream &s, const vector<T> &x) { return _out(s,ALL(x)); }
template<typename T, size_t N>
ostream& operator <<(ostream &s, const array<T,N> &x) { return _out(s,ALL(x)); }
template<typename T>
ostream& operator <<(ostream &s, const set<T> &x) { return _out(s,ALL(x)); }
template<typename A, typename B>
ostream& operator <<(ostream &s, const map<A,B> &x) { return _out(s,ALL(x)); }
#else
#define dump(...)
#endif

template<typename T>
void _R(T &x) { cin>>x; }
void _R(int &x) { scanf("%d",&x); }
void _R(LL &x) { scanf("%" PRId64,&x); }
void _R(double &x) { scanf("%lf",&x); }
void _R(char &x) { scanf(" %c",&x); }
void _R(char *x) { scanf("%s",x); }

void R(){}
template<typename T, typename... X>
void R(T& head, X&... tail) { _R(head); R(tail...); }
// }}}

const int N = 30;
char str[N][N], ans[N][N];
int cnt[N][N];
int vis[N][N];
int n, m;

int check(int a, int b, int c, int d) {
    return cnt[c][d] - cnt[a-1][d] - cnt[c][b-1] + cnt[a-1][b-1];
}

void calc() {
    for (int i=1; i<=n; i++)
        for (int j=1; j<=m; j++)
            cnt[i][j] = cnt[i-1][j] + cnt[i][j-1] - cnt[i-1][j-1] + (ans[i][j] != '?');
}

int main() {
    int T;
    R(T);
    for (int t=1; t<=T; t++) {
        R(n, m);
        memset(vis, 0, sizeof(vis));
        memset(cnt, 0, sizeof(cnt));

        for (int i=1; i<=n; i++)
            scanf(" %s", str[i]+1);

        memcpy(ans, str, sizeof(str));

        calc();

        for (int i=1; i<=n; i++) {
            for (int j=1; j<=m; j++) {
                if (!vis[i][j] && ans[i][j] != '?') {
                    int ax, ay, bx, by;
                    for (ax=i; ax-1 > 0 && check(ax-1, j, i, j) == 1; ax--);
                    for (bx=i; bx+1 <= n && check(ax, j, bx+1, j) == 1; bx++);
                    for (ay=j; ay-1 > 0 && check(ax, ay-1, bx, j) == 1; ay--);
                    for (by=j; by+1 <= m && check(ax, ay, bx, by+1) == 1; by++);


                    for (int x=ax; x<=bx; x++)
                        for (int y=ay; y<=by; y++) {
                            ans[x][y] = ans[i][j];
                            vis[x][y] = 1;
                        }

                    calc();
                }
            }
        }

        int flag = 0;
        for (int i=1; i<=n; i++)
            for (int j=1; j<=m; j++)
                if (ans[i][j] == '?') flag = 1;


        if (flag) {
            memset(vis, 0, sizeof(vis));
            memcpy(ans, str, sizeof(str));

            calc();

            for (int i=1; i<=n; i++) {
                for (int j=1; j<=m; j++) {
                    if (!vis[i][j] && ans[i][j] != '?') {
                        int ax, ay, bx, by;
                        for (ay=j; ay-1 > 0 && check(i, ay-1, i, j) == 1; ay--);
                        for (by=j; by+1 <= m && check(i, ay, i, by+1) == 1; by++);
                        for (ax=i; ax-1 > 0 && check(ax-1, ay, i, by) == 1; ax--);
                        for (bx=i; bx+1 <= n && check(ax, ay, bx+1, by) == 1; bx++);


                        for (int x=ax; x<=bx; x++)
                            for (int y=ay; y<=by; y++) {
                                ans[x][y] = ans[i][j];
                                vis[x][y] = 1;
                            }

                        calc();
                    }
                }
            }
        }

        printf("Case #%d:\n",t);

        for (int i=1; i<=n; i++)
            puts(ans[i]+1);


    }

    return 0;
}
