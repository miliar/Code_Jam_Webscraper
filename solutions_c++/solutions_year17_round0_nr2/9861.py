#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
#define GCD(a,b) __gcd(a, b)
#define mp make_pair
#define DEBUG(x) cout << x << endl
#define ALL(x) x.begin(), x.end()
#define INF (1 << 30)
#define pb push_back
#define lend '\n'

int T;
string N;

int good() {
    int sz = N.size();
    int i = 0;
    for (; i < sz - 1; ++i) {
        if (N[i + 1] < N[i])
            break;
    }
    return i;
}
string solve() {
    cin >> N;
    int sz = N.size();
    int i = good();
    if (i == sz - 1)
        return N;
    while (i >= 0 && N[i] == '1') {
        --i;
    }
    if (i >= 0) {
        N[i] -= 1;
        for (int j = i + 1; j < sz; ++j)
            N[j] = '9';
        return N;
    }
    else {
        return string(sz - 1, '9');
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin >> T;

    for (int tc = 1; tc <= T; ++tc) {
        string ans = solve();
        cout << "Case #" << tc << ": " << ans << lend;
    }
}
