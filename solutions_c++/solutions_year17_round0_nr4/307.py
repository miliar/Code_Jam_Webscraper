#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <ctype.h>
#include <deque>
#include <queue>
#include <cstring>
#include <set>
#include <list>
#include <map>
#include <random>
#include <unordered_map>
#include <stdio.h>

using namespace std;

typedef long long ll;
typedef std::vector<int> vi;
typedef std::vector<bool> vb;
typedef std::vector<string> vs;
typedef std::vector<double> vd;
typedef std::vector<long long> vll;
typedef std::vector<std::vector<int> > vvi;
typedef vector<vvi> vvvi;
typedef vector<vll> vvll;
typedef std::vector<std::pair<int, int> > vpi;
typedef vector<vpi> vvpi;
typedef std::pair<int, int> pi;
typedef std::pair<ll, ll> pll;
typedef std::vector<pll> vpll;

const long long mod = 1000000007;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()
#define forn(i, a, b) for(int i = a; i < b; i++)

#define pb push_back
#define mp make_pair

const int MAXN = 1000;
const int INF = 1000000000;

struct edge {
    int a, b;
    int cap,flow;
};

int s, t, d[MAXN], ptr[MAXN], q[MAXN];
int N;
vector<edge> e;
vector<int> g[MAXN];

void clear_all() {
    forn(i,0,MAXN) {
        d[i]=0;
        ptr[i]=0;
        q[i]=0;
        g[i].clear();
    }
    e.clear();
}

void add_edge (int a, int b, int cap) {
//    cout<<a<<' '<<b<<endl;
    edge e1 = { a, b, cap, 0 };
    edge e2 = { b, a, 0, 0 };
    g[a].push_back ((int) e.size());
    e.push_back (e1);
    g[b].push_back ((int) e.size());
    e.push_back (e2);
}

bool bfs() {
    int qh=0, qt=0;
    q[qt++] = s;
    memset (d, -1, N * sizeof d[0]);
    d[s] = 0;
    while (qh < qt && d[t] == -1) {
        int v = q[qh++];
        for (size_t i=0; i<g[v].size(); ++i) {
            int id = g[v][i],
            to = e[id].b;
            if (d[to] == -1 && e[id].flow < e[id].cap) {
                q[qt++] = to;
                d[to] = d[v] + 1;
            }
        }
    }
    return d[t] != -1;
}

int dfs (int v, int flow) {
    if (!flow)  return 0;
    if (v == t)  return flow;
    for (; ptr[v]<(int)g[v].size(); ++ptr[v]) {
        int id = g[v][ptr[v]],
        to = e[id].b;
        if (d[to] != d[v] + 1)  continue;
        int pushed = dfs (to, min (flow, e[id].cap - e[id].flow));
        if (pushed) {
            e[id].flow += pushed;
            e[id^1].flow -= pushed;
            return pushed;
        }
    }
    return 0;
}

int dinic() {
    int flow = 0;
    for (;;) {
        if (!bfs())  break;
        memset (ptr, 0, N * sizeof ptr[0]);
        while (1) {
            ll pushed = dfs (s, INF);
            flow += pushed;
            if(pushed==0) break;
        }
    }
    return flow;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    int T;
    scanf("%d", &T);
    forn(aff, 0, T) {
//        cout<<"Case #"<<aff+1<<": ";
        printf("Case #%d: ", aff+1);
        int n,m;
        scanf("%d %d\n", &n, &m);
        vvi a(n, vi(n,0));
        set<int> h,w;
        set<int> dp, dm;
        forn(i,1-n, n) dm.insert(i);
        forn(i,0,2*n-1) dp.insert(i);
        forn(i,0,n) {
            h.insert(i);
            w.insert(i);
        }
        set<pi> axys;
        forn(i,0,m) {
            char c;
            int x, y;
            scanf("%c %d %d\n", &c, &x, &y);
            x--;
            y--;
            if(c=='o') {
                a[x][y] = 3;
                dm.erase(x-y);
                dp.erase(x+y);
                h.erase(x);
                w.erase(y);
            }
            else if(c=='x') {
                a[x][y] = 2;
                h.erase(x);
                w.erase(y);
            }
            else {
                a[x][y] = 1;
                dm.erase(x-y);
                dp.erase(x+y);
            }
        }
        vi hor,ver;
        for(auto x : h) hor.pb(x);
        for(auto x : w) ver.pb(x);
        int l = hor.size();
        forn(i,0,l) {
            a[hor[i]][ver[i]] += 2;
            axys.insert(mp(hor[i],ver[i]));
        }
        N=4*n;
        clear_all();
        s = 0;
        t=4*n-1;
        for(auto x : dm) add_edge(0, x+n, 1);
        for(auto x : dp) add_edge(x+2*n, t, 1);
        for(auto x : dm) {
            for(auto y : dp) {
                if((x+y)%2 != 0) continue;
                int xw = (x+y)/2;
                int yw = (y-x)/2;
                if(xw<0 || yw<0 || xw>=n || yw>=n) continue;
                add_edge(x+n, y+2*n, 1);
            }
        }
//        continue;
        dinic();
        for(auto ed : e) {
            if(ed.flow > 0 &&  ed.a != s && ed.b != t) {
                int x = ed.a - n;
                int y = ed.b - 2*n;
                int xw = (x+y)/2;
                int yw = (y-x)/2;
                a[xw][yw] += 1;
                axys.insert(mp(xw,yw));
            }
        }
        vector<char> ac;
        vpi axy;
        int ans = 0;
        forn(i,0,n) forn(j,0,n) {
            if(a[i][j] == 3) ans+=2;
            else if(a[i][j] > 0) ans++;
        }
        for(auto ped : axys) {
            int i = ped.first;
            int j = ped.second;
            if(a[i][j] == 1) {
                ac.pb('+');
                axy.pb(mp(i+1,j+1));
            }
            else if(a[i][j] == 2) {
                ac.pb('x');
                axy.pb(mp(i+1,j+1));
            }
            else if(a[i][j] == 3) {
                ac.pb('o');
                axy.pb(mp(i+1,j+1));
            }
        }
        printf("%d %d\n", ans, (int)ac.size());
        forn(i,0, ac.size()) {
            printf("%c %d %d\n", ac[i], axy[i].first, axy[i].second);
        }
    }
    
    
}


