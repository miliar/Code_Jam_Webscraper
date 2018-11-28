#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;
#define rep(i,n) for(ll i=0;i<(n);i++)

using namespace std;


int main(){
    int t;
    cin >> t;
    rep(times, t){
        ll d;
        int n;
        cin >> d >> n;
        vector<ll> k(n);
        vector<int> s(n);
        rep(i, n)   cin >> k[i] >> s[i];

        double ans = 0.0;

        double end = 0.0;
        rep(i, n){
            end = max(end, (d-k[i])/(double)s[i]);
        }
        ans = d/end;

        cout << fixed << setprecision(6) << "Case #" << times+1 << ": " << ans << endl;
    }

    return 0;
}
