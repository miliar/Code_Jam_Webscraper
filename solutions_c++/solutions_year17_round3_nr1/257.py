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

long double PI = acos(-1.0);
const int N = 1005;
struct pie{
    long double rad,hi,mul;
};

pie ara[N];
bool cmp(pie A,pie B)
{
    return A.mul > B.mul;
}
int n,k;

long double check(int in)
{
    long double area = SQR(ara[in].rad) + 2.0*ara[in].mul;
    int got = 1;
    for(int i = 0;i<n;i++){
        if(i==in)continue;
        if(got==k)break;
        if(ara[i].rad>ara[in].rad)continue;
        got++;
        area += 2.0*ara[i].mul;
        if(got==k)break;
    }
    if(got<k)return 0.0;
    return area;
}
int main()
{
    freopen("Alarge.in","r",stdin);
    freopen("Aout.txt","w",stdout);

    int t,cases=0;
    cin >> t;
    while(t--)
    {
        cin >> n >> k;
        REP(i,n){
            cin >> ara[i].rad >> ara[i].hi;
            ara[i].mul = ara[i].rad * ara[i].hi;
        }
        sort(ara,ara+n,cmp);
        long double mx = 0;
        for(int i = 0;i<n;i++){
            mx = max(mx,check(i));
        }
        cout << "Case #" << ++cases << ": ";
        cout << fixed << setprecision(12) << PI*mx << "\n";
    }
}
