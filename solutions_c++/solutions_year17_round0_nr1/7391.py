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
#define frer freopen ("C:/Users/Sachin/Downloads/A-large.in","r",stdin);

using namespace std;

main()
{
    frer;
    frew;
    int t;
    cin>>t;
    for(int w=1;w<=t;w++)
    {
        string s;
        int k,n;
        cin>>s>>k;
        n=s.length();
        queue <int> q;
        bool f=0;
        int ans=0,i;
        for(i=0;i<n-k+1;i++)
        {
            if(s[i]=='-')
            {
                if(q.size()%2==0)
                {
                    ans++;
                    q.push(i+k-1);
                }
            }
            else if(s[i]=='+')
            {
                if(q.size()%2==1)
                {
                    ans++;
                    q.push(i+k-1);
                }
            }
            if(!q.empty() && q.front()==i)
            {
                q.pop();
            }
        }
        for(i=n-k+1;i<n;i++)
        {
            if(s[i]=='-')
            {
                if(q.size()%2==0)
                {
                    f=1;
                    break;
                }
            }
            else if(s[i]=='+')
            {
                if(q.size()%2==1)
                {
                    f=1;
                    break;
                }
            }
            if(!q.empty() && q.front()==i)
            {
                q.pop();
            }
        }
        cout<<"Case #"<<w<<": ";
        if(f==1)
        {
            cout<<"IMPOSSIBLE\n";
        }
        else
        {
            cout<<ans<<"\n";
        }
    }
}
