#include <iostream>
#include <string>


using namespace std;

void runtest() {
    int k;
    string s;
    cin >> s >> k;
    int res = 0;
    for (int i = 0; i < s.length(); ++i) {
        if (s[i] == '-') {
            res++;
            if (i + k > s.length()) {
                cout << "IMPOSSIBLE\n";
                return;
            }
            for (int j = 0; j < k; ++j) {
                s[i + j] = s[i + j] == '+' ? '-' : '+';
            }
        }
    }
    cout << res << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        runtest();
    }
    return 0;
}