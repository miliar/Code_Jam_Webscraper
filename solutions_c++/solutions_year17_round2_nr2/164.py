#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define INF 1e+9
#define mp make_pair
#define pb push_back
#define fi first
#define fs first
#define se second
#define i64 long long
#define li long long
#define lint long long
#define pii pair<int, int>
#define vi vector<int>

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)

const char symb[3] = {'R', 'Y', 'B'};
int cnt[3];
string ans;
int n, R, O, Y, G, B, V;
bool was[3];

void add(int num) {
    ans += symb[num];
    if (!was[num]) {
        was[num] = true;
        if (symb[num] == 'R') {
            forn(j, G)
                ans += "GR";
        }
        if (symb[num] == 'Y') {
            forn(j, V)
                ans += "VY";
        }
        if (symb[num] == 'B') {
            forn(j, O)
                ans += "OB";
        }
    }
}

set <pair<char, char>> banned;

void check_pair(char c1, char c2) {
    assert(banned.find(mp(c1, c2)) == banned.end());
}

int R1, B1, Y1;

void ass() {
    cerr << "check!" << endl;
    forn(pos, (int)ans.length() - 1) {
        check_pair(ans[pos], ans[pos + 1]);
        check_pair(ans[pos + 1], ans[pos]);
    }
    int RR = 0;
    int OO = 0;
    int YY = 0;
    int GG = 0;
    int BB = 0;
    int VV = 0;
    check_pair(ans[0], ans[(int)ans.length() - 1]);
    for (char c : ans) {
        if (c == 'R')
            RR++;
        if (c == 'O')
            OO++;
        if (c == 'Y')
            YY++;
        if (c == 'G')
            GG++;
        if (c == 'B')
            BB++;
        if (c == 'V')
            VV++;
    }
    assert(RR == R1 && OO == O && YY == Y1 && GG == G && BB == B1 && VV == V);
}

bool check(int & prime, int side, char c1, char c2) {
    if (side == 0)
        return false;
    if (prime < side || (prime == side && prime + side != n)) {
        printf("IMPOSSIBLE\n");
        return true;
    }
    if (prime == side && prime + side == n) {
        forn(j, n / 2)
            printf("%c%c", c1, c2);
        printf("\n");
        return true;
    }
    prime -= side;
    return false;
}

int main() {

    banned.insert(mp('R', 'O'));
    banned.insert(mp('R', 'V'));
    banned.insert(mp('B', 'G'));
    banned.insert(mp('B', 'V'));
    banned.insert(mp('Y', 'O'));
    banned.insert(mp('Y', 'G'));
    int tests;
    scanf("%d", &tests);
    forn(test, tests) {
        cin >> n >> R >> O >> Y >> G >> B >> V;
        R1 = R;
        Y1 = Y;
        B1 = B;
        assert(R + O + Y + G + B + V == n);
        bool found = false;
        printf("Case #%d: ", test + 1);
        if (check(R, G, 'R', 'G'))
            continue;
        if (check(Y, V, 'Y', 'V'))
            continue;
        if (check(B, O, 'B', 'O'))
            continue;
        forn(start, 3) {
            cnt[0] = R;
            cnt[1] = Y;
            cnt[2] = B;
            memset(was, false, sizeof(was));
            cnt[start]--;
            if (cnt[start] < 0)
                continue;
            ans = "";
            add(start);
            int last = start;
            forn(step, n - 1) {
                int best = -1;
                forn(j, 3) if (j != last) {
                    if (best == -1 || (cnt[j] > cnt[best] || (cnt[j] == cnt[best] && j == start)))
                        best = j;
                }
                if (cnt[best] == 0) {
                    break;
                }
                add(best);
                cnt[best]--;
                last = best;
            }
            if ((int)ans.length() == n && ans[(int)ans.length() - 1] != symb[start]) {
                ass();
                cout << ans << endl;
                found = true;
                break;
            }
        }
        if (!found) {
            cout << "IMPOSSIBLE" << endl;   
        }
    }
}
