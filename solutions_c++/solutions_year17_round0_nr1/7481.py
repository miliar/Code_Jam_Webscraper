#include<bits/stdc++.h>
using namespace std;


#define bitcount    __builtin_popcountll
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mp make_pair
#define F first
#define S second
#define ll long long
#define rep(i,x,y) for(i=x;i<y;i++)
#define pf(x,y) printf("x",y)
#define pb push_back
#define MOD 1000000007
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.in","w",stdout);
    int t,x,l,k,ans,i,j,p;
    string s;
    sd(t);
    x=0;
    while(t--)
    {
        p=0;
        x++;
        cin>>s;
        l=s.length();
        sd(k);
        ans=0;
        for(i=0;i<l-k+1;i++)
        {
            if(s[i]=='+')
                continue;
            else
            {
                ans++;
                for(j=i;j<i+k;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
        }
        for(i=0;i<l;i++)
        {
            if(s[i]=='-')
            {
                p=1;
                break;
            }
        }
        cout<<"Case #"<<x<<":"<<" ";
        if(p==1)
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
            cout<<ans<<endl;
    }
}
