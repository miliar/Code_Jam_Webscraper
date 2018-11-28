#include <bits/stdc++.h>

using namespace std;

const int oo = 1e9;

int main() {
    ifstream cin ("C-small-attempt4.in");
    ofstream cout ("dragon.out");
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int test;
    cin >> test;
    for (int ttest = 1; ttest <= test; ttest++) {
        cout << "Case #" << ttest << ": ";

        int hd, ad, hk, ak, b, d;
        cin >> hd >> ad >> hk >> ak >> b >> d;
        int maxBuff = 0;
        if (b != 0)
            while (ad + maxBuff * b < hk) maxBuff++;
        int maxDebuff = 0;
        if (d != 0)
            while (ak - maxDebuff * d > 0) maxDebuff++;

        int ans = oo;
        if (ad >= hk) ans = 1;
        for (int i = 0; i <= maxBuff; i++) {
            for (int j = 0; j <= maxDebuff; j++) {
                bool possible = true;
                int cnt = 0;
                int curHd = hd;
                int curHk = hk;
                int cntBuff = i;
                int cntDebuff = j;
                int curAd = ad;
                int curAk = ak;

                while (curHk > 0) {
                    cnt++;
                    if (curAd >= curHk) break;

                    if (curHd <= curAk) {
                        if (cntDebuff > 0 && curAk - d < curHd) {
                            cntDebuff--;
                            curAk -= d;
                            if (curAk < 0) curAk = 0;
                            curHd -= curAk;
                            continue;
                        } else {
                            curHd = hd - curAk;
                            if (curHd <= curAk) {
                                possible = false;
                                break;
                            }
                            continue;
                        }
                    } else if (cntDebuff > 0) {
                        cntDebuff--;
                        curAk -= d;
                        if (curAk < 0) curAk = 0;
                        curHd -= curAk;
                        continue;
                    } else if (cntBuff > 0) {
                        cntBuff--;
                        curAd += b;
                        curHd -= curAk;
                        continue;
                    } else {
                        curHk -= curAd;
                        if (curHk <= 0) break;
                        curHd -= curAk;
                    }
                }

                if (possible) ans = min(ans, cnt);
            }
        }

        if (ans == oo) cout << "IMPOSSIBLE\n";
        else cout << ans << "\n";
    }
}

