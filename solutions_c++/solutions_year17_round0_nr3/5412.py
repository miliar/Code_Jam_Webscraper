#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int ti = 0; ti < T; ti++) {
        int n, k;
        cin >> n >> k;

        cout << "Case #" << ti+1 << ": ";
        int a[n+2], l[n+2], r[n+2];
        for (int i=1; i<=n; i++) a[i] = 0;
        l[0] = 0; l[n+1] = 0; r[0] = 0; r[n+1] = 0;
        int idx;
        for (int i=0; i<k; i++) {
            for (int j=1; j<=n; j++) {
                if (a[j] == 1) {
                    l[j] = 0;
                } else {
                    l[j] = l[j-1]+1;
                }
            }
            for (int j=n; j>=1; j--) {
                if (a[j] == 1) {
                    r[j] = 0;
                } else {
                    r[j] = r[j+1]+1;
                }
            }
            idx = 1;
            // for (int j=1; j<=n; j++) {
            //     cout << "(" << l[j]-1 << "," << r[j]-1 << ")";
            // }
            // cout << endl;
            for (int j=1; j<=n; j++) {
                if ((l[j] == 0) && (r[j] == 0)) continue;
                if ((min(l[j], r[j]) > min(l[idx], r[idx])) ||
                ((min(l[j], r[j]) == min(l[idx], r[idx])) && (max(l[j], r[j]) > max(l[idx], r[idx])))) {
                    idx = j;
                }
            }
            a[idx] = 1;
            // cout << idx << " ";
        }
        cout << max(l[idx], r[idx])-1 << " " << min(l[idx], r[idx])-1 << endl;
        // cout << endl;
    }
}
