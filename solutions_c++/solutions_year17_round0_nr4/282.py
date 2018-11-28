// Adapted from the following publicly available code:
// https://github.com/jaehyunp/stanfordacm/blob/master/code/Dinic.cc
// Adjacency list implementation of Dinic's blocking flow algorithm.
// This is very fast in practice, and only loses to push-relabel flow.
// Running time:
//     O(|V|^2 |E|) on general graphs (but much faster in practice 5000        //     nodes and 30000 edges takes 0.2 seconds on SPOJ 4110. If TLE, maybe //     shuffle edges from input randomly.
//     O(min(|V|^(2/3), |E|^(1/2))*|E|) on graphs with unit capacities       //     (again, much faster in practice)
// INPUT:
//     - graph, constructed using AddEdge()
//     - source and sink
// OUTPUT:
//     - maximum flow value
//     - To obtain actual flow values, look at edges with capacity > 0
//       (zero capacity edges are residual edges).

#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

struct Edge {
  int u, v;
  LL cap, flow;
  Edge() {}
  Edge(int u, int v, LL cap): u(u), v(v), cap(cap), flow(0) {}
};

struct Dinic {
  int N;
  vector<Edge> E;
  vector<vector<int>> g; //contains indices of edges
  vector<int> d, pt;

  Dinic(int N): N(N), E(0), g(N), d(N), pt(N) {}

  void AddEdge(int u, int v, LL cap) {
    if (u != v) {
      E.emplace_back(Edge(u, v, cap));
      g[u].emplace_back(E.size() - 1);
      E.emplace_back(Edge(v, u, 0));
      g[v].emplace_back(E.size() - 1);
    }
  }

  bool BFS(int S, int T) {
    queue<int> q({S});
    fill(d.begin(), d.end(), N + 1);
    d[S] = 0;
    while(!q.empty()) {
      int u = q.front(); q.pop();
      if (u == T) break;
      for (int k: g[u]) {
        Edge &e = E[k];
        if (e.flow < e.cap && d[e.v] > d[e.u] + 1) {
          d[e.v] = d[e.u] + 1;
          q.emplace(e.v);
        }
      }
    }
    return d[T] != N + 1;
  }

  LL DFS(int u, int T, LL flow = -1) {
    if (u == T || flow == 0) return flow;
    for (int &i = pt[u]; i < g[u].size(); ++i) {
      Edge &e = E[g[u][i]];
      Edge &oe = E[g[u][i]^1];
      if (d[e.v] == d[e.u] + 1) {
        LL amt = e.cap - e.flow;
        if (flow != -1 && amt > flow) amt = flow;
        if (LL pushed = DFS(e.v, T, amt)) {
          e.flow += pushed;
          oe.flow -= pushed;
          return pushed;
        }
      }
    }
    return 0;
  }

  LL MaxFlow(int S, int T) {
    LL total = 0;
    while (BFS(S, T)) {
      fill(pt.begin(), pt.end(), 0);
      while (LL flow = DFS(S, T))
        total += flow;
    }
    return total;
  }
};

