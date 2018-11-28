#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    int t,j;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        int k,l,ans=0,i,a;
        char s[1001];
        cin>>s;
        cin>>k;
        l=strlen(s);
        ans=0;
        for(i=0;i<=l-k;i++)
        {
            if(s[i]=='-')
            {
                for(a=i;a<i+k;a++)
                    if(s[a]=='+')
                        s[a]='-';
                    else
                        s[a]='+';
                ans++;
            }
        }
        for(i=0;i<l;i++)
            if(s[i]=='-')
                break;
        if(i==l)
            cout<<"Case #"<<j<<": "<<ans<<endl;
        else
            cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}


