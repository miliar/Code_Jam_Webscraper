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

int main() {
    int tests;
    scanf("%d", &tests);
    forn(test, tests) {
        cerr << "test " << test << endl;
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        forn(pos, (int)s.length() - k + 1) {
            if (s[pos] == '-') {
                fore(j, pos, pos + k - 1)
                    s[j] = (s[j] == '+' ? '-' : '+');
                ans++;
            }
        }
        //cout << s << endl;
        bool fail = false;
        fore(j, (int)s.length() - k + 1, (int)s.length() - 1) {
            if (s[j] == '-') {
                fail = true;
                break;
            }
        }
        printf("Case #%d: ", test + 1);
        if (fail)
            printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
}
