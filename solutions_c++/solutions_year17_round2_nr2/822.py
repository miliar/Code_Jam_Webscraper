#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <cassert>

using namespace std;

typedef long long ll;
typedef long double ld;

const long double inf = 1e18 + 7;

const long double eps = 1e-18;

void fail(int tt) {
    cout << "Case #" << tt + 1 << ": IMPOSSIBLE\n";
}

void ok(string ans, int tt) {
    cout << "Case #" << tt + 1 << ": " << ans << "\n";
}

void update(string &str, int cnt, char V, char W) {
    if (!cnt)
        return;
    string ans;
    int i = 0;
    bool okfl = 0;
    for (; i < str.size(); ++i) {
        ans.push_back(str[i]);
        if (!okfl && str[i] == W) {
            okfl = 1;
            for (int j = 0; j < cnt; ++j)
                ans.push_back(V), ans.push_back(W);
        }
    }
    if (okfl)
        str = ans;
    else
        str = "";
} 

int main() {
ios_base::sync_with_stdio(0);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        if ((!!R) + (!!O) + (!!Y) + (!!G) + (!!B) + (!!V) == 2) {
            if (R && R != N / 2) {
                fail(tt);
                continue;
            }
            if (O && O != N / 2) {
                fail(tt);
                continue;
            }
            if (Y && Y != N / 2) {
                fail(tt);
                continue;
            }
            if (G && G != N / 2) {
                fail(tt);
                continue;
            }
            if (B && B != N / 2) {
                fail(tt);
                continue;
            }
            if (V && V != N / 2) {
                fail(tt);
                continue;
            }
            if (G)
                if (R != G) {
                    fail(tt);
                    continue;
                }
            if (V)
                if (Y != V) {
                    fail(tt);
                    continue;
                }
            if (O)
                if (B != O) {
                    fail(tt);
                    continue;
                }
            string lans;
            if (R)
                lans.push_back('R');
            if (O)
                lans.push_back('O');
            if (Y)
                lans.push_back('Y');
            if (G)
                lans.push_back('G');
            if (B)
                lans.push_back('B');
            if (V)
                lans.push_back('V');
            string ans;
            for (int i = 0; i < N / 2; ++i)
                ans = ans + lans;
            ok(ans, tt);
            continue;
        }
        R -= G;
        Y -= V;
        B -= O;
        if (R < 0 || Y < 0 || B < 0) {
            fail(tt);
            continue;
        }
        int rr = R;
        int yy = Y;
        int bb = B;
        string ans;
        char cr = 'R';
        char cb = 'B';
        char cy = 'Y';
        if (Y >= R && Y >= B) {
            cr = 'Y', cb = 'B', cy = 'R';
            swap(Y, R);
        } else 
            if (B >= R && B >= Y) {
                cr = 'B', cb = 'R', cy = 'Y';
                swap(B, R);
            }
        string buf(R, cr);
        for (int i = 0; i < Y; ++i)
            ans.push_back(buf.back()), ans.push_back(cy), buf.pop_back();
        ans = ans + buf;
        buf = ans;
        ans = "";
        for (int i = 0; i < B; ++i)
            ans.push_back(cb), ans.push_back(buf.back()), buf.pop_back();
        while (buf.size())
            ans.push_back(buf.back()), buf.pop_back();


        bool okfl = 1;
        for (int i = 0; i < ans.size(); ++i)
            if (ans[i] == ans[(i + 1) % ans.size()]) {
                fail(tt), okfl = 0;
                break;
            }
        if (!okfl)
            continue;
        for (auto x : ans) {
            if (x == 'R')
                --rr;
            if (x == 'Y')
                --yy;
            if (x == 'B')
                --bb;
        }
        if (rr != 0)
            assert(0);
        if (bb != 0)
            assert(0);
        if (yy != 0)
            assert(0);
        update(ans, G, 'G', 'R');
        update(ans, V, 'V', 'Y');
        update(ans, O, 'O', 'B');
        if (!ans.size()) {
            fail(tt);
            continue;
        }
        if (okfl) {
            ok(ans, tt);
        }
    }
    return 0;
}