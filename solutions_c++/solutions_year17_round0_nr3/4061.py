#include <bits/stdc++.h>

using namespace std;

#define vec vector
#define ALL(x) (x).begin(), (x).end()

typedef long long ll;
typedef pair< int, int > pii;
typedef pair< ll, ll > pll;

int const inf = 1000 * 1000 * 1000;
ll const inf64 = 1ll * inf * inf;

void solve() {
    ll n, k;
    cin >> n >> k;
    map< ll, ll > cnt;
    cnt[n] = 1;
    ll n1, n2, cur, len;
    while(1) {
        len = (--cnt.end())->first;
        cur = (--cnt.end())->second;
        cnt.erase(--cnt.end());
        if(len % 2) {
            n1 = n2 = len / 2;
        }else {
            n1 = len / 2 - 1;
            n2 = len / 2;
        }
        if(cur < k) {
            if(n1 > 0) {
                cnt[n1] += cur;
            }
            if(n2 > 0) {
                cnt[n2] += cur;
            }
            k -= cur;
        }else {
            cout << n2 << " " << n1 << "\n";
            break;
        }
    }
}

int main() {

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
