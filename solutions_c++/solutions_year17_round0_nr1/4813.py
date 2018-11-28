#include <iostream>
#include <string>

using namespace std;

bool check_happy(string S) {
    for (unsigned int i = 0; i < S.size(); ++i) {
        if (S[i] != '+') return false;
    }
    return true;
}

char flip(char c) {
    if (c == '+') return '-';
    else return '+';
}

int count_flips(string S, unsigned int K) {
    if (check_happy(S)) return 0;
    int count = 0;
    for (unsigned int i = 0; i < S.size(); ++i) {
        if (S[i] == '-') {
            if ((i + K) > S.size())
                return -1;
            for (unsigned int j = i; j < (i+K); ++j) {
               S[j] = flip(S[j]); 
            }
            ++count;
        } 
    }
    if (check_happy(S)) return count;
    else return -1;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string S;
        unsigned int K;
        cin >> S >> K;
        int count = count_flips(S, K);
        if (count == -1)
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << t << ": " << count << endl;
    }
    return EXIT_SUCCESS;
}
