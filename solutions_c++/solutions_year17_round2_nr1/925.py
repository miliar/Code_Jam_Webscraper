#include <bits/stdc++.h>

using namespace std;

int D, n, k, s;

int main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int _=1; _<=T; _++){
        cout << "Case #" << _ << ": ";
        cin >> D >> n;
        double ans = 1e17;
        for(int i=1; i<=n; i++){
            cin >> k >> s;
            ans = min(ans, 1.0 * D * s / (D - k));
        }
        printf("%0.9f\n", ans);
    }
}
