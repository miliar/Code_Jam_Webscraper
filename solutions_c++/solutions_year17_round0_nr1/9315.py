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
int K;
string S;

int solve() {
    cin >> S >> K;
    int ans = 0;
    for (int i = 0; i <= S.size() - K; ++i) {
        if (S[i] == '-') {
            ++ans;
            for (int j = i; j < i + K; ++j) {
                if (S[j] == '-') S[j] = '+';
                else S[j] = '-';
            }
        }
    }
    for (int i = S.size() - K; i < S.size(); ++i) {
        if (S[i] == '-') {
            ans = -1;
            break;
        }
    }
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        int ans = solve();
        cout << "Case #" << tc << ": ";
        if (ans == -1)
            cout << "IMPOSSIBLE";
        else
            cout << ans;
        cout << lend;
    }
}
