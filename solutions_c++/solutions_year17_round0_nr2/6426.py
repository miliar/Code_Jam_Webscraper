#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int Case = 1; Case <= T; ++Case)
    {
        string s;
        cin >> s;

        long long ans = atoll(s.c_str());
        long long tmp = atoll(s.c_str());
        long long mul = 1;

        for(int i = 0; i < s.size(); ++i)
        {
            for(int j = 0; j < s.size() - 1; ++j)
            {
                if(s[j] > s[j + 1])
                {
                    ans -= ((tmp % 10) + 1) * mul;
                    tmp -= (tmp % 10) + 1;
                    s = to_string(ans);
                    break;
                }
            }
            tmp /= 10;
            mul *= 10;
        }


        cout << "Case #" << Case << ": " << ans << endl;
    }
    return 0;
}