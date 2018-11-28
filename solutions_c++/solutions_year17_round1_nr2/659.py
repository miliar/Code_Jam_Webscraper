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
ld ldabs (ld n) {
    if (n<0)    return -n ;
    return n ;
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
ll n,r[100],p ;
vector <pp<ll,ll> > vec[100] ;
vector <ll> mat[100] ;
ll find1 (ld val,ld have) {
    ld temp = floor((10*have)/(9*val)) ;
    return temp ;
}
ll find2 (ld val,ld have) {
    ld temp = ceil((10*have)/(11*val)) ;
    return temp ;
}
pp <ll,ll> find (ll val,ll have) {
    ll i,s=MAX,e=0 ;
    for (i=1;;i++)
        if ((val*9*i<=have*10)&&(val*11*i>=have*10))
        {   s=min(s,i) ;
            e=max(e,i) ;
        }
        else if (!(val*9*i<=have*10))
            break ;
    if (s==MAX)
        return mmp(0,0) ;
    else
        return mmp(s,e) ;
}
ll process ( ) {
    ll i,cnt=0,mx ;
    while(1)
    {   for (i=0;i<n;i++)
            if (SZ(vec[i])==0)
                return cnt ;
        for (i=0,mx=0;i<n;i++)
        {   mx=max(vec[i].back().F,mx) ;
        }
        for (i=0;i<n;i++)
        {   if (mx>=vec[i].back().F&&mx<=vec[i].back().S)
                vec[i].pop_back() ;
            else
            {   while( SZ(vec[i])>0&&(!(mx>=vec[i].back().F&&mx<=vec[i].back().S)) )
                    vec[i].pop_back() ;
                if (SZ(vec[i])==0)
                    return cnt ;
                vec[i].pop_back() ;
            }
        }
        cnt++ ;
    }
    return cnt ;
}
int main ( ) {
    ll i,j,k,t,mm ;
    cin(t) ;
    for (k=1;k<=t;k++)
    {   cin(n) ;
        cin(p) ;
        for (i=0;i<n;i++)
        {   cin(r[i]) ;
            vec[i].clear() ;
            mat[i].clear() ;
        }
        for (i=0;i<n;i++)
            for (j=0;j<p;j++)
            {   cin(mm) ;
                mat[i].pb(mm) ;
            }
        for (i=0;i<n;i++)
            sort(ALL(mat[i]),greater<ll>()) ;
        for (i=0;i<n;i++)
            for (j=0;j<p;j++)
            {  pp<ll,ll> ar = find(r[i],mat[i][j]) ;
                if (!(ar.F==0&&ar.S==0))
                    vec[i].pb(ar) ;
            }
        for (i=0;i<n;i++)
            sort(ALL(vec[i]),greater<pp<ll,ll> >()) ;
//        for (i=0;i<n;i++)
//        {   for (j=0;j<p;j++)
//                cout<<"( "<<vec[i][j].F<<','<<vec[i][j].S<<" ) " ;
//            cout<<endl ;
//        }
        printf("Case #%lld: ",k) ;
        cout(process( )) ;
    }
    return 0 ;
}
