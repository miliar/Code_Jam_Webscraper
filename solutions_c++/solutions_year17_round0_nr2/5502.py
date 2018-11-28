#include <bits/stdc++.h>

using namespace std;

bool is_tidy(string &s) {
    for (int i = 0; i < s.size() - 1; i++) {
        if (s[i] > s[i + 1])
            return false;
    }

    return true;
}

void make_tidier(string &s) {
    int last;
    for (int i = (s.size() - 2); i >= 0; i--) {
        if (s[i] > s[i + 1]) {
            last = i;
            break;
        }
    }

    s[last]--;
    for (int i = last+1; i < s.size(); i++) {
        s[i] = '9';
    }
}

string trim_zeroes(string s) {
    int start;
    for(int i = 0; i < s.size(); i++) {
        if (s[i] != '0') {
            start = i;
            break;
        }
    }
    string ans;

    for(int i = start; i < s.size(); i++) {
        ans.push_back(s[i]);
    }

    return ans;
}

int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        // scan input
        string s;
        cin >> s;

        // process input
        while (!is_tidy(s)) {
            make_tidier(s);
        }

        // print answer
        cout << "Case #" << i << ": " << trim_zeroes(s) << endl;
    }

    return 0;
}

