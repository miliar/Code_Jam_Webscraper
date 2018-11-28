#include <bits/stdc++.h>

using namespace std;

#define F first
#define S second
#define pb push_back
#define mp make_pair
#define iOS ios_base::sync_with_stdio(false)
#define L(x) (x << 1)
#define R(x) (x << 1) + 1
#define tt cout << '.' << '\n';

typedef long long ll;
typedef pair <ll, ll> pii;

//const int N = 1e2 + 20;

const int oo = 1e9 + 7;

int q, k, ans = oo, cnt;

string s;

void ncb (int x) {
    if (x + k > s.size()) {
        for (int i = 0; i < s.size(); ++i)
            if (s[i] == '-') return;
        ans = min(ans, cnt);
        return;
    }
    ncb(x + 1);
    cnt++;
    for (int i = x; i < x + k; ++i) {
        if (s[i] == '-') s[i] = '+';
        else s[i] = '-';
    }
    ncb(x + 1);
    cnt--;
    for (int i = x; i < x + k; ++i) {
        if (s[i] == '-') s[i] = '+';
        else s[i] = '-';
    }
    return;
}

int main() {
    iOS;
    cin >> q;
    for (int j = 0; j < q; ++j) {
        ans = oo;
        cnt = 0;
        cin >> s >> k;
        ncb(0);
        cout << "Case #" << j + 1 << ": ";
        if (ans != oo) cout << ans << '\n';
        else cout << "IMPOSSIBLE\n";
    }
    return 0;
}
