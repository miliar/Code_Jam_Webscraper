#include <bits/stdc++.h>
using namespace std;

int rem[5];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    int ca=1;
    while(t--)
    {
        int n,p;
        cin>>n>>p;
        memset(rem,0,sizeof(rem));
        for(int i=1;i<=n;i++)
        {
            int t;
            cin>>t;
            rem[t%p]++;
        }
        cout<<"Case #"<<ca<<": ";
        ca++;
        if(p==2)
        {
            cout<<(rem[0]+((rem[1]+1)/2))<<endl;
            continue;
        }
        if(p==3)
        {
            int ans=rem[0];
            int a=rem[1];
            int b=rem[2];
            ans+=min(a,b);
            int c=max(a,b)-min(a,b);
            ans+=(c/3);
            c%=3;
            if(c)
                ans++;
            cout<<ans<<endl;
        }
        if(p==4)
        {
            int ans=rem[0];
            ans+=min(rem[1],rem[3]);
            int c=max(rem[1],rem[3])-min(rem[1],rem[3]);
            ans+=(rem[2]/2);
            ans+=(c/4);
            rem[2]%=2;
            c%=4;
            if(rem[2]==0)
            {
                if(c!=0)
                    ans++;
            }
            else
            {
                if(c==0)
                    ans++;
                else if(c==1)
                    ans++;
                else if(c==2)
                    ans++;
                else if(c==3)
                    ans+=2;
            }
            cout<<ans<<endl;
        }
    }
    return 0;
}
