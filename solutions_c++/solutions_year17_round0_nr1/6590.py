#include<bits/stdc++.h>
using namespace std;
int main()
{
    long int t,k,i,j,x;
    char s[1000];
    freopen("test1.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    cin>>t;
    for(x=1;x<=t;x++)
    {
        cin>>s;
        cout<<"Case #"<<x<<": ";
        long int flag=0,ans=0;
        int l=strlen(s);
        cin>>k;
        for(i=0;i<=l-k;i++)
        {
            if(s[i]=='+')
                continue;
            else
            {
                ans++;
                for(j=i;j<i+k;j++)
                {
                    if(s[j]=='-')
                    {
                        s[j]='+';
                    }
                    else
                        s[j]='-';
                }
            }
        }
        for(i=0;i<l;i++)
        {
            if(s[i]=='-')
            {
                flag=1;
                break;
            }
        }
        //cout<<s<<endl;
        if(flag==1)
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            cout<<ans<<endl;
        }
    }
}
