#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T;

    cin >> T;
    for(int t=1; t <= T; ++t)
    {
        string s;
        int k;
        cin >> s >> k;

        bool impossible = false;
        int res = 0;
        for(int i=0; i < s.size(); ++i)
        {
            if(s[i] == '-')
            {
                if(i+k > s.size())
                {
                    impossible = true;
                    break;
                }
                else
                {
                    for(int j=0; j < k; ++j)
                    {
                        s[i+j] = (s[i+j] == '+' ? '-' : '+');
                    }
                    res++;
                }
            }
        }

        cout << "Case #" << t << ": ";
        if(impossible)
        {
            cout << "IMPOSSIBLE" << endl;
        }
        else
        {
            cout << res << endl;
        }

    }

    return 0;
}
