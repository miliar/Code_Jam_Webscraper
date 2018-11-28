// Oversized Pancake Flipper
// Author: aroussau

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int T, K;
string S;

int solve(string s, int k) {
    int res = 0;
    
    for (int i = 0; i <= s.length() - k; ++i) {
        if (s[i] == '+') {
            continue;
        }
        else {
            res++;
            
            for (int j = i; j < i + k; ++j) {
                if (s[j] == '+') {
                    s[j] = '-';
                }
                else {
                    s[j] = '+';
                }
            }
        }
    }
    
    for (int i = 0; i < s.length(); ++i) {
        if (s[i] == '-') {
            res = -1;
            break;
        }
    }
    
    return res;
}

int main() {
    cin >> T;

    for (int i = 1; i <= T; ++i) {
        cin >> S;
        cin >> K;
        int res = solve(S, K);
        
        if (res == -1) {
            cout << "Case #" << i << ": " << "IMPOSSIBLE\n";
        }
        else {
            cout << "Case #" << i << ": " << res << "\n";
        }
    }

    return 0;
}