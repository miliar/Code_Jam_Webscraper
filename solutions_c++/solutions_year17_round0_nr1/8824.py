#include <iostream>
#include <string>
using namespace std;

char reverse(char a) {
    if(a == '+') {
        return '-';
    }
    else {
        return '+';
    }
}

int solve(string s, int k) {
    int count = 0;
    for (int i = 0; i <= s.length() - k; i++) {
        if (s[i] == '-') {
            count++;
            for (int j = i; j < i + k; j++) {
                s[j] = reverse(s[j]);
                
            }
        }
    }
    for (int i = s.length() - k + 1; i < s.length(); i++) {
        if (s[i] == '-') {
            return -1;
        }
    }
    return count;
}

int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        string s;
        int k;
        cin >> s >> k;
        int ans = solve(s,k);
        if (ans == -1) {
            cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
        }
        else {
            cout << "Case #" << i << ": " << solve(s, k) << endl;
        }
        
    }

    return 0;
}