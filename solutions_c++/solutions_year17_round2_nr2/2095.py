#include <iostream>
#include <queue>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <iomanip>

#define FOR(i,x,y) for(int i =(int)(x); i<(int)(y); i++)
#define REP(i, N) FOR(i, 0, N)
#define SZ(x) (int)x.size()

using namespace std;

typedef vector<int> vin;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vpii;
typedef vector<vector<int> > vvin;

typedef long long LL;
typedef unsigned long long ULL;

#define R 0
#define Y 2
#define B 4

int main ()
{
    // N, R, O, Y, G, B, and V.
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        vector<int> cnt(6); int N; cin >> N;
        for (int i = 0; i < 6; ++i) {
            cin >> cnt[i];
        }

        vector<pair<int, pair<int, char>>> l(3);
        int red = cnt[R], yel = cnt[Y], blu = cnt[B];
        l[0] = make_pair(red, make_pair(red, 'R'));
        l[1] = make_pair(yel, make_pair(yel, 'Y'));
        l[2] = make_pair(blu, make_pair(blu, 'B'));
        sort(l.begin(), l.end(), std::greater<pair<int, pair<int, char>>>());

        vector<char> ans(N);
        for (int i = 0; i < N; ++i) {
            if (i == 0) {
                ans[i] = l[0].second.second;
                l[0] = make_pair(l[0].first - 1, l[0].second);
            } else {
                if (l[0].second.second != ans[i - 1] && l[0].second.second != ans[(i + 1) % N]) {
                    ans[i] = l[0].second.second;
                    l[0] = make_pair(l[0].first - 1, l[0].second);
                } else {
                    ans[i] = l[1].second.second;
                    l[1] = make_pair(l[1].first - 1, l[1].second);
                }
            }

            sort(l.begin(), l.end(), std::greater<pair<int, pair<int, char>>>());
        }

        bool bad = false;
        for (size_t i = 0; i < l.size(); ++i) {
            if (l[i].first != 0) {
                bad = true;
            }
        }

        for (int i = 0; i < N; ++i) {
            if (ans[i] == ans[(i + 1) % N]) {
                bad = true;
            }
        }

        if (bad) {
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << t << ": ";
            for (const auto &c : ans) {
                cout << c;
            }
            cout << endl;
        }
    }
    return 0;
}
