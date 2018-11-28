#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    int hd, ad, hk, ak, b, d;
    for (int l = 1; l <= t; l++) {
        int c = 0, e = 0;
        cin >> hd >> ad >> hk >> ak >> b >> d;
        if (ad >= hk) {
            cout << 1;
            return 0;
        }
        else if (ak - d >= hd) {
            cout << "IMPOSSIBLE";
            return 0;
        }
        else if (d == 0 && ak * 2 >= hd) {
            cout << "IMPOSSIBLE";
            return 0;
        }
        else if (b != 0) {
            while(b * hk > ad * ad + ad * b * (2 * c - 1) + (c - 1) * c * b * b) c++;
            c--;
            if (hk % (ad + c * b) != 0) c += hk / (ad + c * b) + 1;
            else c += hk / (ad + c * b);
        }
        else {
                if (hk % ad != 0) c = hk / ad + 1;
                else c = hk / ad;
        }
        while (hd < c * (ak - e * d)) e++;

        cout << "Case #" << l << ": " << e + c << "\n";
    }
    return 0;
}
