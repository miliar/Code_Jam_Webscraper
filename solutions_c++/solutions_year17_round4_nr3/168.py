#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for (int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for (int i = (int)(n) - 1; i >= (int)(k); i--)

#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define db(x) cout << #x << " = " << x << endl

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;
typedef double ld; 

const ld pi = acos(-1.0);
const ld eps = 1e-8;
const int INF = (int)1e9;
const int MAXN = 55;
const pii delta[4] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

pii operator+(pii a, pii b) {
    return {a.X + b.X, a.Y + b.Y};    
}

int T;
int n, m;
string s[MAXN];
bool shooter[MAXN][MAXN], used[MAXN][MAXN];
vector<pii> shooters[4];
vector<pii> curFree;
vector<pii> covered[MAXN][MAXN][2];
vector<pair<pii, char>> edges[MAXN][MAXN];
int choose[MAXN][MAXN];

void delEdge(vector<pair<pii, char>> &v, pair<pii, char> elem) {
    for (int i = 0; i < (int)v.size(); i++) {
        if (v[i] == elem) {
            swap(v[i], v.back());
            v.pop_back();
            return;   
        }
    }
    
    assert(false);
}

bool correct(pii p) {
    return 0 <= p.X && p.X < n && 0 <= p.Y && p.Y < m;    
}

bool dfs(pii pos, pii dir) {
    pii npos = pos + dir;
    if (!correct(npos)) {
        return 1;
    }
    if (s[npos.X][npos.Y] == '#') {
        return 1;
    }
    if (shooter[npos.X][npos.Y]) {
        return 0;
    }
    curFree.pb(npos);
    return dfs(npos, dir);
}

string PATTERN = "-|";

set<pair<int, pii>> rest;

int main() {
        
    cin >> T;
    forn(tt, T) {
        printf("Case #%d: ", tt + 1);
        
        scanf("%d %d\n", &n, &m);
        forn(i, n) {
            cin >> s[i];
        }
        
        forn(i, 4) {
            shooters[i].clear();
        }
        
        memset(shooter, 0, sizeof(shooter));
        forn(i, n) {
            forn(j, m) {
                shooter[i][j] = (s[i][j] == '-' || s[i][j] == '|');
                if (shooter[i][j]) {
                    s[i][j] = '-';
                }
                forn(d, 2) {
                    covered[i][j][d].clear();
                }
                edges[i][j].clear();
            }
        }
        
        bool fail = 0;
        forn(i, n) {
            forn(j, m) {
                if (shooter[i][j]) {
                    int any = 0;
                    
                    forn(d, 2) {
                        bool ok = 1;
                        curFree.clear();
                        forn(t, 2) {
                            ok &= dfs(mp(i, j), delta[t + d * 2]);
                        }
                        
                        if (ok) {
                            any += (1 << d);
                            covered[i][j][d] = curFree;
                            for (auto p: curFree) {
                                edges[p.X][p.Y].pb(mp(mp(i, j), d));
                            }
                        }
                    }
                    
                    if (any == 0) {
                        fail = 1;   
                    } else {
                        shooters[any].pb(mp(i, j));      
                    }
                }
            }
        }
        
        if (fail) {
            cout << "IMPOSSIBLE\n";    
            continue;
        }
        
        memset(choose, 0, sizeof(choose));
        memset(used, 0, sizeof(used));
        for (int mask = 1; mask <= 2; mask++) {
            for (auto p: shooters[mask]) {
                //cout << "CHOOSE " << p.X << ' ' << p.Y << ' ' << mask - 1 << endl;
                choose[p.X][p.Y] = mask - 1;
                int id = choose[p.X][p.Y];
                for (auto q: covered[p.X][p.Y][id]) {
                    //cout << "COVER " << q.X << ' ' << q.Y << endl;
                    used[q.X][q.Y] = 1;   
                    //cerr << "!" << endl;
                    delEdge(edges[q.X][q.Y], mp(p, id));
                    //cerr << "!!" << endl;
                }
            }
        }

        rest.clear();
                
        forn(i, n) {
            forn(j, m) {
                if (s[i][j] == '.' && !used[i][j]) {
                    //cout << "ADD " << i << ' ' << j << ' ' << edges[i][j].size() << endl;
                    rest.insert(mp((int)edges[i][j].size(), mp(i, j)));    
                }
            }
        }
        
        while (!rest.empty()) {
            auto cur = *rest.begin();
            rest.erase(cur);
            if (cur.X == 2) {
                break;
            }
            
            if (cur.X == 0) {
                fail = 1;
                break;
            }
            
            assert(cur.X == 1);
            pii p = cur.Y;
            assert((int)edges[p.X][p.Y].size() == 1);
            pii q = edges[p.X][p.Y][0].X;
            int id = edges[p.X][p.Y][0].Y;
            
            for (auto r: covered[q.X][q.Y][id]) {
                used[r.X][r.Y] = 1;   
                rest.erase(mp((int)edges[r.X][r.Y].size(), r));
            }
            
            for (auto r: covered[q.X][q.Y][id ^ 1]) {
                if (!used[r.X][r.Y]) {
                    rest.erase(mp((int)edges[r.X][r.Y].size(), r));
                    delEdge(edges[r.X][r.Y], mp(q, id ^ 1));
                    rest.insert(mp((int)edges[r.X][r.Y].size(), r));                
                }
            }
        }
        
        if (fail) {
            cout << "IMPOSSIBLE\n";    
        } else {
            cout << "POSSIBLE\n";    
            
            forn(i, n) {
                forn(j, m) {
                    if (s[i][j] == '.') {
                        //assert(used[i][j]);
                    }
                }
            }
            
            forn(i, n) {
                forn(j, m) {
                    if (shooter[i][j]) {
                        s[i][j] = PATTERN[choose[i][j]];   
                    }
                }
            }
                
            forn(i, n) {
                cout << s[i] << '\n';
            }
        }
    }
    
    return 0;
}
