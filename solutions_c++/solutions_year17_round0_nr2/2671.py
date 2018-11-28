#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);

        string s;
        cin >> s;
        int n = s.length();
        int i = 1;
        while (i < n && s[i] >= s[i - 1]) i++;
        if (i != n) {
            char c = s[--i];
            while (i > 0 && s[i - 1] == c) i--;
            s[i++]--;
            while (i < n) s[i++] = '9';
        } 
        while (s.length() > 1 && s[0] == '0') s = s.substr(1);
        printf("%s\n", s.c_str());
    }
    return 0;
}
