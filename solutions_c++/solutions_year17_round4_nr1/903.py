# include <bits/stdc++.h>

# define fname "stones"
# define mp make_pair
# define F first
# define S second
# define y1 dsfkaj
# define pb push_back
# define prev adskjfa
typedef long long ll;

using namespace std;

const int MAXN = (int)5e5 + 5;
char s1[MAXN], s2[MAXN];
int T, x[MAXN], n, a, b;

int f(int k, int cur) {
    int l = 1, r = n - k;
    int t = T - cur - (k - 1)*a;
    if(t < x[1])
        return 0;
    while(l + 1 < r) {
        int mid = (l + r) / 2;
        if(x[mid] <= t)
            l = mid;
        else
            r = mid - 1;
    }
    if(x[r] <= t)
        l = r;
    return l;
}

int solve() {
    int res = 0;

    for(int i = 1; i < n; i++) {
        x[i] = x[i - 1] + 1 + a;
        if(s2[i] == 'w')
            x[i] += b;
    }

    int cur = 0;
    for(int i = 1; i <= n; i++) {
        cur++;
        if(s1[i] == 'w')
            cur += b;
        if(cur > T)
            break;
        res = max(res, i + f(i, cur));
        cur += a;
    }

    return res;
}

int main() {
    # ifdef alibi
        freopen("in", "r", stdin);
    # endif

    cin >> n >> a >> b >> T;
    for(int i = 1; i <= n; i++)
        cin >> s1[i];
    for(int i = 1; i < n; i++)
        s2[i] = s1[n - i + 1];

    int ans = solve();

    for(int i = 2; i <= n; i++)
        s1[i] = s2[i - 1];
    for(int i = 1; i < n; i++)
        s2[i] = s1[n - i + 1];

    ans = max(ans, solve());
    cout << ans << endl;
    return 0;
}
