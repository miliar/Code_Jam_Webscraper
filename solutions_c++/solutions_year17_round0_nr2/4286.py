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
long long n;
vector<int> num, ans;

bool rec(int idx, bool canAll = false) {
    if (idx == num.size()) {
        return true;
    }

    if (canAll) {
        ans[idx] = 9;
        return rec(idx + 1, true);
    }

    if (!idx || num[idx] >= ans[idx - 1]) {
        ans[idx] = num[idx];
        if (rec(idx + 1, false)) {
            return true;
        }
    }

    if (!idx || num[idx] - 1 >= ans[idx - 1]) {
        ans[idx] = num[idx] - 1;
        if (rec(idx + 1, true)) {
            return true;
        }
    }

    return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> test;
    for (it = 1; it <= test; it++) {
        num.clear();
        ans.clear();
        cin >> n;
        while (n) {
            num.push_back(n % 10);
            n /= 10;
        }
        reverse(num.begin(), num.end());

        ans.resize(num.size());

        rec(0);

        long long total = 0;
        for (auto c : ans) {
            total = total * 10 + c;
        }
        cout << "Case #" << it << ": " << total << endl;
    }
    return 0;
}
