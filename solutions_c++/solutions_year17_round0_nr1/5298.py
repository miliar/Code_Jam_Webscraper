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
        int k;
        cin >> k;
        int flips = 0;
        forn(i, s.length() - k + 1)
        {
            if (s[i] == '-')
            {
                flips++;
                forn(j,k)
                {
                    if (s[i+j] == '-') s[i+j]='+';
                    else s[i+j] = '-';
                }
            }
        }
        printf("Case #%d: ", test + 1);
        bool good = true;
        for (int i = s.length() - k + 1; i < s.length(); i++)
        {
            if (s[i] == '-') good = false;
        }
        if (good)
        {
            printf("%d\n", flips);
        } else
            printf("IMPOSSIBLE\n");
    }


    return 0;
}