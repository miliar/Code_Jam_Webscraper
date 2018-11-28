#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("Ai.in","r",stdin);
    freopen("A.out","w",stdout);
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        string s;
        int k;
        cin>>s>>k;
        int an=0;
        for(int i=0;i+k-1<s.length();i++)
        {
            if(s[i]=='-')
            {
                an++;
                for(int j=i;j<=i+k-1;j++)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
            }
        }
        int u=0;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                u=1;
                break;

            }
        }
        cout<<"Case #"<<tt<<": ";
        if(u)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<an<<endl;
    }
}
