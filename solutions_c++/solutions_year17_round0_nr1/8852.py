#include <iostream>

using namespace std;

int main()
{
    int t, m = 0;
    cin >> t;
    while(t--)
    {
        m++;
        string s;
        cin >> s;
        int k, ctr = 0;
        cin >> k;
        int i = s.length();
        while (i-- >= k)
        {
            if(s[i] == '-')
            {
                for (int j = i; j > i - k; j--)
                    s[j] = (s[j] == '+' ? '-' : '+');
                ctr++;
            }
        }
        i = s.length();
        while(i--)
            if(s[i] == '-')
                ctr = -1;
        cout << "Case #" << m << ": ";
        ctr == -1 ? cout << "IMPOSSIBLE" : cout << ctr;
        cout << endl;
    }
    return 0;
}

