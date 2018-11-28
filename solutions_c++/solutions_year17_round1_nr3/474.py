#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;


int steps(int Hd, int Ad, int Hk, int Ak, int B, int D, int b, int d) {
    int hd = Hd;
    int hk = Hk;
    int ad = Ad;
    int ak = Ak;
    int s = 0;
    while (true) {
        if (ad >= hk) {
            return s + 1;
        }
        if (d == 0 && hd <= ak) {
            hd = Hd - ak;
            s++;
            if (hd <= ak) {
                return -1;
            }
            continue;
        }
        if (d > 0) {
            if (hd <= ak - D) {
                hd = Hd - ak;
                s++;
                if (hd <= ak) {
                    return -1;
                }
                continue;
            }
            ak -= D;
            if (ak < 0) {
                ak = 0;
            }
            d--;
            hd -= ak;
            s++;
            continue;
        }
        if (b > 0) {
            ad += B;
            b--;
            hd -= ak;
            s++;
            continue;
        }
        hk -= ad;
        hd -= ak;
        s++;
    }
}

long long steps2(int Hd, int Ad, int Hk, int Ak, int B, int D, int b, int d) {
    // cerr << b << " " << d << endl;
    long long s = 0;
    int hd1 = Hd;
    int hk1 = Hk;
    int ad1 = Ad;
    int ak1 = Ak;
    for (int i = 0; i < d; i++) {
        if (hd1 <= ak1) {
            s++;
            hd1 = Hd - ak1;
        }
        ak1 -= D;
        if (ak1 < 0) {
            ak1 = 0;
        }
        hd1 -= ak1;
        s++;
    }
    if (ad1 >= hk1) {
        return s + 1;
    }
    if (hd1 <= ak1) {
        s++;
        hd1 = Hd - ak1;
    }
    for (int i = 0; i < b; i++) {
        if (hd1 <= ak1) {
            s++;
            hd1 = Hd - ak1;
        }
        ad1 += B;
        s++;
        hd1 -= ak1;
    }
    if (ad1 >= hk1) {
        return s + 1;
    }
    if (hd1 <= ak1) {
        s++;
        hd1 = Hd - ak1;
    }
    while (hk1 > 0) {
        if (ad1 >= hk1) {
            return s + 1;
        }
        if (hd1 <= ak1) {
            s++;
            hd1 = Hd - ak1;
            if (hd1 <= ak1) {
                return -1;
            }
            continue;
        }
        hk1 -= ad1;
        hd1 -= ak1;
        s++;
    }
    return s;
}

string doit() {
    int Hd, Ad, Hk, Ak, B, D;
    int b1, b2, d1, d2;
    cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
    // cout << Hd << Ad << Hk << Ak << B << D;
    /*
    if (Ad >= Hk) {
        return "1";
    }
    if (Ad + B >= Hk && Ak < Hd) {
        return "2";
    }
    if (Ad + Ad >= Hk && Ak < Hd) {
        return "2";
    }
    if ((Ak - D) * 2 >= Hd) {
        return "IMPOSSIBLE";
    }
    if (Ak - D >= Hd) {
        return "IMPOSSIBLE";
    }
    if (B == 0 || Ad >= Hk) {
        b1 = 0;
        b2 = 0;
    } else {
        b1 = 0;
        b2 = (Hk - Ad + B - 1) / B;
    }
    if (D == 0) {
        d1 = 0;
        d2 = 0;
    } else {
        d1 = 0;
        d2 = (Ak + D - 1) / D;
    }
    */
    int sBest = -1;
    // for (int b = b1; b <= b2; b++) {
        // for (int d = d1; d <= d2; d++) {
    for (int b = 0; b <= 110; b++) {
        for (int d = 0; d <= 110; d++) {
            int s = steps(Hd, Ad, Hk, Ak, B, D, b, d);
            // cerr << b << " " << d << " " << s << endl;
            if (sBest == -1 || (s >= 0 && s < sBest)) {
                sBest = s;
            }
        }
    }
    if (sBest == -1) {
        return "IMPOSSIBLE";
    }
    ostringstream ss;
    ss << sBest;
    return ss.str();
}



int main(int argc, char *argv[]) {
    int C;
    cin >> C;
    for (int i = 1; i <= C; i++) {
        string res = doit();
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}