int main()
{
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    ios::sync_with_stdio(false);
    int tc;
    cin >> tc;
    for(int case_no=1; case_no<=tc; case_no++)
    {
        cerr << "started: " << case_no << endl;

        cout << "Case #" << case_no << ": ";
        int N, M;
        cin >> N >> M;
        vector< vector<char> > field(N, vector<char>(N, '.'));
        for(int i=0; i<M; i++)
        {
            char ch;
            int tmp1, tmp2;
            cin >> ch >> tmp1 >> tmp2;
            tmp1--;
            tmp2--;
            field[tmp1][tmp2]=ch;
        }
        int nb_nodes = 2+2*2*N+2*2*(2*N-1);
        Dinic dinic(nb_nodes);
        int src=nb_nodes-2;
        int snk=nb_nodes-1;

        //cerr << "REACHED" << endl;

        vector<bool> row_allowed(N, true);
        vector<bool> col_allowed(N, true);
        vector<bool> diag1_allowed(2*N-1, true);
        vector<bool> diag2_allowed(2*N-1, true);
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
            {

                int enter_row=2*i;
                int enter_col=2*N+2*j;

                int idx_diag1=N+j-i-1;
                int idx_diag2=N+N-1-i-j-1;

                int enter_diag1=4*N+2*idx_diag1;
                int enter_diag2=8*N-2+2*idx_diag2;


                if(field[i][j]=='.')
                {
                    dinic.AddEdge(src, enter_row, 1);
                    dinic.AddEdge((enter_row^1), enter_col, 1);
                    dinic.AddEdge((enter_col^1), snk, 1);

                    dinic.AddEdge(src, enter_diag1, 1);
                    dinic.AddEdge((enter_diag1^1), enter_diag2, 1);
                    dinic.AddEdge((enter_diag2^1), snk, 1);
                }
                else if(field[i][j]=='x')
                {
                    dinic.AddEdge(src, enter_diag1, 1);
                    dinic.AddEdge((enter_diag1^1), enter_diag2, 1);
                    dinic.AddEdge((enter_diag2^1), snk, 1);

                    row_allowed[i]=false;
                    col_allowed[j]=false;
                }
                else if(field[i][j]=='+')
                {
                    dinic.AddEdge(src, enter_row, 1);
                    dinic.AddEdge((enter_row^1), enter_col, 1);
                    dinic.AddEdge((enter_col^1), snk, 1);

                    diag1_allowed[idx_diag1]=false;
                    diag2_allowed[idx_diag2]=false;
                }
                else
                {
                    row_allowed[i]=false;
                    col_allowed[j]=false;

                    diag1_allowed[idx_diag1]=false;
                    diag2_allowed[idx_diag2]=false;
                }
            }
        }


        for(int i=0; i<N; i++)
        {
            int enter_node=2*i;
            int cap=1;
            if(!row_allowed[i]) cap=0;
            dinic.AddEdge(enter_node, (enter_node^1), cap);
        }
        for(int i=0; i<N; i++)
        {
            int enter_node=2*N+2*i;
            int cap=1;
            if(!col_allowed[i]) cap=0;
            dinic.AddEdge(enter_node, (enter_node^1), cap);
        }
        for(int i=0; i<2*N-1; i++)
        {
            int enter_node=4*N+2*i;
            int cap=1;
            if(!diag1_allowed[i]) cap=0;
            dinic.AddEdge(enter_node, (enter_node^1), cap);
        }
        for(int i=0; i<2*N-1; i++)
        {
            int enter_node=8*N-2+2*i;
            int cap=1;
            if(!diag2_allowed[i]) cap=0;
            dinic.AddEdge(enter_node, (enter_node^1), cap);
        }

        // cerr << "REACHED" << endl;

        dinic.MaxFlow(src, snk);

        // cerr << "REACHED" << endl;

        vector< vector<bool> > is_plus(N, vector<bool>(N, false));
        vector< vector<bool> > is_x(N, vector<bool>(N, false));
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
            {
                if(field[i][j]=='+')
                {
                    is_plus[i][j]=true;
                }
                else if(field[i][j]=='x')
                {
                    is_x[i][j]=true;
                }
                else if(field[i][j]=='o')
                {
                    is_plus[i][j]=true;
                    is_x[i][j]=true;
                }
            }
        }

        for(int i=0; i<dinic.E.size(); i++)
        {
            int u = dinic.E[i].u;
            int v = dinic.E[i].v;
            long long cap = dinic.E[i].cap;
            long long flow = dinic.E[i].flow;
            if(cap <= 0) continue;
            if(flow <= 0) continue;
            if(0 <= u && u <= 2*N-1 && 2*N<=v && v <= 4*N-1)
            {
                /*if(case_no==4)
                {
                    cerr << "A" << endl;
                }*/
                int row = u/2;
                int col = (v-2*N)/2;
                is_x[row][col]=true;
                /*if(case_no==4)
                {
                    cerr << "B" << endl;
                }*/
            }
            else if(4*N <= u && u <= 8*N-3 && 8*N-2 <= v)
            {
                /*if(case_no==4)
                {
                    cerr << "C" << endl;
                }*/
                int idx_diag1 = (u-4*N)/2;
                int idx_diag2 = (v-(8*N-2))/2;

                /*if(case_no==4)
                {
                    cerr << idx_diag1 << " " << idx_diag2 << " " << N << endl;
                }*/

                int verschil = idx_diag2-idx_diag1;
                verschil -= N-1;
                verschil *= -1;
                int col = verschil/2;

                int som = idx_diag1+idx_diag2;
                som -= N-1;
                som /= 2;
                int row = N-1-som;

                is_plus[row][col]=true;

                /*if(case_no==4)
                {
                    cerr << "D" << endl;
                }*/
            }
        }

        long long total_score=0;
        vector< pair<char, pair<int, int> > > ans;
        vector< vector<char> > new_field(N, vector<char>(N));
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
            {
                if(is_plus[i][j] && is_x[i][j])
                {
                    new_field[i][j]='o';
                    total_score += 2;
                }
                else if(is_plus[i][j])
                {
                    new_field[i][j]='+';
                    total_score++;
                }
                else if(is_x[i][j])
                {
                    new_field[i][j]='x';
                    total_score++;
                }
                else
                {
                    new_field[i][j]='.';
                }
                if(field[i][j] != new_field[i][j])
                {
                    ans.push_back(make_pair(new_field[i][j], make_pair(i+1, j+1)));
                }
            }
        }
        cout << total_score << " " << ans.size() << endl;
        for(int i=0; i<ans.size(); i++)
        {
            cout << ans[i].first << " " << ans[i].second.first << " " << ans[i].second.second << endl;
        }
    }
    return 0;
}
