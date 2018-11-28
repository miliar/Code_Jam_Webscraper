#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

#define INF 1000000000

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int tidx = 1; tidx <= t; ++tidx)
    {
        string s;
        cin >> s;
        int n = s.size();
        reverse(s.begin(), s.end());

        for (int i=0; i<n-1; ++i)
        {
            if (s[i] < s[i+1])
            {
                for (int j=0; j<=i; ++j)
                    s[j] = '9';
                --s[i+1];
            }
        }

        if (s[n-1] == '0')
            s.pop_back();
        reverse(s.begin(), s.end());

        printf("Case #%d: %s\n", tidx, s.c_str());
    }
    return 0;
}
