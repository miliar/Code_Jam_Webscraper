#include <iostream>
#include <vector>
#include <set>

#include <string.h>

int n, m;

const int MAXNODE = 50 + 50 * 2 + 10;
const int MAXEDGE = 50 * 50 * 2 + 10;

struct Edge {
    int to, c;
    Edge *next, *part;
} e[MAXEDGE], *head[MAXNODE];
int ne, source, end;

void init() {
    memset(head, 0, sizeof(head));
    ne = 0;
}

void add(int f, int t, int c) {
    e[ne].to = t, e[ne].c = c;
    e[ne].next = head[f];
    head[f] = e + ne ++;
}

void addedge(int f, int t, int c) {
    //std::cout << f << " " << t << " " << c << std::endl;
    e[ne].part = e + ne + 1;
    e[ne + 1].part = e + ne;
    add(f, t, c), add (t, f, 0);
}

int list[MAXNODE], d[MAXNODE];
bool bfs() {
    int l = 0, r = 1;
    list[l] = source;
    memset(d, -1, sizeof(d));
    d[source] = 0;
    while (l < r) {
        int now = list[l ++];
        for (Edge* p = head[now]; p; p = p->next) 
            if (p->c > 0 && d[p->to] == -1) {
                d[p->to] = d[now] + 1;
                list[r ++] = p->to;
            }
    }
    return d[end] != -1;
}

int dfs(int now, int now_flow) {
    if (now == end) return now_flow;
    int out = 0;
    Edge* p;
    for (p = head[now]; p; p = p->next)
        if (p->c > 0 && d[now] + 1 == d[p->to]) {
            int flow = dfs(p->to, std::min(now_flow, p->c));
            p->c -= flow, p->part->c += flow;
            now_flow -= flow, out += flow;
            if (now_flow <= 0) break;
        }
    if (!p) d[now] = -1;
    return out;
}

int dinic(int s, int e) {
    source = s, end = e;
    int res = 0, inc = 0;
    while (bfs()) 
        do {
            inc = dfs(source, 0x3f3f3f3f);
            res += inc;
        } while (inc);
    return res;
}

void solve() {
    std::cin >> n >> m;
    std::vector <int> r;
    for (int i = 0; i < n; i ++) {
        int t;
        std::cin >> t;
        r.push_back(t);
    }
    std::vector <std::vector <std::set <int> > > q;
    for (int i = 0; i < n; i++) {
        std::vector <std::set <int> > line;
        for (int j = 0; j < m; j ++) {
            int t, k = r[i];
            std::cin >> t;
            int l = 10 * t / 11 / k - 1;
            int u = 10 * t / 9 / k + 1;
            std::set <int> curr;
            for (int s = l; s <= u; s ++) {
                int min_ing = k * s * 9 / 10;
                int max_ing = k * s * 11 / 10;
                if (t >= min_ing && t <= max_ing) curr.insert(s);
            }
            line.push_back(curr);
        }
        q.push_back(line);
    }
    /*
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < m; j ++) {
            std::cout << "{";
            for (std::set <int>::iterator it = q[i][j].begin(); it != q[i][j].end(); it ++)
                std::cout << *it << ",";
            std::cout << "} ";
        }
        std::cout << std::endl;
    }
    */
    if (n == 1) {
        int ans = 0;
        for (int j = 0; j < m; j ++)
            if (q[0][j].size() > 0) ans ++;
        std::cout << ans << std::endl;
    }
    else {
        source = m * n + 2, end = m * n + 3;
        init();
        for (int i = 0; i < m; i ++)
            for (int j = 0; j < m; j ++) {
                for (std::set <int> ::iterator it = q[0][i].begin(); it != q[0][i].end(); it ++)
                    if (q[1][j].find(*it) != q[1][j].end()) {
                        addedge(i, m + j, 1);
                        break;
                    }
            }
        for (int i = 0; i < m; i ++)
            addedge(source, i, 1), addedge(m+i, end, 1);
        std::cout << dinic(source, end) << std::endl;
    }
}

int main() {
    int T;
    std::cin >> T;
    for (int i = 1; i <= T; i ++) {
        std::cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
