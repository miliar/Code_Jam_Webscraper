#include <bits/stdc++.h>
using namespace std;
#define int long long
#define all(x) ((x).begin(), (x).end())
#define pb push_back

typedef pair<int, int> ii;
typedef long double LD;

const int N = 105;
int g[N][N];
LD g2[N][N];
int E[N], S[N];

void solve(int tn){
    cout << "Case #" << tn << ": ";
    int n, q;
    cin >> n >> q;

    for(int i = 0; i < n; i++){
        cin >> E[i] >> S[i];
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> g[i][j];
            if(g[i][j] == -1) g[i][j] = 1e16;
            if(i == j) g[i][j] = 0;
        }
    }

    for(int k = 0; k < n; k++){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
            }
        }
    }

    

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(g[i][j] <= E[i])
                g2[i][j] = 1.L*g[i][j]/S[i];
            else
                g2[i][j] = 1e16;
        }
    }
    
    for(int k = 0; k < n; k++){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                g2[i][j] = min(g2[i][j], g2[i][k] + g2[k][j]);
            }
        }
    }
    for(int i = 0; i < q; i++){
        int s, t;
        cin >> s >> t;
        s--, t--;

        cout << g2[s][t] << " ";
    }

    cout << endl;
}

int32_t main(){
    cout << fixed << setprecision(11);  
        int T;
    cin >> T;
    for(int i = 1; i <= T; i++)
        solve(i);
}
