#include<bits/stdc++.h>
using namespace std;
int main()
{

    long long int u,k,t,l,i,j,a,b,ans,flag;
    char s[2004];
    cin>>t;
    for( u=1;u<=t;u++)
    {
        ans=0;
        cin>>s>>k;
        l=strlen(s);
        int flag=0;
        for(i=l-1;i>=0;i--)
        {
            if(s[i]=='+')
            {
                continue;
            }
            else if(s[i]=='-')
            {
                for(j=i;j>i-k;j--)
                {
                    if(j<0)
                    {
                        flag=1;
                        cout<<"Case #"<<u<<": "<<"IMPOSSIBLE"<<endl;
                        break;
                    }
                    if(s[j]=='+')
                    {
                        s[j]='-';
                    }
                    else if(s[j]=='-')
                    {
                        s[j]='+';
                    }
                }

                ans++;
            }
            if(flag==1)
            {
                break;
            }

        }

        /*for(i=0;i<l;i++)
        {
            if(s[i]=='-')
            {
                flag=1;
                cout<<"IMPOSSIBLE"<<endl;
                break;
            }
        }*/
        if(flag==0)
        {
            cout<<"Case #"<<u<<": "<<ans<<endl;
        }
    }
    return 0;
}

