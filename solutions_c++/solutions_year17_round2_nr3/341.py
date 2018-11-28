#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}

int N;
int Q;
int E[110];
int S[110];
int D[110][110];
int U[110];
int V[110];
double times[110][110];
const int INF = 1 << 30;
const double DINF = 1e+15;

void dijkstra(int d[110], int start, int limit_dist){
    for(int i = 0; i < N; i++) d[i] = INF;
    priority_queue<pii, vector<pii>, greater<pii> > pq;
    pq.push(pii(0, start));
    d[start] = 0;
    while(pq.size()){
        pii p = pq.top(); pq.pop();
        int cpos = p.second;
        int cdist = p.first;
        if(d[cpos] < cdist) continue;
        for(int npos = 0; npos < N; npos++){
            if(D[cpos][npos] == -1) continue;
            int ndist = cdist + D[cpos][npos];
            if(ndist > limit_dist) continue;
            if(d[npos] > ndist){
                d[npos] = ndist;
                pq.push(make_pair(ndist, npos));
            }
        }
    }
}

int main(){
    fastStream();
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        printf("Case #%d: ", t);
        // cout << "Case #" << t << ":";
        cin >> N >> Q;
        for(int i = 0; i < N; i++) cin >> E[i] >> S[i];
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                cin >> D[i][j];
        for(int i = 0; i < Q; i++){
            cin >> U[i] >> V[i];
            U[i]--; V[i]--;
        }
        // 最初にすべての点からの最短経路をdijkstra法で計算する
        for(int i = 0; i < N; i++){
            int d[110];
            dijkstra(d, i, E[i]);
            for(int j = 0; j < N; j++){
                if(d[j] != INF)
                    times[i][j] = 1.0 * d[j] / S[i];
                else
                    times[i][j] = DINF;
            }
        }
        // すべての点からの時間をパスとしたグラフを作成し、最短経路を計算
        for(int k = 0; k < N; k++)
            for(int i = 0; i < N; i++)
                for(int j = 0; j < N; j++)
                    times[i][j] = min(times[i][j], times[i][k] + times[k][j]);
        for(int i = 0; i < Q; i++){
            printf("%.10f", times[U[i]][V[i]]);
            if(i == Q - 1) printf("\n");
            else printf(" ");
        }
    }
    return 0;
}
