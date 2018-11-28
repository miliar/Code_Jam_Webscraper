#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;

    for (int caseNum = 1; caseNum <= T; ++caseNum) {

        string S;
        int K, result = 0;
        cin >> S >> K;

        for (int i = 0; i < S.length(); ++i) {

            if (S[i] == '-') {
//                cout << "minus at " << i << endl;
                if (i+K-1 >= S.length()) {
                    result = INT_MIN;
                    break;
                }
                for (int j = i; j < i+K; ++j) {
                    if (S[j] == '-') S[j] = '+';
                    else S[j] = '-';
                }
                result++;
            }
        }

        if (result < 0) cout << "Case #" << caseNum << ": IMPOSSIBLE" << endl;
        else cout << "Case #" << caseNum << ": " << result << endl;
    }
}
