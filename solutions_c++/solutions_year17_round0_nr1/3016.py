#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#define F first
#define S second
#define PB push_back
typedef long long ll;
using namespace std;
int K;
string S;

void flipFrom(int i) {
    for (int j = 0; j < K; ++j) {
        if (S[i+j] == '-')
            S[i+j] = '+';
        else
            S[i+j] = '-';
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);

    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> S; cin >> K;

        int cnt = 0;
        bool impossible = false;
        for (int i = 0; i + K <= S.size(); ++i) {
            if (S[i] == '-')
                flipFrom(i), ++cnt;
        }

        for (int i = 0; i < S.size(); ++i) if (S[i] == '-') {
            impossible = true;
            break;
        }

        cout << "Case #" << t << ": ";
        if (impossible) cout << "IMPOSSIBLE";
        else cout << cnt;
        cout << '\n';
    }

    return 0;
}
