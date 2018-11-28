// Special Thanks to the Template 
#define INF 100000
// C++ implementation of Dinic's Algorithm
#include<bits/stdc++.h>
using namespace std;
char init[201][201], finale[201][201];
// A structure to represent a edge between
// two vertex
struct Edge
{
    int v ;  // Vertex v (or "to" vertex)
             // of a directed edge u-v. "From"
             // vertex u can be obtained using
             // index in adjacent array.
 
    int flow ; // flow of data in edge
 
    int C;    // capacity
 
    int rev ; // To store index of reverse
              // edge in adjacency list so that
              // we can quickly find it.
};
 
//Edge* flow[201][201];
// Residual Graph
class Graph
{
    int V, s, t; // number of vertex
    int *level ; // stores level of a node
    vector< Edge > *adj;
public :
    Graph(int V, int s, int t)
    {
        adj = new vector<Edge>[V];
        this->V = V;
        this->s = s;
        this->t = t;
        level = new int[V];
    }
 
    // add edge to the graph
    void addEdge(int u, int v, int C)
    {
        // Forward edge : 0 flow and C capacity
        Edge a{v, 0, C, adj[v].size()};
 
        // Back edge : 0 flow and 0 capacity
        Edge b{u, 0, 0, adj[u].size()};
 
        adj[u].push_back(a);
        adj[v].push_back(b); // reverse edge
        //printf("info: %d %d %d %d\n", this->s, this->t, u, V);
        //if (this->s != u && this->t !=v) flow[u][v-V/2+1]=&(*(--adj[u].end()));
    }
 
    bool BFS(int s, int t);
    int sendFlow(int s, int flow, int t, int ptr[]);
    int DinicMaxflow(int s, int t);
    void CheckFlow();
    Edge* GetRev(Edge* cur);
};
 
void Graph::CheckFlow()
{
    for (int i=1; i<V/2; i++)
    {
        vector<Edge>::iterator e;
        for (e = adj[i].begin(); e != adj[i].end(); e++)
        {
            Edge &d = *e;
            if (d.flow > 0) 
            {
                int dx=i, dy=d.v-V/2+1;
                int x=(dy-dx+V/4+1)/2, y=(dx+dy-V/4+1)/2;
                //place +
                //printf("tro \n");
                if ('.'==finale[x][y]) finale[x][y]='+';
                else finale[x][y]='o';
            }
        }
    }
}
Edge* Graph::GetRev(Edge* cur)
{
    return &adj[cur->v][cur->rev];
}
// Finds if more flow can be sent from s to t.
// Also assigns levels to nodes.
bool Graph::BFS(int s, int t)
{
    for (int i = 0 ; i < V ; i++)
        level[i] = -1;
 
    level[s] = 0;  // Level of source vertex
 
    // Create a queue, enqueue source vertex
    // and mark source vertex as visited here
    // level[] array works as visited array also.
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
                // Level of current vertex is,
                // level of parent + 1
                level[e.v] = level[u] + 1;
 
                q.push_back(e.v);
            }
        }
    }
 
    // IF we can not reach to the sink we
    // return false else true
    //printf("level: %d\n", level[t]);
    return level[t] < 0 ? false : true ;
}
 
// A DFS based function to send flow after BFS has
// figured out that there is a possible flow and
// constructed levels. This function called multiple
// times for a single call of BFS.
// flow : Current flow send by parent function call
// start[] : To keep track of next edge to be explored.
//           start[i] stores  count of edges explored
//           from i.
//  u : Current vertex
//  t : Sink
int Graph::sendFlow(int u, int flow, int t, int start[])
{
    //printf("info: %d %d %d\n", u, t, start[u]);
    // Sink reached
    if (u == t)
        return flow;
 
    // Traverse all adjacent edges one -by - one.
    for (  ; start[u] < adj[u].size(); start[u]++)
    {
        // Pick next edge from adjacency list of u
        Edge &e = adj[u][start[u]]; 
        //printf("fool %d %d %d %d\n",level[u], level[e.v], e.flow, e.C);                            
        if (level[e.v] == level[u]+1 && e.flow < e.C)
        {
            // find minimum flow from u to t
            int curr_flow = min(flow, e.C - e.flow);
            int temp_flow = sendFlow(e.v, curr_flow, t, start);
 
            // flow is greater than zero
            if (temp_flow > 0)
            {
                // add flow  to current edge
                e.flow += temp_flow;
 
                // subtract flow from reverse edge
                // of current edge
                adj[e.v][e.rev].flow -= temp_flow;
                return temp_flow;
            }
        }
    }
 
    return 0;
}
 
