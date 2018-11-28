#include <bits/stdc++.h>
using namespace std;

#define REPU(i, a, b) for (int i = (a); i < (b); ++i)
#define REPD(i, a, b) for (int i = (a); i > (b); --i)
#define FORE(it, a) for (auto it = a.begin(); it != a.end(); ++it)
#define MEM(a, x) memset(a, x, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) a.erase(unique(ALL(a)), a.end())

vector<string> split(const string &s, char c) {
    vector<string> v;
    stringstream ss(s);
    string x;
    while (getline(ss, x, c)) v.push_back(x);
    return v;
}

#define DEBUG(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }

void err(vector<string>::iterator it) {}

template<typename T, typename... Args>
void err(vector<string>::iterator it, T a, Args... args) {
    cerr << "[DEBUG] " << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << '\n';
    err(++it, args...);
}

typedef long long ll;
const int MOD = 1000000007;

template<class T, class U> inline T tmin(T a, U b) { return (a < b) ? a : b; }
template<class T, class U> inline T tmax(T a, U b) { return (a > b) ? a : b; }
template<class T, class U> inline void amax(T &a, U b) { if (b > a) a = b; }
template<class T, class U> inline void amin(T &a, U b) { if (b < a) a = b; }
template<class T> inline T tabs(T a) { return (a > 0) ? a : -a; }
template<class T> T gcd(T a, T b) { while (b != 0) { T c = a; a = b; b = c % b; } return a; }

const int N = 2005;
int p[N], b[N];

typedef pair<int, int> P;
const int INF = (int) 1e8;
struct E { int to, cap, cost, rev; };
int V;
vector<E> G[N];
int h[N], dist[N], prevv[N], preve[N];

void clear() {
    REPU(i, 0, N) {
        G[i].clear();
        MEM(h, 0); MEM(dist, 0); MEM(prevv, 0); MEM(preve, 0);
    }
}

void add_edge(int from, int to, int cap, int cost) {
    G[from].push_back((E) {to, cap, cost, G[to].size()});
    G[to].push_back((E) {from, 0, -cost, G[from].size() - 1});
}

int min_cost_flow(int s, int t, int f) {
    int res = 0;
    fill(h, h + V, 0);
    while (f > 0) {
        priority_queue<P, vector<P>, greater<P>> que;
        fill(dist, dist + V, INF);
        dist[s] = 0;
        que.push(P(0, s));
        while (!que.empty()) {
            P p = que.top(); que.pop();
            int v = p.second;
            if (dist[v] < p.first) continue;
            REPU(i, 0, G[v].size()) {
                E &e = G[v][i];
                if (e.cap > 0 && dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]) {
                    dist[e.to] = dist[v] + e.cost + h[v] - h[e.to];
                    prevv[e.to] = v;
                    preve[e.to] = i;
                    que.push(P(dist[e.to], e.to));
                }
            }
        }
        if (dist[t] == INF) return -1;
        REPU(v, 0, V) h[v] += dist[v];
        int d = f;
        for (int v = t; v != s; v = prevv[v]) {
            d = tmin(d, G[prevv[v]][preve[v]].cap);
        }
        f -= d;
        res += d * h[t];
        for (int v = t; v != s; v = prevv[v]) {
            E &e = G[prevv[v]][preve[v]];
            e.cap -= d;
            G[v][e.rev].cap += d;
        }
    }
    return res;
}

int main(int argc, char *argv[]) {
    ios_base::sync_with_stdio(false);

    int ntest; cin >> ntest;
    REPU(it, 1, ntest + 1) {
        int n, c, m; cin >> n >> c >> m;
        REPU(i, 0, m) cin >> p[i] >> b[i];
        int rids = 0, tics = 0;
        if (c == 2) {
            vector<int> x1, x2;
            int y1 = 0, y2 = 0;
            REPU(i, 0, m) {
                if (b[i] == 1) {
                    if (p[i] == 1) y1++;
                    else x1.push_back(p[i]);
                }
                else {
                    if (p[i] == 1) y2++;
                    else x2.push_back(p[i]);
                }
            }
            int z1 = x1.size() - y2, z2 = x2.size() - y1;
            rids = y1 + y2 + max(0, max(z2, z1));
            if (z1 > 0 || z2 > 0) {
                clear();
                if (z1 > z2) {
                    swap(z1, z2); x1.swap(x2);
                }
                int sc = x1.size() + x2.size(), sk = sc + 1;
                V = sk + 1;
                REPU(i, 0, x1.size()) add_edge(sc, i, 1, 0);
                REPU(i, 0, x2.size()) add_edge(x1.size() + i, sk, 1, 0);
                REPU(i, 0, x1.size()) REPU(j, 0, x2.size()) {
                    add_edge(i, x1.size() + j, 1, (x1[i] == x2[j] ? 1 : 0));
                }
                tics = min_cost_flow(sc, sk, z1);
            }
        }
		printf("Case #%d: %d %d\n", it, rids, tics);
    }

	return 0;
}
