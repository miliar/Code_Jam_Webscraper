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
   // fraction();

    ll n,k,i,j,a,b,ln,tst,cs = 0,sb;

    FILE *in,*out;
    in = fopen("input.txt","r");
    out = fopen("output.txt","w");
    //cin >> tst;
    fscanf(in,"%lld",&tst);
    while(++cs <= tst){
        //cin >> n >> k;
        fscanf(in,"%lld %lld",&n,&k);
        fprintf(out,"Case #%lld: ",cs);
        if(n == k){
            //cout << 0 << ' ' << 0 << endl;
            fprintf(out,"%lld %lld\n",0LL,0LL);
            continue;
        }
        ln = 0;
        a = k;
        b = n;
        while(n != 0){
          //  cout << n % 2;
            n /= 2;
        }
        while(k != 0){
            k /= 2;
            ln++;
        }
        k = a;
        n = b;
        sb = n - a;
        i = 0;

        //cout << endl;
        while(i < ln - 1){
          //  cout << sb << ' ' << sb % 2 << endl;
            sb /= 2;
            i++;
        }

        a = sb % 2;
        //cout << sb << ' ' << a << endl;
        sb /= 2;

        b = sb % 2;

        //cout << sb << ' ' << b << endl;

        if(a == 0 && b == 1){
            //cout << sb << ' ' << sb << endl;
            fprintf(out,"%lld %lld\n",sb,sb);
        }

        else if(a == 1 && b == 0){
            //cout << sb + 1 << ' ' << sb << endl;
            fprintf(out,"%lld %lld\n",sb + 1,sb);
        }

        else if(a == 1 && b == 1){
            //cout << sb + 1 << ' ' << sb << endl;
            fprintf(out,"%lld %lld\n",sb + 1,sb);
        }

        else if(a == 0 && b == 0){
            //cout << sb << ' ' << sb << endl;
            fprintf(out,"%lld %lld\n",sb,sb);
        }
    }

        //fclose(in);
        //fclose(out);
    return 0;
}
