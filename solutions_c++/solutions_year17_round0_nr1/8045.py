#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long int ll;

main()
{
    string str;
    ll t, k, cases=1;
    cin >> t;

    while(t--)
    {
        cin.ignore();
        cin >> str >> k;

        ll cont = 0;
        for(ll i = 0; i <= str.size()-k; i++)
        {
            //cout << i << " " << str << endl;
            if(str[i] == '-')
            {
                cont++;
                for(ll j = 0; j < k; j++)
                {
                    if(str[i+j] == '-') str[i+j] = '+';
                    else str[i+j] = '-';
                }
                i = 0;
            }
        }

        bool flag = true;
        for(ll i = 0; i < str.size(); i++)
            if(str[i] == '-')
                flag = false;

        if(flag)
            cout << "Case #" << cases++ << ": " << cont << endl;
        else
            cout << "Case #" << cases++ << ": IMPOSSIBLE" << endl;
    }
}
