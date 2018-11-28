#include<bits/stdc++.h>
using namespace std;


#define li          long long int
#define rep(i,to)   for(li i=0;i<((li)(to));i++)
#define repp(i,start,to)    for(li i=(li)(start);i<((li)(to));i++)
#define pb          push_back
#define sz(v)       ((li)(v).size())
#define bgn(v)      ((v).begin())
#define eend(v)     ((v).end())
#define allof(v)    (v).begin(), (v).end()
#define dodp(v,n)       memset(v,(li)n,sizeof(v))
#define bit(n)      (1ll<<(li)(n))
#define mp(a,b)     make_pair(a,b)
#define rin rep(i,n)
#define EPS 1e-12
#define ETOL 1e-8
#define MOD 1000000007
typedef pair<li, li> PI;

#define INF bit(60)

#define DBGP 1


#define idp if(DBGP)
#define F first
#define S second
#define p2(a,b)     idp cout<<a<<"\t"<<b<<endl
#define p3(a,b,c)       idp cout<<a<<"\t"<<b<<"\t"<<c<<endl
#define p4(a,b,c,d)     idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<endl
#define p5(a,b,c,d,e)       idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<endl
#define p6(a,b,c,d,e,f)     idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<endl
#define p7(a,b,c,d,e,f,g)       idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<"\t"<<g<<endl
#define p8(a,b,c,d,e,f,g,h)     idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<"\t"<<g<<"\t"<<h<<endl
#define p9(a,b,c,d,e,f,g,h,i)       idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<"\t"<<g<<"\t"<<h<<"\t"<<i<<endl
#define p10(a,b,c,d,e,f,g,h,i,j)        idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<"\t"<<g<<"\t"<<h<<"\t"<<i<<"\t"<<j<<endl
#define foreach(it,v)   for(__typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
#define p2p(x)      idp p2((x).F, (x).S)
#define dump(x,n)   idp{rep(i,n){cout<<x[i]<<" ";}puts("");}
#define dump2(x,n)  idp{rep(i,n){cout<<"["<<x[i].F<<" , "<<x[i].S<<"] ";}puts("");}
#define dumpi(x)    idp{foreach(it, x){cout<<(*it)<<" ";}puts("");}
#define dumpi2(x)   idp{foreach(it, x){cout<<"["<<(it)->F<<" , "<<(it)->S<<"] ";}puts("");}

#define read2d(a,w,h)   rep(i,h)rep(j,w)cin>>a[i][j]
#define dump2d(a,w,h)   rep(i,h){rep(j,w)cout<<a[i][j]<<" ";puts("");}

#define M_PI 3.1415926535897932384626

typedef pair<li, li> PI;

li g[111];
bool can[2020][2020];
bool used[2020];
// {to, {cap, rev}}
vector<pair<li, PI>> graph[2020];

inline void add_edge(li from, li to, li cap) {
    graph[from].pb({to, {cap, graph[to].size()}});
    graph[to].pb({from, {0, graph[from].size() - 1}});
}

li dfs(li v, li t, li f) {
    if (v == t)return f;
    used[v] = true;
    rep(i, sz(graph[v])) {
        auto& edge = graph[v][i];
        if (!used[edge.F] && edge.S.F > 0) {
            li d = dfs(edge.F, t, min(f, edge.S.F));
            if (d > 0) {
                edge.S.F -= d;
                graph[edge.F][edge.S.S].S.F += d;
                return d;
            }
        }
    }
    return 0;
}

inline li max_flow(li s, li t) {
    li flow = 0;
    while (1) {
        memset(used, 0, sizeof(used));
        li f = dfs(s, t, INF);
        if (f == 0)return flow;
        flow += f;
    }
}

inline void solve() {
    li n, c, m;
    cin >> n >> c >> m;
    vector<li> v[2020];
    rep(i, m) {
        li p, b;
        cin >> p >> b;
        p--;
        b--;
        v[b].pb(p);
    }
    rep(i, c) {
        sort(allof(v[i]));
    }
    if (c != 2) {
        return;
    }
    rep(i, 2020)rep(j, 2020)can[i][j] = false;
    rep(i, 2020) {
        graph[i].clear();
        used[i] = false;
    }
    li s = sz(v[0]) + sz(v[1]);
    li t = s + 1;
    rep(i, sz(v[0])) {
        add_edge(s, i, 1);
    }
    rep(i, sz(v[1])) {
        add_edge(sz(v[0]) + i, t, 1);
    }

    rep(i, sz(v[0])) {
        rep(j, sz(v[1])) {
            if (v[0][i] != v[1][j]) {
                add_edge(i, sz(v[0]) + j, 1);
            }
        }
    }

    li res = max_flow(s, t);
    vector<li> vv[2];
    li num = -1;
    rep(i, sz(graph[s])) {
        if (graph[s][i].S.F != 0) {
            //cout << v[0][graph[s][i].F] << " ";
            vv[0].pb(v[0][graph[s][i].F]);
            num = v[0][graph[s][i].F];
        }
    } //cout << endl;
    rep(i, sz(graph[t])) {
        auto& rev = graph[graph[t][i].F][graph[t][i].S.S];
        if (rev.S.F != 0) {
            //cout << v[1][graph[t][i].F - sz(v[0])] << " ";
            vv[1].pb(v[1][graph[t][i].F - sz(v[0])]);
            num = v[1][graph[t][i].F - sz(v[0])];
        }
    } //cout << endl;
    li res2 = 0;
    if (num == 0) {
        res += sz(vv[0]) + sz(vv[1]);
    } else {
        res += max(sz(vv[0]), sz(vv[1]));
        res2 += min(sz(vv[0]), sz(vv[1]));
    }
    cout << res << " " << res2 << endl;
    return;
}

int main() {
    li t;
    cin >> t;
    rep(case_num, t) {
        cout << "Case #" << case_num + 1 << ": ";
        solve();
    }

    return 0;
}