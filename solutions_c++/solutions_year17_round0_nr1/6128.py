#include <iostream>
using namespace std;

void flip(char &ch) {
    if (ch == '+')
        ch = '-';
    else
        ch = '+';
}

int main() {
    int T, Case = 1;
    cin >> T;
    while (T--) {
        string str;
        int k;
        cin >> str >> k; 
        int ans = 0;
        for (int i = 0; i < str.length(); i++) {
            if (i + k <= str.length()) {
                if (str[i] == '-')
                {
                    for (int j = 0; j < k; j++) {
                        flip(str[i + j]);
                    }
                    ans++;
                }
            } else {
                if (str[i] == '-')
                    ans = -1;
            }
        }
        cout << "Case #" << Case++ << ": ";
        if (ans == -1) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }
    return 0;
}
