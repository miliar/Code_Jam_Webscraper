#include<bits/stdc++.h>
#define ll long long
#define M 1000000007
using namespace std;

pair<ll, ll> optimal(ll n, ll k) {
    int r = 0;
    ll pw = 1;
    while(true) {
        if(k < pw) {
            break;
        }
        pw = pw*2;
        r++;
    }
    return make_pair((n-k)/pw ,  (n - (k - pw/2))/pw);
}

void solve(int t) {

    ll n, k;
    cin>>n>>k;


//*
    pair<ll, ll>x = optimal(n, k);
    cout<<"Case #"<<t<<": "<<x.second<<" "<<x.first<<endl;
    
    //*/
}


int main() {
    //A-small-attempt0 (1).in
   freopen("C-large.in", "r", stdin); freopen("output.txt", "w", stdout);

    int tc = 1;
    cin>>tc;
    
    for(int t=1; t<=tc; t++) {
        solve(t);
    }

}