#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF = 1e18, N = 101;
ll dist[N][N], maxdist[N];
double horse[N][N], speed[N];
double solve(){
    for(int i = 0; i < N; ++i)
        for(int j = 0; j < N; ++j){
            dist[i][j] = INF;
            horse[i][j] = INF;
        }
    int n,q;
    cin >> n >> q;
    for(int i = 1; i <= n; ++i){
        cin >> maxdist[i] >> speed[i];
    }
    for(int i = 1; i <= n; ++i){
        for(int j = 1; j <= n; ++j){
            cin >> dist[i][j];
            if(dist[i][j] == -1)
                dist[i][j] = INF;
        }
        dist[i][i] = 0;
        horse[i][i] = 0;
    }
    for(int k = 1; k <= n; ++k)
        for(int i = 1; i <= n; ++i)
            for(int j = 1; j <= n; ++j)
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j]);
    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= n; ++j){
            if(maxdist[i] >= dist[i][j])
                horse[i][j] = min(horse[i][j],dist[i][j]/speed[i]);
        }
    for(int k = 1; k <= n; ++k)
        for(int i = 1; i <= n; ++i)
            for(int j = 1; j <= n; ++j)
                horse[i][j] = min(horse[i][j],horse[i][k]+horse[k][j]);
    //for(int t = 0; t < 100; ++t)
    //cout << '\n';
    //for(int i = 1; i <= n; ++i){
        //for(int j = 1; j <= n; ++j)
            //cout << horse[i][j] << ' ';
        //cout << '\n';
    //}
    //cout << (dist[3][4] <= maxdist[3]) << '\n';
    //cout << dist[3][4] << ' ' << speed[3] << '\n';
    //cout << horse[3][4] << '\n';
    //cout << horse[4][1] << '\n';
    for(int i = 0; i < q; ++i){
        int u,v;
        cin >> u >> v;
        cout << horse[u][v] << ' ';
    }
    cout << '\n';
}
int main(){
    int t;
    cin >> t;
    cout << fixed << setprecision(12);
    for(int tc = 1; tc <= t; ++tc){
        cout << "Case #" << tc << ": ";
        solve();
    }
}
