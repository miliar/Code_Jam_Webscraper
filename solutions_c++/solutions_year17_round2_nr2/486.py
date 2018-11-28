/******************************************************************************\
*                         Author:  Dumbear                                     *
*                         Email:   dumbear[#at]163.com                         *
*                         Website: http://dumbear.com                          *
\******************************************************************************/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std;

#define output(x) cout << #x << ": " << (x) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<long long> VL;
typedef vector<double> VD;
typedef vector<string> VS;

int t;
int n, r, o, y, g, b, v;

void solve() {
    scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
    printf("Case #%d: ", ++t);
    if (r > n / 2 || y > n / 2 || b > n / 2) {
        puts("IMPOSSIBLE");
    } else {
        string s;
        char last = '\0';
        for (int i = 0; i < n; ++i) {
            pair<int, char> ch[] = {make_pair(r, 'R'), make_pair(y, 'Y'), make_pair(b, 'B')};
            if (i != 0) {
                if (ch[0].first < ch[1].first) swap(ch[0], ch[1]);
                if (ch[1].first < ch[2].first) swap(ch[1], ch[2]);
                if (ch[0].first < ch[1].first) swap(ch[0], ch[1]);
            }
            for (int j = 0; j <= 2; ++j) {
                if (ch[j].second != last && ch[j].first != 0) {
                    s += ch[j].second;
                    last = ch[j].second;
                    if (last == 'R') --r;
                    if (last == 'Y') --y;
                    if (last == 'B') --b;
                    break;
                }
            }
        }
        if (s[0] == s[s.size() - 1] || s.size() != n) puts("!!!!!!!!!!!!");
        puts(s.c_str());
    }
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
