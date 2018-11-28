#pragma comment(linker, "/stack:640000000")

#include<bits/stdc++.h>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
#define ll long long int
#define scanl(a) scanf("%lld",&a)
#define scanii(a,b) scanf("%d%d",&a,&b)
#define scaniii(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define scanll(a,b) scanf("%lld%lld",&a,&b)
#define scanlll(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define scani(a) scanf("%d",&a)
#define clr(a) memset(a,0,sizeof(a))
#define clr_(a) memset(a,-1,sizeof(a))
#define pb(a) push_back(a)
#define pii pair<int,int>
#define sqr(a) a*a
#define eps 1e-9
#define inf INT_MAX
#define pi acos(-1.0)
#define ff first
#define ss second
#define INF 1e18
#define endl '\n'
#define vsort(v) sort(v.begin(),v.end())
int main()
{
    /// ios_base::sync_with_stdio(0);
    /// cin.tie(0);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int c=1;c<=t;c++)
    {
        string s;
        int k;
        cin>>s>>k;
        int len=s.size(),ans=0,f=0;
        for(int i=0;i<len;i++)
        {
            if(s[i]=='+')continue;
            else
            {
                ans++;
                if(i+k>len)
                {
                    f=1;break;
                }
              ///  cout<<i<<" "<<i+k<<endl;
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='+')s[j]='-';
                    else s[j]='+';
                }
            }
//            for(int j=0;j<len;j++)
//                cout<<s[j];
//            cout<<endl;
        }
        if(!f)cout<<"Case #"<<c<<": "<<ans<<endl;
        else cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}

