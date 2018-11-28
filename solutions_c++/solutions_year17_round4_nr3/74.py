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


vector < vector<int> > g, gt;
vector<bool> used;
vector<int> order, comp;

void dfs1 (int v) {
    used[v] = true;
    for (size_t i=0; i<g[v].size(); ++i) {
        int to = g[v][i];
        if (!used[to])
        dfs1 (to);
    }
    order.push_back (v);
}

void dfs2 (int v, int cl) {
    comp[v] = cl;
    for (size_t i=0; i<gt[v].size(); ++i) {
        int to = gt[v][i];
        if (comp[to] == -1)
        dfs2 (to, cl);
    }
}

void sanitize() {
    int x = g.size();
    forn(i,0,x) {
        vi lol = g[i];
        g[i].clear();
        sort(all(lol));
        forn(j,0,lol.size()) {
            if(j==0 || lol[j] != lol[j-1]) g[i].pb(lol[j]);
        }
    }
    x = gt.size();
    forn(i,0,x) {
        vi lol = gt[i];
        gt[i].clear();
        sort(all(lol));
        forn(j,0,lol.size()) {
            if(j==0 || lol[j] != lol[j-1]) gt[i].pb(lol[j]);
        }
    }
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    int totcasnum;
    scanf("%d", &totcasnum);
    forn(casnum,0,totcasnum) {
        g.clear();
        gt.clear();
        used.clear();
        order.clear();
        comp.clear();
        printf("Case #%d: ", casnum+1);
        int r,c;
        scanf("%d %d\n", &r, &c);
        vs a(r);
        forn(i,0,r) getline(cin, a[i]);
//        vvi nb(4, vi(r*c,-1));
//        vvi vis(4, vi(r*c, 0));
//        vvi res(4, vi(r*c, -1));
//        deque<pi> q;
//        forn(i,0,r) {
//            int last = -1;
//            forn(j,0,c) {
//                if(a[i][j] == '.') continue;
//                else if(a[i][j] == '#') {
//                    last = -1;
//                }
//                else {
//                    int cur = i * c + j;
//                    if (last != -1) {
//                        nb[0][last] = cur;
//                    }
//                    else {
//                        vis[2][cur] = 1;
//                        q.pb(mp(2,cur));
//                    }
//                    nb[2][cur] = last;
//                    last = cur;
//                }
//            }
//            if(last != -1) {
//                vis[0][last] = 1;
//                q.pb(mp(0,last));
//            }
//        }
//        forn(j,0,c) {
//            int last = -1;
//            forn(i,0,r) {
//                if(a[i][j] == '.') continue;
//                else if(a[i][j] == '#') {
//                    last = -1;
//                }
//                else {
//                    int cur = i * c + j;
//                    if (last != -1) {
//                        nb[3][last] = cur;
//                    }
//                    else {
//                        vis[1][cur] = 1;
//                        q.pb(mp(1,cur));
//                    }
//                    nb[1][cur] = last;
//                    last = cur;
//                }
//            }
//            if(last != -1) {
//                vis[3][last] = 1;
//                q.pb(mp(3,last));
//            }
//        }
        vi laser;
        vpi dir = {{1,0}, {0,-1}, {-1,0}, {0,1}};
        int num = 0;
        vvi res(r, vi(c,-1));
        forn(i,0,r) {
            forn(j,0,c) {
                if(a[i][j] == '|' || a[i][j] =='-') {
                    int cur = i*c+j;
                    laser.pb(cur);
                    res[i][j] = num;
                    num++;
                }
            }
        }
        int cal = 1;
        vvi can(r*c);
        int n = 2*num;
        g.resize(n);
        gt.resize(n);
        forn(i,0,num) {
            vvi passed(4);
            vi possb(4,1);
            forn(st,0,4) {
                int cdir = st;
                int cx = laser[i] % c;
                int cy = laser[i] / c;
                while(1) {
                    cx += dir[cdir].first;
                    cy += dir[cdir].second;
                    if(cx >= c || cx < 0 || cy>=r || cy < 0 || a[cy][cx] == '#') {
                        break;
                    }
                    else if(a[cy][cx] == '.') {
                        passed[st].pb(cy*c+cx);
                        continue;
                    }
                    else if(a[cy][cx] == '\\') cdir = 3 - cdir;
                    else if(a[cy][cx] == '/') cdir = (5 - cdir) % 4;
                    else if(res[cy][cx] >= 0) {
                        possb[st] = 0;
                        break;
                    }
                }
            }
            int canthis = 0;
            if(possb[0]+possb[2] == 2) {
                canthis = 1;
                for(auto u : passed[0]) {
                    can[u].pb(2*i);
                }
                for(auto u : passed[2]) {
                    can[u].pb(2*i);
                }
            }
            else {
                int ind = 2*i;
                int pind = ind^1;
                g[ind].pb(pind);
                gt[pind].pb(ind);
            }
            if(possb[1]+possb[3] == 2) {
                canthis = 1;
                for(auto u : passed[1]) {
                    can[u].pb(2*i+1);
                }
                for(auto u : passed[3]) {
                    can[u].pb(2*i+1);
                }
            }
            else {
                int ind = 2*i+1;
                int pind = ind^1;
                g[ind].pb(pind);
                gt[pind].pb(ind);
            }
            if(canthis == 0) cal = 0;
        }
        if(cal == 0) {
            printf("IMPOSSIBLE\n");
            continue;
        }

        forn(i,0,r) forn(j,0,c) {
            if(a[i][j] == '.') {
                int cur = i*c+j;
                if(can[cur].size()==0) {
                    cal = 0;
                    break;
                }
                else if(can[cur].size() == 1) {
                    int ind = can[cur][0];
                    int pind = ind^1;
                    g[pind].pb(ind);
                    gt[ind].pb(pind);
                }
                else if(can[cur].size() == 2){
                    int ind1 = can[cur][0];
                    int pind1 = ind1^1;
                    int ind2 = can[cur][1];
                    int pind2 = ind2^1;
                    g[pind1].pb(ind2);
                    gt[ind2].pb(pind1);
                    g[pind2].pb(ind1);
                    gt[ind1].pb(pind2);
                }
            }
        }
        
        sanitize();
        used = vb(n,false);
        for (int i=0; i<n; ++i)
        if (!used[i])
        dfs1 (i);
        
        if(cal == 0) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        
        comp = vi(n, -1);
        for (int i=0, j=0; i<n; ++i) {
            int v = order[n-i-1];
            if (comp[v] == -1)
            dfs2 (v, j++);
        }
        
        for (int i=0; i<n; ++i)
        if (comp[i] == comp[i^1]) {
            printf("IMPOSSIBLE\n");
            cal = 0;
            break;
        }
        if(cal == 0) continue;
        for (int i=0; i<n; ++i) {
            int ans = comp[i] > comp[i^1] ? i : i^1;
            if(i%2 == 0) {
                int x = laser[i/2]%c;
                int y = laser[i/2]/c;
                if(ans%2 == 0) {
                    a[y][x] = '-';
                }
                else a[y][x] = '|';
            }
        }
        printf("POSSIBLE\n");
        forn(i,0,r) {
            printf("%s\n", a[i].c_str());
        }
        
//        while(!q.empty()) {
//            auto lol = q.front();
//            q.pop_front();
//        }
        //        printf("\n");
    }
    
    
}


