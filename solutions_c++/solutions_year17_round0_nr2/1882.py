#include<bits/stdc++.h>
#define PB(u)  push_back(u)
#define AA   first
#define BB   second
#define inf 0x3f3f3f3f
using namespace std ;
#define MAX 100005
#define sz size()
typedef long long ll ;
typedef pair<int,int> PII ;
const double eps=1e-8;
const double pi=acos(-1.0);
const int mod=1e9+7;

ll ans(ll n)
{
    int a[30];
    int len=0;
    while(n)
    {
        a[++len]=n%10;
        n/=10;
    }
    for(int i=1;i<len;i++)
    {
        if(a[i]<a[i+1])
        {
            a[i+1]--;
            //cout<<i<<endl;
            for(int j=1;j<=i;j++)
                a[j]=9;
        }
    }
    ll res=0;
    for(int i=len;i>0;i--)
        res=res*10+a[i];
    return res;
}


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    int T,cas=1;
    cin>>T;
    while(T--)
    {
        ll n ;
        cin>>n;
        printf("Case #%d: ",cas++);
        printf("%I64d\n",ans(n));
    }
    return 0 ;
}

