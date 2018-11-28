#include "bits/stdc++.h"
using namespace std;
using ll = long long;
using P = pair<ll, ll>;
const ll MOD = 1000000007;
const ll INF = 1000000000000LL;

using namespace std;

struct edge
{
    int to, cost;
    edge(int to_, int cost_) : to(to_), cost(cost_) {}
};

struct edge2 {
    int to;
    double cost;
    edge2(int to_, double cost_) : to(to_), cost(cost_) {}
};

struct State {
    int pos;
    double c;
    State(int pos_, double c_) : pos(pos_), c(c_) {}
    bool operator<(const State& right) const {
        return c > right.c;
    }
};

vector<vector<edge>> G;
vector<vector<edge2>> Gdir;
ll D[102][102];
ll E[102];
ll S[102];
ll past[102];
double dp[102];

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, Q;
        cin >> N >> Q;
        
        for(int i=0;i<N;i++)
        {
            cin >> E[i] >> S[i];
        }

        G.assign(N, vector<edge>());
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                int d;
                cin >> d;
                if(d != -1)
                {
                    G[i].emplace_back(j, d);
                }
            }
        }

        Gdir.assign(N, vector<edge2>());
        for(int i=0;i<N;i++)
        {
            for (int j = 0; j<N; j++) {
                dp[j] = INF;
                past[j] = INF;
            }
            dp[i] = 0;
            past[i] = 0;

            priority_queue<State> que;
            que.emplace(i, 0);

            while(que.size())
            {
                State s = que.top(); que.pop();
                if (dp[s.pos] < s.c) continue;
                if(s.pos != i)
                {
                    Gdir[i].emplace_back(s.pos, dp[s.pos]);
                }

                for(auto to_edge : G[s.pos])
                {
                    if (E[i] < past[s.pos] + to_edge.cost) continue;
                    double nc = s.c + double(to_edge.cost) / S[i];
                    if(dp[to_edge.to] > nc)
                    {
                        past[to_edge.to] = past[s.pos] + to_edge.cost;
                        dp[to_edge.to] = nc;
                        que.emplace(to_edge.to, nc);
                    }
                }
            }

        }
        
        printf("Case #%d: ", t);
        for(int i=0;i<Q;i++)
        {
            int U, V;
            cin >> U >> V;
            U--; V--;

            priority_queue<State> que;
            que.emplace(U, 0);

            for(int j=0;j<N;j++)
            {
                dp[j] = INF;
            }
            dp[U] = 0;

            while(que.size())
            {
                State s = que.top(); que.pop();
                if (s.pos == V) break;                
                if (dp[s.pos] < s.c) continue;
                for(edge2 to_edge : Gdir[s.pos])
                {
                    double nc = s.c + to_edge.cost;
                    if(dp[to_edge.to] > nc)
                    {
                        dp[to_edge.to] = nc;
                        que.emplace(to_edge.to, nc);
                    }
                }
            }
            if (i != 0) printf(" ");
            printf("%.8f", dp[V]);
        }
        printf("\n");
    }
    return 0;
}
