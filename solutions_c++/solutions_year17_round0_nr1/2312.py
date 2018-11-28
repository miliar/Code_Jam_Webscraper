#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int solve(string s, int k) {
    //cout << s << endl << k << endl;
    int ans = 0;
    
    for (int i = 0; i < s.size() - k + 1; i++) {
        if (s[i] == '-') {
            ans++;
            for (int j = i; j < i + k; j++) {
                s[j] = (s[j] == '+' ? '-' : '+');
            }
        }
        //cout << s << endl;
    }


    for (int i = s.size() - k + 1; i < s.size(); i++) {
        if (s[i] == '-') {
            return -1;
        }
    }

    return ans;
}
            

int main() {
    int tests;

    cin >> tests;

    for (int test = 1; test <= tests; test++) {
        string s;
        int k;
        cin >> s >> k;
        int ans = solve(s, k);
        cout << "Case #" << test << ": ";
        if (ans == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << ans;
        }
        cout << endl;
    }

    return 0;
}
