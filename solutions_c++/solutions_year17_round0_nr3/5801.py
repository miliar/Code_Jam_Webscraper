#include <stdio.h>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <math.h>
#include <string.h>
#include <time.h>
#include <iostream>
#include <algorithm>
#include <fstream>
#define ll /*unsigned*/ long long int
#define ld double
#define cinf(a) scanf("%lf",&a)
#define coutf(a) printf("%.12lf\n",a)
#define cins(a) scanf("%s",a)
#define couts(a) printf("%s",a)
#define cin(a) scanf("%lld",&a)
#define cout(a) printf("%lld\n",a)
#define cout_(a) printf("%lld ",a)
#define coutc(a) printf("%c",a)
#define cinc(a) scanf(" %c",&a)
#define coutp(a,b) printf("%lld %lld\n",a,b)
#define debug couts("chu") ;
#define SZ(a) (ll)a.size()
#define next_prm std::next_permutation
#define ALL(x) x.begin(),x.end()
#define endl '\n'
#define M 1000000007
#define MAX 9223372036854775807
#define MIN -9223372036854775807
#define pb(a) push_back(a)
#define mmp(a,b) make_pair (a,b)
#define pmp(a,b) push_back(make_pair(a,b))
#define pp pair
#define rev reverse
#define S second
#define F first
#define LB lower_bound
#define UB upper_bound
#define cnt_bin1(x) __builtin_popcountll(x)
#define bsa(v,n,a) binary_search(v,v+n,a)
#define bsv(v,a) binary_search(v.begin(),v.end(),a)
#define PI 3.1415926535897932
using namespace std ;
//******************************************************************--UTILITIES--************************************************************************//
/*FILE INPUT OUTPUT REDIRECT
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 */
/*struct node2 {
 ll val ;
 ll id ;
 }aux2 ;
 struct compare {
 bool operator()(node2 l, node2 r)
 {
 return l.val > r.val ;					// MIN PQ
 }
 };
 std::priority_queue<node2,std::vector<node2>,compare > pq;*/
ll fast_power(ll val,ll deg,ll mod) {
    if (!deg) return 1 % mod;
    if (deg & 1) return fast_power(val, deg - 1, mod) * val % mod;
    long long res = fast_power(val ,deg >> 1, mod);
    return (res*res) % mod;
}
ll SumOfDigits (ll x) {
    ll sum=0 ;
    while (x>0)
    {   sum+=x%10 ;
        x/=10 ;
    }
    return sum ;
}
ld angle (ld x,ld y) {
    ld theta=90 ;
    if (y!=0)   theta=(atan((ld)abs((ll)x)/abs((ll)y))*180)/PI ;
    if (x>=0&&y>=0) return theta ;
    if (x>=0&&y<0)  return 180-theta ;
    if (x<0&&y<=0)  return 180+theta ;
    else return 360-theta ;
}
ll mod (ll a,ll b) {
    if (a<0)
    {	a=(-a)%b ;
        if (a!=0)
            a=b-a ;
    }
    else
        a=a%b ;
    return a ;
}
ll mul (ll a,ll b,ll mm) {
    return (mod(a,mm)*mod(b,mm))%mm ;
}
ll add(ll a,ll b,ll mm) {
    return (mod(a,mm)+mod(b,mm))%mm ;
}
ll gcd (ll a,ll b) {
    if (a==-1||b==-1)   return -1 ;
    if (a==0||b==0)   return b|a ;
    else    return __gcd(a,b) ;
}
ll lcm (ll a,ll b) {
    return (a*b)/__gcd(a,b) ;
}
ll MMI (ll a,ll mm) {
    return fast_power(a,mm-2,mm)%mm ;
}
//*******************************************************************************************************************************************************//
//*****************************************************************-BY YOUR_DAD-*************************************************************************//
//*****************************************************************-PROGRAM STARTS FROM HERE-************************************************************//
ll n,k,arr[500005] ;
pp<pp<ll,ll>,ll> find (ll index) {
    ll i,cnt1,cnt2 ;
    for (i=index-1,cnt1=0;arr[i]==0&&i>0;i--)  cnt1++ ;
    for (i=index+1,cnt2=0;arr[i]==0&&i<n+1;i++) cnt2++ ;
    return mmp(mmp(min (cnt1,cnt2) , max(cnt1,cnt2) ), index  ) ;
}
pp<ll,ll> place ( ) {
    ll i,j,LS=-1,RS ;
    pp<pp<ll,ll>,ll> p ;
    for (i=1;i<=n;i++)
    {   if (arr[i]==0)
        {   p=find(i) ;
            if (p.F.F>LS)
            {   LS=p.F.F ;
                RS=p.F.S ;
                j=p.S ;
            }
            else if (p.F.F==LS&&p.F.S>RS)
            {   LS=p.F.F ;
                RS=p.F.S ;
                j=p.S ;
            }
        }
    }
    arr[j]=1 ;
    return mmp(LS,RS) ;
}
int main ( ) {
    ll j,t,i ;
    cin(t) ;
    for (j=1;j<=t;j++)
    {   cin(n) ;
        cin(k) ;
        pp <ll,ll> p ;
        for (i=0;i<=n+2;i++)
            arr[i]=0 ;
        arr[0]=arr[n+1]=1 ;
        for (i=0;i<k;i++)
            p=place() ;
        printf("Case #%lld: ",j) ;
        coutp(p.S,p.F) ;
    }
    return 0 ;
}
