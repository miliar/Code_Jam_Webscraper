#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

void solve()
{
    string s;
    cin >> s;

    for (int i = 0; i < s.size() - 1; i++) {
        if (s[i] - '0' > s[i + 1] - '0')
        {
            int j;
            for (j = i; j >= 0 && (s[j] == s[i]); j--);

            j++;
            s[j] = (s[j] - 1);
            for (j = j + 1; j < s.size(); j++) {
                s[j] = '9';
            }
        }
    }

    bool leadingZero = true;
    for (int i = 0; i < s.size(); i++) {
        if (leadingZero && s[i] == '0') {
            continue;
        } else {
            leadingZero = false;
            cout << s[i];
        }
    }
    cout << endl;
}

int main()
{
    freopen("tidy.in", "r", stdin);
    freopen("tidy.out", "w", stdout);

    int T;
    scanf("%d ", &T);
    for (int i = 0; i < T; i++)
    {
        cout << "CASE #" << i + 1 << ": ";
        solve();
    }
}
