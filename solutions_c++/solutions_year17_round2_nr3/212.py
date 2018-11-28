#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ld, int> ldi;

int N, Q;
int E[200], S[200];
ll D[200][200];
ld K[200][200];
ld dist[200];

void solve() {
    cin >> N >> Q;
    for(int n = 0; n < N; ++n) {
        cin >> E[n] >> S[n];
    }
    for(int n = 0; n < N; ++n) {
        for(int m = 0; m < N; ++m) {
            ll x;
            cin >> x;
            if(x < 0) D[n][m] = 1LL << 60;
            else D[n][m] = x;
        }
    }
    for(int k = 0; k < N; ++k) {
        for(int n = 0; n < N; ++n) {
            for(int m = 0; m < N; ++m) {
                if(D[n][m] > D[n][k] + D[k][m]) D[n][m] = D[n][k] + D[k][m];
            }
        }
    }
    for(int n = 0; n < N; ++n) {
        for(int m = 0; m < N; ++m) {
            if(D[n][m] > E[n]) K[n][m] = 1e16;
            else K[n][m] = ld(D[n][m]) / ld(S[n]);
        }
    }
    while(Q--) {
        int U, V;
        cin >> U >> V;
        --U; --V;
        priority_queue<ldi, vector<ldi>, greater<ldi>> PQ;
        PQ.emplace(0, U);
        for(int n = 0; n < N; ++n) dist[n] = 1e16;
        dist[U] = 0;
        while(true) {
            int n = PQ.top().second;
            ld d = PQ.top().first;
            PQ.pop();
            if(dist[n] < d) continue;
            if(n == V) {
                printf("%.14f ", double(d));
                break;
            }
            //cerr << n << ' ' << d << '\n';
            for(int m = 0; m < N; ++m) {
                if(d + K[n][m] < dist[m]) {
                    PQ.emplace(dist[m] = d + K[n][m], m);
                }
            }
        }
    }
}

int main () {
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        solve();
        printf("\n");
    }
} 
 
