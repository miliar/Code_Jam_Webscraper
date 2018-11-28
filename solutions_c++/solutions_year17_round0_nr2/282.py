#include <bits/stdc++.h>
using namespace std;

void solve(){
    long long n, add=111111111111111111ll, ans=0;
    cin >> n;
    for(int i=0; i<20; i++){
        while(add>0 && ans%10!=9 && ans+add<=n){
            ans+=add;
        }
        add/=10;
    }
    cout << ans;
}

int main(){
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int t;
    cin >> t;
    for(int c=1; c<=t; c++){
        cout << "Case #" << c << ": ";
        solve();
        cout << endl;
    }
}
