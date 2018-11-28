#include <iostream>
using namespace std;
int main() {
    int T;
    cin >> T;
    string s;
    int n;
    int a[1003];
    for (int I = 1; I <= T; ++I)
    {
        cin >> s >> n;
        for (int i = 0; i < s.size(); ++i)
        {
            a[i] = (s[i] == '+' ? 1 : 0);
        }
        int cnt = 0;
        for (int i = 0; i <= s.size() - n; ++i)
            if (a[i] == 0)
            {
                cnt++;
                for (int j = i; j < i + n; ++j)
                    a[j] = 1 - a[j];
//               for (int i = 0; i < s.size(); ++i ) cout << a[i]; cout << endl;
            }
        bool possible = true;
        for (int i = 0; i < s.size(); ++i)
            if (a[i] == 0)
                possible = false;
        cout << "Case #" << I << ": ";
        if (!possible)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << cnt << endl;
    }

}

