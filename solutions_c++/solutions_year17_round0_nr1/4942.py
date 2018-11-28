#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int test = 1; test < T + 1; ++test)
    {
        string s;
        int k;
        cin >> s >> k;

        int counter = 0;
        int i = 0;
        for (; (int) s.length() - i >= k; ++i)
        {
            if (s[i] == '-')
            {
                ++counter;
                for (int j = i; j < i + k; ++j)
                {
                    s[j] = s[j] == '-' ? '+' : '-';
                }
            }
        }

        bool ans = true;
        for (; i < (int) s.length(); ++i)
        {
            if (s[i] == '-')
            {
                ans = false;
                break;
            }
        }

        std::cout << "Case #" << test << ": ";
        if (ans)
        {
            std::cout << counter << std::endl;
        }
        else
        {
            std::cout << "IMPOSSIBLE" << std::endl;
        }
    }

    return 0;
}
