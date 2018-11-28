#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++)
    {
        string str;
        cin >> str;
        int len = str.length();
        bool flag = true, first = false;
        cout << "Case #" << cas << ": ";
        for (int i = 0; i < len; i++)
        {
            if (flag)
            {
                for (int j = i + 1; j < len && flag; j++)
                    if (str[j] < str[i])
                        flag = false;
                    else if (str[j] > str[i])
                        break;
                if (!flag)
                {
                    if (first || str[i] != '1')
                    {
                        cout << (char)(str[i] - 1);
                        first = true;
                    }
                }
                else
                    cout << str[i];
            }
            else
            {
                cout << 9;
            }
        }
        cout << endl;
    }
    return 0;
}
