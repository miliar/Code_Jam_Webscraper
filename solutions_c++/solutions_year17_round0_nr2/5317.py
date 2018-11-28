#include <bits/stdc++.h>

using namespace std;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("1.out", "w", stdout);

    int tests;
    cin >> tests;

    for (int testNum = 1; testNum <= tests; ++testNum)
    {
        string s;
        cin >> s;

        while(1)
        {
            bool p = 0;
            for (int i = 1; i < s.size(); ++i)
                if (s[i - 1] > s[i])
                {
                    p = 1;
                    if (s[i - 1] != '0')
                    {
                        --s[i - 1];
                        for (int j = i; j < s.size(); ++j)
                            s[j] = '9';
                        break;
                    }

                }
            while(s.size() > 1 && s[0] == '0') s.erase(s.begin()), p = 1;

            if (!p) break;
        }

        cout << "Case #" << testNum << ": " << s << "\n";
    }
}
