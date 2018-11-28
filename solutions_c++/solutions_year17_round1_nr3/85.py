#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long LL;
typedef pair<int, int> PII;

const LL INF = int(1e9);
const LL INF64 = LL(4e18);

int test, testCount;
LL hp, a, ehp, ea, buff, debuff;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &testCount);
    for (int test = 1; test <= testCount; ++test) {
        printf("Case #%d: ", test);
        cin >> hp >> a >> ehp >> ea >> buff >> debuff;
        LL x = 0;
        LL need = -1;
        while (true) {
            LL wasa = a + buff * x;
            LL was = x + (ehp + wasa - 1) / wasa;
            LL nowa = a + buff * (x + 1);
            LL now = x + 1 + (ehp + nowa - 1) / nowa;
            if (now > was) {
                need = was;
                break;
            }
            ++x;
        }
        if (need == 1) {
            cout << 1 << endl;
            cerr << "done " << test << endl;
            continue;
        }
        LL ans = INF64;
        LL remh = hp;
        LL steps = 0;
        for (LL x = 0; ; ++x) {
            LL nowa = max(0ll, ea - x * debuff);
            if (nowa == 0) {
                ans = min(ans, steps + need);
                break;
            }
            if (2 * nowa >= hp) {
                if (need == 2 && nowa < remh) {
                    ans = min(ans, steps + 2);
                }
            } else {
                LL can = (remh - 1) / nowa;
                if (can + 1 >= need) {
                    ans = min(ans, steps + need);
                } else {
                    LL rem = need - can;
                    LL curSteps = steps + can + 1;
                    can = (hp - nowa - 1) / nowa;
                    assert(can > 0);
                    curSteps += rem;
                    curSteps += (rem + can - 1) / can - 1;
                    if (rem % can == 1 || (can == 1 && rem > 1)) {
                        --curSteps;
                    }
                    ans = min(ans, curSteps);
                }
            }
            if (debuff == 0) {
                break;
            }
            if (remh > ea - (x + 1) * debuff) {
                remh -= ea - (x + 1) * debuff;
                ++steps;
            } else {
                steps += 2;
                remh = hp - (ea - x * debuff);
                remh -= ea - (x + 1) * debuff;
                if (remh <= 0) {
                    break;
                }
            }
        }
        if (ans == INF64) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << '\n';
        }
        cerr << "done " << test << endl;
    }
    return 0;
}
