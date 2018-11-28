#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for (int ii=1; ii<=t; ii++)
    {
        string s;
        int k;
        cin>>s>>k;
        int n=s.size();
        int cnt=0;

        for (int i=0; i+k<=n; i++)
        {
            if (s[i]=='+')
                continue;

            for (int j=i; j<i+k; j++)
                s[j]=(s[j]=='+' ? '-' : '+');
            cnt++;
        }

        bool good=true;
        for (int i=0; i<n; i++)
            if (s[i]=='-')
            {
                good=false;
                break;
            }
        cout<<"Case #"<<ii<<": ";
        if (good)   cout<<cnt<<endl;
        else        cout<<"IMPOSSIBLE"<<endl;
    }
}

