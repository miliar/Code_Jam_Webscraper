#include <iostream>

using namespace std;

void flip(string &pancakes, int start, int flipper_size) {
    for (int i = start; i < start + flipper_size; ++i) {
        //cout << "i = " << i << endl;
        if (pancakes[i] == '-') {
            pancakes[i] = '+';
        } else {
            pancakes[i] = '-';
        }
    }
}

int main() {
    int T; // Number of test cases
    string S; // String of pancakes
    int K; // Size of flipper

    cin >> T;
    //cout << "T = " << T << endl;
    for (int i = 1; i <= T; ++i) {
        int numberOfFlips = 0;
        bool isPossible = true;
        cin >> S >> K;
      //  cout << "S = " << S << "\t" << "K = " << K << endl;

        for (int j = 0; j <= S.length() - K; ++j) {
            //cout << "j = " << j << endl;
            if (S[j] == '-') {
                //cout << "S before flip: " << '\t' << S << endl;
                flip(S, j, K);
                numberOfFlips++;
                //cout << "S after flip: " << '\t' << S << endl;
            }
        }

        for (int k = 0; k < S.length(); ++k) {
            if (S[k] == '-') {
                isPossible = false;
            }
        }

        if (isPossible) {
            cout << "Case #" << i << ": " << numberOfFlips << endl;
        } else {
            cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
        }

    }

    return 0;
}