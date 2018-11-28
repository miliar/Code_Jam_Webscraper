#include <cstdio>
#include <cstring>

#define N 60
#define INF 0x33333333

const int MAX_N = 6000;
const int MAX_M = 1000000;
const int SIZE = MAX_N * 10;

typedef struct Edge {
    int u, v;
    int c;
    struct Edge *rev, *next;
} * edge_pointer;

int level[MAX_N], queue[SIZE];
edge_pointer head[MAX_N], edge_tail;

Edge edge[MAX_M];

int node_num, source, sink;

void init(int num_of_node);
void add_edge(int u, int v, int c);
int max_flow(int s, int t);

inline int min(int a, int b) {
    return a < b ? a : b;
}

inline int max(int a, int b) {
    return a > b ? a : b;
}

void init(int num_of_node) {
    node_num = num_of_node;
    edge_tail = edge;
    for (int i = 0; i < node_num; i++)
      head[i] = NULL;
}

void add_edge(int u, int v, int c) {
    edge_pointer edge_ptr1;
    edge_pointer edge_ptr2;

    edge_ptr1 = edge_tail++;
    edge_ptr2 = edge_tail++;

    edge_ptr1->u = u;
    edge_ptr1->v = v;
    edge_ptr1->c = c;
    edge_ptr1->rev = edge_ptr2;
    edge_ptr1->next = head[u];
    head[u] = edge_ptr1;

    edge_ptr2->u = v;
    edge_ptr2->v = u;
    edge_ptr2->c = 0;
    edge_ptr2->rev = edge_ptr1;
    edge_ptr2->next = head[v];
    head[v] = edge_ptr2;
}

bool BFS() {
    edge_pointer edge_ptr;
    int node_id, *qf, *qb;

    memset(level, 0xff, sizeof level);
    level[source] = 0;
    qf = qb = queue;
    *qb++ = source;

    while (qf < qb) {
        node_id = *qf++;
        for (edge_ptr = head[node_id]; edge_ptr != NULL; edge_ptr = edge_ptr->next)
            if (level[edge_ptr->v] == -1 && edge_ptr->c > 0) {
                level[edge_ptr->v] = level[node_id] + 1;
            if (edge_ptr->v == sink)
                return true;
            *qb++ = edge_ptr->v;
        }
    }

    return false;
}

int DFS(int node_id, int min_cap) {
    int flow;
    edge_pointer edge_ptr;

    if (node_id == sink)
        return min_cap;

    for (edge_ptr = head[node_id]; edge_ptr != NULL; edge_ptr = edge_ptr->next)
        if (edge_ptr->c > 0 && level[edge_ptr->v] == level[node_id] + 1)
            if (flow = DFS(edge_ptr->v, min(min_cap, edge_ptr->c))) {
                edge_ptr->c -= flow;
                edge_ptr->rev->c += flow;
                return flow;
            }

    level[node_id] = -1;

    return 0;
}

int max_flow(int s, int t) {
    int f, flow;

    source = s;
    sink = t;
    flow = 0;

    while (BFS())
        while (f = DFS(source, (int) INF))
            flow += f;

    return flow;
}

int same_servings(int la, int ua, int lb, int ub) {
    if (la <= lb && lb <= ua)
        return 1;
    if (la <= ub && ub <= ua)
        return 1;
    if (lb <= la && la <= ub)
        return 1;
    if (lb <= ua && ua <= ub)
        return 1;
    return 0;
}

void solve(int case_no) {
    int q[N][N], upper[N][N], lower[N][N], r[N];
    int n, p, ans, num_of_node, source, sink;

    scanf("%d%d", &n, &p);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &r[i]);
        r[i] *= 10;
    }
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= p; j++) {
            scanf("%d", &q[i][j]);
            q[i][j] *= 10;
        }

    num_of_node = n * p + 2;
    source = 0;
    sink = n * p + 1;

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= p; j++) {
            int upper_size = r[i] / 10 * 11;
            int lower_size = r[i] / 10 * 9;
            upper[i][j] = q[i][j] / lower_size;
            int upper_limit = upper[i][j] * upper_size;
            int lower_limit = upper[i][j] * lower_size;
            if (!(lower_limit <= q[i][j] && q[i][j] <= upper_limit))
                upper[i][j]--;
            lower[i][j] = q[i][j] / upper_size;
            upper_limit = lower[i][j] * upper_size;
            lower_limit = lower[i][j] * lower_size;
            if (!(lower_limit <= q[i][j] && q[i][j] <= upper_limit))
                lower[i][j]++;
        }

    init(num_of_node);
    for (int j = 1; j <= p; j++)
        if (lower[1][j] <= upper[1][j])
            add_edge(source, j, 1);

    for (int i = 2; i <= n; i++)
        for (int j = 1; j <= p; j++)
            for (int pj = 1; pj <= p; pj++) {
                if (same_servings(lower[i][j], upper[i][j], lower[i-1][pj], upper[i-1][pj]))
                    add_edge((i-2)*p+pj, (i-1)*p+j, 1);
            }

    for (int j = 1; j <= p; j++)
        if (lower[n][j] <= upper[n][j])
            add_edge((n-1)*p+j, sink, 1);

    ans = max_flow(source, sink);

    printf("Case #%d: %d\n", case_no, ans);
}

int main(int argc, char** argv) {
    int case_no, t;

    scanf("%d", &t);
    for (case_no = 1; case_no <= t; case_no++)
        solve(case_no);

    return 0;
}
