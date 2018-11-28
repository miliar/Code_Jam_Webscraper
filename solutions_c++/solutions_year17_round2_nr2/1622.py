#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    long long t;
    scanf("%lld",&t);
    for(long long i=1;i<=t;i++)
    {   long long n;
        scanf("%lld",&n);
        string ss = "RYB";
        vector<array<long long,2> > v;
        for(long long j=0;j<6;j++)
        {
            long long a;
            scanf("%lld",&a);
            v.push_back({n-a,j});
        }
        sort(v.begin(),v.end());
        long long tp[3];
        string s[3];
        for(ll j=0;j<3;j++)
        {
            tp[j] = n - v[j][0];
            s[j] = ss[v[j][1]/2];
            //cout<<tp[j]<<" "<<s[j]<<endl;
        }
        string ans="";
        bool b=0;
        if(tp[0]<=(tp[1]+tp[2]))
        {
            b=1;
            for(ll j=0;j<tp[0];j++)
            {
                ans = ans+s[0];
                if(tp[1])
                {
                    ans = ans+s[1];
                    tp[1]--;
                }
                else
                {
                    ans=ans+s[2];
                    tp[2]--;
                }
            }
            ll j=1;
            while(tp[2]>0)
            {
                ans.insert(j,s[2]);
                tp[2]--;;
                j+=2;
            }
        }
        if(!b)
        cout<<"Case #"<<i<<": IMPOSSIBLE\n";
        else
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}

