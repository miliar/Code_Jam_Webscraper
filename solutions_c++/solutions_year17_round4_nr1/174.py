#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int N = 1000;

int n, a[4], p, ans;

int _abs(int x){
    if (x < 0) return -x;
    return x;
}
void _main() {
    cin >> n >> p;
    memset(a, 0, sizeof(a));
    for(int i = 0, x; i < n; ++i) {
        cin >> x;
        a[x % p] += 1;
    }
    if (p == 2) {
        cout << a[0] + (a[1] + 1) / 2 << endl;
    }
    else if(p == 3) {
        ans = a[0] + min(a[1], a[2]);
        int lft = _abs(a[1] - a[2]);
        ans += (lft + 2) / 3;
        cout << ans << endl;
    }
    else if(p == 4) {
        ans = a[0] + a[2] / 2 + min(a[1], a[3]);
        int lft = _abs(a[1] - a[3]);
        if (a[2] & 1) {
            lft += 2;
        }
        ans += (lft + 3) / 4;
        cout << ans << endl;
    }
}
int main() {
    int t, cas = 0;
    for (scanf("%d", &t); t--; ) {
        printf("Case #%d: ", ++cas);
        _main();
    }
    return 0;
}