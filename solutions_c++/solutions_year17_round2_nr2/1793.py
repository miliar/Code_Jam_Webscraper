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
#define openin freopen("b.in","r",stdin)
#define openout freopen("b.txt","w",stdout)
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
bool is_power_of_two(int n)
{
    if(n == 0) return false ;
    return (n & (n-1)) == 0 ;
}
int count_bits(int n)
{
    return __builtin_popcount(n) ;
}
int count_bits_ll(int n)
{
    return __builtin_popcountll(n) ;
}
int largest_power(int n)
{
    int i ;
    for(i = 1 ; i <= n ; i *= 2) ;
    return i/2 ;
}
int n , arr[6] ;
char change(int i)
{
    if(i == 0 ) return 'R' ;
    if(i == 1 ) return 'O' ;
    if(i == 2 ) return 'Y' ;
    if(i == 3 ) return 'G' ;
    if(i == 4 ) return 'B' ;
    if(i == 5 ) return 'V' ;
}
map<char,int> cnt ;
string solve()
{
    int red = cnt['R'] ;
    int blue = cnt['B'] ;
    int yellow = cnt['Y'] ;
    int green = cnt['G'] ;
    int violet = cnt['V'] ;
    int orange = cnt['O'] ;
    string imp = "IMPOSSIBLE" ;
    if(orange >= blue || green >= red || violet >= yellow) return imp ;
    string blue_orange = "" ;

}
string small()
{
    int red = cnt['R'] , blue = cnt['B'] , yellow = cnt['Y'] ;
    char one , two , three ;
    string imp = "IMPOSSIBLE" ;
    vector<pair<int,char> > arr ;
    arr.pb({red,'R'}) ; arr.pb({yellow,'Y'}) , arr.pb({blue,'B'}) ;
    sort(all(arr)) ;
    reverse(all(arr)) ;
    int cnt_one = arr[0].ff , cnt_two = arr[1].ff , cnt_three = arr[2].ff ;
    one = arr[0].ss , two = arr[1].ss , three = arr[2].ss ;
    if(cnt_two + cnt_three < cnt_one) {
        return imp ;
    }
    string ans = "" ;
    // put all ones first
    rep(i,1,cnt_one) ans += one ;
    cnt_one = 0 ;
    string temp = "" ;
    for(int i = 0 ; i + 1 < ans.size() ; ++i) {
        if(ans[i] == one && ans[i + 1] == one && cnt_two) {
            temp += ans[i] ;
            temp += two ;
            cnt_two-- ;
        }
        else temp += ans[i] ;
    }
    if(ans[ans.size() - 1] == one && ans[0] == one && cnt_two) {
        temp += ans[ans.size() - 1] ;
        temp += two ;
        cnt_two-- ;
    }
    else temp += ans[ans.size() - 1] ;
    ans = temp ;
    temp = "" ;
    for(int i = 0 ; i + 1 < ans.size() ; ++i) {
        if(ans[i] == one && ans[i + 1] == one && cnt_three) {
            temp += ans[i] ;
            temp += three ;
            cnt_three-- ;
        }
        else temp += ans[i] ;
    }
    if(ans[ans.size() - 1] == one && ans[0] == one && cnt_three) {
        temp += ans[ans.size() - 1] ;
        temp += three ;
        cnt_three-- ;
    }
    else temp += ans[ans.size() - 1] ;
    ans = temp ;
    temp = "" ;
    for(int i = 0 ; i + 1 < ans.size() ; ++i) {
        if(ans[i] == one && ans[i + 1] == two && cnt_three) {
            temp += ans[i] ;
            temp += three ;
            cnt_three-- ;
        }
        else temp += ans[i] ;
    }
    if(ans[ans.size() - 1] == two && ans[0] == one && cnt_three) {
        temp += ans[ans.size() - 1] ;
        temp += three ;
        cnt_three-- ;
    }
    else temp += ans[ans.size() - 1] ;
    ans = temp ;
    return ans ;
}
int32_t main()
{
    fast;
    openin ;
    openout ;
    int t ; cin >> t ;
    rep(tt,1,t)
    {
        cin >> n ;
        rep(i,0,5) cin >> arr[i] ;
        cnt.clear() ;
        rep(i,0,5) cnt[change(i)] = arr[i] ;
        string ans = small() ;
        cout << "Case #" << tt << ": " ;
        cout << ans << "\n" ;
    }
    return 0;
}
