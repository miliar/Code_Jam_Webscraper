
#include <bits/stdc++.h>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)
#define FORD(i,b,e) for(int i=(b); i >= (e); --i)
#define SIZE(c) (int) (c).size()
#define FORE(i,c) FOR(i,0,SIZE(c)-1)
#define FORDE(i,c) FORD(i,SIZE(c)-1,0)

#define pb push_back
#define mp make_pair
#define st first
#define nd second


using namespace std;

typedef long long ll;
typedef pair <int,int> pii;
typedef pair <ll,ll> pll;

typedef vector <int> VI;
typedef vector <bool> VB;
typedef vector <pii> VP;
typedef vector <ll> VL;
typedef vector <pll> VPL;

typedef vector <VI> VVI;
typedef vector <VL> VVL;
typedef vector <VB> VVB;
typedef vector <VP> VVP;

const int MOD = 1000000007;
const int INF = 1000000001;
const ll LINF = 1000000000000000001LL;

/*************************************************************************/

struct TurboMatching {
    int value = 0;

    VVI G;
    VI mate; VB vis;

    TurboMatching(int n): G(n), mate(n,-1), vis(n,0) {}

    void addEdge(int u, int v) {
        G[u].pb(v);
        G[v].pb(u);
    }

    bool findPath(int v) {
        if (vis[v]) return false;
        vis[v] = true;

        for (int u : G[v]) if (mate[u] == -1 || findPath(mate[u])) {
            mate[v] = u;
            mate[u] = v;
            return true;
        }

        return false;
    }

    pair <int,VI> runMatching() {
        while (true) {
            bool found = false;
            FORE(v,G) vis[v] = false;

            FORE(v,G) if (mate[v] == -1 && findPath(v)) {
                found = true;
                value++;
            }

            if (!found) break;
        }

        return {value, mate};
    }
};

/*************************************************************************/

VP improve(VP &possible, VP &taken) {
    set <int> badX, badY;
    
    for (auto &e : taken) {
        badX.insert(e.st);
        badY.insert(e.nd);
    }
    
    VP rest;
    for (auto &e : possible) if (!badX.count(e.st) && !badY.count(e.nd)) {
        rest.pb(e);
    }
    
    int n = 1;
    for (auto &e : rest) {
        n = max({n, e.st, e.nd});
    }
    
    n++;    
    TurboMatching match(2 * n);
    
    for (auto &e : rest) {
        match.addEdge(e.st, n + e.nd);
    }
    
    VI mate = match.runMatching().nd;
    VP ans;
    
    FOR(i,0,n-1) if (mate[i] != -1) {
        ans.pb({i, mate[i] - n});
    }
    
    return ans;
}

int n;

pii fCross(int x, int y) {
    return {x ,y};
};

pii fPlus(int x, int y) {
    return {x + y, x + n - y};
};

typedef pii (func_t)(int, int);

void improve(int n, VVB &tab, func_t func) {
    VP possible;
    map <pii,pii> possibleVia;
    
    FOR(x,0,n-1) FOR(y,0,n-1) {
        auto f = func(x, y);
    
        possible.pb(f);
        possibleVia[f] = {x, y};
    }
    
    VP taken;
    FOR(x,0,n-1) FOR(y,0,n-1) if (tab[x][y]) {
        taken.pb(func(x, y));
    }
    
    VP res = improve(possible, taken);
    
    for (auto &e : res) {
        auto pos = possibleVia[e];
        tab[pos.st][pos.nd] = true;
    }
}

void solve(int n, VVB &plus, VVB &cross) {
    improve(n, plus, fPlus);
    improve(n, cross, fCross);
}

int calcScore(int n, VVB &plus, VVB &cross) {
    int ans = 0;
    FOR(i,0,n-1) FOR(j,0,n-1) {
        ans += plus[i][j];
        ans += cross[i][j];
    }
    
    return ans;
}

void check(int n, VVB &plus, VVB &cross) {
    vector <string> tab(n, string(n, ' '));
    FOR(i,0,n-1) FOR(j,0,n-1) {
        char c;
        if (plus[i][j] && cross[i][j]) {
            c = 'o';
        } else if (plus[i][j]) {
            c = '+';
        } else if (cross[i][j]) {
            c = 'x';
        } else {
            c = '.';
        }
        
        tab[i][j] = c;
    }
    
    FOR(i,0,n-1) FOR(j,0,n-1) if (tab[i][j] != '.')
        FOR(i2,0,n-1) FOR(j2,0,n-1) if (tab[i2][j2] != '.') if (i != i2 || j != j2) {
            if (i == i2 || j == j2) {
                assert(tab[i][j] == '+' || tab[i2][j2] == '+');
            }
            
            if (i-j == i2-j2 || i+j == i2+j2) {
                if (tab[i][j] != 'x' && tab[i2][j2] != 'x') {
                    assert(false);
                }
            }
        }
}

/*************************************************************************/

int main() {
    ios_base::sync_with_stdio(0);
    
    int t;
    cin >> t;
    
    FOR(i,1,t) {
        cin >> n;
        
        VVB plus(n, VB(n, false));
        VVB cross(n, VB(n, false));
        
        int m;
        cin >> m;
        
        while (m--) {
            char c;
            int x, y;
            
            cin >> c >> x >> y; x--; y--;
            
            if (c == '+' || c == 'o') {
                plus[x][y] = true;
            }
            
            if (c == 'x' || c == 'o') {
                cross[x][y] = true;
            }
        }
        
        VVB oldPlus = plus;
        VVB oldCross = cross;
        
        solve(n, plus, cross);
        
        cout << "Case #" << i << ": " << calcScore(n, plus, cross);
        
        VP changed;
        FOR(x,0,n-1) FOR(y,0,n-1) if (plus[x][y] != oldPlus[x][y] || cross[x][y] != oldCross[x][y]) {
            changed.pb({x, y});
        }
        
        //check(n, plus, cross);
        
        cout << ' ' << SIZE(changed) << '\n';
        
        for (auto &e : changed) {
            char c;
            int x = e.st, y = e.nd;
            
            if (plus[x][y] && cross[x][y]) {
                c = 'o';
            } else if (plus[x][y]) {
                c = '+';
            } else {
                c = 'x';
            }
            
            cout << c << ' ' << 1 + x << ' ' << 1 + y << '\n';
        }
    }

    return 0;
}

/*************************************************************************/

