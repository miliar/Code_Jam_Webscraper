#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
#define ll long long
//#define sort(A) sort(A.begin(),A.end())
//#define rsort(A) sort(A.rbegin(),A.rend())
using namespace std;
static const ll D = 1000000007;
static const double PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;

bool ord(pair<ll, ll> a, pair<ll, ll> b){
    return a.first*a.second < b.first*b.second;
}

int main() {
    ll T, n, k, r, h;
    cin >> T;
    for(ll t = 0; t<T; ++t){
        cin >> n >> k;
        vector<pair<ll, ll> > Y(n);
        vector<pair<pair<ll, ll>, ll> > X(n);
        for(ll i = 0; i<n; ++i){
            cin >> r >> h;
            Y[i] = make_pair(r,h);
        }
        sort(Y.rbegin(), Y.rend(), ord);
        for(ll i = 0; i<n; ++i){
            X[i] = make_pair(Y[i], i);
        }
        sort(X.rbegin(), X.rend());
        ll maxi = 0;
        for(ll i = 0; i<n-k+1; ++i){
            ll val = X[i].first.first*X[i].first.first + 2*X[i].first.first*X[i].first.second;
            Y.erase(Y.begin()+X[i].second);
            for(ll j = 0; j<k-1; ++j){
                val += 2*Y[j].first*Y[j].second;
            }
            maxi = max(maxi, val);
        }
        cout << "Case #" << t+1 << ": " << fixed << setprecision(6) << maxi*PI << endl;
    }
    return 0;
}
