#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    string s;
    int t,x,ans=0,br=0;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        cin>>s>>x;
        for(int j=0; j<s.length()-x+1; j++)
        {
            ///cout<<j<<endl;
            if(s[j]=='-')
            {
                ///cout<<j<<endl;
                for(int k=j; k<j+x; k++)
                    if(s[k]=='-')
                        s[k]='+';
                    else
                        s[k]='-';
                        ans++;
            }
        }
        for(int j=0;j<s.length();j++)
            if(s[j]=='+')
            br++;

        ///cout<<br<<endl;
        cout<<"case #"<<i+1<<": ";
        if(br==s.length())
        cout<<ans<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
        ans=0;
            br=0;
    }
}
