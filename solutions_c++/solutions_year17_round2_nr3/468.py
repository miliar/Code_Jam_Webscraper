// @author cebrusfs
// headers {{{
#include<bits/stdc++.h>
using namespace std;
// }}}
// macros {{{
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define UNIQUE(x) (sort(ALL(x)), ((x).erase(unique(ALL(x)), (x).end())))
#define MSA(x, v) std::fill(ALL(x), (v))
#define MS(st, ed, v) std::fill((st), (ed), (v))

#define REP(i,n) for(int i=0;i<(n);i++)
#define REP1(i,a,b) for(int i=(a);i<=(b);i++)

#define PER(i,n) for(int i=(n)-1;i>=0;i--)
#define PER1(i,a,b) for(int i=(a);i>=(b);i--)

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

typedef pair<int, int> PII;
#define MP make_pair
#define F first
#define S second

typedef vector<int> VI;
#define PB push_back
#define PF push_front

#define PPB pop_back
#define PPF pop_front

#define runtime() ((double)clock() / CLOCKS_PER_SEC)

const double eps = 1e-7;

// C++11
#if __cplusplus >= 201103L
#define MT make_tuple
typedef tuple<int, int> TII;

// dump() {{{
template<typename T>
void _dump(const char* s, T&& head) {
    cerr<< s << "=" << head << endl;
}

template<typename T, typename... Args>
void _dump(const char* s, T&& head, Args&&... tail) {
    int c = 0;
    while (*s!=',' || c!=0) {
        if (*s=='(' || *s=='[' || *s=='{') c++;
        if (*s==')' || *s==']' || *s=='}') c--;
        cerr << *s++;
    }
    cerr << "=" << head << ", ";
    _dump(s+1, tail...);
}

#ifdef FISH
#define dump(...) do { \
    fprintf(stderr, "%s:%d - ", __PRETTY_FUNCTION__, __LINE__); \
    _dump(#__VA_ARGS__, __VA_ARGS__); \
} while (0);
#else
#define dump(...) ;
#endif

template<typename Iter>
ostream& _out(ostream &s, Iter b, Iter e) {
    s << "[";
    for (auto it = b; it != e; it++) s << (it == b ? "":" ") << *it;
    s << "]";
    return s;
}

template<typename A, typename B>
ostream& operator <<(ostream &s, const pair<A,B> &p) { return s<<"("<<p.first<<","<<p.second<<")"; }
template<typename T>
ostream& operator <<(ostream &s, const vector<T> &c) { return _out(s,ALL(c)); }
template<typename T>
ostream& operator <<(ostream &s, const set<T> &c) { return _out(s,ALL(c)); }
template<typename T>
ostream& operator <<(ostream &s, const unordered_set<T> &c) { return _out(s,ALL(c)); }
template<typename A, typename B>
ostream& operator <<(ostream &s, const map<A,B> &c) { return _out(s,ALL(c)); }
template<typename A, typename B>
ostream& operator <<(ostream &s, const unordered_map<A,B> &c) { return _out(s,ALL(c)); }
// }}}

#endif
// }}}

#define MAX 105
#define INF (1e18)

int es[MAX];
int ss[MAX];


long long dis[MAX][MAX];
double dis2[MAX][MAX];

int main()
{
    int z;
    scanf("%d", &z);

    for (int zi = 1; zi <= z; ++zi)
    {
        int n, q;
        scanf("%d %d", &n, &q);

        for (int i = 0; i < n; ++i)
            scanf("%d %d", &es[i], &ss[i]);

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
            {
                int d;
                scanf("%d", &d);
                if (d == -1)
                    dis[i][j] = INF;
                else
                    dis[i][j] = d;
            }

        for (int k = 0; k < n; ++k)
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                    dis[i][j] = min(dis[i][k] + dis[k][j], dis[i][j]);

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
            {
                long long d = dis[i][j];
                if (d > es[i])
                {
                    dis2[i][j] = INF;
                }
                else
                {
                    dis2[i][j] = 1.0 * d / ss[i];
                }
            }

        for (int k = 0; k < n; ++k)
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                    dis2[i][j] = min(dis2[i][k] + dis2[k][j], dis2[i][j]);
        /*
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                dump(i, j, dis[i][j], dis2[i][j]);
                */

        printf("Case #%d: ", zi);
        for (int i = 0; i < q; ++i)
        {
            if(i > 0) printf(" ");

            int u, v;
            scanf("%d %d", &u, &v);
            --u, --v;

            printf("%.9lf", dis2[u][v]);
        }
        printf("\n");
    }
}

