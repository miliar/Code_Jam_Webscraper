#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
    int T, K;
    string S;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> S;
        cin >> K;
        int j = 0, count = 0;
        while (j < S.length() - K) {
            if (S[j] == '-') {
                count++;
                for (int l = j + 1; l < j + K; l++) {
                    S[l] = S[l] == '+' ? '-' : '+';
                }
            }
            //cout << j << ": " << S << endl;
            j++;
        }
        //cout << S.substr(j, K) << "vs. " << string(K, '+') << endl;
        if (S.substr(j, K) == string(K, '+')) {
            cout << "Case #" << i << ": " << count << endl;
        } else if (S.substr(j, K) == string(K, '-')) {
            cout << "Case #" << i << ": " << count + 1 << endl;
        } else {
            cout << "Case #" << i << ": IMPOSSIBLE\n";
        }
    }
    return 0;
}