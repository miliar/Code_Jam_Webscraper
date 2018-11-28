#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int main() {
    int T;
    int n;
    string s, ans;
    bool flag;

    cin >> T;
    for (int Ti = 0; Ti < T; ++Ti) {
        n = 0;
        cin >> s;
        ans.clear();
        for (int i = 0; i < s.length(); ++i) {
            flag = true;
            for (int j = i+1; j < s.length(); ++j) {
                if (s[j] > s[i]) break;
                if (s[j] < s[i]) {
                    flag = false;
                    break;
                }
            }
            if (flag)
                ans += s[i];
            else {
                ans += s[i] - 1;
                for (int j = i+1; j < s.length(); ++j)
                    ans += '9';
                break;
            }
        }

        cout << "Case #" << Ti+1 << ": ";
        int t = 0;
        while (t < ans.length() && ans[t] == '0') t++;
        for (int i = t; i < ans.length(); ++i)
            cout << ans[i];
        if (t == ans.length()) cout << "0";
        cout << endl;
    }

    return 0;
}
