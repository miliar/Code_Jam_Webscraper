#include<bits/stdc++.h>
using namespace std;

//unsigned long long dp[400][20];

int main()
{
    int i,j,k,n,m;
    int testcase,test=0,temp;
    string s;

    cin>>testcase;

    while(test++ < testcase)
    {
        cin>>s;
        bool tr = true;

        for(i=0;i<s.size()-1;i++)
        {
            if(s[i]<=s[i+1])continue;
            else
            {
                tr=false;
                break;
            }
        }

        printf("Case #%d: ",test);

        if(tr)
        {
            cout<<s<<endl;
            continue;
        }
        while(i>0)
        {
            if(s[i]==s[i-1])i--;
            else break;
        }
        s[i]-=1;

        for(i=i+1;i<s.size();i++)s[i]='9';

        while(s[0]=='0')
        {
            s.erase(s.begin());
        }

        cout<<s<<endl;
    }

    return 0;
}
