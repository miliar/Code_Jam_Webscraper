#include <bits/stdc++.h>

using namespace std;

int main(){
    int t, cases = 1;
    cin >> t;
    cout.precision(6);
    while (t--){
        double d;
        int n;
        cin >> d >> n;
        double x = LONG_LONG_MAX;
        for (int i = 0; i < n; i++){
            double k, s;
            cin >> k >> s;
            x = min(x, s*d / (d-k));
        }
        cout << fixed << "Case #" << cases++ << ": " << x << endl;
    }
    return 0;
}
