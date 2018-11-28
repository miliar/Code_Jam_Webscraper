#include <bits/stdc++.h>

using namespace std;

int main()
{
   freopen("A-large.in","r",stdin);
    freopen("a.txt","w",stdout);
    int t;
    cin>>t;
    int c=1;
    while(t--)
    {
        string s;
        int n;
        cin>>s>>n;
        bool f=0;
        int count=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-'&& i+n<=s.size())
            {
                count++;
               // cout<<i<<endl;

                for(int j=i;j<i+n;j++)
            {
                if(s[j]=='+')
                    s[j]='-';
                else if(s[j]=='-')
                    s[j]='+';
                    //cout<<j<<" "<<s<<endl;
            }
            }
            else if(s[i]=='-'&& i+n>s.size())
               {
                   f=1;
                   break;
               }
        }
        if(f==0)
            cout<<"Case #"<<c<<": "<<count<<endl;
        if(f==1)
            cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
    c++;
   }
    return 0;
}
