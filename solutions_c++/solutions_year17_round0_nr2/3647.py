#include <bits/stdc++.h>

using namespace std;

bool test(string &s) {
    for (int i = 1; i < s.size(); i++)
        if (s[i] < s[i-1]) return false;
    return true;
}

int main()
{
    int T, ans;
    string N;

    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        cin >> N;
        ans = 0;
        for (int j = N.size() - 1; j >= 0; j--)
        {
            int d;
            for (d = N[j]; d >= '0'; d--)
            {
                N[j] = d;
                if (test(N)) {
                    if (N[0] == '0') cout << N.substr(1, N.size() - 1) << endl;
                    else cout << N << endl;
                    ans = 1;
                    break;
                }
            }
            if (d < '0') {
                N[j] = '9';
                N[j-1]--;
            }
            if (ans) break;
        }
    }

    return 0;
}