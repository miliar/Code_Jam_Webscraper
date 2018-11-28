/*
ye mera template hai
apna khud likho bc :P
*/

/*
Author : Sarvagya Agarwal
*/

#include<bits/stdc++.h>
using namespace std;

//defines
#define openin freopen("a.in","r",stdin)
#define openout freopen("output.txt","w",stdout)
#define fast ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define ll long long
#define int long long
#define mod 1000000007
#define repr(i,x,y) for (__typeof(x) i=x;i>=y;i--)
#define rep(i,x,y) for (__typeof(x) i=x;i<=y;i++)
#define all(c) (c).begin(),(c).end()
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

/* Print pair */
template <typename T,typename S>
ostream & operator << (ostream &os , const pair<T,S> &v) {
    os << "(" ;
    os << v.first << "," << v.second << ")" ;
    return os ;
}
/* Print vector */
template <typename T>
ostream & operator << (ostream &os , const vector<T> &v) {
    os << "[" ;
    int sz = v.size() ;
    for(int i = 0 ; i < sz ; ++i) {
        os << v[i] ;
        if(i!=sz-1)os << "," ;
    }
    os << "]\n" ;
    return os ;
}
/* Print set */
template <typename T>
ostream & operator << (ostream &os , const set<T> &v) {
    T last = *v.rbegin() ;
    os << "[" ;
    for(auto it : v) {
        os << it  ;
        if(it != last) os << "," ;
    }
    os << "]\n" ;
    return os ;
}
/* Print Map */
template <typename T,typename S>
ostream & operator << (ostream &os , const map<T,S> &v) {
    for(auto it : v) {
        os << it.first << " : " << it.second << "\n" ;
    }
    return os ;
}
int power(int a , int b)
{
    int res = 1 ;
    while(b)
    {
        if(b%2) {
            res = (res * a) % mod ;
        }
        b/=2 ;
        a = (a*a) % mod ;
    }
    return res ;
}

//debug
#define TRACE

#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
		cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
		const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif
const double PI = 3.14159265359 ;
double r[1005] , h[1005] ;
double dp[1005][1005] ;
bool cmp(pair<int,int> a,pair<int,int> b)
{
    if(a.ff == b.ff) return a.ss > b.ss ;
    return a.ff < b.ff ;
}
int32_t main()
{
    fast;
    openin ;
    openout ;
    int t ;
    cin >> t ;
    rep(tt,1,t)
    {
        int n , k ;
        cin >> n >> k ;
        rep(i,1,n) cin >> r[i] >> h[i] ;
        memset(dp,0,sizeof(dp)) ;
        vector<pair<int,int> > arr ;
        rep(i,1,n) arr.pb({r[i],h[i]}) ;
        sort(all(arr),cmp) ;
        rep(i,0,n-1)
        {
            r[i+1] = arr[i].ff , h[i+1] = arr[i].ss ;
        }
        rep(i,1,n) dp[i][1] = PI * r[i] * r[i] + 2 * PI * r[i] * h[i] ;
        rep(i,2,n) rep(j,2,k)
        {
            rep(p,1,i-1)
            {
               dp[i][j] = max(dp[i][j] , dp[p][j-1] + 2 * PI * r[i] * h[i] + PI * r[i] * r[i] - PI * r[p] * r[p]) ;
            }
        }
        double ans = 0.0 ;
        rep(i,1,n) ans = max(ans , dp[i][k]) ;
        cout << "Case #" << tt << ": " ;
        cout << fixed << setprecision(10) << ans << "\n" ;
    }
    return 0;
}
