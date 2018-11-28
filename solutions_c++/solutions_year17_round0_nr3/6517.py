#include <iostream>
#include <algorithm>
using namespace std;
bool c[10001];
pair<int,int> simulate(int n) {
    int ansl = -1;
    int ansr = -1;
    int where = 0;
    pair<int,int> p;
    for (int i=1; i<=n; i++) {
        if (c[i] == true) continue;
        int l=0, r=0;
        for (int j=i-1; j>=0; j--) {
            if (c[j]) {
                l = i-j-1;
                break;
            }
        }
        for (int j=i+1; j<=n+1; j++) {
            if (c[j]) {
                r = j-i-1;
                break;
            }
        }
        int templ = min(l, r);
        int tempr = max(l, r);
        if (ansl < templ || (ansl == templ && ansr < tempr)) {
            ansl = templ;
            ansr = templ;
            where = i;
            p = make_pair(l, r);
        }
    }
    c[where] = true;
    /*for (int i=0; i<=n+1; i++) {
        cout << (int)c[i];
    }
    cout << '\n';*/
    return p;
}
int main() {
    int t;
    cin >> t;
    for (int tc=1; tc<=t; tc++) {
        int n, k;
        cin >> n >> k;
        for (int i=0; i<=n+1; i++) {
            c[i] = false;
        }
        c[0] = c[n+1] = true;
        pair<int,int> p;
        for (int i=0; i<k; i++) {
            p = simulate(n);
        }
        int ansl = max(p.first,p.second);
        int ansr = min(p.first,p.second);
        cout << "Case #" << tc << ": " << ansl << ' ' << ansr << '\n';
    }
    return 0;
}
