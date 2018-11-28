#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <climits>
using namespace std;

void dfs(int N, vector<vector<double>> &LL, vector<vector<pair<int, int>>> &L, int s, int cur, int E, int S, double t){
    for(auto &edge : L[cur]){
        if(edge.second > E) continue;
        int remain = E - edge.second;
        double time = static_cast<double>(edge.second) / S + t;
        LL[s][edge.first] = min(LL[s][edge.first], time);
        dfs(N, LL, L, s, edge.first, remain, S, time);
    }
}

void warshall_floyd(int N, vector<vector<double>> &G) {
    for (int i = 0; i < N; i++) G[i][i] = 0.0;

    for (int k = 0; k < N; k++)
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if(G[i][k] != 1e12 && G[k][j] != 1e12)
                    G[i][j] = min(G[i][j], G[i][k] + G[k][j]);
}

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        int N, Q;
        cin >> N >> Q;
        vector<int> E(N), S(N);
        for(int i=0; i<N; i++) cin >> E[i] >> S[i];
        vector<vector<pair<int, int>>> L(N);
        for(int i=0; i<N; i++)
            for(int j=0; j<N; j++){
                int D;
                cin >> D;
                if(D != -1)
                    L[i].push_back(pair<int, int>(j, D));
            }

        cout << "Case #" << i+1 << ": ";

        vector<vector<double>> LL(N, vector<double>(N, 1e12));
        for(int i=0; i<N; i++)
            dfs(N, LL, L, i, i, E[i], S[i], 0.0);

        warshall_floyd(N, LL);

        for(int i=0; i<Q; i++){
            int U, V;
            cin >> U >> V;
            U--; V--;
            cout << fixed << setprecision(12) << LL[U][V] << " ";
        }
        cout << endl;
    }

    return 0;
}
