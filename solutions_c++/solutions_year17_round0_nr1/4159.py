#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    for (int kase = 1; kase <= T; ++kase)
    {
        string s;
        int k;
        cin >> s >> k;
        int count = 0;
        for (int i = 0; i < s.length()-k+1; ++i)
        {   if (s[i] == '-')
            {
                count = count + 1;
                for (int j = 0; j < k; ++j)
                {
                    if (s[i+j] == '-')
                        s[i+j] = '+';
                    else 
                        s[i+j] = '-';
                }
            }
        }
        bool flag = true;
        for (int i = 0; i < s.length(); ++i)
            if (s[i] == '-')  { flag = false; break; }
        if (flag)
            cout << "Case #" << kase << ": " << count <<  endl;
        else 
            cout << "Case #" << kase << ": IMPOSSIBLE" << endl;
    }
}
