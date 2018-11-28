#include <bits/stdc++.h>
using namespace std;
#define f(i,a,b) for(int i=a;i<b;i++)
#define b(i,a,b) for(int i=a;i>b;i--)
#define mpr(a,b) make_pair(a,b)
#define prll pair<ll,ll>
#define si(s) scanf("%d",&s)
#define pri pair<int,int>
#define ll long long
#define inf INT_MAX/10
#define gmax 1005
#define mod 1000000009
#define mod1 1610612741
#define mod2 1000000009
#define line cout<<"\n"
#define bp __builtin_popcount
#define pb push_back
#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define getfile freopen("C:\\Users\\VISHAL ASHANK\\Desktop\\A-large.in","r",stdin)
#define givefile freopen("C:\\Users\\VISHAL ASHANK\\Desktop\\inp2.txt","w",stdout)
main()
{
    getfile;
    givefile;
    int t,tot;
    cin>>t;tot=t;int k;
    while(t--)
    {
        string s;
        cin>>s;cin>>k;
        vector<int> v;
        f(i,0,s.length())
        {
            if(s[i]=='+')
                v.pb(1);
            else
                v.pb(0);
        }
        int flag=0;int ans=0;
        f(i,0,v.size())
        {
            int lim=i+k;
            if(lim>v.size())
            {
                f(j,i,v.size())
                {
                    if(v[j]!=1)
                        flag=1;
                }
            }
            else if(v[i]!=1)
            {
                ans++;
                f(j,i,i+k)
                {
                    if(v[j]==1)
                        v[j]=0;
                    else
                        v[j]=1;
                }
            }
            /*f(l,0,v.size())
            cout<<v[l]<<" ";line;*/
        }
        cout<<"Case #"<<tot-t<<": ";
        if(flag==0)
            cout<<ans<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;


    }
}
