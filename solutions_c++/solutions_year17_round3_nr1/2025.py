#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <climits>
#include <unordered_map>
#include <iomanip>

using namespace std;
using ll = long long;

vector< pair<ll, ll> > P;
vector< vector< vector<ll> > > S;
ll K, N;

ll surface(vector<ll>& sel) {
    ll s = 0;
    ll largestIndex = 0;
    for( ll i = 0; i < sel.size(); ++i ) {
        if( sel[i] == 1 ) {
            s += 2 * P[i].first * P[i].second;
            largestIndex = i;
        }
    }
    s += P[largestIndex].first * P[largestIndex].first;
    return s;
}

vector<ll> improveSelection(vector<ll> sel, ll n) {
    ll currentSurface = surface(sel);
    ll bestSurface = currentSurface;
    ll bestIndex = 0;
    for (ll i = 0; i <= n; ++i) {
        if (sel[i] == 0) {
            sel[i] = 1;
            if (surface(sel) > bestSurface) {
                bestSurface = surface(sel);
                bestIndex = i;
            }
            sel[i] = 0;
        }
    }
    sel[bestIndex] = 1;
    return sel;
} 

void solve() {
    S = vector< vector< vector<ll> > >(N, vector< vector<ll> >(K, vector<ll>(N)));

    vector<ll> empty(N);
    for( ll n = 0; n < N; ++n ) {
        S[n][0] = improveSelection(empty, n);
    }
    
    for (ll k = 1; k < K; ++k) {
        for (ll n = 0; n < N; ++n) {
            S[n][k] = improveSelection(S[n][k-1], n);
        }
    }
}

int main()
{
    ll T;
    cin >> T;

    for( ll t = 1; t <= T; t++ )
    {
        cout << "Case #" << t << ": ";

        cin >> N >> K;

        P = vector< pair<ll,ll> >(N);
        for( ll i = 0; i < N; ++i ) {
            ll r,h;
            cin >> r >> h;
            P[i] = make_pair(r,h);
        }
        sort(P.begin(), P.end());

        solve();

        cout << setprecision(20) << M_PI * surface(S[N-1][K-1]);

        cout << endl;
    }

    return 0;
}
