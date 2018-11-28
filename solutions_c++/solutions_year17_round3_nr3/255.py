#include<bits/stdc++.h>

using namespace std;

#define fRead(x)        freopen(x,"r",stdin)
#define fWrite(x)       freopen (x,"w",stdout)

#define LL              long long
#define ULL             unsigned long long
#define ff              first
#define ss              second
#define pb              push_back
#define INF             2e16
#define mk              make_pair
#define pii             pair<int,int>
#define pll             pair<LL,LL>


#define min3(a,b,c)     min(a,min(b,c))
#define max3(a,b,c)     max(a,max(b,c))
#define min4(a,b,c,d)   min(a,min(b,min(c,d)))
#define max4(a,b,c,d)   max(a,max(b,max(c,d)))
#define SQR(a)          ((a)*(a))
#define FOR(i,a,b)      for(int i=a;i<=b;i++)
#define ROF(i,a,b)      for(int i=a;i>=b;i--)
#define REP(i,b)        for(int i=0;i<b;i++)
#define MEM(a,x)        memset(a,x,sizeof(a))
#define ABS(x)          ((x)<0?-(x):(x))

#define SORT(v)         sort(v.begin(),v.end())
#define REV(v)          reverse(v.begin(),v.end())


#define FastRead        ios_base::sync_with_stdio(0);cin.tie(nullptr);

int n,k;
long double ara[55],U;
long double eps = 0.00000001;
int check(long double mn)
{
    long double temp = 0;
    REP(i,n){
        if(ara[i]<mn){
            temp += mn - ara[i];
        }
        if(temp>U)return 0;
    }
    if(temp>U)return 0;
    return 1;
}
int main()
{
    freopen("c1.in","r",stdin);
    freopen("Cout.txt","w",stdout);

    int t,cases=0;
    cin >> t;
    while(t--)
    {
        cin >> n >> k;
        cin >> U;
        REP(i,n){
            cin >> ara[i];
        }
        long double lo = 0 , hi = 1.0 , mid ,ans=0;
        for(int i = 1;i<=500;i++){
            mid = (lo+hi)/2.0;
            if(check(mid)){
                ans = mid;
                lo = mid;
            }else{
                hi = mid;
            }
        }
        long double m = 1.0;
        REP(i,n){
            m = m * max(ans,ara[i]);
        }
        if(m<eps)
        {
            m = 0.0;
        }
        cout << "Case #" << ++cases << ": ";
        cout << fixed << setprecision(12) << m << "\n";
    }
}
