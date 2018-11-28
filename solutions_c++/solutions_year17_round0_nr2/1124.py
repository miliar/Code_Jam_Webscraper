#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int ct = 1; ct <= T; ct++)
    {
        string s;
        cin >> s;
        int n = s.size();

        ll ans = 1;

        bool tidy = true;
        for(int i = 0; i < n; i++)
        {
            if((s[i] != '0') && ((i == 0) || (s[i] > s[i-1])))
            {
                string t = s;
                t[i]--;
                for(int j = i+1; j < n; j++)
                    t[j] = '9';

                 ans = max(ans, strtoll (t.c_str(), NULL, 10));
            }

            if((i < n-1) && s[i] > s[i+1])
            {
                tidy = false;
                break;
            }
        }

        if(tidy)
            ans = strtoll (s.c_str(), NULL, 10);

        printf("Case #%d: %lld\n", ct, ans);
    }

    return 0;
}
