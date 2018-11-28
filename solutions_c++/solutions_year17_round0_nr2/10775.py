#include <bits/stdc++.h>

using namespace std;

bool valid(string S)
{
    if (S.size() <= 1)
        return true;
    bool rc = true;
    char prev = S[0];
    int len = S.size();
    for (int i = 1; i < len; i ++) {
        if (prev > S[i]) {
            rc = false;
        }
        prev = S[i];
    }
    return rc;
}

int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; t ++) {
        printf("Case #%d: ", t);

        unsigned long long num;
        cin >> num;

        if (num < 10) {
            cout << num << endl;
        } else {
            while (!valid(to_string(num))) {
                num --;
            }
            cout << num << endl;
        }
    }

    return 0;
}

