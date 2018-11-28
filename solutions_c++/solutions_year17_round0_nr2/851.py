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
#define openin freopen("B.in","r",stdin)
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
int is(int n)
{
    vector<int> d ;
    while(n) {
        d.pb(n % 10) ; n /= 10 ;
    }
    reverse(all(d)) ;
    int prev = -1 ;
    for(int i = 0 ; i < d.size() ; ++i) {
        if(d[i] >= prev) {}
        else return false ;
        prev = d[i] ;
    }
    return true ;
}
int get(int n)
{
    for(int i = n ; i >= 1 ; --i) {
        if(is(i)) return i ;
    }
}
int iter = 0 ;
int get2(int n)
{
    //iter += 1;
    //if(is(n)) return n ;
    vector<int> digits ;
    int temp = n ;
    bool ok = true ;
    while(temp > 0) {
        digits.push_back(temp % 10) ;
        temp /= 10 ;
    }
    reverse(all(digits)) ;
    int sz = digits.size() ;
    for(int i = 0 ; i + 1 < sz ; ++i) {
        if(digits[i] > digits[i + 1]) {
            ok = false ; break ;
        }
    }
    if(ok) return n ;
    int index = 0 ;
    while(index + 1 < sz) {
        if(digits[index] <= digits[index + 1]) {
            index += 1 ;
        }
        else {
            break ;
        }
    }
    if(index != sz - 1) digits[index] -= 1 ;
    for(int i = index + 1 ; i < sz ; ++i) {
        digits[i] = 9 ;
    }
    int res = 0 ;
    for(auto it : digits) {
        res *= 10 ;
        res += (it) ;
    }
    return get2(res) ;
}
int32_t main()
{
    fast;
    openin ;
    openout ;
    int t ;
    cin >> t ;
    rep(i,1,t) {
        int n ;
        cin >> n ;
        cout << "Case #" << i << ": " ;
        cout << get2(n) << "\n" ;
    }
    /*int t ;
    cin >> t ;
    while(t--) {
        int n ;
        cin >> n ;
        int iter = 0 ;
        trace(n , get2(n) , iter) ;
    }*/
    return 0;
}
