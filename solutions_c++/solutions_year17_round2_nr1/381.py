#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    long long d;
    long long k[1001],s[1001];
    long double time = 0;
    cin >> d >> n;
    for(int i=1; i<=n; i++){
        cin >> k[i] >> s[i];
        time = max(time,(long double)(d-k[i])/s[i]);
    }
    printf("%.10f",(double)d/(double)time);
}

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t;
    cin >> t;
    for(int c=1; c<=t; c++){
        cout << "Case #" << c << ": ";
        solve();
        cout << endl;
    }
}