// Returns maximum flow in graph
int Graph::DinicMaxflow(int s, int t)
{
    // Corner case
    if (s == t)
        return -1;
 
    int total = 0;  // Initialize result
 
    // Augment the flow while there is path
    // from source to sink
    while (BFS(s, t) == true)
    {
        //printf("try\n");
        // store how many edges are visited
        // from V { 0 to V }
        int *start = new int[V+1];
        for (int i=0; i<V+1; i++) start[i]=0;
        // while flow is not zero in graph from S to D
        while (int flow = sendFlow(s, INT_MAX, t, start))
            {
                // Add path flow to overall flow
                total += flow;
            }
    }
 
    // return maximum flow
    return total;
}
bool row[201], column[201];
bool diax[201], diay[201];

// Driver program to test above functions
int main()
{
    int t;
    scanf("%d", &t);
    for (int i=0; i<t; i++)
    {
        int point=0;
        int xcount=0;
        int n, c;
        scanf("%d%d", &n, &c);
        for (int j=1; j<=n; j++)
            for (int k=1; k<=n; k++)
            {
                init[j][k]='.';
                finale[j][k]='.';
            }
        Graph g(n*4, 0, n*4-1);
        memset(row, false, sizeof(row));
        memset(column, false, sizeof(column));
        memset(diax, false, sizeof(diax));
        memset(diay, false, sizeof(diay));
        for (int j=0; j<c; j++)
        {
            char model[10];
            scanf("%s", model);
            int x, y;
            scanf("%d%d", &x, &y);
            init[x][y]=finale[x][y]=model[0];
            if ('+'==model[0]) 
            {
                point++;
                diax[y-x+n]=true;
                diay[x+y-1]=true;
            }
            if ('x'==model[0])
            {
                row[x]=true;
                column[y]=true;
                xcount++;
            }
            if ('o'==model[0])
            {
                point++;
                diax[y-x+n]=true;
                diay[x+y-1]=true;
                row[x]=true;
                column[y]=true;
                xcount++;
            }
        }
        //printf("Check Point 1\n");
        for (int j=1; j<n*2; j++)
        {
            if (!diax[j]) g.addEdge(0, j, 1);
            if (!diay[j]) g.addEdge(j+n*2-1, n*4-1, 1);
        }
        //printf("Check Point 5\n");
        for (int x=1; x<=n; x++)
        {
            for (int y=1; y<=n; y++)
            {
                g.addEdge(y-x+n, x+y-1+n*2-1, INF);
            }
        }
        //printf("Check Point 4\n");
        int delta=g.DinicMaxflow(0, n*4-1);
        //printf("Check Point 2\n");
        //printf("delta: %d\n", delta);
        point+=delta;
        point+=n;
        int place=0;
        g.CheckFlow();
        /*for (int x=1; x<=n; x++)
            for (int y=1; y<=n; y++)
            {
                
                Edge *cur=flow[y-x+n][x+y-1];
                printf("flow info: %d %d %d\n", y-x+n, cur->v, cur->flow);
                if (cur->flow>0||g.GetRev(cur)->flow>0) 
                {
                    //place +
                    printf("tro \n");
                    if ('.'==finale[x][y]) finale[x][y]='+';
                    else finale[x][y]='o';
                }
            }*/
        for (int x=1; x<=n; x++)
        {
            if (!row[x])
            {
                for (int y=1; y<=n; y++)
                {
                    if (!column[y])
                    {
                        //place x
                        if ('.'==finale[x][y]) finale[x][y]='x';
                        else finale[x][y]='o';
                        row[x]=true;
                        column[y]=true;
                        break;
                    }
                }
            }
        }
        //printf("Check Point 3\n");
        for (int x=1; x<=n; x++)
            for (int y=1; y<=n; y++)
            {
                if (init[x][y]!=finale[x][y])
                {
                    place++;
                }
            }
        printf("Case #%d: %d %d\n", i+1, point, place);
        for (int x=1; x<=n; x++)
            for (int y=1; y<=n; y++)
            {
                if (init[x][y]!=finale[x][y])
                {
                    printf("%c %d %d\n", finale[x][y], x, y);
                }
            }
    }
    return 0;
}