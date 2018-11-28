#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <deque>
#include <iomanip>
using namespace std;
class Edge{
    public:
        long dest, revInd, cap, flow;
        Edge(long a, long b, long c){
            dest = a;
            revInd = b;
            cap = c;
            flow = 0;
        }
};
class Flow{
    public:
        vector<vector<Edge> > graph;
        vector<vector<Edge> > copy;
        Flow(long nodes){
            graph.resize(nodes);
        }
        void add(long s, long t, long cap){
            graph[s].push_back(Edge(t,graph[t].size(),cap));
            graph[t].push_back(Edge(s,graph[s].size()-1,0));
        }
        bool bfs(long src, long dest, long dist[]){
            for(long i = 0; i<copy.size(); i++){
                dist[i] = -1;
            }
            dist[src] = 0;
            long q[copy.size()];
            for(long i = 0; i<copy.size(); i++){
                q[i] = 0;
            }
            long pointer = 0;
            q[pointer++] = src;
            for(long i = 0; i<pointer; i++){
                long now = q[i];
                for(long j = 0; j<copy[now].size(); j++){
                    Edge e = copy[now][j];
                    if(dist[e.dest]<0 && e.flow<e.cap){
                        dist[e.dest] = dist[now]+1;
                        q[pointer++] = e.dest;
                    }
                }
            }
            return dist[dest] >=0;
        }
        int dfs(long pointer[], long dist[], long dest, long now, long flow){
            if(now==dest){
                return flow;
            }
            for(; pointer[now] < copy[now].size(); pointer[now]++){
                Edge e = copy[now][pointer[now]];
                if(dist[e.dest]==dist[now]+1 && e.flow<e.cap){
                    long added = dfs(pointer, dist, dest, e.dest, min(flow,e.cap-e.flow));
                    if(added>0){
                        copy[now][pointer[now]].flow += added;
                        copy[e.dest][e.revInd].flow -= added;
                        return added;
                    }
                }
            }
            return 0;
        }
        void copyGraph(){
            copy.resize(graph.size());
            for(long i = 0; i<graph.size(); i++){
                for(long j = 0; j<graph[i].size(); j++){
                    Edge e = graph[i][j];
                    copy[i].push_back(Edge(e.dest,e.revInd,e.cap));
                }
            }
        }
        long maxFlow(long src, long dest){
            copyGraph();
            long flow = 0;
            long dist[copy.size()];
            for(long i = 0; i<copy.size(); i++){
                dist[i] = 0;
            }
            while(bfs(src, dest, dist)){
                long pointer[copy.size()];
                for(long i = 0; i<copy.size(); i++){
                    pointer[i] = 0;
                }
                while(true){
                    long added = dfs(pointer, dist, dest, src, 2147483647L);
                    if(added==0){
                        break;
                    }
                    flow+=added;
                }
            }
            return flow;
        }
};
int main() {
    ifstream in ("cjB17.in");
    ofstream out ("cjB17.out");
    long cases;
    in >> cases;
    for(long q=1; q<=cases; q++){
        long n, c, m;
        in >> c >> n >> m;
        long edges[2][m];
        for(long i = 0; i<m; i++){
            for(long j = 0; j<2; j++){
                in >> edges[j][i];
                edges[j][i]--;
            }
        }
        // cout << "A" << endl;
        //position, buyer
        long low = 1; 
        long high = m;
        while(low<high){
            long mid = (low+high)/2;
            Flow f = Flow(n+c+2);
            for(long i = 0; i<n; i++){
                f.add(0,2+i,mid);
            }
            for(long i = 0; i<c; i++){
                f.add(2+n+i,1,mid);
            }
            for(long i = 1; i<c; i++){
                f.add(n+i+2,n+i+1,m);
            }
            for(long i = 0; i<m; i++){
                f.add(2+edges[1][i],2+n+edges[0][i],1);
            }
            if(f.maxFlow(0,1)==m){
                // cout << "YES" << mid << endl;
                high = mid;
            }
            else{
                // cout << "NO" << mid << endl;
                low = mid+1;
            }
        }
        long ans = low;
        Flow f = Flow(n+c+2);
        for(long i = 0; i<n; i++){
            f.add(0,2+i,ans);
        }
        for(long i = 0; i<c; i++){
            f.add(2+n+i,1,ans);
        }
        for(long i = 0; i<m; i++){
            f.add(2+edges[1][i],2+n+edges[0][i],1);
        }
        long promo = m-f.maxFlow(0,1);
        out << "Case #" << q << ": " << ans << " " << promo << endl;
    }
    out.close();
    return 0;
}