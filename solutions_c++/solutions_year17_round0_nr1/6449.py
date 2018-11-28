#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string S;
        int K, A = 0;
        cin >> S >> K;
        for (int j = 0; j < S.length(); j++) {
            if (S[j] == '-') {
                if (j + K <= S.length()) {
                    for (int k = 0; k < K; k++) {
                        if (S[j + k] == '+') S[j + k] = '-';
                        else S[j + k] = '+';
                    }
                    A++;
                } else {
                    cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
                    A = -1;
                    break;
                }
            }
        }
        if (A != -1) {
            cout << "Case #" << i + 1 << ": " << A << endl;
        }
    }
    return 0;
}