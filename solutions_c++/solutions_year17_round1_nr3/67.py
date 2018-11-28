
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int B, D;
int Hstart;
int cnt[101][101][101][101]; // Hd Ad Hk Ak
constexpr static int LOSE = 1e9;

int calc(int Hd, int Ad, int Hk, int Ak) {
    if (Hk <= 0)
        return 0;
    if (Hd <= 0)
        return LOSE;
    int& r = cnt[Hd][Ad][Hk][Ak];
    if (r != -1)
        return r;

    r = LOSE;

    // buff
    if (Ad < Hk) {
        int Adnew = min(Hk, Ad + B);
        r = min(r, calc(Hd - Ak, Adnew, Hk, Ak) + 1);
    }
    // debuff
    if (Ak > 0) {
        int Aknew = max(0, Ak - D);
        r = min(r, calc(Hd - Aknew, Ad, Hk, Aknew) + 1);
    }
    // attack
    r = min(r, calc(Hd - Ak, Ad, Hk - Ad, Ak) + 1);
    // cure
    r = min(r, calc(Hstart - Ak, Ad, Hk, Ak) + 1);

    return r;
}

string solve() {
    int Hd, Ad, Hk, Ak;
    cin >> Hd >> Ad >> Hk >> Ak;
    cin >> B >> D;
    Hstart = Hd;

    memset(cnt, -1, sizeof(cnt));
    int r = calc(Hd, Ad, Hk, Ak);
    if (r == LOSE)
        return "IMPOSSIBLE";
    return to_string(r);
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": " << solve() << endl;
    }
}
