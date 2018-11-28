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
#define openin freopen("c.in","r",stdin)
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
int get_powm(int n)
{
    for(int i = 60 ; i >= 0 ; --i) {
        int temp = (1ll << i) ; temp-- ;
        if(temp <= n) return temp ;
    }
}
int get_pow(int n)
{
    int res = 1 ;
    while(res < n) res *= 2 ;
    if(res > n) res /= 2 ;
    return res ;
}
pair<int,int> get_kth(int n,int k)
{
    // n is assumed to be a power of two here
    int len = 1 ;
    int kk = 1 ;
    int num = n/2 ;
    for(;;) {
        if(k >= kk && k <= kk + len - 1) {
            break ;
        }
        kk += len ;
        len *= 2 ;
        num /= 2 ;
    }
    return {num,num} ;
}
pair<int,int> solve(int n,int k)
{
    if(k >= get_pow(n)) {
        return {0,0} ;
    }
    int temp = get_powm(n) ;
    pair<int,int> ans = get_kth(temp , k) ;
    int start , endd ;
    int len = endd - start + 1 ;
    start = 1 , len = 1 ;
    for(;;) {
        if(k >= start && k <= start + len - 1) {
            break ;
        }
        start += len ;
        len *= 2 ;
    }
    endd = start + len - 1 ;
    int diff = n - temp ;
    int count_full = diff/(2*len) ;
    ans.first += count_full , ans.ss += count_full ;
    diff %= (2*len) ;
    int count_half = diff/len ;
    if(count_half == 0) {
        int y = diff % len ;
        if(k >= start && k <= start + y - 1) {
            ans.first += 1 ;
        }
    }
    else {
        ans.first += 1 ;
        int y = diff % len ;
        if(k >= start && k <= start + y - 1) {
            ans.second += 1 ;
        }
    }
    return ans ;
}
int32_t main()
{
    fast;
    openin ;
    openout ;
    int t ;
    cin >> t ;
    rep(i,1,t) {
        int n , k ;
        cin >> n >> k ;
        cout << "Case #" << i << ": " ;
        auto ans = solve(n,k) ;
        cout << ans.ff << " " << ans.ss << "\n" ;
    }
    return 0;
}
