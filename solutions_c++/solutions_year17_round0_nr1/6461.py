#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int Case = 1; Case <= T; ++Case)
    {
        string s;
        int k;
        cin >> s >> k;

        int ans = 0;
        for(int i = 0; i <= s.size() - k; ++i)
        {
            if(s[i] == '-')
            {
                for(int j = 0; j < k; ++j)
                {
                    if(s[i + j] == '-') s[i + j] = '+';
                    else s[i + j] = '-';
                }
                ++ans;
            }
        }

        bool imposs = false;
        for(int i = s.size() - k; i < s.size(); ++i)
        {
            if(s[i] == '-')
            {
                imposs = true;
                break;
            }
        }

        cout << "Case #" << Case << ": ";
        if(imposs) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;

    }
    return 0;
}