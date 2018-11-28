#include <bits/stdc++.h>
using namespace std;

#define pii pair<int, int>
#define mp make_pair
#define loop(i,n) for (int i=0; i<n; i++)
#define pb push_back
#define ll long long
#define vi vector<int>

int main () {
    ios_base::sync_with_stdio(false);
    int tests;
    cin>>tests;
    for(int test=1; test<=tests; test++) {
        cout<<"Case #"<<test<<": ";
        ll n, k;
        cin>>n>>k;
        map<ll, ll> M;
        M[n] = 1;
        while (true) {
            map<ll, ll>::iterator it = M.end();
            it--;
            ll val = it->first;
            ll cnt = it->second;
            M.erase(it);
            k -= cnt;
            if (val % 2) {
                if (val / 2 > 0) M[val / 2] += cnt * 2;
                if (k <= 0) {
                    cout<<val / 2<<" "<<val / 2<<endl;
                    break;
                }
            }
            else {
                if (val / 2 > 0) M[val / 2] += cnt;
                if (val / 2 - 1 > 0) M[val / 2 - 1] += cnt;
                if (k <= 0) {
                    cout<<val / 2<<" "<<val / 2 - 1<<endl;
                    break;
                }
            }
        }
    }
    return 0;
}