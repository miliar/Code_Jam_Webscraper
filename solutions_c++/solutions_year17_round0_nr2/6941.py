#include <bits/stdc++.h>

using namespace std;

string solve(string s)
{
    for (int i = s.size()-2; i>=0; --i) {
        if (s[i] > s[i+1]) {
            s[i] = s[i]-1;
            for (int j = i+1; j < s.size(); ++j) {
                s[j] = '9';
            }
        }
    }

    if (s[0] == '0') {
        return s.substr(1);
    } else {
        return s;
    }
}

int main() {
    int case_num;
    cin >> case_num;

    for (int i = 0; i < case_num; ++i) {
        string x; cin >> x;
        cout << "Case #" << i+1 << ": " << solve(x) << endl;
    }

    return 0;
}
