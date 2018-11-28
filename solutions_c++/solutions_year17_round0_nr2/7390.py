#include <bits/stdc++.h>
#define int long long
#define pii pair <int,int>
#define piii pair < pair<int,int> ,int>
#define f first
#define s second
#define pb push_back
#define MOD 1000000007
#define INF 4000000000000000000
#define frew freopen ("C:/Users/Sachin/Downloads/out.txt","w",stdout);
#define frer freopen ("C:/Users/Sachin/Downloads/B-large.in","r",stdin);

using namespace std;

main()
{
    frer;
    frew;
    int t;
    cin>>t;
    for(int w=1;w<=t;w++)
    {
        int i,n;
        string s,ans;
        cin>>s;
        n=s.length();
        for(i=0;i<n-1;i++)
        {
            if(s[i+1] > s[i])
                ans.pb(s[i]);
            else if(s[i+1] == s[i])
            {
                int f=0,j=i;
                while(j<n-1)
                {
                    if(s[j+1] > s[j])
                    {
                        f=1;
                        break;
                    }
                    else if(s[j+1] < s[j])
                    {
                        f=2;
                        break;
                    }
                    j++;
                }
                if(f==0 || f==1)
                    ans.pb(s[i]);
                else
                {
                    ans.pb(s[i]-1);
                    break;
                }
            }
            else
            {
                ans.pb(s[i]-1);
                break;
            }
        }
        if(i==n-1)
        {
            ans.pb(s[i]);
        }
        else
        {
            for(i=i+1;i<n;i++)
                ans.pb('9');
        }
        for(i=0;i<n;i++)
            if(ans[i]!='0')
                break;
        cout<<"Case #"<<w<<": "<<ans.substr(i,n-i)<<"\n";
    }
}
