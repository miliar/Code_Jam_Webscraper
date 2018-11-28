#include <iostream>
#include <cstring>
using namespace std;

int T;
char s[1001];

int main()
{
    int k;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> s >> k;
        cout << "Case #" << t << ": ";
        int cnt = 0, l = strlen(s);
        for (int i = 0; i < l - k + 1; ++i)
            if (s[i] == '-')
            {
                ++cnt;
                for (int j = 0; j < k; ++j)
                    s[i + j] = (s[i + j]=='-')?'+':'-';
            }
        bool imp = false;
        for (int i = 0; i < k - 1; ++i)
            if (s[l - 1 - i] == '-')
            {
                imp = true;
                break;
            }
        if (imp)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << cnt << endl;
    }
}
