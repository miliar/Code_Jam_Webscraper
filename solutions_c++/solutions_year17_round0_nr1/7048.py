#include <iostream>
#include <string>
using namespace std;

int calc(string& s, int k) {
    int ret = 0;
    int l = -1;
    int i = 0;
    for (i=0; i<s.length() - (k - 1);) {
        if (s[i] == '-') {
            ret += 1;
            int j = 0;
            l = -1;
            while (j < k) {
                if (s[i + j] == '+') {
                    s[i+j] = '-';
                    if (l == -1)
                        l = i + j;
                }
                else {
                    s[i+j] = '+';
                }
                ++j;
            }
            if (l == -1) {
                i += k;
            }
            else {
                i = l;
            }
        }
        else {
            i += 1;
        }
    }
    if (l != -1) {
        ret = -1;
    }
    while (i < s.length()) {
        if (s[i] != '+') {
            ret = -1;
            break;
        }
        ++i;
    }
    return ret;
}

int main()
{
    int T;
    cin >> T;
    for (int i=0; i<T; ++i) {
        string S;
        cin >> S;
        int K;
        cin >> K;
        cout << "Case #" << i + 1 << ": ";
        int r = calc(S, K);
        if (r >=0) {
            cout << r;
        }
        else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }
    return 0;
}
