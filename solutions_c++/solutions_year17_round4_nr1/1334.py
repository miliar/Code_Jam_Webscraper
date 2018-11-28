#include <cassert>
#include <cstring>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int tbl[101][101][101];

int rec(int p, int p1, int p2, int p3)
{
    int& ret = tbl[p1][p2][p3];

    if (ret >= 0) {
        return ret;
    }

    ret = (p1 + p2 + p3 > 0) ? 1 : 0;

    if (p == 4) {
        if (p1 >= 4) {
            ret = max(ret, 1 + rec(p, p1 - 4, p2, p3));
        }
        if (p1 >= 2 && p2 >= 1) {
            ret = max(ret, 1 + rec(p, p1 - 2, p2 - 1, p3));
        }
        if (p1 >= 1 && p3 >= 1) {
            ret = max(ret, 1 + rec(p, p1 - 1, p2, p3 - 1));
        }
        if (p2 >= 2) {
            ret = max(ret, 1 + rec(p, p1, p2 - 2, p3));
        }
        if (p2 >= 1 && p3 >= 2) {
            ret = max(ret, 1 + rec(p, p1, p2 - 1, p3 - 2));
        }
        if (p3 >= 4) {
            ret = max(ret, 1 + rec(p, p1, p2, p3 - 4));
        }
    } else {
        if (p1 >= 3) {
            ret = max(ret, 1 + rec(p, p1 - 3, p2, p3));
        }
        if (p1 >= 1 && p2 >= 1) {
            ret = max(ret, 1 + rec(p, p1 - 1, p2 - 1, p3));
        }
        if (p2 >= 3) {
            ret = max(ret, 1 + rec(p, p1, p2 - 3, p3));
        }
    }

    return ret;
}

void solve()
{
    int n, p;
    cin >> n >> p;

    vector<int> gs(n);
    for (auto& g : gs)
        cin >> g;

    map<int, int> mm;
    for (auto& g : gs) {
        mm[g % p]++;
    }

    int ans = -1;
    if (p == 2) {
        ans = mm[0] + (mm[1] + 1) / 2;
    } else if (p == 3) {
        memset(tbl, -1, sizeof(tbl));
        ans = mm[0] + rec(p, mm[1], mm[2], 0);
    } else {
        memset(tbl, -1, sizeof(tbl));
        ans = mm[0] + rec(p, mm[1], mm[2], mm[3]);
    }

    assert(ans >= 0);

    printf("%d\n", ans);
}

int main()
{
    int cases;
    cin >> cases;
    for (int i = 0; i < cases; i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}
