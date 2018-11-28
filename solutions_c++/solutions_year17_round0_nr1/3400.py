#include<bits/stdc++.h>
using namespace std;

int T, K, N, pancake[1003], ans;
string S;

int main() {
    cin >> T;
    for (int cases = 1; cases <= T; cases++) {
        cin >> S >> K;

        N = S.length();
        for (int i = 0; i < N; i++)
            pancake[i + 1] = (S[i] == '-' ? 0 : 1);

        ans = 0;
        for (int i = 1; i <= N - K + 1; i++) {
            if (pancake[i] == 0) {
                ans++;
                for (int j = i; j <= i + K - 1; j++)
                    pancake[j] = 1 - pancake[j];
            }
        }

        bool allHappy = true;
        for (int i = 1; i <= N; i++) {
            if (pancake[i] == 0)
                allHappy = false;
        }

        cout << "Case #" << cases << ": ";
        if (allHappy)
            cout << ans << endl;
        else
            cout << "IMPOSSIBLE\n";
    }
}
