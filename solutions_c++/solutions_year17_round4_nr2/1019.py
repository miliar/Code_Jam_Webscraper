#include <bits/stdc++.h>
using namespace std;

struct edge {
  int nod, cost, cap, flow, last;
};

const int INF = 1e9 + 69 * 69;

int i, j, n, c, m, x[1005], y[1005], tata[1005], poz[1005];
int id[1005], d[1005], q[1005], qt, qh, flow, rs;
vector<edge> lda[1005];

void addEdge(int x, int y, int cap, int cost) {
  edge r1 = {y, cost, cap, 0, (int)lda[y].size()};
  edge r2 = {x, -cost, 0, 0, (int)lda[x].size()};
 
  lda[x].push_back(r1);
  lda[y].push_back(r2);
}

int update() {
  int addflow = INF;
 
  for(int x = m + 1; x; x = tata[x]) {
    int p = tata[x], pos = poz[x];
    addflow = min(addflow, lda[p][pos].cap - lda[p][pos].flow);
  }
 
  for(int x = m + 1; x; x = tata[x]) {
    int p = tata[x], pos = poz[x];
    int rev = lda[p][pos].last;
 
    lda[p][pos].flow += addflow;
    lda[x][rev].flow -= addflow;
    rs += lda[p][pos].cost;
  }
 
  return addflow;
}

void clearAll() {
  for(int i = 0; i <= 1001; ++i) lda[i].clear();
  memset(tata, 0, sizeof(tata));
  memset(poz, 0, sizeof(poz));
  memset(q, 0, sizeof(q));
  memset(d, 0, sizeof(d));
  memset(x, 0, sizeof(x));
  memset(y, 0, sizeof(y));
  memset(id, 0, sizeof(id));
  flow = rs = 0;
}

int main() {
  ifstream cin("file.in");
  ofstream cout("file.out");
  ios_base::sync_with_stdio(0);

  int test, tests;
  cin >> tests;
  for(test = 1; test <= tests; ++test) {
    cout << "Case #"<< test << ": ";

    clearAll();

    cin >> n >> c >> m;
    for(i = 1; i <= m; ++i) cin >> x[i] >> y[i];

    for(i = 1; i <= m; ++i) {
      if(y[i] == 2) {
        addEdge(i, m + 1, 1, 0);
        continue;
      }

      addEdge(0, i, 1, 0);
      for(j = 1; j <= m; ++j) {
        if(y[j] == 1) continue;
        if(x[i] != x[j]) addEdge(i, j, 1, 0);
        else if(x[i] > 1) addEdge(i, j, 1, 1);
      }
    }

    while(1) {
      for(i = 0; i <= m + 1; ++i) id[i] = 0, d[i] = INF;

      qt = qh = 0; q[qt++] = 0; d[0] = 0;
      while(qh != qt) {
        int X = q[qh++]; id[X] = 2;
        if(qh == m + 2) qh = 0;
        for(i = 0; i < (int)lda[X].size(); ++i) {
          edge &r = lda[X][i];
          if(r.flow < r.cap && d[r.nod] > d[X] + r.cost) {
            d[r.nod] = d[X] + r.cost;

            if(!id[r.nod]) {
              q[qt++] = r.nod;
              if(qt == m + 2) qt = 0;
            } else if(id[r.nod] == 2) {
              if(--qh == -1) qh = m + 1;
              q[qh] = r.nod;
            }
            id[r.nod] = 1; tata[r.nod] = X; poz[r.nod] = i;
          }
        }
      }

      if(d[m + 1] == INF) break;
      flow += update();
    }

    cout << m - flow << ' ' << rs << '\n';
  }

  return 0;
}