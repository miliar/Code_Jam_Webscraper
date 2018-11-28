#include <bits/stdc++.h>

using namespace std;

typedef long long li;

void solve(int test_number);

int main() {
    ios_base::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) 
        solve(i + 1);
}

const int MAXN = 110;
int hpd, ad, hpk, ak;
int buff, debuff;

int check(int deb_cnt, int buf_cnt) {
    int hpd = ::hpd, ad = ::ad, hpk = ::hpk, ak = ::ak;
    int oldhpd = hpd, oldhpk = hpk, oldad = ad, oldak = ak;
    int cur = 0; 
    while (true) {
        cur++;
        if (deb_cnt > 0) {
            int ak2 = ak;
            ak = max(0, ak - debuff);
            deb_cnt--;
            if (hpd <= ak) {
                ak = ak2;
                hpd = oldhpd;
                deb_cnt++;
            }
            hpd -= ak;
            if (hpd <= 0) {
                return 1e9;
            }
        } else if (buf_cnt > 0) {
            ad += buff;
            buf_cnt--;
            if (hpd <= ak) {
                ad -= buff;
                hpd = oldhpd;
                buf_cnt++;
            }
            hpd -= ak;
            if (hpd <= 0) {
                return 1e9;
            }
        } else {
            hpk -= ad;
            if (hpk <= 0) {
                return cur;
            }
            if (hpd <= ak) {
                hpd = oldhpd;
                hpk += ad;
            }
            hpd -= ak;
            if (hpd <= 0) {
                return 1e9;
            }

        }
        if (cur > 1000) {
            break;
        }
    }
    return 1e9;
}

void solve(int test_number) {
    cin >> hpd >> ad >> hpk >> ak >> buff >> debuff;
    int result = 1e9;

    for (int deb_cnt = 0; deb_cnt < 120; deb_cnt++) {
        for (int buf_cnt = 0; buf_cnt < 120; buf_cnt++) {
            result = min(result, check(deb_cnt, buf_cnt));
        }
    }

    cout << "Case #" << test_number << ": ";
    if (result == 1e9) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << result << endl;
    }
}
