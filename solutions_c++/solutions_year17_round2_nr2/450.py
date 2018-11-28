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


#define MAX 1005

// G, V, O, R, Y, B
int G[6][6] =
{
    {0, 0, 0, 1, 0, 0},
    {0, 0, 0, 0, 1, 0},
    {0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 1, 1},
    {0, 1, 0, 1, 0, 1},
    {0, 0, 1, 1, 1, 0},
};
int cnt[6];
int ans[MAX];
int ord[6];
char output[] = "GVORYB";

bool cmp(int a, int b)
{
    return cnt[a] > cnt[b];
}

bool solve(int n)
{
    for (int i = 0; i < n; ++i)
    {
        bool good = false;
        for (int j = 0; j < 3; ++j)
        {
            int c = j;
            if (!cnt[c]) continue;
            if (i > 0 and not G[ans[i-1]][c]) continue;

            ans[i] = c;
            cnt[c]--;
            good = true;
            break;
        }

        if (good) continue;

        for (int j = 0; j < 3; ++j)
            ord[j] = j + 3;

        sort(ord, ord + 3, cmp);

        int macnt = -1;
        for (int j = 0; j < 3; ++j)
        {
            int c = ord[j];
            if (i > 0 and not G[ans[i-1]][c]) continue;
            macnt = max(cnt[c], macnt);
        }
        dump(i, macnt);
        if (macnt <= 0) return false;

        int choice = -1;
        for (int j = 0; j < 3; ++j)
        {
            int c = ord[j];

            if (cnt[c] != macnt) continue;
            if (i > 0 and not G[ans[i-1]][c]) continue;

            if (cnt[c] == macnt)
            {
                choice = c;
                break;
            }
        }
        for (int j = 0; j < 3; ++j)
        {
            int c = ord[j];

            if (cnt[c] != macnt) continue;
            if (i > 0 and not G[ans[i-1]][c]) continue;

            if (cnt[c] == macnt and i > 0 and c == ans[0])
            {
                choice = c;
                break;
            }
        }


        if (choice != -1)
        {
            ans[i] = choice;
            cnt[choice]--;
        }
        else
            return false;
    }
    return G[ans[0]][ans[n-1]];
}

int main()
{
    int z;
    scanf("%d", &z);

    for (int zi = 1; zi <= z; ++zi)
    {
        int n;
        {
            int r, o, y, g, b, v;
            scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);

            cnt[0] = g;
            cnt[1] = v;
            cnt[2] = o;
            cnt[3] = r;
            cnt[4] = y;
            cnt[5] = b;
        }
        bool good = solve(n);

        printf("Case #%d: ", zi);
        if (!good)
            printf("IMPOSSIBLE\n");
        else
        {
            for (int i = 0; i < n; ++i)
                printf("%c", output[ans[i]]);
            printf("\n");
        }



    }
}

