//BISMILLAHIR RAHMANIR RAHIM
#include<bits/stdc++.h>
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
//#define RIP
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
#define fraction() cout.unsetf(ios::floatfield); cout.precision(10); cout.setf(ios::fixed,ios::floatfield);
#define hi cout<<"Dhukse " << endl;
#define infLL (ll)2e18
#define si(x) scanf("%d",&x)
#define sii(x,y) scanf("%d %d",&x,&y)
#define siii(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define sl(x) scanf("%lld",&x)
#define sll(x,y) scanf("%lld %lld",&x,&y)
#define slll(x,y,z) scanf("%lld %lld %lld",&x,&y,&z)

const double PI = acos(-1);
const double eps = 1e-9;
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

int main()
{
    //optimize();
    //freopen("input.txt","r",stdin );
    //freopen("output.txt","w",stdout );

    int t , cs = 0 , i , j , k  ;
    FILE *in,*out;
    in=fopen("input.txt","r");
    out=fopen("output.txt","w");
    fscanf(in,"%d",&t);
    freopen("input.txt","r",stdin );
    //si(t);
    while(t--){
            int n;
            int ans = 0;
            char s[1005];
            fscanf(in,"%s",s);
            fscanf( in, "%d",&k );
            //scanf("%s",s);
            //scanf("%d",&k);
            //cout << s  << " " << k << endl;
            //cout << endl;
            bool f = true;
            for( i = 0 ; i < strlen(s) && f ; i++ ){
                 if( s[i] == '-' ){
                    if( (i+k - 1) >= strlen(s) ){
                          for( j = i ; j < strlen(s) ; ++j ){
                            if( s[j] != '+' ){
                                fprintf(out,"Case #%d: IMPOSSIBLE\n",++cs);
                                 //printf("Case #%d: IMPOSSIBLE\n",++cs);
                                f = false;
                                break;
                            }
                          }
                    }
                    else{
                        for( j = i ; j < i + k ; ++j ){
                            if( s[j] == '+' )s[j] = '-';
                            else if( s[j] == '-' )s[j] = '+';

                        }
                    }
                    ans++;
                 }
                 /*for(int l = 0 ; i < strlen(s) ; ++l  ){
                    fprintf(out,"%c",s[l]);
                 }
                 fprintf(out,"\n"); */

         }

         if( f) fprintf(out , "Case #%d: %d\n",++cs, ans) ;

         //if( f) printf("Case #%d: %d\n",++cs, ans) ;
    }

    //fclose(in);
    //fclose(out);

     return 0;

}



