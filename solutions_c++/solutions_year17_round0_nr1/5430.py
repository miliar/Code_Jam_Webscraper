#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int solve(string s, const int &k) {
    int slen = s.length();
    int result = 0;
    for (int j = 0; j < slen;) {
        while (s[j] == '+') j++;
        if (j == slen) return result;
        if (j+k-1 >= slen) return -1;
        result++;
        for (int i = 0; i < k; i++) {
            if (s[j+i] == '-') s[j+i] = '+';
            else s[j+i] = '-';
        }
        //cout << s << endl;
    }
    return result;
}

int main(int argc, char* argv[]) {
    int T; cin >> T;
    for (int t = 0; t < T; t++) {
        string s; cin >> s;
        int k; cin >> k;
        //cout << s << endl;
        int z = solve(s, k);
        if (z == -1) cout << "Case #" << (t+1) << ": IMPOSSIBLE" << endl;
        else cout << "Case #" << (t+1) << ": " << z << endl;
    }
    return 0;
}

