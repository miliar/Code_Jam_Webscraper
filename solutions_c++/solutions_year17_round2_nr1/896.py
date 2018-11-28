#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MOD = 1e9+7;
double solve(){
    double l;
    int n;
    cin >> l >> n;
    double ans = 0;
    for(int i = 0; i < n; ++i){
        double x,v;
        cin >> x >> v;
        ans = max(ans,(l-x)/v);
    }
    return l/ans;
}
int main(){
    int t;
    cin >> t;
    cout << fixed << setprecision(12);
    for(int tc = 1; tc <= t; ++tc){
        cout << "Case #" << tc << ": ";
        cout << solve() << '\n';
    }
}
