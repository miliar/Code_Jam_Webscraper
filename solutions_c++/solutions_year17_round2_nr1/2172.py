#include<bits/stdc++.h>
#define PI acos(-1)
#define ll long long
#define eps 1e-9
#define PB push_back
#define EB emplace_back
#define F first
#define S second
#define MP make_pair
#define RS resize
#define BG begin
#define sf scanf
#define pf printf
#define optimize() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define MOD 1000000007
#define fraction() cout.unsetf(ios::floatfield); cout.precision(6); cout.setf(ios::fixed,ios::floatfield);
#define harmonic(n) 0.577215664901532861 + log(n);

using namespace std;

typedef vector<ll>   vll;
typedef vector<int>   vi;
typedef pair<int,int>  pii;
typedef pair<ll,ll>   pll;
typedef vector<pii>  vpi;
typedef vector<vector<int> > vvi;
typedef vector<vector<ll> > vvl;
typedef vector<pll> vpl;

int dx[] = {+1 , -1 , 0 , 0};
int dy[] = {0 , 0 , +1 , -1};
int dx2[] = {+1 , -1 , 0 , 0 , +1 , +1 , -1 , -1};
int dy2[] = {0 , 0 , +1 , -1 , +1 , -1 , -1 , +1};

inline ll squ(ll x)
{
    return (x*x);
}

inline ll power(ll bs,ll k)
{
    ll x = 1LL,y = bs;
    if(k == 0) return 1LL;

    while(k > 0){
        if(k % 2) x *= y;

        y *= y;
        k /= 2;
    }

    return x;
}

#define MX 2000

ll d,n,pos[MX],sp[MX];

bool valid(double x)
{
    ll i,j;
    double ds;

    for(i = 0 ;i < n; i++){
        if(x <= sp[i]) continue;

        ds = -x * pos[i] / (double)(sp[i] - x);
        if(ds < (double)d){
            //cout << x << ' ' << ds << endl;
            //printf("%lf %lf\n",ds,x);
            return false;
        }
    }

    return true;
}

int main()
{
    optimize();
    fraction();

    FILE *in,*out;
    in=fopen("inputs.txt","r");
    out=fopen("outputs.txt","w");

    ll tst,cs = 0,i,j;
    fscanf(in,"%lld",&tst);

    while(++cs <= tst){
        fscanf(in,"%lld %lld",&d,&n);
        for(i = 0; i < n; i++) fscanf(in,"%lld %lld",&pos[i],&sp[i]);



        double lo = 0.0,hi = 1000000000000000.000,mid;
        for(j = 0; j <= 300; j++){
            mid = (lo + hi) / 2;
            if(valid(mid)){
                lo = mid;
                //cout << lo << endl;
               // printf("%lf\n",lo);
            }
            else hi = mid;
        }

        fprintf(out,"Case #%lld: %lf\n",cs,lo);

       // printf("\n\n\n");
    }

    return 0;
}
