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

#define MAX 55

char mp[MAX][MAX];

int R, C;

vector<int> candi[MAX][MAX];
vector<PII> beams;

vector<int> e[2 * MAX*MAX];

int vis[2 * MAX*MAX];
int sat[2 * MAX*MAX];

// u, r, d, l
int dirs[4][2] = {
    {-1, 0}, {0, 1}, {1, 0}, {0, -1}
};

bool dfs(int now)
{
    if (vis[now] == 1 or sat[now] == 1) return true;
    if (vis[now] == 2 or sat[now] == 2) return false;

    vis[now] = 1;
    vis[now^1] = 2;

    for (int b : e[now])
    {
        if (!dfs(b))
            return false;
    }
    return true;
}
void mark(int now)
{
    if (sat[now] == 1) return;
    sat[now] = 1;
    sat[now^1] = 2;

    for (int b : e[now])
        mark(b);
}

void follow(PII p, int d, int id)
{
    PII now = p;

    while (true)
    {
        now.F += dirs[d][0];
        now.S += dirs[d][1];

        //dump(now.F, now.S, d, id);

        if (not (0 <= now.F and now.F < R and
                 0 <= now.S and now.S < C))
            break;

        if (mp[now.F][now.S] == '#')
            break;

        candi[now.F][now.S].PB(id);

        // cycle
        if (now == p)
            break;
        if (mp[now.F][now.S] == '|')
            break;

        if (mp[now.F][now.S] == '/')
        {
            d ^= 1;
        }
        else if (mp[now.F][now.S] == '\\')
        {
            d = (d + 2) % 4;
        }
        else
        {
            //dump(now.F, now.S, mp[now.F][now.S]);
            assert(mp[now.F][now.S] == '.');
        }
    }
}

int main()
{
    int T;
    scanf("%d", &T);

    for (int zi = 1; zi <= T; ++zi)
    {

        scanf("%d %d", &R, &C);
        beams.clear();
        for (int i = 0; i < R; ++i)
            for (int j = 0; j < C; ++j)
            {
                scanf(" %c", &mp[i][j]);
                candi[i][j].clear();

                if (mp[i][j] == '|' or mp[i][j] == '-')
                {
                    beams.emplace_back(i, j);
                    mp[i][j] = '|';
                }
            }


        for (int i = 0; i < SZ(beams); ++i)
        {
            e[2 * i].clear();
            e[2 * i+1].clear();

            follow(beams[i], 0, i * 2);
            follow(beams[i], 2, i * 2);
            follow(beams[i], 1, i * 2 + 1);
            follow(beams[i], 3, i * 2 + 1);
        }

        for (int i = 0; i < SZ(beams); ++i)
        {
            const auto& b = beams[i];

            for (int id : candi[b.F][b.S])
            {
                //dump(candi[b.F][b.S]);

                // must not id
                // a => not a
                e[id].PB(id^1);
            }
        }

        bool ans = true;
        for (int i = 0; i < R; ++i)
            for (int j = 0; j < C; ++j)
            {
                if (mp[i][j] != '.') continue;

                //dump(i, j, candi[i][j]);
                assert(candi[i][j].size() <= 2);

                if (candi[i][j].size() == 0)
                    ans = false;

                if (candi[i][j].size() == 1)
                {
                    int a = candi[i][j][0];

                    // must a
                    // not a => a
                    e[a^1].PB(a);
                }

                if (candi[i][j].size() == 2)
                {
                    int a = candi[i][j][0];
                    int b = candi[i][j][1];

                    // a or b
                    // ^a => b
                    // ^b => a
                    e[a^1].PB(b);
                    e[b^1].PB(a);
                }
            }

        memset(sat, 0, sizeof(sat));

        for (int i = 0; i < SZ(beams); ++i)
        {
            memset(vis, 0, sizeof(vis));
            if (dfs(2 * i))
            {
                mark(2 * i);
                continue;
            }
            memset(vis, 0, sizeof(vis));
            if (dfs(2 * i + 1))
            {
                mark(2 * i + 1);
                continue;
            }
            ans = false;
        }

        if (ans)
        {
            for (int i = 0; i < SZ(beams); ++i)
            {
                int a = i * 2;
                int b = i * 2 + 1;

                assert( (sat[a] == 1 and sat[b] == 2) or (sat[a] == 2 and sat[b] == 1) );

                mp[ beams[i].F ][ beams[i].S ] = sat[a] == 1 ? '|' : '-';
            }

            // double check
            for (int i = 0; i < R; ++i)
                for (int j = 0; j < C; ++j)
                {
                    if (mp[i][j] != '.') continue;

                    if (candi[i][j].size() == 1)
                    {
                        int a = candi[i][j][0];
                        assert(ans and sat[a] == 1);
                    }

                    if (candi[i][j].size() == 2)
                    {
                        int a = candi[i][j][0];
                        int b = candi[i][j][1];
                        assert(ans and (sat[a] == 1 or sat[b] == 1));
                    }
                }
        }

        printf("Case #%d: %s\n", zi, ans ? "POSSIBLE" : "IMPOSSIBLE");
        if (ans)
        {

            for (int i = 0; i < R; ++i)
            {
                for (int j = 0; j < C; ++j)
                    printf("%c", mp[i][j]);
                printf("\n");
            }
        }
    }
}

