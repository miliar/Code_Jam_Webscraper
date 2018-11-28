#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <map>
#include <sstream>
#include <stack>
#include <cctype>
#include <bitset>
#include <queue>
using namespace std;

#define INF (1LL << 60)

typedef pair<int,int> pii;

using namespace std;

double pi = acos(-1);

struct Horse{
    int E, S;
};

vector<vector<int64_t> > dist;
vector<vector<double> > t;
vector<Horse> hs;

void floyd_warshall (){
	int64_t n = dist.size();
    for(int64_t k = 0; k < n; k++){
        for(int64_t i = 0; i < n; i++){
            for(int64_t j = 0; j < n; j++){
                if(dist[i][k] != INF && dist[k][j] != INF){
                    if(dist[i][j] > dist[i][k] + dist[k][j]){
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
    }

    //Extra loop for Infinite loop checks.
    //Alternative check dist[u][u] < 0 || dist[v][v] < 0;
//    for(int64_t i = 0; i < n; i++){
//        for(int64_t j = 0; j < n; j++){
//            for(int64_t k = 0; k < n; k++){
//                if(dist[i][k] != INF && dist[k][j] != INF && dist[k][k] < 0){
//                    dist[i][j] = -INF;
//                }
//            }
//        }
//    }
}

void time_warshall(){
    int64_t n = t.size();
    for(int64_t i = 0; i < n; i++){
        for(int64_t j = 0; j < n; j++){
            if(hs[i].E < dist[i][j] || dist[i][j] == INF) continue;
            t[i][j] = (double)dist[i][j]/(double)hs[i].S;
        }
    }

    for(int64_t k = 0; k < n; k++){
        for(int64_t i = 0; i < n; i++){
            for(int64_t j = 0; j < n; j++){
                if(dist[i][k] == INF || dist[k][j] == INF) continue;
//                if(t[i][k] == (double)INF || t[k][j] == (double)INF) continue;
//                    if(t[i][k] + t[k][j] < t[i][j]){
//                        t[i][j] = t[i][k] + t[k][i];
//                    }
                if(hs[i].E < dist[i][k] || hs[k].E < dist[k][j]) continue;
                if((double)dist[i][k] / (double)hs[i].S + (double)dist[k][j] / (double)hs[k].S < t[i][j]){
                    t[i][j] = (double)dist[i][k] / (double)hs[i].S + (double)dist[k][j] / (double)hs[k].S;
                }
//                if(hs[k].E < dist[k][j]) continue;

            }
        }
    }
}

vector<double> disti;

void dijkstra(int64_t u){
	int64_t n = dist.size();
	disti.assign(n,(double)INF);
    disti[u] = 0.0;
    priority_queue<pii> Q;
    Q.push({-disti[u],u});
    vector<bool> seen (n);

    while(!Q.empty()){
        pii p = Q.top();
        int64_t w = p.second;
        Q.pop();
        if(seen[w]) continue;
	    seen[w] = true;
	    for(int i = 0; i < n; i++){
            int to = i;
            if(t[w][to] == (double)INF) continue;

        	if(seen[to] || disti[to] <= disti[w] + t[w][to])
        		continue;

            disti[to] = disti[w] + t[w][to];
            Q.push({-disti[to],to});
        }
    }
}

int main()
{
    freopen("C-small-attempt1 (1).in","r",stdin);
    freopen("out.txt","w",stdout);
    //cout << (double) INF << endl;
    ios::sync_with_stdio(false); cin.tie(0);
    int T, cnt = 0;
    cin >> T;
    while(T--){
        cnt++;
        int N, Q;
        cin >> N >> Q;
        dist.assign(N, (vector<int64_t> (N,INF)));
        t.assign(N, (vector<double> (N,(double)INF)));
        hs.assign(N, {0,0});

        for(int i = 0; i < N; i++){
            cin >> hs[i].E >> hs[i].S;
        }

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                int D;
                cin >> D;
                if(i == j) dist[i][j] = 0;
                if(D == -1) continue;
                dist[i][j] = D;
            }
        }
        floyd_warshall();
        time_warshall();

        cout << "Case #" << cnt << ": ";// << endl;
//        for(int i = 0; i < N; i++){
//            for(int j = 0; j < N; j++){
//                if(dist[i][j] == INF) cout << "-1" << " ";
//                cout << dist[i][j] << " ";
//            }
//            cout << endl;
//        }
//        cout << "--------------Time-----------" << endl;
//        for(int i = 0; i < N; i++){
//            for(int j = 0; j < N; j++){
//                if(t[i][j] == (double)INF ) cout << -1 << "\t";
//                else cout << t[i][j] << "\t";
//            }
//            cout << endl;
//        }
        for(int i = 0; i < Q; i++){
            int U, V;

            cin >> U >> V;
            U--; V--;
//            double mini = (double) INF;
//            for(int k = 0; k < N; k++){
//                mini = min(mini,t[U][k] + t[k][V]);
//                cout << "Option " << k << " " << t[U][k] << " + " << t[k][V] << endl;
//            }
            dijkstra(U);
            cout << setprecision(10) << disti[V] << " ";
        }
        cout << endl;
    }
    return 0;
}
