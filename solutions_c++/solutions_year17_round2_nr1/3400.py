#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {

    freopen("in.txt", "r", stdin);
    freopen("op.txt", "w", stdout);

    int t;
    cin >> t;
    for(int q = 0; q<t; ++q) {
        
        double d, n;
        cin >> d >> n;

        double ans = 0;
        for(int i = 0; i<n; ++i) {
            double dis, sp;
            cin >> dis >> sp;
            ans = max(ans, ((d-dis)/sp));
        }
        
        printf("Case #%d: %.6f\n", q+1, d/ans);
        //cout << "Case #" << q+1 << ": " << d/ans << endl ;
        
    }

    return 0;
}
