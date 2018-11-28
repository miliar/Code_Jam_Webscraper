#include <bits/stdc++.h>
#define ll long long int
#define mod 1000000007
using namespace std;

ll tt,t,k,n,ctr,ans,i,j,flag;
string str1,str2;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    tt=t;
    while(t)
    {
        cin>>str1>>k;
        str2=str1;
        n=str1.length();
        ctr=0;
        flag=1;
        ans=1000000;
        for(i=0;i<n-k+1;i++)
        {
            if(str1[i]=='-')
            {
                ctr++;
                for(j=i;j<i+k;j++)
                {
                    if(str1[j]=='-')
                        str1[j]='+';
                    else
                        str1[j]='-';
                }
            }
        }
        for(i=0;i<n;i++)
        {
            if(str1[i]=='-')
                break;
        }
        if(i==n)
        {
            flag=0;
            ans=ctr;
        }

        ctr=0;
        for(i=n-1;i>=k-1;i--)
        {
            if(str2[i]=='-')
            {
                ctr++;
                for(j=i;j>i-k;j--)
                {
                    if(str2[j]=='-')
                        str2[j]='+';
                    else
                        str2[j]='-';
                }
            }
        }

        for(i=0;i<n;i++)
        {
            if(str1[i]=='-')
                break;
        }
        if(i==n)
        {
            flag=0;
            ans=min(ans,ctr);
        }
        if(flag)
            cout<<"Case #"<<tt-t+1<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<tt-t+1<<": "<<ans<<endl;
        t--;

    }

    return 0;
}
