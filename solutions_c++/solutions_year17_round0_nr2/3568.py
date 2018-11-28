#include <bits/stdc++.h>

using namespace  std;

using ll = long long;

#define clr(a) (a.clear())
#define MP(a,b) make_pair(a,b)
#define sz(x) (int)x.size()
#define mem(a,b) memset(a, b, sizeof(a))
#define Unique(store) store.resize(unique(store.begin(),store.end())-store.begin())
#define pb push_back
#define FAST ios_base::sync_with_stdio(0);cin.tie(0);

#define X first
#define Y second

using pii = pair <int , int>;
using pll = pair <ll , ll>;
const ll inf = 1;
const ll mod = 1E9;

#define SZ 20

int num[SZ];
int len;

int dp[SZ][2][10];

void prepare (ll n) {
    len = 0;
    while (n) {
        num[len++] = n % 10;
        n /= 10;
    }
    return;
}

int solve (int indx, int flag, int pre) {
    if (indx == -1) return 1;
    int &ret = dp[indx][flag][pre];
    if (ret != -1) return ret;
    ret = 0;
    int lim = flag? num[indx]: 9;
    for (int i = pre; i <= lim; i++) {
        ret = max(ret, solve(indx - 1, i == lim? flag: 0, i));
    }
    return ret;
}

string path (int indx, int flag, int pre) {
    if (indx == -1) return "";
    int lim = flag? num[indx]: 9;
    string num = "";
    for (int i = lim; i >= pre; i--) {
        if (solve(indx - 1, i == lim? flag: 0, i) == 1) {
            num = (char)(i + '0') + path(indx - 1, i == lim? flag: 0, i);
            break;
        }
    }
    return num;
}

int main() {
//    #if defined JESI
//        freopen("B-large.in", "r", stdin);
//        freopen("3.txt", "w", stdout);
//    #endif

    int t;
    cin >> t;

    for (int cs = 0; cs < t; cs++) {
        ll n;
        cin >> n;
        prepare(n);

        mem(dp, -1);
        solve(len - 1, 1, 0);
        string num = path(len - 1, 1, 0);
        ll ans = 0;

        for (int i = 0; i < num.size(); i++) {
            ans = ans * 10 + num[i] - '0';
        }

        cout << "Case #" << cs + 1 << ": " << ans << endl;
    }

    return 0;
}






