#include <iostream>
using namespace std;

string s;
int z;

string solution(string s) {
    for (int i = 1; i < s.size(); i++) {
        if (s[i] < s[i - 1]) {
            i--;
            while (i > 0 && s[i] == s[i - 1]) {
                i--;
            }
            s[i]--;
            if (s[i] == '0') {
                string s2(s.size() - 1, '9');
                return s2;
            }
            for (i++; i < s.size(); i++) {
                s[i] = '9';
            }
            return s;
        }
    }
    return s;
}

int main() {
    cin >> z;
    for (int nr = 1; nr <= z; nr++) {
        cin >> s;
        cout << "Case #" << nr << ": " << solution(s) << endl;
    }
}