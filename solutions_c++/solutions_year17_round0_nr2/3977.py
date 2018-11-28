#include <iostream>
#include <string>

using namespace std;

int findLastDescendPos(string s, int& pos) {
    for (; pos > 0; --pos) {
        if (s[pos] < s[pos-1]) break;
    }
    return pos;
}

string getTidyNumber(string& s) {
    int len = s.length();
    if (len == 1) return s;
    int i = len-1;
    while (i >= 0) {
        i = findLastDescendPos(s, i);
        if (!i) break;
        s[i-1]--;
        for (int j = i; j < len; ++j) {
            if (s[j] == '9') break;
            s[j] = '9';
        }
    }
    if (s[0] == '0')
        return s.substr(1);
    return s;
}

int main() {
    int t;
    string n;
    cin >> t;
    for (int i =1; i < t+1; ++i) {
        cin >> n;
        cout << "Case #" << i << ": " << getTidyNumber(n) << endl;
    }
    return 0;
}
