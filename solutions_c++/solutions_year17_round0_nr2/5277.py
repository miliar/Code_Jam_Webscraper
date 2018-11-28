#include <bits/stdc++.h>
using namespace std;
#define forn(i,n) for(int i=0; i < n; i++)
#define vvi vector<vector<int>>
#define vi vector<int>



int main() {
#ifndef ONLINE_JUDGE
   freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int TEST;
    cin >> TEST;
    forn(test, TEST)
    {
        string s;
        cin >> s;
        if (s.length() > 1)
        {
            char last = s[s.length() - 1];
            for (int i = s.length() - 2; i >= 0; i--)
            {
                if (s[i] > last)
                {
                    for (int j = i + 1; j < s.length(); j++)
                    {
                        s[j] = '9';
                    }
                    s[i] = s[i] - 1;
                }
                last = s[i];
            }
        }
        while (s[0] == '0')
        {
            s.erase(0, 1);
        }



        printf("Case #%d: ", test + 1);
        cout << s << endl;
    }


    return 0;
}