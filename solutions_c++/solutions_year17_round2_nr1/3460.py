#include <bits/stdc++.h>

using namespace std;

int main(){
    long long i,j,k,l,m,n,test,t, p, s,d ;
    cin >> test;
    for (t = 0; t < test; t++){
        cin >> d >> n;
        cout << "Case #" << t + 1 << ": ";
        double ans = 1000000000000000;
        for (i = 0; i < n; i++){
            cin >> k >> s;
            double cur = 1.0 * d / ( 1.0 * (d - k) / s);
            if (ans > cur) ans = cur;
        }           
        cout.precision(8);
        cout << fixed << ans << "\n";
    }
    return 0;
}
