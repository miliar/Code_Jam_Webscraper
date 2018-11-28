#include <bits/stdc++.h>
using namespace std;

#define GET_MACRO(_1,_2,_3,_4,NAME,...) NAME
#define REP2(i,n) for(int i=0;i<(int)(n);i++)
#define REP3(i,m,n) for(int i=m;i<(int)(n);i++)
#define REP4(i,m,n,s) for(int i=m;(s>0 and i<(int)(n)) or (s<0 and i>(int)(n));i+=s)
#define REP(...) GET_MACRO(__VA_ARGS__, REP4, REP3, REP2)(__VA_ARGS__)
#define REPIT(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define PIS(x) printf("%d ",x)
#define PRINTIA(a,n) REP(i,n){printf("%d ", *((a)+i));}putchar('\n');
#define PN() putchar('\n')
#define MP make_pair
#define PB push_back

typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;

void RI() {}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}
void PI() {putchar('\n');}
template<typename... T>
void PI(const int head, T... tail ) {
    printf("%d ", head);
    PI(tail...);
}

#define MAX_N 100
#define INF INT_MAX

struct edge {
    int to, cap, rev;
};

vector<edge> G[MAX_N * MAX_N];
int level[MAX_N * MAX_N];
int iter[MAX_N * MAX_N];

void add_edge(int from, int to, int cap) {
    int i = G[from].size();
    int j = G[to].size();
    G[from].push_back((edge){to, cap, j});
    G[to].push_back((edge){from, 0, i});
}

void bfs(int s) {
    memset(level, -1, sizeof(level));
    queue<int> que;
    level[s] = 0;
    que.push(s);
    while(!que.empty()) {
        int v = que.front();
        que.pop();
        for(int i = 0; i < (int)G[v].size(); i++) {
            edge &e = G[v][i];
            if(e.cap > 0 && level[e.to] < 0) {
                level[e.to] = level[v] + 1;
                que.push(e.to);
            }
        }
    }
}

int dfs(int v, int t, int f) {
    if(v == t)
        return f;
    for(int &i = iter[v]; i < (int)G[v].size(); i++) {
        edge &e = G[v][i];
        if(e.cap > 0 && level[v] < level[e.to]) {
            int d = dfs(e.to, t, min(f, e.cap));
            if(d > 0) {
                e.cap -= d;
                G[e.to][e.rev].cap += d;
                return d;
            }
        }
    }
    return 0;
}

int max_flow(int s, int t) {
    int flow = 0;
    while(true) {
        bfs(s);
        if(level[t] < 0)
            return flow;
        memset(iter, 0, sizeof(iter));
        int f;
        while((f=dfs(s, t, INF)) > 0) {
            flow += f;
        }
    }
}
int R[MAX_N];
int Q[MAX_N][MAX_N];
unordered_map<int, vector<int> > M[MAX_N];

void solve() {
    memset(level, 0, sizeof(level));
    memset(iter, 0, sizeof(level));
    REP(i, MAX_N*MAX_N) {
        G[i].clear();
    }

    int N, P;
    RI(N, P);
    REP(i, N) {
        RI(R[i]);
    }
    REP(i, N) {
        REP(j, P) {
            RI(Q[i][j]);
            bool yes = false;
            int l = ceil(Q[i][j] / 1.1 / R[i]);
            int r = floor(Q[i][j] / 0.9 / R[i]) + 1;
            REP(k, l, r) {
                if(0.9*R[i]*k <= Q[i][j] and 1.1*R[i]*k >= Q[i][j]) {
                    M[i][k].PB(j);
                    yes = true;
                }
            }
            if(i == 0 and yes) {
                add_edge(0, 2 + P*i + j, 1);
            }
            if(i == N-1 and yes) {
                add_edge(2 + P*i + j, 1, 1);
            }
        }
    }
    REP(i, N-1) {
        REPIT(ii, M[i]) {
            REPIT(jj, ii->second) {
                REPIT(kk, M[i+1][ii->first]) {
                    add_edge(2 + P*i + (*jj), 2 + P*(i+1) + (*kk), 1);
                }
            }
        }
    }
    PI(max_flow(0, 1));

    REP(i, N) {
        M[i].clear();
    }
}

int main()
{
    int T;
    RI(T);
    REP(i, T) {
        printf("Case #%d: ", i+1);
        solve();
    }

    return 0;
}
