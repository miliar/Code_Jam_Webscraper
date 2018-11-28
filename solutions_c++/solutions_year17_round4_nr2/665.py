#include <bits/stdc++.h>
using namespace std;

const int MAXN = 3010;
const int MAXM = 3010 * 3010;
struct Edge {
    int next, to, cap, cost;
    Edge() {}
    Edge(int next, int to, int cap, int cost)
            : next(next), to(to), cap(cap), cost(cost) {}
} edge[MAXM];
int head[MAXN], countedge;

inline void addEdge(const int& s, const int& t, const int& cap,
                                        const int& cost) {
    edge[countedge] = Edge(head[s], t, cap, cost);
    head[s] = countedge++;
    edge[countedge] = Edge(head[t], s, 0, -cost);
    head[t] = countedge++;
}

const int maxint = 0x3F3F3F3F;
int pi1, flow, cost, S, T, N;
bool v[MAXN];
int aug(int no, int m) {
    if (no == T) {
        return flow += m, cost += pi1 * m, m;
    }
    v[no] = true;
    int l = m;
    for (int tmp = head[no]; ~tmp; tmp = edge[tmp].next) {
        //std::cerr << 1 << endl;
        Edge& e = edge[tmp];
        if (e.cap && !e.cost && !v[e.to]) {
            int d = aug(e.to, l < e.cap ? l : e.cap);
            e.cap -= d, edge[tmp ^ 1].cap += d, l -= d;
            if (!l) return m;
        }
    }
    return m - l;
}

bool modlabel() {
    int d = maxint;
    for (int i = 0; i < N; ++i)
        if (v[i])
            for (int tmp = head[i]; ~tmp; tmp = edge[tmp].next)
                if (edge[tmp].cap && !v[edge[tmp].to] && edge[tmp].cost < d)
                    d = edge[tmp].cost;
    if (d == maxint) return false;
    for (int i = 0; i < N; ++i)
        if (v[i])
            for (int tmp = head[i]; ~tmp; tmp = edge[tmp].next) {
                edge[tmp].cost -= d, edge[tmp ^ 1].cost += d;
            }
    pi1 += d;
    return true;
}
std::pair<int, int> zkwmcmf() {
    //int a = clock();
    flow = 0, cost = 0, pi1 = 0;
    do {
        do {
            memset(v, 0, sizeof(*v) * N);
        } while (aug(S, maxint));
    } while (modlabel());
    return {flow, cost};
}

const int NN = 1010;
int P[NN], B[NN];
int tot[NN];

int n, C, m;
bool judge(int val) {
    S = 0, T = n + C + 1;
    N = n + C + 2;
    memset(head, -1, sizeof(*head) * N);
    countedge = 0;
    for(int i = 1; i <= C; i++) {
        if(tot[i]) {
            addEdge(S, i, tot[i], 0);
        }
    }
    for(int i = 1; i <= n; i++) {
        addEdge(i + C, T, val, 0);
    }
    for(int i = 0; i < m; i++) {
        for(int j = 1; j <= P[i]; j++) {
            if(j < P[i]) {
                addEdge(B[i], j + C, 1, 1);
            } else {
                addEdge(B[i], j + C, 1, 0);
            }
        }
    }
    pair<int, int> ret = zkwmcmf();
    if(ret.first >= m)return true;
    return false;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for(int _ = 1; _ <= test; _++) {
        std::cerr << "__" << _ << std::endl;
        scanf("%d%d%d", &n, &C, &m);

        memset(tot, 0, sizeof(tot));
        for(int i = 0; i < m; i++) {
            scanf("%d%d", &P[i], &B[i]);
            tot[B[i]]++;
        }

        int mx = 0;
        for(int i = 1; i <= C; i++) {
            mx = max(mx, tot[i]);
        }

        int l = mx - 1, r = m;
        while(l + 1 < r) {
            int mid = (l + r) / 2;
            if(judge(mid)) r = mid;
            else l = mid;
        }
        judge(r);
        printf("Case #%d: %d %d\n", _, r, cost);
    }
    return 0;
}
