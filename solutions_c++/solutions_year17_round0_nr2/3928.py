#include <bits/stdc++.h>

using namespace std;

#define vec vector
#define ALL(x) (x).begin(), (x).end()

typedef pair< int, int > pii;
typedef long long ll;

int const inf = 1000 * 1000 * 1000;
ll const inf64 = 1ll * inf * inf;

string toString(ll n) {
    string result = "";
    while(n) {
        result.push_back(n % 10 + '0');
        n /= 10;
    }
    reverse(ALL(result));
    return result;
}

ll dp[20][10];

ll count(string s) {
    int sz = (int)s.size();
    ll total = 0;
    for(int l = 1;l < sz;l++) {
        for(int x = 1;x < 10;x++) {
            total += dp[l][x];
        }
    }
    for(int i = 0;i < sz;i++) {
        int start;
        if(i > 0) {
            start = s[i - 1] - '0';
        }else {
            start = 1;
        }
        for(int x = start;x < s[i] - '0';x++) {
            total += dp[sz - i][x];
        }
        if(i > 0 && s[i] < s[i - 1]) break;
        if(i + 1 == sz) total++;
    }
    return total;
}

void solve() {
    ll n;
    cin >> n;
    ll bl = 1;
    ll br = n;
    ll bm;
    ll need = count(toString(n));
    while(br - bl > 1) {
        bm = (bl + br) / 2;
        if(count(toString(bm)) == need) br = bm;
        else bl = bm + 1;
    }
    if(bl < br && count(toString(bl)) == need) {
        cout << bl << "\n";
    }else {
        cout << br << "\n";
    }
}

void precalc() {
    for(int i = 0;i < 10;i++) {
        dp[1][i] = 1;
    }
    for(int l = 2;l < 20;l++) {
        for(int x = 0;x < 10;x++) {
            for(int y = x;y < 10;y++) {
                dp[l][x] += dp[l - 1][y];
            }
        }
    }
}

bool check(string s) {
    for(int i = 1;i < (int)s.size();i++) {
        if(s[i] < s[i - 1]) return 0;
    }
    return 1;
}

ll simple(ll n) {
    ll result = 0;
    for(ll x = 1;x <= n;x++) {
        result += check(toString(x));
    }
    return result;
}

int main() {

    precalc();

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int testNumber;

    scanf("%d", &testNumber);

    for(int test = 1;test <= testNumber;test++) {
        printf("Case #%d: ", test);
        solve();
    }

    return 0;
}
