#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int N = 1100;
int t, cas = 1;
ll n, k;

void solve(){
    ll y=1;
    while(y <= k){
        y <<= 1;
    }
    y /= 2;
    //cout << "y:" << y << endl;
    ll a = n / y;
    ll b = k - y + 1;
    ll x = y - (a * y - n + y - 1);
    //cout << "##:" << a << " " << b << " " << x << endl;

    if(a & 1){
        if(b <= x) cout  << a/2 << " " << a/2 << endl;
        else cout  << a/2 << " " << a/2 - 1<< endl;
    }else{
        if(b <= x) cout  << a/2 << " " << a/2 - 1<< endl;
        else cout  << a/2 - 1 << " " << a/2 - 1 << endl;
    }
}

int main(){
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    while(t--){
        cin >> n >> k;
        printf("Case #%d: ", cas++);
        solve();
    }
	return 0;
}

