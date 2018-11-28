
#include<bits/stdc++.h>
using namespace std;
string s,ss;

int main()
{
    int p,m,t,n,ans,i,j,k,rr=0;
    cin>>t;
    while(t--)
    {
        cin>>s;
        cin>>k;
        n=s.size();
        ans=0;
        p=0;m=0;
        for(i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                ans++;
                p=-1;
                for(j=i;j<i+k&&j<n;j++)
                {
                    if(s[j]=='+'&&p==-1)
                        p=j;
                    if(s[j]=='+')
                        s[j]='-';
                    else if(s[j]=='-')
                        m++,s[j]='+';
                }
                if(j==i+k)
                    m=0;
                if(p==-1)
                    i=j-1;
                else
                    i=p-1;
            }
        }
        rr++;
        if(m>0)
            cout<<"Case #"<<rr<<": IMPOSSIBLE\n";
        else
            cout<<"Case #"<<rr<<": "<<ans<<"\n";
    }
}
