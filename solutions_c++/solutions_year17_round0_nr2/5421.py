#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        string S;
        cin >> S;

        int n = S.length();
        int *s = new int[n];

        for(int j = 0; j < n; ++j)
            s[j] = S[j] - '0';

        for(int j = n - 2; j >= 0; --j) {
            if(s[j] > s[j + 1]) {
                --s[j];
                for(int k = j + 1; k < n && s[k] != 9; ++k)
                    s[k] = 9;
            }
        }

        cout << "Case #" << i << ": ";

        for(int j = s[0] == 0 ? 1 : 0; j < n; ++j)
            cout << s[j];

        cout << endl;

        delete []s;
    }
}