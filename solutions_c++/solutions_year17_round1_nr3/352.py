#include <algorithm>
#include <iostream>

using namespace std;

constexpr int MAXROUNDS {1000};

pair<int, int> calc(int ad, int hk, int b) {
        int minr {100}, k {0};
        for (int i {0}; i <= 100; ++i) {
                int adb {ad + b * i};
                int r {(hk + adb - 1) / adb};
                if (i + r < minr)
                        minr = i + r, k = i;
        }
        return {minr, k};
}

int simulate(int debuffnum, int buffnum, int hd, int ad, int hk, int ak, int b, int d) {
        int oldhd {hd};
        int r {0};
        int c {0};
        while (r < MAXROUNDS) {
                ++r;
                if (hk > ad && hd <= ak && c >= debuffnum || hk > ad && hd <= ak - d && c < debuffnum) {
                        // cerr << "CURE" << endl;
                        hd = oldhd;
                        hd -= ak;
                        if (hd <= 0)
                                return MAXROUNDS;
                } else if (c < debuffnum) {
                        // cerr << "DEBUFF" << endl;
                        ak -= d;
                        if (ak < 0)
                                ak = 0;
                        hd -= ak;
                        if (hd <= 0)
                                return MAXROUNDS;
                        ++c;
                } else if (c < debuffnum + buffnum) {
                        // cerr << "BUFF" << endl;
                        ad += b;
                        hd -= ak;
                        if (hd <= 0)
                                return MAXROUNDS;
                        ++c;
                } else {
                        // cerr << "ATTACK" << endl;
                        hk -= ad;
                        if (hk <= 0)
                                break;
                        hd -= ak;
                        if (hd <= 0)
                                return MAXROUNDS;
                }
                // cerr << "hd = " << hd << endl;
                // cerr << "hk = " << hk << endl;
        }
        return r;
}

int main() {
        size_t casenum;
        cin >> casenum;
        for (size_t caseid {1}; caseid <= casenum; ++caseid) {
                int hd, ad, hk, ak, b, d;
                cin >> hd >> ad >> hk >> ak >> b >> d;
                auto p = calc(ad, hk, b);
                // cerr << p.first << '\t' << p.second << endl;
                int ans {MAXROUNDS};
                for (int k {0}; k <= 100; ++k) {
                        int t {simulate(k, p.second, hd, ad, hk, ak, b, d)};
                        // break;
                        if (t < ans)
                                ans = t;
                }
                cout << "Case #" << caseid << ": ";
                if (ans >= MAXROUNDS)
                        cout << "IMPOSSIBLE";
                else
                        cout << ans;
                cout << endl;
        }
        return 0;
}