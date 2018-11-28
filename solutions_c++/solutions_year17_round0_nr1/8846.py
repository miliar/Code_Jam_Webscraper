/* In the name of Allah
   The most beneficent,
   The most merciful
*/
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define dbl double
#define vl vector<ll>
#define sf(zz) scanf("%lld",&zz)
#define sf2(zz,zzz) scanf("%lld %lld",&zz,&zzz)
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define read freopen("in.txt","r",stdin)
#define write freopen("out.txt","w",stdout)
#define ck puts("ok")
#define reset(a,d) memset(a,d,sizeof(a))
#define pb(a,b) a.push_back(b)
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define min4(a,b,c,d) min(min(a,b),min(c,d))
#define max4(a,b,c,d) max(max(a,b),max(c,d))
#define DIST(x1,y1, x2, y2) (((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)))
#define DIST3D(x1,x2, y1, y2, z1, z2) (((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)) + ((z1-z2)*(z1-z2)))
#define ALL(x) (x).begin(),(x).end()
#define LLA(x) x.rbegin(), x.rend()
#define SORT(v) sort(ALL(v))
#define inf   1<<30
#define mod   1000000007
#define PI acos(-1.0)
string sss="0123456789ABCDEF";
//-----------------------------------------------------------//
string s;
ll arr[1009];

int main()
{
    read;write;
    //ios_base::sync_with_stdio(0);
    ll t,no=0,i,j,k,res=0,f,l;
    cin>>t;
    getchar();
    while(t--)
    {
        s.clear();
        res=0,f=1;
        cin>>s>>k;
        l=s.size();
        for(i=1;i<=l;i++)arr[i]=(s[i-1]=='+');

        for(i=1;i<=l-k+1;i++)
        {
            /*for(j=1;j<=l;j++)cout<<arr[j]<<" ";
            cout<<endl;*/
            if(arr[i])continue;
            res++;
            ll st=i,ed=i+k-1;
            for(j=st;j<=ed;j++)arr[j]=1-arr[j];
        }
        /*for(j=1;j<=l;j++)cout<<arr[j]<<" ";
            cout<<endl;*/
        for(;i<=l;i++)
        {
            if(arr[i]==0)
            {
                f=0;break;
            }
        }
        cout<<"Case #"<<++no<<": ";
        if(f)cout<<res<<endl;
        else puts("IMPOSSIBLE");
    }
}
