#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;

    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        std::string s;
        size_t k;
        cin >> s >> k;
        int cnt = 0;
        for (size_t j = 0; j < s.length(); ++j)
        {
            if (s[j] == '-')
            {
                if (j + k > s.length())
                {
                    cnt = -1;
                    break;
                }
                cnt ++;
                for (size_t l = 0; l < k; ++l)
                {
                    s[j + l] ^= '+' ^ '-';
                }
            }
        }
        if (cnt == -1)
        {
            cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
        }
        else
        {
            cout << "Case #" << (i + 1) << ": " << cnt << endl;
        }
    }
    return 0;
}
