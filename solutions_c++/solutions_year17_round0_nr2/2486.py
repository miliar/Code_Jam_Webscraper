#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    long T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string S;
        cin >> S;
        long N = S.size();
        for (long i = 1; i < N; i++) {
            if (S[i-1] > S[i]) {
                while (i > 0 && S[i-1] > S[i]) i--, S[i]--;
                for (long j = i+1; j < N; j++) S[j] = '9';
                break;
            }
        }
        cout << "Case #" << t << ": ";
        cout << stol(S) << endl;
    }
}
