/*Divyam Goyal - IIT-BHU*/
#include<bits/stdc++.h>
using namespace std;

#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define bitcount    __builtin_popcountll
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define ll long long
#define mp(a,b) make_pair(a,b)
#define F first
#define S second
#define pb(x) push_back(x)
#define MOD 1000000007
#define MAX 100005



int main()
{
    //ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    freopen("A-large (2).in","r",stdin);freopen("output.txt","w",stdout);
    int qt;
    sd(qt);
    for(int t=1;t<=qt;t++)
    {
        printf("Case #%d: ",t);
        string s;
        cin>>s;
        int n=s.size();
        int k;cin>>k;
        int ans=0;
        for(int i=0;i<=n-k;i++)
        {
            if(s[i]=='-')
            {
                ans++;
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
            }
        }
        k=0;
        for(int i=0;i<n;i++)
        {
            if(s[i]=='-')k=1;
        }
        if(k)cout<<"IMPOSSIBLE\n";
        else cout<<ans<<"\n";


    }






    return 0;


}