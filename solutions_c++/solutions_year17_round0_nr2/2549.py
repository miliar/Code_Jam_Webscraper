#include <iostream>
#include <string>
using namespace std;

int T;

string sol(string s) {
    int i = 0;
    while (i < s.size()-1 && s[i] <= s[i+1]) i++;
    if (i == s.size()-1) return s;
    int j = i;
    while (0 < j && s[j] == s[j-1]) j--;
    if (0 < j) {
        s[j]--;
        for (int k = j+1; k < s.size(); k++) s[k] = '9';
        return s;
    }
    if (s[0] != '1') {
        s[0]--;
        for (int k = 1; k <= s.size(); k++) s[k] = '9';
        return s;
    }
    return string(s.size()-1, '9');
}

int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        cin >> s;
        cout << "Case #" << t << ": " << sol(s) << endl;
    }
    return 0;
}
