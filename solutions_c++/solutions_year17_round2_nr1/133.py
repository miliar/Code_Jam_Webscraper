#include <bits/stdc++.h>

using namespace std;

int main()
{
    #ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    int t;
    cin >> t;
    for (int cur = 0; cur < t; cur++){
        int n;
        long long d;
        cin >> d >> n;
        long long k, s;
        cin >> k >> s;
        for (int i = 1; i < n; i++){
            long long k1, s1;
            cin >> k1 >> s1;
            if ((d - k) * s1 < (d - k1) * s){
                s = s1;
                k = k1;
            }
        }
        cout << fixed << setprecision(20);
        cout << "Case #" << cur + 1 << ": " << (d * s) / (double) (d - k) << "\n";
    }
    return 0;
}
