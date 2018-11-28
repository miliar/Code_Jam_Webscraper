#include<iostream>
#include <cstdio>
#include <string>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("CJ17_2.out","w",stdout);
    int t;
    cin>>t;
    for(int x=1;x<=t;x++)
    {

        string s;
        cin>>s;

        for(int i=s.length()-1;i>0;i--)
        {
            if(s[i-1]>s[i])
            {
                for(int j=i;j<s.length();j++)
                    s[j]='9';
                if(s[i-1]==0)
                    s[i-1]='9';
                else
                    s[i-1]=s[i-1]-1;
            }

        }
        cout<<"Case #"<<x<<": ";
        if(s[0]=='0')
            cout<<s.substr(1)<<endl;
        else
            cout<<s<<endl;
    }
    return 0;

}
