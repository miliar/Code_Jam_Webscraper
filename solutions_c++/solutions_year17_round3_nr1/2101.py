//BISMILLAHIR RAHMANIR RAHIM
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <list>
#include <stack>
#include <utility>
#include <set>
#include <ctime>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <cctype>
#define RIP
using namespace std;

typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<int,int> pii;
typedef pair<double, double> pdd;
typedef pair<ll, ll> pll;
typedef vector<pii> vii;
typedef vector<pll> vll;

#define PB push_back
#define F first
#define S second
#define MP make_pair
#define endl '\n'
#define mx1 100005
#define mx2 200005
#define mx3 300005
#define WHITE 0
#define GRAY 1
#define BLACK 2
#define MOD 1000000007
#define bp __builtin_popcount
#define fraction() cout.unsetf(ios::floatfield); cout.precision(15); cout.setf(ios::fixed,ios::floatfield);
#define hi cout<<"Dhukse " << endl;
#define infLL (ll)2e18
#define si(x) scanf("%d",&x)
#define sii(x,y) scanf("%d %d",&x,&y)
#define siii(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define sl(x) scanf("%lld",&x)
#define sll(x,y) scanf("%lld %lld",&x,&y)
#define slll(x,y,z) scanf("%lld %lld %lld",&x,&y,&z)

const double PI = acos(-1);
const double eps = 1e-10;
const int inf = 2000000000;
//const int MOD = 1000000007;
int MOD1 = 1000000007;
int MOD2 = 1000000009;
#define harmonic(n) 0.57721566490153286l+log(n)

#define mem(a,b) memset(a, b, sizeof(a) )
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define sqr(a) ((a) * (a))
#define optimize() ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

typedef vector<int>::iterator vit;
typedef set<int>::iterator sit;

inline bool checkBit(ll n, ll i) { return n&(1LL<<i); }
inline ll setBit(ll n, ll i) { return n|(1LL<<i);; }
inline ll resetBit(ll n, ll i) { return n&(~(1LL<<i)); }

int dx[] = {0, 0, +1, -1};
int dy[] = {+1, -1, 0, 0};
//int dx[] = {+1, 0, -1, 0, +1, +1, -1, -1};
//int dy[] = {0, +1, 0, -1, +1, -1, +1, -1};

inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
inline bool isLeapYear(ll year) { return (year%400==0) || (year%4==0 && year%100!=0); }
inline void normal(ll &a) { a %= MOD; (a < 0) && (a += MOD); }
inline ll modMul(ll a, ll b) { a %= MOD, b %= MOD; normal(a), normal(b); return (a*b)%MOD; }
inline ll modAdd(ll a, ll b) { a %= MOD, b %= MOD; normal(a), normal(b); return (a+b)%MOD; }
inline ll modSub(ll a, ll b) { a %= MOD, b %= MOD; normal(a), normal(b); a -= b; normal(a); return a; }
inline ll modPow(ll b, ll p) { ll r = 1LL; while(p) { if(p&1) r = modMul(r, b); b = modMul(b, b); p >>= 1LL; } return r; }
inline ll modDiv(ll a, ll b) { return modMul(a, modPow(b, MOD-2)); }

bool comp( const pair < int , int > &p1 , const pair < int , int > &p2 ){ return p1.S < p2.S ;}
ll converter( string a )
{
    ll i , mul = 1 , r , t ,ans = 0LL;if( a.length() == 0 )return 0;for( i = a.length() - 1 ; i >= 0 ; i-- ){
        t = a[i] - '0';r = t%10;ans += (mul*r);mul = mul*10;
    }
    return ans;
}

//
//debug
#ifdef RIP
template < typename F, typename S >
ostream& operator << ( ostream& os, const pair< F, S > & p ) {
            return os << "(" << p.first << ", " << p.second << ")";
}

template < typename T >
ostream &operator << ( ostream & os, const vector< T > &v ) {
            os << "{";
                for(auto it = v.begin(); it != v.end(); ++it) {
                                if( it != v.begin() ) os << ", ";
                                        os << *it;
                                            }
                    return os << "}";
}

template < typename T >
ostream &operator << ( ostream & os, const set< T > &v ) {
            os << "[";
                for(auto it = v.begin(); it != v.end(); ++it) {
                                if( it != v.begin() ) os << ", ";
                                        os << *it;
                                            }
                    return os << "]";
}

template < typename T >
ostream &operator << ( ostream & os, const multiset< T > &v ) {
            os << "[";
                for(auto it = v.begin(); it != v.end(); ++it) {
                                if( it != v.begin() ) os << ", ";
                                        os << *it;
                                            }
                    return os << "]";
}

template < typename F, typename S >
ostream &operator << ( ostream & os, const map< F, S > &v ) {
            os << "[";
                for(auto it = v.begin(); it != v.end(); ++it) {
                                if( it != v.begin() ) os << ", ";
                                        os << it -> first << " = " << it -> second ;
                                            }
                    return os << "]";
}

#define dbg(args...) do {cerr << #args << " : "; faltu(args); } while(0)

void faltu () {
            cerr << endl;
}

template <typename T>
void faltu( T a[], int n ) {
            for(int i = 0; i < n; ++i) cerr << a[i] << ' ';
                cerr << endl;
}

template <typename T, typename ... hello>
void faltu( T arg, const hello &... rest) {
            cerr << arg << ' ';
                faltu(rest...);
}
#else
#define dbg(args...)
#endif  //RIP

double dp[(1<<12 ) + 5 ][12][12][2];
pii a[15];
int  n , k;

double solve( int mask , int taken , int prev , int t )  {

     if( dp[mask][taken][prev][t] != -1.0 ) return dp[mask][taken][prev][t];
     if( taken == k ) return 0.0;
     int i;
     double ret1 = 0.0 , ret2 = 0.0;
     for( i = 1 ; i <= n ; ++i ) {
        if( !checkBit(mask ,i) && t == 1 && a[prev].F >= a[i].F ) {
                 double height = 1.0*2*PI*a[i].F*a[i].S;
                 double radi_cur = 1.0*PI*a[i].F*a[i].F;
                 double radi_prev = 1.0*PI*a[prev].F*a[prev].F;
                 ret1 = max ( ret1 , radi_cur - radi_prev + ( radi_prev - radi_cur) + height + solve( setBit(mask , i ) , taken + 1 , i , t ) );
        }
        if( !checkBit(mask , i) && t == 0 ) {
                 double height = 1.0*2*PI*a[i].F*a[i].S;
                 double radi_cur = 1.0*PI*a[i].F*a[i].F;
            ret1 = max( ret1 , height + radi_cur + solve(setBit(mask , i) , taken + 1 , i , 1 ) );
        }
     }
     return dp[mask][taken][prev][t] = ret1;
}
void clr() {
    int i , j , k , l ;

    for( i = 0 ; i <= (1 << 12 ) ; ++i ) {
        for( j = 0 ; j <= 11 ; j++ ){
            for( k = 0 ; k <= 11 ; k++ ){
                for(l = 0 ; l < 2 ; l++ ) {
                    dp[i][j][k][l] = -1.0;
                }
            }
        }
    }
}

int main()
{
    optimize();
    fraction();
    freopen("input.txt","r",stdin );
    freopen("output.txt","w", stdout );
    int t , cs = 0 , i ;
    cin >> t;

    while(t-- ){
        clr();
        cin >> n >> k;
        for( i = 1; i <= n ; ++i ) {
            cin >> a[i].F >> a[i].S;

        }
        double ans = solve( 0, 0 , 0 , 0 );
        cout << "Case #" << ++cs << ": " << ans << endl;
    }


    return 0;
}


