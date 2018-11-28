#include<bits/stdc++.h>
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define FORD(i,b,a) for (int i=(b),_a=(a);i>=_a;i=i-1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define ALL(v) (v).begin(),(v).end()
#define fi   first
#define se   second
#define MASK(i) (1LL<<(i))
#define BIT(x,i) (((x)>>(i))&1)
#define div   ___div
#define next   ___next
#define prev   ___prev
#define left   ___left
#define right   ___right
#define __builtin_popcount __builtin_popcountll
using namespace std;
template<class X,class Y>
    void minimize(X &x,const Y &y) {
        if (x>y) x=y;
    }
template<class X,class Y>
    void maximize(X &x,const Y &y) {
        if (x<y) x=y;
    }
template<class T>
    T Abs(const T &x) {
        return (x<0?-x:x);
    }

/* Author: Van Hanh Pham */

/** END OF TEMPLATE - ACTUAL SOLUTION COMES HERE **/

class DinicFlow {
private:
    static const int INF = (int)1e9 + 7;
    int n, m;
    vector<int> dist, head, work;
    vector<int> point, flow, capa, next;

public:
    DinicFlow(int n = 0) {
        this->n = n;
        this->m = 0;
        dist.assign(n + 7, 0);
        head.assign(n + 7, -1);
        work.assign(n + 7, 0);
    }

    int addEdge(int u, int v, int c1, int c2 = 0) {
        int res = m;
        point.push_back(v); capa.push_back(c1); flow.push_back(0); next.push_back(head[u]); head[u] = m++;
        point.push_back(u); capa.push_back(c2); flow.push_back(0); next.push_back(head[v]); head[v] = m++;
        return res;
    }

    int bfs(int s, int t) {
        FOR(i, 1, n) dist[i] = -1;
        queue<int> q;
        dist[s] = 0; q.push(s);

        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int i = head[u]; i >= 0; i = next[i])
                if (dist[point[i]] < 0 && flow[i] < capa[i]) {
                    dist[point[i]] = dist[u] + 1;
                    q.push(point[i]);
                }
        }

        return dist[t] >= 0;
    }

    int dfs(int s, int t, int f = INF) {
        if (s == t) return f;
        for (int &i = work[s]; i >= 0; i = next[i])
            if (dist[point[i]] == dist[s] + 1 && flow[i] < capa[i]) {
                int d = dfs(point[i], t, min(f, capa[i] - flow[i]));
                if (d > 0) {
                    flow[i] += d;
                    flow[i ^ 1] -= d;
                    return d;
                }
            }
        return 0;
    }

    int maxFlow(int s, int t) {
        int totFlow = 0;
        while (bfs(s, t)) {
            FOR(i, 1, n) work[i] = head[i];
            while (true) {
                int d = dfs(s, t);
                if (d == 0) break;
                totFlow += d;
            }
        }
        return totFlow;
    }

    int trace(int id) const {
        return flow[id];
    }
};

#define MAX   1111

const char EMPTY = '.';
const char ROW_ONLY = 'x';
const char DIAG_ONLY = '+';
const char BOTH = 'o';

char board[MAX][MAX], newBoard[MAX][MAX];
bool markRow[MAX][MAX], markDiag[MAX][MAX];
bool row[MAX], col[MAX], addDiag[2 * MAX], subDiag[2 * MAX];
int n;
int edgeID[MAX][MAX];

int rowCase(void) {
    memset(row, false, sizeof row);
    memset(col, false, sizeof col);
    memset(markRow, false, sizeof markRow);

    int res = 0;
    FOR(i, 1, n) FOR(j, 1, n) if (board[i][j] == ROW_ONLY || board[i][j] == BOTH) {
        res++;
        row[i] = true; col[j] = true;
        markRow[i][j] = true;
    }

    DinicFlow df(2 * n + 2);
    int src = 2 * n + 1;
    int snk = 2 * n + 2;

    FOR(i, 1, n) {
        if (!row[i]) df.addEdge(src, i, 1);
        if (!col[i]) df.addEdge(n + i, snk, 1);
    }
    FOR(i, 1, n) FOR(j, 1, n) if (!markRow[i][j])
        edgeID[i][j] = df.addEdge(i, n + j, 1);

    res += df.maxFlow(src, snk);
    FOR(i, 1, n) FOR(j, 1, n) if (!markRow[i][j] && df.trace(edgeID[i][j]))
        markRow[i][j] = true;

//    printf("ROW %d\n", res);
//    FOR(i, 1, n) {
//        FOR(j, 1, n) printf("%d ", markRow[i][j] == 1);
//        printf("\n");
//    }

    return res;
}

int diagCase(void) {
    int res = 0;
    memset(addDiag, false, sizeof addDiag);
    memset(subDiag, false, sizeof subDiag);
    memset(markDiag, false, sizeof markDiag);

    FOR(i, 1, n) FOR(j, 1, n) if (board[i][j] == DIAG_ONLY || board[i][j] == BOTH) {
        res++;
        addDiag[i + j - 1] = true; subDiag[i - j + n] = true;
        markDiag[i][j] = true;
    }

    DinicFlow df(4 * n);
    int src = 4 * n - 1;
    int snk = 4 * n;

    FOR(i, 2, 2 * n) if (!addDiag[i - 1]) df.addEdge(src, i - 1, 1);
    FOR(i, 1 - n, n - 1) if (!subDiag[i + n]) df.addEdge(i + n + 2 * n - 1, snk, 1);

    FOR(i, 1, n) FOR(j, 1, n) if (!markDiag[i][j])
        edgeID[i][j] = df.addEdge(i + j - 1, i - j + n + 2 * n - 1, 1);

    res += df.maxFlow(src, snk);
    FOR(i, 1, n) FOR(j, 1, n) if (!markDiag[i][j] && df.trace(edgeID[i][j]))
        markDiag[i][j] = true;

//    printf("DIAG %d\n", res);
//    FOR(i, 1, n) {
//        FOR(j, 1, n) printf("%d ", markRow[i][j] == 1);
//        printf("\n");
//    }

    return res;
}

void process(int tc) {
    if (tc % 5 == 0) cerr << tc << endl;
    int m; scanf("%d%d", &n, &m);
    FOR(i, 1, n) FOR(j, 1, n) board[i][j] = newBoard[i][j] = EMPTY;

    REP(love, m) {
        int x, y; char s[3]; scanf("%s%d%d", s, &x, &y);
        board[x][y] = s[0];
    }

    int res = rowCase() + diagCase();
    FOR(i, 1, n) FOR(j, 1, n) {
        if (markRow[i][j]) newBoard[i][j] = markDiag[i][j] ? BOTH : ROW_ONLY;
        else newBoard[i][j] = markDiag[i][j] ? DIAG_ONLY : EMPTY;
    }

    vector<pair<int, int> > changes;
    FOR(i, 1, n) FOR(j, 1, n) if (board[i][j] != newBoard[i][j])
        changes.push_back(make_pair(i, j));

    printf("Case #%d: %d %d\n", tc, res, (int)changes.size());
    FORE(it, changes) printf("%c %d %d\n", newBoard[it->fi][it->se], it->fi, it->se);
}

int main(void) {
    int t; scanf("%d", &t);
    REP(love, t) process(love + 1);
    return 0;
}

/*** LOOK AT MY CODE. MY CODE IS AMAZING :D ***/
