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

const int MAXN = 1e3 + 200;
const int INF = int(1e9) + 7;
const long long LINF = 1ll * INF * INF;
const int md = int(1e9) + 7;
const ld eps = 1e-9;
const ld PI = 3.1415926535897932384626433832795l;

const map<int, char> trans = {{0, 'R'}, {1, 'O'}, {2, 'Y'}, {3, 'G'}, {4, 'B'}, {5, 'V'}};

int test, iter;
int n;
vector<int> ans(MAXN);
vector<pair<int, int>> cnt;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> test;

    for (int iter = 1; iter <= test; iter++) {
        cnt.clear();
        cin >> n;
        for (int i = 0; i < 6; i++) {
            int x;
            cin >> x;
            cnt.emplace_back(x, i);
        }
        sort(cnt.begin(), cnt.end());
        reverse(cnt.begin(), cnt.end());

        ans[0] = cnt[0].second;
        cnt[0].first--;
        bool ok = true;
        for (int i = 1; i < n; i++) {
            int mx = -1;
            int idx = -1;
            for (int j = 0; j < 6; j++) {
                if (cnt[j].second != ans[i - 1] && cnt[j].first > mx) {
                    mx = cnt[j].first;
                    idx = cnt[j].second;
                }
            }

            if (mx <= 0) {
                ok = false;
                break;
            }

            ans[i] = idx;
            for (int j = 0; j < 6; j++) {
                if (cnt[j].second == idx) {
                    cnt[j].first--;
                }
            }
        }

        if (ans[0] == ans[n - 1]) {
            ok = false;
        }

        string result;
        if (!ok) {
            result = "IMPOSSIBLE";
        } else {
            for (int i = 0; i < n; i++) {
                result += trans.at(ans[i]);
            }
        }

        cout << "Case #" << iter << ": " << result << endl;
    }
    return 0;
}
