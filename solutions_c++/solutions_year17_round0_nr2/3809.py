#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>
#include <iterator>

using namespace std;

bool checkIfTidy(string s) {
    int prev_digit = 10;
    while (s.length() != 0) {
        int digit = s[s.length() - 1] - '0';
        if (digit > prev_digit) {
            return false;
        }
        s = s.substr(0, s.length() - 1);
        prev_digit = digit;
    }
    return true;
}

string findLastTidyNumber(string s) {

    while (!checkIfTidy(s)) {
        int i = 0;
        while (i < s.length() - 1 && s[i + 1] >= s[i]) {
            i++;
        }
        int curr_digit = s[i] - '0';
        int next_digit = s[i + 1] - '0';
        if (next_digit < curr_digit) {
            s[i] = ('0' + (curr_digit - 1));     
            for (int j = i + 1; j < s.length(); j++) {
                s[j] = '9';                        
            }
        }
        if (s.length() > 1 && s[0] == '0') {
            s = s.substr(1, s.length() - 1);
        }
    }

    return s;
    
}

int main() {
    int n;
    cin >> n;
    vector<string> Z(n);
    for (int i = 0; i < n; i++) {
        cin >> Z[i];
    }

    for (int i = 0; i < n; i++) {
        cout << "Case #" << (i + 1) << ": ";
        string output = findLastTidyNumber(Z[i]);
        cout << output << endl;
    }
    return 0;
}
