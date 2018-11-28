#include<iostream>

using namespace std;

int main(void)
{
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        string s;
        int k;
        cin >> s;
        cin >> k;
        int res = 0;
        for (int j=0; j<s.length()-k+1; j++) {
            if (s[j] == '+') continue;
            res++;
            for (int t = j; t<j+k; t++)
                if (s[t] == '+')
                    s[t] = '-';
                else
                    s[t] = '+';
        }
        for (int j=s.length()-k; j<s.length(); j++) {
            if (s[j] == '-') {
                res = -1;
                break;
            }
        }
        if (res >= 0)
            cout << "Case #" << i+1 << ": " << res << endl;
        else
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
    }
    return 0;
}
