#include <iostream>
#include <string>
using namespace std;

int T, K;
string S;
int x[1000];

void solve()
{
    for (int i = 0; i < S.size(); i++) {
        x[i] = (S[i] == '+');
    }
    int cnt = 0;
    for (int i = 0; i < S.size(); i++) {
        if (!x[i]) {
            if (i > S.size() - K) {
                cout << "IMPOSSIBLE";
                return;
            }
            cnt++;
            for (int j = 0; j < K; j++) {
                x[i + j] ^= 1;
            }
        }
    }
    cout << cnt;
}

int main()
{
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> S >> K;
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
}
