#include <cstdint>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; t++)
    {
        uint64_t N;
        cin >> N;

        string sN = to_string(N);

        string res = sN;
        for (size_t i = 0; i < sN.size()-1; i++)
        {
            for (size_t j = 0; j < sN.size()-1; j++)
            {
                int c = abs((int)('0' - res[j]));
                int n = abs((int)('0' - res[j+1]));
                if (n < c)
                {
                    res[j] = (c-1) + '0';
                    for (size_t k = j+1; k < sN.size(); k++)
                        res[k] = '9';
                    break;
                }
            }
        }

        size_t first = 0;
        for (size_t i = 0; i < sN.size(); i++)
        {
            if (res[i] == '0')
                first = i+1;
            else
                break;
        }
        res = res.substr(first);

        cout << "Case #" << t+1 << ": " << res << endl;
    }
}
