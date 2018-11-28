//Mitesh Agrawal
#include <bits/stdc++.h>
using namespace std;

#define ii pair<int,int>
#define ff first
#define ss second

int n,p;
int R[55];
int Q[55][55];
vector<ii> ans[55];
int solver[10][10];

void fill(int a, int b){
    int lo,hi;
    lo = ceil(1.0*Q[a][b]/(1.1*R[a]));
    hi = 10*Q[a][b]/(9*R[a]);
    if(lo<=hi){
        ans[a].push_back(ii(lo,hi));
    }
}


struct Edge
{int v,flow,C,rev;};
 
class Graph{
    int V; 
    int *level ; 
    vector< Edge > *adj;
public :
    Graph(int V)
    {
        adj = new vector<Edge>[V];
        this->V = V;
        level = new int[V];
    }
 
    void addEdge(int u, int v, int C)
    {
        Edge a = {v, 0, C, (int)adj[v].size()};
 
        Edge b = {u, 0, 0, (int)adj[u].size()};
 
        adj[u].push_back(a);
        adj[v].push_back(b); 
    }
 
    bool BFS(int s, int t);
    int sendFlow(int s, int flow, int t, int ptr[]);
    int DinicMaxflow(int s, int t);
};
 
bool Graph::BFS(int s, int t){
    for (int i = 0 ; i < V ; i++)
        level[i] = -1;
 
    level[s] = 0;  
 
    list< int > q;
    q.push_back(s);
 
    vector<Edge>::iterator i ;
    while (!q.empty())
    {
        int u = q.front();
        q.pop_front();
        for (i = adj[u].begin(); i != adj[u].end(); i++)
        {
            Edge &e = *i;
            if (level[e.v] < 0  && e.flow < e.C)
            {
                level[e.v] = level[u] + 1;
 
                q.push_back(e.v);
            }
        }
    }
 
    return level[t] < 0 ? false : true ;
}
 
int Graph::sendFlow(int u, int flow, int t, int start[]){
    if (u == t)
        return flow;
 
    for (  ; start[u] < adj[u].size(); start[u]++)
    {
        Edge &e = adj[u][start[u]]; 
                                     
        if (level[e.v] == level[u]+1 && e.flow < e.C)
        {
            int curr_flow = min(flow, e.C - e.flow);
 
            int temp_flow = sendFlow(e.v, curr_flow, t, start);
 
            if (temp_flow > 0)
            {
                e.flow += temp_flow;
 
                adj[e.v][e.rev].flow -= temp_flow;
                return temp_flow;
            }
        }
    }
 
    return 0;
}
 
int Graph::DinicMaxflow(int s, int t){
    if (s == t)
        return -1;
    int total = 0;  

    while (BFS(s, t) == true)
    {
        int *start = new int[V+1];
 
        while (int flow = sendFlow(s, INT_MAX, t, start))
 
            total += flow;
    }
 
    return total;
}

int main(){
    freopen ("B-small-attempt1.in","r",stdin); 
    // freopen ("B-small-attempt0.out","w",stdout); 
    int i,j,t,test,temp;
    scanf("%d",&t);
    for(test=1;test<=t;test++){
        printf("Case #%d: ",test);
        scanf("%d %d",&n,&p);
        for(i=0;i<n;i++)
            scanf("%d",&R[i]);
        for(i=0;i<n;i++){
            ans[i].clear();
            for(j=0;j<p;j++){
                scanf("%d",&Q[i][j]);
                fill(i,j);
            }
        }
        // for(i=0;i<n;i++){
        //     for(j=0;j<ans[i].size();j++){
        //         printf("%d %d %d\n",i,ans[i][j].ff,ans[i][j].ss);
        //     }
        //     printf("\n");
        // }
        if(n==1){
            printf("%lu\n",ans[0].size());
            continue;
        }
        // printf("making size %d\n",ans[0].size(),ans[1].size()+2);
        Graph g(ans[0].size() + ans[1].size() + 2);
        for(i=0;i<ans[0].size();i++){
            // printf("%d %d\n",0,i+1);
            g.addEdge(0,1+i,1);
        }
        for(i=0;i<ans[1].size();i++){
            // printf("%d %d\n",ans[0].size()+i+1,ans[0].size() + ans[1].size() + 1);
            g.addEdge(ans[0].size()+i+1 ,ans[0].size() + ans[1].size() + 1,1);
        }


        for(i=0;i<ans[0].size();i++){
            for(j=0;j<ans[1].size();j++){
                if(max(ans[0][i].ff,ans[1][j].ff)<=min(ans[0][i].ss,ans[1][j].ss)){
                    // printf("%d %d\n", i+1,ans[0].size()+j+1);
                    g.addEdge(i+1,ans[0].size()+j+1,1);
                }
                else{
                    g.addEdge(i+1,ans[0].size()+j+1,0);
                }
            }
        }
        printf("%d\n",g.DinicMaxflow(0,ans[0].size() + ans[1].size() + 1));
    }


    return 0;
}