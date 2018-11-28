#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";

        string S;
        int K;
        cin >> S >> K;

        int num = 0;
        for (int i = 0; i < S.size() - K + 1; i++) {
            if (S[i] == '-') {
                num++;
                for (int j = 0; j < K; j++) {
                    S[i+j] = S[i+j] == '-' ? '+' : '-';
                }
            }
        }
        bool good = true;
        for (int i = S.size() - K; i < S.size() && good; i++) {
            if (S[i] == '-') {
                good = false;
            }
        }
        if (!good) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << num << "\n";
        }
    }
}
