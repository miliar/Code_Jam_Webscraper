#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <iomanip>
using namespace std;
class Edge{
    public:
        double t;
        long dest;
        Edge(double a, long b){
            t = a;
            dest = b;
        }
        bool operator<(const Edge& o) const {
           return t>o.t;
        }
};
int main() {
    ifstream in ("cjC.in");
    ofstream out ("cjC.out");
    
    long cases;
    in >> cases;
    for(long q=1; q<=cases; q++){
        long n, queries;
        in >> n >> queries;
        long long maxDist[n];
        long long speed[n];
        long long dist[n][n];
        for(long i = 0; i<n; i++){
            long long e, s;
            in >> e >> s;
            maxDist[i] = e;
            speed[i] = s;
        }
        for(long i = 0; i<n; i++){
            for(long j = 0; j<n; j++){
                long long v;
                in >> v;
                if(i==j){
                    v = -1;
                }
                if(v==-1){
                    v=2000000000LL;
                }
                dist[i][j] = v;
            }
        }
        for(long k = 0; k<n; k++){
            for(long i = 0; i<n; i++){
                for(long j = 0; j<n; j++){
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j]);
                }
            }
        }
        double answer[n][n];
        for(long i = 0; i<n; i++){
            bool v[n];
            for(long i = 0; i<n; i++){
                v[i] = false;
            }
            priority_queue<Edge> pq;
            pq.push(Edge(0.0,i));
            while(pq.size()>0){
                Edge now = pq.top();
                pq.pop();
                if(v[now.dest]){
                    continue;
                }
                v[now.dest] = true;
                answer[i][now.dest] = now.t;
                for(long j = 0; j<n; j++){
                    if(!v[j] && dist[now.dest][j]<=maxDist[now.dest]){
                        pq.push(Edge(now.t+(double)dist[now.dest][j]/(double)speed[now.dest],j));
                    }
                }
            }
        }
        out << "Case #" << q <<":";
        for(long i = 0; i<queries; i++){
            long a, b;
            in >> a >> b;
            a--;
            b--;
            out << " ";
            out << fixed << setprecision(6) << answer[a][b];
        }
        out << endl;
    }
    
    return 0;
}