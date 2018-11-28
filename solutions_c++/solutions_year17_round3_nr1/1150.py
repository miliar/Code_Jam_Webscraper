/// ///////////////////// ///
///                       ///
///      Tamanna_24       ///
///                       ///
///         JU            ///
///                       ///
/// ///////////////////// ///

#include<iostream>
#include<sstream>
#include<cstring>
#include<cstdio>
#include<string>
#include<cmath>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<cstdlib>
#include<cctype>

typedef long long ll;
typedef unsigned long long ull;

#define pi 2.0*acos(0.0)

template <class T> T _diff(T a,T b) {return (a<b?b-a:a-b);}
template <class T> T _abs(T a) {return(a<0?-a:a);}
template <class T> T _max(T a, T b) {return (a>b?a:b);}
template <class T> T _min(T a, T b) {return (a<b?a:b);}
template <class T> T max3(T a, T b, T c) {return (_max(a,b)>c ? _max(a,b) : c);}
template <class T> T min3(T a, T b, T c) {return (_min(a,b)<c ? _min(a,b) : c);}
template< class T>T GCD(T a,T b) {
    a=_abs(a);b=_abs(b);T tmp;while(a%b){ tmp=a%b; a=b; b=tmp; } return b;
}
template< class T>T LCM(T a,T b) {
    a=_abs(a);b=_abs(b);return (a/GCD(a,b))*b;
}
template<class T> T toRad(T deg) { return (deg*pi)/(180.0) ;}
template<class T> T toDeg(T rad) { return (rad*180.0)/(pi) ;}

#define pb(a) push_back(a)
#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define S(a) scanf("%lld",&a)
#define P(a) printf("%lld",a)
#define PN() puts("")
#define PCASE() printf("Case #%lld: ",kk++)
#define eps 1e-9
#define inf 2000000000
#define mod 1000000007
#define MX  1000000
using namespace std;

vector<pair<long long,long long> >pan;
long long n,k,dp[1005][1005],r,h;
long long t,kk=1;

long long takePan(int pos, int cnt){
    long long res = pan[pos].second*pan[pos].first*2;
    if(cnt == 0) res += pan[pos].first * pan[pos].first;
    return res;
}

long long func(long long pos, long long cnt){
    if(cnt==k) return 0;
    else if(pos<0){
        return -inf;
    }
    else if(dp[pos][cnt] != -1 ) return dp[pos][cnt];
    return dp[pos][cnt] = max(takePan(pos,cnt)+func(pos-1,cnt+1), func(pos-1,cnt));
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.txt","w",stdout);

    cin>>t;
    while(t--){
        S(n);S(k);
        pan.clear();
        SET(dp);
        for(int i=0;i<n;i++){
            S(r);S(h);
            pan.push_back(make_pair(r,h));
        }
        sort(pan.begin(),pan.end());
        long long res = func(n-1,0);
        double res1 = ((double)res)*pi;
        PCASE();
        printf("%.9lf\n",res1);
    }
return 0;
}





