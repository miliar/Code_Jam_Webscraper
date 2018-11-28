#include<bits/stdc++.h>
#define two(a) (1<<(a))
#define LINF (1ll<<61)
#define EPS (1e-14)
#define Lshift(a,b) (a<<b)
#define Rshift(a,b) (a>>b)
#define rep(a,b) for(a=0 ; a<b ; a++)
#define xrep(a,b,c) for(a=b ; a<c ; a++)
#define INF (1<<29)
#define swap(a,b) ( (a^=b) , (b^=a) , (a^=b) )
#define GET(x) (mark[x>>5]>>(x&31)&1)
#define SET(x) (mark[x>>5]|=1<<(x&31))
#define maxL (10000000>>5)+1
#define mod 1000000007
typedef long long ll;
using namespace std;

ll s[200], e[200];
ll dist[110][110];
double speed[110][110];

void solve(int t) {
    vector<double> ans;
    ll i, j, k, l, n, q;
    cin >> n >> q;
    rep(i, n) {
        cin >> e[i] >> s[i];
    }
    rep(i, n) rep(j, n) {
        cin >> dist[i][j];
    }
    rep(i, n) rep(j, n) rep(k, n) {
        if (dist[j][i] != -1 && dist[i][k] != -1 && (dist[j][i] + dist[i][k] < dist[j][k] || dist[j][k] == -1)) {
            dist[j][k] = dist[j][i] + dist[i][k];
        }
    }
    rep(i, n) rep(j, n) {
        speed[i][j] = 1e20;
    }
    rep(i, n) rep(j, n) {
        if (dist[i][j] > -1 && dist[i][j] <= e[i]) {
            double sp = dist[i][j] / double(s[i]);
            if (speed[i][j] >= sp) {
                speed[i][j] = sp;
            }
        }
    }

    rep(i, n) rep(j, n) rep(k, n) {
        if (speed[j][i] + speed[i][k] < speed[j][k]) {
            speed[j][k] = speed[j][i] + speed[i][k];
        }
    }

    cout << "Case #" << t << ":";
    rep(i, q) {
        int u, v;
        cin >> u >> v;
        u--,v--;
        printf(" %.10lf", speed[u][v]);
    }
    cout << endl;
}

int main() {
    int t, tt;
    cin >> tt;
    xrep(t, 1, tt+1) {
        solve(t);
    }
}
