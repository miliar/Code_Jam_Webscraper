#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    int T,n,k,ans,ntest=1;
    bool posible;
    string s;
    cin >> T;
    while(T--)
    {
        cin >> s >> k;
        n = s.size();
        ans = 0;
        for(int i = 0; i <= n - k; i++)
            if(s[i] == '-')
            {
                ans++;
                for(int j = i + 1; j < i + k; j++)
                    if(s[j] == '+')
                        s[j] = '-';
                    else
                        s[j] = '+';
            }

        posible = true;
        for(int i = n - k + 1; i < n; i++)
            if(s[i] == '-')
                posible = false;

        cout << "Case #" << ntest++ << ": ";
        if(!posible)
            cout << "IMPOSSIBLE" << '\n';
        else
            cout << ans << '\n';
    }
    return 0;
}