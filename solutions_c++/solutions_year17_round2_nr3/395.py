#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,q;
    long long e[101], s[101];
    long long d[101][101];
    double D[101][101];
    bool c[101][101];
    cin >> n >> q;
    for(int i=1; i<=n; i++){
        cin >> e[i] >> s[i];
    }
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            cin >> d[i][j];
        }
    }
    for(int k=1; k<=n; k++){
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                if(d[i][k]!=-1 && d[k][j]!=-1){
                    long long t = d[i][k]+d[k][j];
                    d[i][j] = (d[i][j]==-1)?t:min(d[i][j],t);
                }
            }
        }
    }
    memset(D, 0, sizeof D);
    memset(c, 0, sizeof c);
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(i==j) continue;
            if(d[i][j]!=-1 && d[i][j]<=e[i]){
                D[i][j] = (double)d[i][j]/s[i];
                c[i][j] = 1;
            }
        }
    }
    for(int k=1; k<=n; k++){
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                if(c[i][k] && c[k][j]){
                    double t = D[i][k]+D[k][j];
                    D[i][j] = c[i][j]?min(D[i][j],t):t;
                    c[i][j] = 1;
                }
            }
        }
    }
    for(int i=1; i<=q; i++){
        int u,v;
        cin >> u >> v;
        printf("%.10f ",D[u][v]);
    }
}

int main(){
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int t;
    cin >> t;
    for(int c=1; c<=t; c++){
        cout << "Case #" << c << ": ";
        solve();
        cout << endl;
    }
}
