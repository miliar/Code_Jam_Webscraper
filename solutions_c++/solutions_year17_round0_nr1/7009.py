#include <iostream>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <cstdio>
#include <fstream>

using namespace std;

char Inverse(char x) {
    if (x == '+') return '-';
    else return '+';
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    string s;
    int t, k;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int sum = 0;
        int count = 0;
        cin >> s;
        cin >> k;
        for (int j = 0; j < s.length() - k + 1; j++) {
            if (s[j] == '-') {
                count++;
                for (int h = j; h < j + k; h++) s[h] = Inverse(s[h]);
            }
        }
        for (int j = 0; j < s.length(); j++) {
            if (s[j] == '-') sum--;
            else sum++;
        }
        if (sum == s.length()) cout << "Case #" << i + 1 << ": " << count;
        else cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE";
        cout << endl;
    }
    return 0;
}
