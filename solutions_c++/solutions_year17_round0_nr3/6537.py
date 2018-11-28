#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, c = 0; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        int a = 0,b = 0;
        bool oc[n+2];
        fill(oc, oc+n+3, false);
        for (int i = 1; i <= k; i++) {
            int ls[n+2], rs[n+2];
            int no[n+2], po[n+2];
            po[0] = 0;
            no[n+1] = n+1;
            for (int l = 1; l <= n; l++) {
                if (oc[l]) po[l] = l;
                else po[l] = po[l-1];
            }
            for (int l = n; l >= 1; l--) {
                if (oc[l]) no[l] = l;
                else no[l] = no[l+1];
            }
            for (int l = 1; l <= n; l++) {
                    ls[l] = abs(l-po[l])-1;
                    rs[l] = abs(l-no[l])-1;
            }
            // for (int l = 1; l <= n; l++) {
                // cout << po[l] << " ";
            // }
            // cout << endl;
            // for (int l = 1; l <= n; l++) {
                // cout << no[l] << " ";
            // }
            // cout << endl;
            // cout << endl;
            
            int mx = -1, mn = -1, idx = -1;
            for (int l = 1; l <= n; l++) {
                if (mn < min(ls[l],rs[l])) {
                    idx = l;
                    mn = min(ls[l],rs[l]);
                } else if (mn == min(ls[l],rs[l])) {
                    if (mx < max(ls[l],rs[l])) {
                        idx = l;
                        mx = max(ls[l],rs[l]);
                    }
                }
            } 
            oc[idx] = true;
            a = max(ls[idx],rs[idx]);
            b = min(ls[idx],rs[idx]);
        }
        cout << "Case #" << ++c << ": ";
        cout << a << " " << b << endl;
    }
}