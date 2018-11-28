#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

using lli = long long int;

void docase() {
    lli N,Q;
    cin >> N >> Q;
    vector<lli> E = vector<lli>(N,0);
    vector<lli> S = vector<lli>(N,0);
    vector<vector<lli> > D = vector<vector<lli> >(N, vector<lli>(N,-1));
    vector<lli> U = vector<lli>(Q,0);
    vector<lli> V = vector<lli>(Q,0);
    for(lli i = 0; i<N; i++) {
        cin >> E[i];
        cin >> S[i];
    }
    for(lli i = 0; i<N; i++) {
        for(lli j = 0; j<N; j++) {
            cin >> D[i][j];
        }
    }
    for(lli i = 0; i<Q; i++) {
        cin >> U[i];
        cin >> V[i];
        U[i]--;
        V[i]--;
    }

    for(int k = 0; k<N; k++) {
        for(int i = 0; i<N; i++) {
            for(int j = 0; j<N; j++) {
                if(D[i][k] != -1 && D[k][j] != -1 && (D[i][j] > D[i][k] + D[k][j] || D[i][j] == -1)) {
                    D[i][j] = D[i][k] + D[k][j];
                }
            }
        }
    }


    vector<vector<long double> > G = vector<vector<long double> >(N, vector<long double>(N,-1));
    for(int i = 0; i<N; i++) {
        for(int j = 0; j<N; j++) {
            if(E[i] >= D[i][j] && D[i][j] != -1) {
                if(G[i][j] == -1) {
                    G[i][j] = (long double)D[i][j] / (long double)(S[i]);
                }
                else {
                    G[i][j] = min(G[i][j], (long double)D[i][j] / (long double)(S[i]));
                }
            }
        }
    }

    for(int k = 0; k<N; k++) {
        for(int i = 0; i<N; i++) {
            for(int j = 0; j<N; j++) {
                if(G[i][k] != -1 && G[k][j] != -1 && (G[i][j] > G[i][k] + G[k][j] || G[i][j] == -1))
                {
                    G[i][j] = G[i][k] + G[k][j];
                }
            }
        }
    }


    for(int i = 0; i<Q; i++) {
        printf("%.9Lf ", G[U[i]][V[i]]);
    }
    cout << endl;
}

int main() {
    int T;
    cin >> T;
    for(int i = 0 ; i<T; i++) {
        cout << "Case #" << i+1 << ": ";
        docase();
    }
}
