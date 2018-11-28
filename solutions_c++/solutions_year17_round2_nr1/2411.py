#include<bits/stdc++.h>
#define ll long long
#define M 1000000007
using namespace std;

void solve(int t) {
    ll d, n;
    cin>>d>>n;

    double mn = LONG_LONG_MAX;
    for(int i=0; i<n; i++) {
        ll k, s;
        cin>>k>>s;
        mn = min(mn, d*((double) s)/(d-k));
    }

    cout<<setprecision(10)<<"Case #"<<t<<": "<<mn<<endl;
}


int main() {

    freopen("A-small-attempt0.in", "r", stdin); freopen("output.txt", "w", stdout);

    int tc = 1;
    cin>>tc;
    
    for(int t=1; t<=tc; t++) {
        solve(t);
    }

}