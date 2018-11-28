#include <iostream>
#include <string>

typedef uint64_t llu;
typedef int64_t ll;

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int c = 0; c < t; c++)
    {
        llu ans = 0, n = 0;
        string s;

        cin >> s;
        cin >> n;

        int idx = 0;

        while ((s.size() - idx) >= n)
        {
            if (s[idx] == '+')
            {
                idx++;
            }
            else
            {
                for (int i = idx; i < idx + n; i++)
                {
                    s[i] = s[i] == '+' ? '-' : '+';
                }
                idx++;
                ans++;
            }
        }

        bool passed = true;
        for (unsigned int i = idx; i < s.size(); i++)
        {
            if (s[i] == '-')
            {
                passed = false;
                break;
            }
        }

        if (passed == false)
        {
            cout << "Case #" << c + 1 << ": IMPOSSIBLE" << endl;
        }
        else
        {
            cout << "Case #" << c + 1 << ": " << ans << endl;
        }
    }

    return 0;
}