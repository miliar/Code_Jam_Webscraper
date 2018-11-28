#include <iostream>

using namespace std;

void flip(char & c) {
    if (c == '+') {
        c = '-';
    }
    else {
        c = '+';
    }
}

int main (void) {

    int T; cin >> T;

    for (int t = 1; t <= T; t++) {
        string S; cin >> S;
        int K; cin >> K;
        int min_flips = 0;

        for (int i = 0; i < S.size()-K+1; i++) {
            if (S[i] == '-') {
                min_flips++;
                for (int j = 0; j < K; j++) {
                    flip(S[i+j]); 
                }
            }
        }

        bool possible = true;
        for (int i = S.size()-K+1; i < S.size(); i++) {
            if (S[i] == '-') {
                possible = false;
                break;
            }
        }

        cout << "Case #" << t << ": ";
        if (!possible) {
            cout << "IMPOSSIBLE" << endl;
        }
        else {
            cout << min_flips << endl;
        }
    }   
    
    return 0;
};
