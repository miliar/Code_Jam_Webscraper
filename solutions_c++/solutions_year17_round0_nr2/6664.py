#include <bits/stdc++.h>

using namespace std;

string n;
int t;

string to_string(long long n) {
    string s;
    while (n) {
        s.push_back('0' + n%10);
        n /= 10;
    }
    reverse(s.begin(), s.end());
    return s;
}

bool tidy(string s) {
    for (size_t i = 1; i < s.size(); ++i) {
        if (s[i-1] > s[i]) {
            return false;
        }
    }
    return true;
}

bool tidy(long long n) {
    string s = to_string(n);
    return tidy(s);
}

string solve(string s) {
    for (size_t i = 1; i < s.size(); ++i) {
        if (s[i-1] > s[i]) {
            --s[i-1];
            for (size_t j = i; j < s.size(); ++j) {
                s[j] = '9';
            }
            for (size_t j = i-1; j > 0; --j) {
                if (s[j] < s[j - 1]) {
                    --s[j - 1];
                    s[j] = '9';
                } else {
                    break;
                }
            }
            if (s[0] == '0') {
                string s2;
                for (size_t j = 0; j < s.size() - 1; ++j) {
                    s2.push_back('9');
                }
                return s2;
            }

            return s;
        }
    }
    return s;
}

int main()
{
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cin >> n;
        //n = to_string(rand() * 1.0 / __INT16_MAX__ * 1000000000000000000ll);
        //cerr << n << "\n";
        cout << "Case #" << i+1 << ": " << solve(n) << "\n";
    }

    return 0;
}
