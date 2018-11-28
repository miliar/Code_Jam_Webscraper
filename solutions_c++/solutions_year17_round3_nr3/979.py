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
#define S(a) scanf("%d",&a)
#define P(a) printf("%.9lf\n",a)
#define PN() puts("")
#define PCASE() printf("Case #%d: ",kk++)
#define eps 1e-9
#define inf 2000000000
#define mod 1000000007
#define MX  1000000
using namespace std;

int t,kk=1;
int n,k;
long long u;
double x;

struct data{
    long long p;
    bool operator<(const data &b)const{
        return p>b.p;
    }
}tmp;
priority_queue<data>pq;

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.txt","w",stdout);
    cin>>t;
    while(t--){
        cin>>n>>k>>x;
        u = (x*10000+eps);
        while(!pq.empty())pq.pop();
        for(int i=0;i<n;i++){
            cin>>x;
            tmp.p= ((long long)(x*10000.0+eps));
            pq.push(tmp);
        }
        for(int i = 1;i<=u;i++){
            //cout<<i<<endl;
            if(!pq.empty()){
                tmp= pq.top();
                pq.pop();
                //cout<<i<<" "<<tmp.p<<endl;
                if(tmp.p <10000){
                    tmp.p++;
                    pq.push(tmp);
                }
            }
            else break;
        }

        double res = 1.0;
        while(!pq.empty()){
            tmp = pq.top();
            pq.pop();
            x=((double)tmp.p) / 10000.0;
            res*=x;
        }
        PCASE();
        P(res);
    }

return 0;
}





