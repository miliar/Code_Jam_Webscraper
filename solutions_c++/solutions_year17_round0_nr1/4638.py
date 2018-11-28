#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t)
    {
        string s;
        cin >> s;

        int k;
        cin >> k;

        int i = 0;
        bool possible = true;
        int count = 0;
        while(true)
        {
            if (i >= s.size())
                break;

            if (s[i] == '+')
            {
                ++i;
                continue;
            }

            for (int j = i; j < i + k; ++j)
            {
                if (j >= s.size())
                {
                    possible = false;
                    break;
                }

                s[j] = (s[j] == '+') ? '-' : '+';
            }
            ++count;
        }

        cout << "Case #" << t + 1 << ": ";
        if (possible)
            cout << count << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}
