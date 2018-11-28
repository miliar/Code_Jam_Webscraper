#include <iostream>
using namespace std;

int main() {
    int T, t, i, j, pr;
    long long N;
    cin >> T;
    for (t = 1; t <= T; t++) {
        cin >> N;
        string s = to_string(N);
        for (i = s.size()-2; i >= 0; i--) {
            if (s[i] > s[i+1]) {
                s[i]--;
                for (j = i+1; j < s.size(); j++) s[j] = '9';
                if (s[i] < '0' && i > 0) s[i] = '9', s[i-1]--;
            }
        }
        pr = 0;
        cout << "Case #" << t << ": ";
        for (i = 0; i < s.size(); i++) {
            if (s[i] > '0') pr = 1;
            if (pr) cout << s[i];
        }
        cout << endl;
    }
}