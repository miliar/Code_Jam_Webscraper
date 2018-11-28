#include <bits/stdc++.h>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
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
#define F first
#define S second
#define fast_io ios_base::sync_with_stdio(0);cin.tie(0)
 
#define CLR(v, d)     memset(v, d, sizeof(v))
 
template<typename T> T gcd(T a, T b){return (b?__gcd(a,b):a);}
template<typename T> T lcm(T a, T b){return (a*(b/gcd(a,b)));}
template<typename T> T mod(T a, T b) {return (a<b ? a : a%b);}
template<typename T> T mod_neg(T a, T b) {return ((a%b)+b)%b;}
ll mulmod(ll a,ll b, ll m){ll q=(ll)(((ld)a*(ld)b)/(ld)m);ll r=a*b-q*m;if(r>m)r%=m;if(r<0)r+=m;return r;}
template<typename T> T expo(T e, T n){T x=1,p=e;while(n){if(n&1)x=x*p;p=p*p;n>>=1;}return x;}
template<typename T> T power(T e, T n, T m){T x=1,p=e;while(n){if(n&1)x=mod(x*p,m);p=mod(p*p,m);n>>=1;}return x;}
template<typename T> T extended_euclid(T a, T b, T &x, T &y){T xx=0,yy=1;y=0;x=1;while(b){T q=a/b,t=b;b=a%b;a=t;t=xx;xx=x-q*xx;x=t;t=yy;yy=y-q*yy;y=t;}return a;}
template<typename T> T mod_inverse(T a, T n){T x,y;T d = extended_euclid(a, n, x, y);return (d>1?-1:mod_neg(x,n));}
 
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

// inline bool cmp(pair<ii> &p1,pair<ii> &p2)
// {
//     if(p1.F < p2.F)
//         return true;
//     else
//         return false;
// }
 
ll largestPowerOf2(ll n)
{
    return (ll)pow(2, floor(log(n) / log(2)));
}
 
//lower case std::transform(str.begin(), str.end(), str.begin(), ::tolower);
//Ascii A-65 Z-90 a-97 z-122 0-48 9-57


int check(vector<int> v1, vector<ii> v2)
{
    
}
std::vector<ii> v,u;
ll t,n,m,sum = 0,count = 0,m1,m2,m3,i,j,k,sum1,sum2,p,p1,q1;
string str[50],ptr[50];
string nm;
std::vector<int> v1;
int main() 
{
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>n>>m;
        nm = "";
        for(i=0;i<n;i++)
        {
            cin>>str[i];
        }
        for(i=0;i<m;i++)
            nm = nm + "?";
        m1 = -1;
        m2 = -1;
        v.clear();
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(str[i][j] == '?')
                {
                    if(m1 != -1 and m2 != -1)
                    {
                        if(m1 == i)
                            str[i][j] = str[m1][m2];
                        else
                            v.pb(mp(i,j));
                    }
                    else
                        v.pb(mp(i,j));
                }
                else
                {
                    m1 = i;
                    m2 = j;
                    for(p=0;p<v.size();p++)
                    {
                        if(m1 == v[p].F)
                            str[v[p].F][v[p].S] = str[m1][m2];
                        else
                            u.pb(mp(v[p].F,v[p].S));
                    }
                    v.clear();
                    v = u;
                    u.clear();
                }
            }
        }
        v1.clear();
        int flag = 0;
        string kk = "";
        for(i=0;i<n;i++)
        {
            if(str[i] == nm)
            {
                if(kk.length() == 0)
                    v1.pb(i);
                else
                    str[i] = kk;
            }
            else
            {
                kk = str[i];
                for(j=0;j<v1.size();j++)
                    str[v1[j]] = str[i];
                v1.clear();
            }
        }
        cout<<"Case #"<<k<<":"<<"\n";
        for(i=0;i<n;i++)
        {
            
            cout<<str[i];
            cout<<"\n";
        }
    }
    return 0;
}
 