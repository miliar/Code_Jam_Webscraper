#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb push_back
#define mp make_pair

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    ll test,t,ans,k,n,i,j;
    char s[100005];
    cin>>test;
    for(t=1;t<=test;t++)
    {
        ans = 0;
        cin>>s;
        cin>>k;
        n = strlen(s);

        for(i=0;i<=n-k;i++)
        {
            if(s[i]=='-')
            {
                ans++;
                for(j=i;j<(i+k);j++)
                {
                    if(s[j]=='-')
                        s[j] = '+';
                    else if(s[j]=='+')
                        s[j] = '-';
                }
            }
        }

        for(i=0;i<n;i++)
        {
            if(s[i]=='-')
                break;
        }

        if(i<n)
        {
            ans = 0;
            for(i=n-1;i>=k-1;i--)
            {
                if(s[i]=='-')
                {
                    ans++;
                    for(j=i;j>(i-k);j--)
                    {
                        if(s[j]=='-')
                            s[j] = '+';
                        else if(s[j]=='+')
                            s[j] = '-';
                    }
                }
            }

            for(i=0;i<n;i++)
            {
                if(s[i]=='-')
                    break;
            }
            if(i<n)
                cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
            else
                cout<<"Case #"<<t<<": "<<ans<<endl;
        }
        else
            cout<<"Case #"<<t<<": "<<ans<<endl;
    }

    return 0;
}













