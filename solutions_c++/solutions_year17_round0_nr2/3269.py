#include <iostream>

using namespace std;

typedef unsigned long long ull;

int main()
{
    int T;
    cin >> T;

    for(int t = 1; t <= T; t++)
    {
        ull N;
        cin >> N;

        string s = to_string(N);
        int n = s.length();

        for(int i = n - 1; i > 0; i--)
        {
            if(s[i] == '9') continue;
            
            bool found = false;
            for(int j = 0; j < i; j++)
            {
                if(s[j] > s[j + 1]) found = true;
            }
            if(!found) break;

            s[i] = '9';
            for(int j = i - 1; j >= 0; j--)
            {
                if(s[j] != '0')
                {
                    s[j] = s[j] - 1;
                    break;
                }
                else s[j] = '9';
            }
        }

        ull res = stoull(s);
        cout << "Case #" << t << ": " << res << endl;
    }

    return 0;
}