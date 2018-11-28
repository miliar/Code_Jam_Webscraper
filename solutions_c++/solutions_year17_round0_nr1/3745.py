#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string S;
        int K;
        cin >> S >> K;
        bool end = true;
        int sol = 0;
        for (int i = 0; i < (int)S.size(); i++) {
            if (S[i] == '+') {
                continue;
            }
            if (i + K > (int)S.size()) {
                end = false;
                break;
            }
            for (int j = i; j < i + K; j++) {
                if (S[j] == '+') {
                    S[j] = '-';
                } else {
                    S[j] = '+';
                }
            }
            sol++;

        }
        cout << "Case #" << t << ": ";
        if (!end) {
            cout << "IMPOSSIBLE";
        } else {
            cout << sol;
        }
        cout << endl;
    }

	return 0;
}

