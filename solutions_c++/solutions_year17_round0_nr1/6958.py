#include <bits/stdc++.h>
typedef long long ll;
const int MAX =1e6 +10;
using namespace std;

int main()
{
    int t ;
    scanf("%d",&t);
    for(int u=1;u<=t;u++)
    {
        string s; int k; ;
        cin>>s>>k;
        if(k>s.size())
        {
            bool flg = 0;
            for(int i=0;i<s.size();i++)
            {
                if(s[i] == '-')
                {
                    flg = 1;
                    break;
                }
            }
            if(flg)
                cout << "Case #" << u << ": "<< "IMPOSSIBLE"<< endl;
            else
                cout << "Case #" << u << ": "<<"0"<< endl;
            continue;
        }
        int ans = 0;
        for(int i=0;i<s.size() - k+1;i++)
        {
            if(s[i] == '-')
            {
                ans++;
                for(int j = i;j<i+k; j++)
                {
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
            }

        }
        //for(int i=0;i<s.size();i++)
            //cout<<s[i];
        //cout<<endl;
        bool fl = 0;
        for(int i=s.size()-k+1;i<s.size();i++)
        {
            if(s[i] == '-')
            {
                fl = 1;
                break;
            }
        }
        if(!fl)
            cout << "Case #" << u << ": " << ans << endl;
        else
            cout << "Case #" << u << ": "<< "IMPOSSIBLE"<< endl;

    }
    return 0;
}
