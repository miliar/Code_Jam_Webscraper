#include <bits/stdc++.h>
#define ll long long int
#define ld long double
#define vl vector<ll>
#define vi vector<int>
#define vvl vector< vl >
#define vvi vector< vi >
#define pb push_back
#define mp make_pair
#define max_int_value 2147483647
#define max_long_value 9223372036854775807
#define min_long_value -9223372036854775806
#define ii pair<ll,ll>
#define kk pair<int,int>
#define jj pair<kk,kk>
#define F first
#define S second
#define fast_io ios_base::sync_with_stdio(0);cin.tie(0)
#define CLR(v, d)     memset(v, d, sizeof(v))
 
template<typename T> T gcd(T a, T b){return (b?__gcd(a,b):a);}
template<typename T> T lcm(T a, T b){return (a*(b/gcd(a,b)));}
// template<typename T> T mod(T a, T b) {return (a<b ? a : a%b);}
// template<typename T> T mod_neg(T a, T b) {return ((a%b)+b)%b;}
// ll mulmod(ll a,ll b, ll m){ll q=(ll)(((ld)a*(ld)b)/(ld)m);ll r=a*b-q*m;if(r>m)r%=m;if(r<0)r+=m;return r;}
// template<typename T> T expo(T e, T n){T x=1,p=e;while(n){if(n&1)x=x*p;p=p*p;n>>=1;}return x;}
// template<typename T> T power(T e, T n, T m){T x=1,p=e;while(n){if(n&1)x=mod(x*p,m);p=mod(p*p,m);n>>=1;}return x;}
// template<typename T> T extended_euclid(T a, T b, T &x, T &y){T xx=0,yy=1;y=0;x=1;while(b){T q=a/b,t=b;b=a%b;a=t;t=xx;xx=x-q*xx;x=t;t=yy;yy=y-q*yy;y=t;}return a;}
// template<typename T> T mod_inverse(T a, T n){T x,y;T d = extended_euclid(a, n, x, y);return (d>1?-1:mod_neg(x,n));}
 
using namespace std;
 
string IntToString (int a)
{
    ostringstream temp;
    temp<<a;
    return temp.str();
}
 
int StringToInt (string str)
{
    int xx;
    stringstream ss;
    ss << str;
    ss >> xx;
    return xx;
}
 
ll powerwithmodulus(ll base, ll exponent,ll modulus){
    ll result = 1; base%=modulus;
    while (exponent > 0)
    {
        if (exponent % 2 == 1) result = (result * base) % modulus;
        exponent = exponent >> 1;
        base = (base * base) % modulus;
    }
    return result;
}
 
/*  NCR using DP
for(int n = 0; n <= 1000; n++)
        for(int r = 0; r <= n; r++)
            if(r == 0 || n == r) ncr[n][r] = 1;
            else ncr[n][r] = (ncr[n-1][r-1] + ncr[n-1][r]) % mod;
*/
 
inline bool cmp(pair<ll,ll> &p1, pair<ll,ll> &p2)
{
    if(p1.F == p2.F)
        return p1.S > p2.S;
    else
        return p1.F < p2.F;
}
 
// ll largestPowerOf2(ll n)
// {
//     return (ll)pow(2, floor(log(n) / log(2)));
// }
 
//lower case std::transform(str.begin(), str.end(), str.begin(), ::tolower);
//Ascii A-65 Z-90 a-97 z-122 0-48 9-57
 
 
 
string str2,str1;
char ch;
ll max1=max_long_value,min1=min_long_value;
ll MOD=1000000007;
 
// stack<int> mystack;    //mystack.push(i); mystack.top(); (!mystack.empty()) mystack.pop();
// queue<int> myqueue;     // myqueue.push (myint);   myqueue.front(); (!myqueue.empty()) myqueue.pop();
// std::vector<ii> v,u;
 
ll gcd (ll n1, ll n2) {
    return (n2 == 0) ? n1 : gcd (n2, n1 % n2);
}
 
 
long long int i,l,j,t,k,n,p,q,r,s1,s2,m,f,c = 0,sum=0,e,coun=0,cont = 0;
bool flag;


int main()
{
    string nm = "", str = "";
    cin>>t;
    for(p=1;p<=t;p++)
    {
        str = "";
        cin>>nm;
        if(nm.length() == 1)
            cout<<"Case #"<<p<<": "<<nm<<endl;
        else
        {
            for(i=nm.length()-2;i>=0;i--)
            {
                if(nm[i] > nm[i+1])
                {
                    nm[i]--;
                    for(j=i+1;j<nm.length();j++)
                        nm[j] = '9';
                }
            }
            if(nm[0] != '0')
                str = nm[0];

            for(i=1;i<nm.length();i++)
            {
                str = str + nm[i];
            }
            cout<<"Case #"<<p<<": "<<str<<endl;
        }
    }
}