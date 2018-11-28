#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        string s;
        cin >> s;
        int K;
        cin >> K;

        int flips = 0;
        for (int a = 0; a <= s.size() - K; a++) {
            if (s[a] == '-') {
                for (int k = a; k < K+a; k++) {
                    s[k] = s[k] == '-' ? '+' : '-';
                }
                flips++;
            } 
        }

        int a = 0;
        for (; a < s.size(); a++)
            if (s[a] != '+') {
                cout << "Case #" << i << ": IMPOSSIBLE" << endl;
                break;
            }
        if (a == s.size()) 
            cout << "Case #" << i << ": " << flips << endl;
    }
    return 0;
}
