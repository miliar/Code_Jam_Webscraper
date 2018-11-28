#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <valarray>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<double, int> ii;
typedef pair<ii, int> iii;
typedef pair<ii, ii> pp;

const int CMAX = 105;
const int INF = 2e9 + 5;

vector<ii> edges[CMAX];
double dist[CMAX];


void bfs() {
    
    queue <int> Q;
    Q.push(0);
    
    while(!Q.empty()) {
        int u  = Q.front();
        Q.pop();
        
        for(int i = 0; i < edges[u].size(); i++) {
            int v = edges[u][i].second;
            double time = edges[u][i].first;
            
            if (dist[u] + time < dist[v] || dist[v] == -1) {
                dist[v] = dist[u] + time;
                Q.push(v);
            }
        }
    }
}

int main() {
    
    freopen("/Users/Lukas/Desktop/in.txt", "r", stdin);
    freopen("/Users/Lukas/Desktop/out.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, q;
        cin >> n >> q;

        ll E[CMAX], S[CMAX];
        ll D[CMAX];
        int x;
        for (int i = 0; i < n; i++) { dist[i] = -1; edges[i].clear(); }
        dist[0] = 0.0f;
        for (int i = 0; i < n; i++) cin >> E[i] >> S[i];
        for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) { cin >> x; if (j == i+1) D[i] = x; }
        for (int i = 0; i < q; i++) cin >> x >> x;
        for (int i = 0; i < n; i++) {
            ll d = 0;
            for(int j = i; j < n; j++) {
                d += D[j];
                if (d <= E[i]) edges[i].push_back(ii((double)d / (double)S[i], j+1));
                else break;
            }
        }
        bfs();
        cout << "Case #" << t << ": " << fixed << setprecision(10) << dist[n-1] << endl;
    }
    
    return 0;
}
