#define FNAME ""

#include <bits/stdc++.h>

#define hash padjf9srpi
#define y0 sdkfaslhagaklsldk
#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define forn(i, n) for (int i = 0; i < (n); i++)
#define fornr(i, n) for (int i = (n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (a); i < (b); i++)
#define gcd __gcd
#define all(a) (a).begin(), (a).end()
#define sz(v) (int) v.size()
 
#ifdef _WIN32
    #define I64 "%I64d"
#else
    #define I64 "%lld"
#endif

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair <int, int> pii;                                                                                                                                                                                      
typedef vector <int> vi;

template <class T> T sqr(const T &a) {return a * a;}


const int MAX_N = 1000;

//MAX_N - 2 * vars
vector <int> g[MAX_N], rg[MAX_N], tsort;
vector <bool> values;
int used[MAX_N], comp[MAX_N];

void dfs(int v) {
    used[v] = 1;
    for(int to : g[v])
        if (!used[to])
            dfs(to);
    tsort.pb(v);
}

void rdfs(int v, int num) {
    used[v] = 1;
    comp[v] = num;
    for(int to : rg[v]) 
        if (!used[to])
            rdfs(to, num);
}

void addEdge(int a, int b) {
    g[a ^ 1].pb(b);
    g[b ^ 1].pb(a);
    rg[b].pb(a ^ 1);
    rg[a].pb(b ^ 1);
}
//n - удвоенное
bool solveSat(const vector <pii> &v, int n) {
    forn(i, n) g[i].clear(), rg[i].clear();
    tsort.clear();
    values.clear();
    forn(i, sz(v)) {
        addEdge(v[i].fst, v[i].snd); 
    }
    memset(used, 0, sizeof(used));
    memset(comp, 0, sizeof(comp));
    forn(i, n)
        if (!used[i])
            dfs(i);
    memset(used, 0, sizeof(used));
    int num = 0;
    fornr(i, n) {
        int u = tsort[i];
        if (!used[u])
            rdfs(u, num), num++;
    }
    values.resize(n);
  //  forn(i, n) cerr << comp[i] << " ";
//    cerr << endl;
    for(int i = 0; i < n; i += 2)
        if (comp[i] == comp[i ^ 1])
            return 0;
        else if (comp[i] > comp[i ^ 1])
            values[i] = 1, values[i ^ 1] = 0;
        else
            values[i] = 0, values[i ^ 1] = 1;
    return 1;
}


