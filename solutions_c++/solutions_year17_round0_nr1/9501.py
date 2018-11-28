#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int case_no = 1;
    while(n--)
    {
        string s;
        cin >> s;
        int k;
        cin >> k;
        int ans = 0;
        for(int i = 0;i < (s.length() - k + 1);++i)
        {
            if(s[i] == '-')
            {
                ans+=1;
                for(int j = i;j < (i + k);++j)
                {
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
            }
        }
        bool flg = 0;
        cout << "Case #" << case_no++ << ": ";
        for(int i = 0;i < s.length();++i)
        {
            if(s[i] == '-')
            {
                flg = 1;
                cout << "impossible\n";
                break;
            }
        }
        if(!flg)
        {
            cout << ans << '\n';
        }
    }
    return 0;
}