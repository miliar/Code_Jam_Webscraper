#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        string S;
        int K;
        cin >> S >> K;

        int flip = 0;
        bool impossible = false;
        vector<char> pancakes(S.begin(), S.end());

        for (int j = 0; j < pancakes.size(); j++) {
            if (pancakes[j] == '-') {
                if ((j + K - 1) < pancakes.size()) {
                    flip++;

                    for (int k = 0; k < K; k++) {
                        int idx = j + k;
                        if (pancakes[idx] == '-') {
                            pancakes[idx] = '+';
                        } else {
                            pancakes[idx] = '-';
                        }
                    }
                } else {
                    impossible = true;
                    break;
                }
            }
        }

        if (impossible) {
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << i+1 << ": " << flip << endl;
        }

    }
}
