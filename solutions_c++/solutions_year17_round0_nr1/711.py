#include <iostream>
#include <cstdio>
#include <string>

#define INF 1000000000

using namespace std;

char flip(char c)
{
    if (c == '+')
        return '-';
    return '+';
}

int main()
{
    int t;
    cin >> t;
    for (int tidx = 1; tidx <= t; ++tidx)
    {
        string s;
        int k;
        cin >> s;
        cin >> k;
        int n = s.size();
        int d = 0;

        for (int i=0; i<(n - k + 1); ++i)
        {
            if (s[i] == '-')
            {
                for (int j=0; j<k; ++j)
                    s[i + j] = flip(s[i + j]);
                ++d;
            }
        }

        bool impossible = false;
        for (int i=0; i<n; ++i)
            if (s[i] == '-')
                impossible = true;

        printf("Case #%d: ", tidx);
        if (impossible)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", d);
    }
    return 0;
}
