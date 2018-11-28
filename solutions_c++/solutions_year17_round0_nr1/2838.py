#include <bits/stdc++.h>
using namespace std;
void go(int cnum)
{
    int k;
    string s;
    cin >> s >> k;
    cout << "Case #" << cnum << ": ";
    int res = 0;
    for(int i=0; i<=s.size()-k; i++)
    {
        if(s[i] == '-')
        {
            res++;
            for(int j=i; j<i+k; j++)
            {
                if(s[j] == '-')
                    s[j] = '+';
                else s[j] = '-';
            }
        }
    }
    for(auto &i: s)
    {
        if(i == '-')
        {
            cout << "IMPOSSIBLE\n";
            return;
        }
    }
    cout << res << "\n";
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i=1; i<=t; i++)
        go(i);
    return 0;
}
