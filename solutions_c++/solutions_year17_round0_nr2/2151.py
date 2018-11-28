#include <iostream>
using namespace std;


void first_tidy(string& s) {
    int i = 0;
    for(int j = 1; j < s.size(); ++j) {
        if(s[i] > s[j]) {
            s[i] -= 1;
            for(int k = i+1; k < s.size(); ++k) {
                s[k] = '9';
            }
        } else if(s[i] < s[j]) {
            i = j;
        }
    }
}

int main() {
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        string s;
        cin >> s;
        first_tidy(s);
        cout << "Case #" << i << ": ";
        bool first = true;
        for(int j = 0; j < s.size(); ++j) {
            if(!first || s[j] != '0') {
                first = false;
                cout << s[j];
            }
        }
        cout << endl;
    }
}