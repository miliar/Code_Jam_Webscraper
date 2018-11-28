#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int caso = 1; caso <= t; caso++)
    {
        string s;
        cin >> s;
        for(int i = s.size() - 1; i >= 1; i--)
        {
            if(s[i - 1] <= s[i])
                continue;
            s[i - 1]--;
            for(int j = i; j < s.size(); j++)
                s[j] = '9';
        }
        if(s[0] == '0')
            s.erase(s.begin());
        cout << "Case #" << caso << ": " << s << endl;
    }
    return 0;
}