const int turn[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

char s[110][100];
pii pos[110];
int num[110][110];
vector <pair <int, pii> > visited[110][110];

inline int rotateMain(int dir) {
    if (dir == 0) return 3;
    if (dir == 1) return 2;
    if (dir == 2) return 1;
    if (dir == 3) return 0;   
    assert(0);
}

inline int rotateSide(int dir) {
    if (dir == 0) return 2;
    if (dir == 1) return 3;
    if (dir == 2) return 0;
    if (dir == 3) return 1;
    assert(0);
}

int n, m;
inline int inside(int x, int y) {return x >= 0 && x < n && y >= 0 && y < m;}

bool cmp(pair <int, pii> x, pair <int, pii> y) {
    return x.second < y.second;
}

bool cmpEq(pair <int, pii> x, pair <int, pii> y) {
    return x.second == y.second;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

#ifdef LOCAL
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);
#endif
    int T;

    scanf("%d", &T);
    forn(tNum, T) {
        scanf("%d%d", &n, &m);
        forn(i, n) scanf("%s", s[i]);
        int beamCnt = 0;
        forn(i, n) {
            forn(j, m) {
                if (s[i][j] == '|') s[i][j] = '-';
                if (s[i][j] == '-') {
                    pos[beamCnt] = {i, j};
                    num[i][j] = beamCnt;
                    beamCnt++;
                }
            }
        }
        forn(i, n) forn(j, m) visited[i][j].clear();
        vector <pii> sat2;
        forn(i, beamCnt) {
            forn(orient, 2) {
                forn(dd, 2) {
                    int x = pos[i].first, y = pos[i].second, curDir = 2 * orient + dd;
                    x += turn[curDir][0], y += turn[curDir][1];
                    while (inside(x, y) && s[x][y] != '-' && s[x][y] != '#') {
                        int z = turn[curDir][0] + turn[curDir][1] + 2;
                        int zz = turn[curDir][0] - turn[curDir][1] + 2;
                        if (s[x][y] == '/')
                            visited[x][y].pb({z, {i, orient}});
                        else if (s[x][y] == '\\') 
                            visited[x][y].pb({zz, {i, orient}});
                        else
                            visited[x][y].pb({curDir / 2, {i, orient}});
                        if (s[x][y] == '/') curDir = rotateMain(curDir);
                        if (s[x][y] == '\\') curDir = rotateSide(curDir);
                        x += turn[curDir][0], y += turn[curDir][1];
                    }
                    if (inside(x, y) && s[x][y] != '#') {
    //                    int z = num[x][y
                        sat2.pb({2 * i + 1 - orient, 2 * i + 1 - orient});
//                        if (curDir < 2) sat2.pb2 * z + 1});
  //                      else sat2.pb({2 * i + 1 - orient, 2 * z + 0});
                    }

                }
            }
        }
       // cerr << 123 << endl;
        int ok = 1; 
        forn(i, n) {
            forn(j, m) {
                forn(k, (int) visited[i][j].size()) {
                 //   cerr << visited[i][j][k].second.first << " " << i << " " << j << endl;
                }
                sort(all(visited[i][j]), cmp);
                visited[i][j].resize(unique(all(visited[i][j]),  cmpEq) - visited[i][j].begin());  
                int canDir[4] = {0};
                
                forn(k, (int) visited[i][j].size()) {
                    canDir[visited[i][j][k].first]++;
                }                                
                vector <pii> vvv;
                forn(k, (int) visited[i][j].size()) {
                    //cerr << visited[i][j][k].first << " " << visited[i][j][k].second.first << " " << i << " " << j << endl;
                    if (canDir[visited[i][j][k].first] == 1) vvv.pb(visited[i][j][k].second);
                }                                

//                visited[i][j].resize(unique(all(visited[i][j])) - visited[i][j].begin());
                if (s[i][j] == '-' || s[i][j] == '#') continue;
                vvv.resize(unique(all(vvv)) - vvv.begin());
                if (vvv.size() == 0) {
                 //   cerr << i << " " << j << " " << visited[i][j].size() << endl;
        //            for (auto z: visited[i][j])
          //              cerr << z.first << "  " << z.second.first << " " <<z.second.second << endl;
                    ok = 0;
                    continue;
                }
                if (vvv.size() > 2) {
               //     cerr << i << " " << j << endl;
                    for (pii p: vvv)
                        cerr << p.first << " " <<p.second << endl;
                    ok = 0;
                    continue;
                }
                if (vvv.size() == 1) {
             //       cerr << i << " " << j << " " << 2 * vvv[0].first + vvv[0].second << endl;
                    sat2.pb({2 * vvv[0].first + vvv[0].second, 2 * vvv[0].first + vvv[0].second});
                } else {
                    sat2.pb({2 * vvv[0].first + vvv[0].second, 2 * vvv[1].first + vvv[1].second});
                }
            }
        }
        //for (auto p: sat2) printf("%d %d\n", p.first, p.second);
        //cerr << 456 << " " << ok << endl;
    
        if (!ok || !solveSat(sat2, 2 * beamCnt)) {
            printf("Case #%d: IMPOSSIBLE\n", tNum + 1);
            continue;
        }
        printf("Case #%d: POSSIBLE\n", tNum + 1);
        forn(i, n) {
            forn(j, m) {
                if (s[i][j] != '-') printf("%c", s[i][j]);
                else printf("%c", values[2 * num[i][j]] ? '|' : '-');
            }
            puts("");
        }
       // cerr << 789 << endl;
    }
    
}


