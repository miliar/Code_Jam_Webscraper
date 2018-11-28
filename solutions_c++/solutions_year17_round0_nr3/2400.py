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
#define PCASE() printf("Case #%d: ",kk++)
#define eps 1e-9
#define inf 2000000000
#define mod 1000000007
#define MX  1000000
using namespace std;

int t,kk=1;
long long n,k,sum,val,valCount;
map<long long, long long>m[2];
map<long long, long long>::reverse_iterator it;

void printResult(long long num){
  num--;
  PCASE();
  if(num%2) cout<<num/2+1<<" "<<num/2<<endl;
  else cout<<num/2<<" "<<num/2<<endl;
}

int main()
{
    freopen("c2.in","r",stdin);
    freopen("c2.txt","w",stdout);
    scanf("%d",&t);
    while(t--){
        S(n);S(k);
        sum = 0;
        m[0].clear();
        m[1].clear();
        m[0][n] = 1;
        int cur=0,nw = 1;
        while(sum<k){
            m[nw].clear();
            for(it = m[cur].rbegin(); it!=m[cur].rend(); it++){
                val = it->first;
                valCount = it->second;
                if(sum+valCount >= k) {
                    printResult(val);
                    sum+=valCount;
                    break;
                }
                sum+=valCount;
                val--;
                if(val%2 == 0){
                    val/=2;
                    valCount*=2;
                    if(m[nw][val]) m[nw][val]+=valCount;
                    else m[nw][val] = valCount;
                }
                else{
                    val/=2;
                    if(m[nw][val]) m[nw][val]+=valCount;
                    else m[nw][val] = valCount;
                    if(m[nw][val+1]) m[nw][val+1]+=valCount;
                    else m[nw][val+1] = valCount;
                }
            }
            nw = (nw^1);
            cur = (cur^1);
        }
    }
    return 0;
}


