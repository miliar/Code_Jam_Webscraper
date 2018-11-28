#include <bits/stdc++.h>

#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define forn(i, n) for(int i=0;i<(n);++i)
#define clr(ar, val) memset(ar, val, sizeof(ar))

using namespace std;

typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<ld, ld> point;

const int MAXN = 2e5 + 200;
const int INF = int(1e9) + 7;
const long long LINF = 1ll * INF * INF;
const int md = int(1e9) + 7;
const ld eps = 1e-9;
const ld PI = 3.1415926535897932384626433832795l;

int it, test;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> test;
    for (it = 1; it <= test; it++) {
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        bool lose = false;
        for (int i = 0; i < s.length(); i++) {
            if (lose) {
                break;
            }
            if (s[i] == '+') {
                continue;
            }

            ans++;
            for (int j = 0; j < k; j++) {
                if (i + j >= s.length()) {
                    lose = true;
                    break;
                }

                s[i + j] = s[i + j] == '+' ? '-' : '+';
            }
        }

        if (lose) {
            cout << "Case #" << it << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << it << ": " << ans << endl;
        }
    }
    return 0;
}
