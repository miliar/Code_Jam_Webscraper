// Push-Relabel implementation of the cost-scaling algorithm
// Runs in O( <max_flow> * log(V * max_edge_cost)) = O( V^3 * log(V * C))
// Operates on integers

#include<bits/stdc++.h>
using namespace std;

template<typename flow_t = int, typename cost_t = int>
struct mcFlow{
    struct Edge{
        cost_t c;
        flow_t f;
        int to, rev;
        Edge(int _to, cost_t _c, flow_t _f, int _rev):c(_c), f(_f), to(_to), rev(_rev){}
    };
    const cost_t INFCOST = numeric_limits<cost_t>::max()/2;
    const cost_t INFFLOW = numeric_limits<flow_t>::max()/2;
    cost_t epsilon;
    int N, S, T;
    vector<vector<Edge> > G;
    mcFlow(int _N, int _S, int _T):epsilon(0), N(_N), S(_S), T(_T), G(_N){}
    void add_edge(int a, int b, cost_t cost, flow_t cap){
        if(a==b){assert(cost>=0); return;}
        cost*=N;// to preserve integer-values
        epsilon = max(epsilon, abs(cost));
        assert(a>=0&&a<N&&b>=0&&b<N);
        G[a].emplace_back(b, cost, cap, G[b].size());
        G[b].emplace_back(a, -cost, 0, G[a].size()-1);
    }
    flow_t calc_max_flow(){ // Dinic max-flow
        vector<flow_t> dist(N), state(N);
        vector<Edge*> path(N);
        auto cmp = [](Edge*a, Edge*b){return a->f < b->f;};
        flow_t addFlow, retflow=0;;
        do{
            fill(dist.begin(), dist.end(), -1);
            dist[S]=0;
            auto head = state.begin(), tail = state.begin();
            for(*tail++ = S;head!=tail;++head){
                for(Edge const&e:G[*head]){
                    if(e.f && dist[e.to]==-1){
                        dist[e.to] = dist[*head]+1;
                        *tail++=e.to;
                    }
                }
            }
            addFlow = 0;
            fill(state.begin(), state.end(), 0);
            auto top = path.begin();
            Edge dummy(S, 0, INFFLOW, -1);
            *top++ = &dummy;
            while(top != path.begin()){
                int n = (*prev(top))->to;
                if(n==T){
                    auto next_top = min_element(path.begin(), top, cmp);
                    flow_t flow = (*next_top)->f;
                    while(--top!=path.begin()){
                        Edge &e=**top, &f=G[e.to][e.rev];
                        e.f-=flow;
                        f.f+=flow;
                    }
                    addFlow=1;
                    retflow+=flow;
                    top = next_top;
                    continue;
                }
                for(int &i=state[n], i_max = G[n].size(), need = dist[n]+1;;++i){
                    if(i==i_max){
                        dist[n]=-1;
                        --top;
                        break;
                    }
                    if(dist[G[n][i].to] == need && G[n][i].f){
                        *top++ = &G[n][i];
                        break;
                    }
                }
            }
        }while(addFlow);
        return retflow;
    }
    vector<flow_t> excess;
    vector<cost_t> h;
    void push(Edge &e, flow_t amt){
        //cerr << "push: " << G[e.to][e.rev].to << " -> " << e.to << " (" << e.f << "/" << e.c << ") : " << amt << "\n";
        if(e.f < amt) amt=e.f;
        e.f-=amt;
        excess[e.to]+=amt;
        G[e.to][e.rev].f+=amt;
        excess[G[e.to][e.rev].to]-=amt;
    }
    void relabel(int vertex){
        cost_t newHeight = -INFCOST;
        for(Edge const&e:G[vertex]){
            if(e.f) newHeight = max(newHeight, h[e.to] - e.c);
        }
        h[vertex] = newHeight - epsilon;
    }
    const int scale=2;
    pair<flow_t, cost_t> minCostFlow(){

        cost_t retCost = 0;
        for(int i=0;i<N;++i){
            for(Edge &e:G[i]){
                retCost += e.c*(e.f);
            }
        }
        //find feasible flow
        flow_t retFlow = calc_max_flow();

        excess.resize(N);h.resize(N);
        queue<int> q;
        vector<unsigned int> isEnqueued(N, 0), state(N);
        for(;epsilon;epsilon>>=scale){
            //refine
            fill(state.begin(), state.end(), 0);
            for(int i=0;i<N;++i)
                for(auto &e:G[i])
                    if(h[i] + e.c - h[e.to] < 0 && e.f) push(e, e.f);
            for(int i=0;i<N;++i){
                if(excess[i]>0){
                    q.push(i);
                    isEnqueued[i]=1;
                }
            }
            while(!q.empty()){
                int cur=q.front();q.pop();
                isEnqueued[cur]=0;
                // discharge
                while(excess[cur]>0){
                    if(state[cur] == G[cur].size()){
                        relabel(cur);
                        state[cur]=0;
                    }
                    for(unsigned int &i=state[cur], max_i = G[cur].size();i<max_i;++i){
                        Edge &e=G[cur][i];
                        if(h[cur] + e.c - h[e.to] < 0){
                            push(e, excess[cur]);
                            if(excess[e.to]>0 && isEnqueued[e.to]==0){
                                q.push(e.to);
                                isEnqueued[e.to]=1;
                            }
                            if(excess[cur]==0) break;
                        }
                    }
                }
            }
            if(epsilon>1 && epsilon>>scale==0){
                epsilon = 1<<scale;
            }
        }
        for(int i=0;i<N;++i){
            for(Edge &e:G[i]){
                retCost -= e.c*(e.f);
            }
        }
        //cerr << " -> " << retFlow << " / " << retCost << " bzw. " << retCost/2/N << "\n";
        return make_pair(retFlow, retCost/2/N);
    }
    flow_t getFlow(Edge const &e){
        return G[e.to][e.rev].f;
    }
};


int main()
{
    freopen("inB.txt", "r", stdin);
    freopen("outB.txt", "w", stdout);
    cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);
    int Tests; cin >> Tests;
    for(int cas=1;cas<=Tests;++cas){
        cout << "Case #" << cas << ": ";
        int N, C, M, bu, pos;
        cin >> N >> C >> M;
        vector<vector<int> > ticks(C);
        int ma_siz = 0;
        for(int i=0;i<M;++i){
            cin >> pos >> bu;
            --bu;
            ticks[bu].push_back(pos);
            ma_siz = max(ma_siz, (int)ticks[bu].size());
        }
        long long ans = -1e8;
        long long rides, cost;
        int l=ma_siz-1, r=M+1;
        while(l+1<r){
            int m = l+(r-l)/2;
            mcFlow<int, long long> fl(2*N+3, 2*N+1, 2*N+2);
            for(int i=N;i>1;--i){
                fl.add_edge(i, i-1, 0, 1e8);
            }
            for(int i=N;i>0;--i){
                fl.add_edge(N+i, fl.T, 0, m);
                fl.add_edge(i, N+i, 0, 1e8);
                fl.add_edge(N+i, i, 1, 1e8);
            }
            for(int i=0;i<C;++i){
                for(int e:ticks[i]){
                    fl.add_edge(fl.S, N+e, 0, 1);
                }
            }
            tie(rides, cost) = fl.minCostFlow();
            //cerr << m << " : " << rides << " / " << cost << "\n";
            if(rides == M){
                r=m;
                ans = cost;
            } else {
                l=m;
            }
        }
        cout << r << " " << ans;
        cerr << r << " " << ans << "\n";


        cout << "\n";
    }


    return 0;
}
