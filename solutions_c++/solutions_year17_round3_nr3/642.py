/*While alive CODE*/

                    /*War will happen and code will follow*/

#include <bits/stdc++.h>
using namespace std;
#define mem(x,y) memset(x,y,sizeof(x))
#define bitcount    __builtin_popcountll
#define mod 1000000007
#define N 1000009
#define fast ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define ss(s) cin>>s;
#define si(x)  scanf("%d",&x);
#define sl(x)  cin>>x;
#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()
#define S second
#define F first
#define ll long long 
ll power(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
string a,b,c;
int q,n,t,k;
int arr[N];
int brr[N];
double p[N];
double anstemp[N];
double u;
void init(){
    cin>>n>>k>>u;
        for(int i =0;i<57;i++)anstemp[i] = 0.00;
        for(int i = 1;i<=n;i++)cin>>p[i];

        sort(p+1,p+1+n);
}
int main()
{
  freopen("C-small-1-attempt0 (1).in", "r", stdin);
    freopen("Output3.out", "w", stdout);


cin>>t;
for(int y=0;y<t;y++)
        {

            
        
        init();

        for(int i = 1;i<=n;i++)anstemp[i]=anstemp[i-1]+1.0*(i-1)*(p[i]-p[i-1]);

        int curnum=1;
        double ans=1.0;
        for(int i = 1;i<=n;i++)if(anstemp[i]<=u)curnum=i;

        double div=1.0*(u-anstemp[curnum])/curnum;
        p[curnum]+=div;

       for(int i = 1;i<=curnum;i++)ans=1.0*ans*p[curnum];

        for(int i = curnum+1;i<=n;i++)ans=1.0*ans*p[i];


        cout<<"Case #"<<y+1<<fixed << setprecision(12) <<": "<<ans<<"\n";



}




return 0;}

