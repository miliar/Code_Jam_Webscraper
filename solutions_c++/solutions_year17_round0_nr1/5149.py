#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("A-large.out","wt",stdout);
    int t;
    cin >> t;
    for(int w = 1; w <= t; w++)
    {
        string s;
        cin >> s;
        int k;
        cin >> k;
        int res = 0;
        for(int i = 0; i < s.size()-k+1;i++)
        {
            char c = s[i];
            if(s[i] == '-')
            {
                res++;
                for(int j = i; j < i+k; j++)
                {
                    if(s[j] == '-')
                        s[j] = '+';
                    else if(s[j] == '+')
                        s[j] = '-';
                }
            }
        }
        bool right = true;
        for(int i = 0;i < s.size();i++)
        {
            if(s[i] == '-')
                right = false;
        }
        if(!right)
            cout << "Case #"<<w<<": "<< "IMPOSSIBLE\n";
        else
            cout << "Case #"<<w<<": " << res <<endl;
    }
    return 0;
}
