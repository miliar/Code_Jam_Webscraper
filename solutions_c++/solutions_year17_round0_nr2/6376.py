#include <iostream>

using namespace std;

bool istidy(string s) {
    for (int i = 0; i < s.length() - 1; i++) {
        if (s[i] > s[i + 1]) return false;
    }
    return true;
}

void gettidy(string &s) {
    for (int i = 0; i < s.length() - 1; i++) {
        if (s[i] > s[i + 1]) {
            s[i]--;
            for (int j = i + 1; j < s.length(); j++) s[j] = '9';
        }
    }
    if (!istidy(s)) gettidy(s);
}

int main() {
    long long t;
    cin >> t;
    long long x;
    string s;
    for (int i = 1; i <= t; i++) {
        cin >> x;
        s = to_string(x);
        cout << "Case #" << i << ": ";
        if (istidy(s)) cout << stoll(s) << endl;
        else {
            gettidy(s);
            cout <<fixed<< stoll(s) << endl;
        }
    }
}