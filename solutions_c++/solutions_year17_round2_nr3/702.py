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

typedef pair<li, li> PI;

li e[111];
li s[111];
li d[111][111];
li n, q;
li from, to;

li sum_distance[111];

// {dest, distance} 道路の距離
vector<PI> edge[110];

// {行先、コスト} i番目の都市の馬でどこまでいけるか
vector<pair<li, double>> edge2[110];

inline double calc(li from, li to) {
    // edge2をつかってダイクストラする
    bool visited[111] = {false};
    // {cost, index}
    priority_queue<pair<double, li>> pq;
    pq.push({0.0, from});
    while (!pq.empty()) {
        li now = pq.top().S;
        double cost_now = pq.top().F;
        pq.pop();
        if (visited[now])continue;
        visited[now] = true;
        if (now == to)return -cost_now;
        rep(i, sz(edge2[now])) {
            li next = edge2[now][i].F;
            double cost = cost_now - edge2[now][i].S;
            if (!visited[next]) {
                pq.push({cost, next});
            }
        }
    }
    return -1;
}

// rootから行ける場所をダイクストラしてコスト求める
inline void dijkstra_first(li root) {
    // {cost, index}
    bool visited[111] = {false};
    li total_distance[111] = {0};
    priority_queue<PI> pq;
    pq.push({0, root});
    while (!pq.empty()) {
        li now = pq.top().S;
        li cost_now = pq.top().F;
        pq.pop();
        if (visited[now])continue;
        total_distance[now] = -cost_now;
        visited[now] = true;
        rep(i, sz(edge[now])) {
            li next = edge[now][i].F;
            li dd = cost_now - edge[now][i].S;
            if (-dd <= e[root] && !visited[next]) {
                pq.push({dd, next});
            }
        }
    }
    rep(i, n) {
        if (total_distance[i] != 0) {
            edge2[root].pb({i, total_distance[i] * 1.0 / s[root]});
        }
    }
}

inline void solve() {
    cin >> n >> q;
    rin{
        cin >> e[i] >> s[i];
    }
    rin{
        edge[i].clear();
        edge2[i].clear();
        rep(j, n) {
            cin >> d[i][j];
            if (d[i][j] >= 0) {
                edge[i].pb({j, d[i][j]});
            }
        }
    }
    // 各点から行ける場所についてダイクストラ
    rin{
        dijkstra_first(i);
        /*
        rep(j, sz(edge2[i])) {
            cout << edge2[i][j].F << "," << edge2[i][j].S << " ";
        } puts("");
        //*/
    }

    rep(i, q) {
        cin >> from >> to;
        --from;
        --to;
        printf("%.12f", calc(from, to));
        if (i != q - 1)cout << " ";
    }
    cout << endl;

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