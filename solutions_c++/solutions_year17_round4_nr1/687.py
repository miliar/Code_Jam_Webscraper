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


int cnt[10];


vector<vector<vector<int>>> rules = {
    // 0, 1, 2, 3
    {
        {1, 0},
        {0, 2}
    },
    {
        {1, 0, 0},
        {0, 1, 1}, // 1 + 2

        {0, 3, 0}, // 1 * 3
        {0, 0, 3}, // 2 * 3
    },
    {
        {1, 0, 0, 0},
        {0, 1, 0, 1}, // 1 + 3
        {0, 0, 2, 0}, // 2 + 2

        {0, 0, 1, 2}, // 2 + 3 + 3
        {0, 2, 1, 0}, // 1 + 1 + 2

        {0, 0, 0, 4},
        {0, 4, 0, 0},
    }
};

int main()
{
    int T;
    scanf("%d", &T);

    for (int zi = 1; zi <= T; ++zi)
    {
        int n, p;

        scanf("%d %d", &n, &p);

        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < n; ++i)
        {
            int g;
            scanf("%d", &g);
            cnt[g % p] += 1;
        }

        int ans = 0;

        const auto& r = rules[p - 2];

        for (const auto& rr : r)
        {
            while (true)
            {
                bool enough = true;

                for (int i = 0; i < p; ++i)
                    if (cnt[i] < rr[i])
                        enough = false;

                if (not enough) break;

                for (int i = 0; i < p; ++i)
                    cnt[i] -= rr[i];

                ans += 1;
            }
        }
        if (p == 4)
            dump(zi, p, cnt[0], cnt[1], cnt[2], cnt[3]);

        ans += cnt[0] + cnt[1] + cnt[2] + cnt[3] > 0;

        printf("Case #%d: %d\n", zi, ans);
    }
}

