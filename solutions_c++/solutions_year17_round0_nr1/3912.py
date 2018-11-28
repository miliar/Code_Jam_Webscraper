#include <iostream>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
    int T, K; string S;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> S >> K;

        int R = 0, len = S.length();
        for (int ii = 0; ii < len; ++ii) {
            if (S[ii] == '+') continue;
            if (ii + K > len) { R = -1; break; }
            else {
                for (int j = 0; j < K; ++j) S[ii + j] = S[ii + j] == '+' ? '-' : '+';
                ++R;
            }
        }

        if (R >= 0) cout << "Case #" << i << ": " << R << endl;
        else cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    }
}