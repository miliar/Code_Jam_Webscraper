#include <iostream>
#include <vector>

using namespace std;

char flip(char c) {
    if (c == '-') {
        return '+';
    } else {
        return '-';
    }
}

bool isFun(const string& s) {
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] != '+') {
            return false;
        }
    }
    
    return true;
}

int main() {
    int T;
    cin >> T;
    for (int ii = 0; ii < T; ++ii) {
        string s;
        int k;
        cin >> s >> k;
        int flippersAmount = 0;
        for (int i = 0; i <= s.size() - k; ++i) {
            if (s[i] == '-') {
                flippersAmount++;
                for (int j = i; j < i + k; ++j) {
                    s[j] = flip(s[j]);
                }
            }
        }
        
        cout << "Case #" << ii + 1 << ": ";
        if (isFun(s)) {
            cout << flippersAmount << "\n";
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }
    
    return 0;
}
