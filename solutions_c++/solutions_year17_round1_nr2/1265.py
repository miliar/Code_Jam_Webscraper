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

const int N = 2;

int main() {
    int T;
    R(T);

    for (int t=1; t<=T; t++) {
        int n, p, r[N], q[N][10], perm[10], ans = 0;
        R(n, p);
        dump(t);

        for (int i=0; i<n; i++)
            R(r[i]);
        for (int i=0; i<n; i++)
            for (int j=0; j<p; j++)
                R(q[i][j]);

        for (int i=0; i<p; i++)
            perm[i] = i;

        if (n == 1) {
            double a = r[0]*0.9, b = r[0]*1.1;
            for (int i=0; i<p; i++) {
                int kits = int(q[0][i] / b);
                int flag = 0;
                dump(kits);
                for (int j=kits; j*r[0]*0.9 <= q[0][i]; j++) {
                    dump(a, b, j, q[0][i], j*a, j*b);
                    if (j*r[0]*0.9 <= q[0][i] && q[0][i] <= j*r[0]*1.1) flag = 1;
                }
                ans += flag;
            }
        }

        else {
            double a = r[0]*0.9, b = r[0]*1.1, c = r[1]*0.9, d = r[1]*1.1;
            do {
                int tmp_ans = 0;
                for (int i=0; i<p; i++) {
                    int kits = int(q[0][i] / b);
                    int flag = 0;
                    for (int j=kits; j*r[0]*0.9 <= q[0][i]; j++) {
                        if (j*r[0]*0.9 <= q[0][i] && q[0][i] <= j*r[0]*1.1 &&
                            j*r[1]*0.9 <= q[1][perm[i]] &&
                            q[1][perm[i]] <= j*r[1]*1.1)
                                flag = 1;
                    }
                    tmp_ans += flag;
                }
                ans = max(ans, tmp_ans);
            } while (next_permutation(perm, perm+p));
        }

        printf("Case #%d: %d\n", t, ans);
    }

    return 0;
}
