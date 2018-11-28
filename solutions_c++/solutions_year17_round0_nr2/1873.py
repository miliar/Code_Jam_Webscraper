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
#define harmonic(n) 0.57721566490153286l+log(n)
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define MOD 1000000007
#define fraction() cout.unsetf(ios::floatfield); cout.precision(6); cout.setf(ios::fixed,ios::floatfield);
#define inf INT_MAX

using namespace std;

typedef vector<ll>   vli;
typedef vector<int>   vi;
typedef pair<int,int>  pii;
typedef pair<ll,ll>   pll;
typedef vector<pii>  vpi;
typedef vector<vector<int> > vvi;
typedef vector<vector<ll> > vvl;
typedef vector<pll> vpl;
typedef vector<vector<ll> > vvli;


int dx[] = {+1 , -1 , 0 , 0};
int dy[] = {0 , 0 , +1 , -1};
int dx2[] = {+1 , -1 , 0 , 0 , +1 , +1 , -1 , -1};
int dy2[] = {0 , 0 , +1 , -1 , +1 , -1 , -1 , +1};

ll squ(ll x)
{
    return (x*x);
}

ll power(ll bs,ll k)
{
    ll x = 1,y = bs;
    if(k == 0) return 1;

    while(k > 0){
        if(k % 2 == 1) x = (x * y) ;

        y *= y;
        k /= 2;
    }
    return x;
}

#define MX

int main()
{
    //optimize();
    fraction();

    ll tst,cs = 0,i,j,n,k;
    vli a;
    FILE *in,*out;
    in = fopen("tidynumbersSmall.txt","r");
    out = fopen("optidynumbersSmall.txt","w");

    fscanf(in,"%lld",&tst);
  //  printf("%lld\n",tst);
    while(++cs <= tst){

        fscanf(in,"%lld",&n);
        //scanf("%lld",&n);
       // cout << "Case " << cs << ": " << n << endl;
        //printf("Case #%lld: %lld\n",cs,n);

        while(n != 0){
            a.PB(n % 10);
            n /= 10;
        }
        n = 0;
        k = a.size();
        //for(i = sz - 1; i >= 0 ; i--) printf(")
        for(i = k - 1; i > 0; i--){
            if(a[i] > a[i - 1]){
                j = a[i];
                int p = i;

                while(a[i] == j && i < k){
                    i++;
                }
                a[i - 1] = j - 1;

                for(j = i - 2; j >= 0; j--) a[j] = 9;
                break;
            }
        }

        for(i = 0; i < k; i++){
            n += (a[i] * power(10,i));
        }
        // cout << "Case " << cs << ": " << n << endl;
        //printf("Case #%lld: %lld\n",cs,n);
        fprintf(out,"Case #%lld: %lld\n",cs,n);
        a.clear();
    }

    return 0;
}
