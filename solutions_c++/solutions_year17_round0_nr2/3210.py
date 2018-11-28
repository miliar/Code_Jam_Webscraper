#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

bool issorted(string s) {
    for (int i = 1; i < s.length(); i++) {
       if (s[i] < s[i - 1]) {
           return false;
       }
    }

    return true;
}

string _9(int x) {
    string res;
    for (int i = 0; i < x; i++)
        res += '9';

    return res;
}

#define INPUT     ""
#define OUTPUT    ""

int main() {
    // freopen(INPUT, "r", stdin);
    // freopen(OUTPUT, "w", stdout);

    int nTest;
    scanf("%d", &nTest);

    for (int test = 0; test < nTest; test++) {
        long long number;
        scanf("%lld", &number);

        string n = to_string(number);

        string res = n;
        if (issorted(res)) goto exit;
        for (int i = n.length(); i > 0; i--) {
            int digit = n[i - 1] - '0';

            if (digit == 0)
                continue;

            digit--;

            if (!issorted(n.substr(0, i - 1) + to_string(digit)))
                continue;

            if (digit == 0 && i == 1) {
                res = _9(n.length() - 1);
            }
            else {
                res = n.substr(0, i - 1) + to_string(digit) + _9(n.length() - i);
            }
            break;
        }

        exit:
        printf("Case #%d: %s\n", test + 1, res.c_str());
    }

    return 0;
}
