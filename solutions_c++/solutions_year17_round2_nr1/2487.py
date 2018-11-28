/* Author => Aakash Prakash (akki744) */
#include<bits/stdc++.h>

#define MOD 1000000007
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define SET(a,val) memset(a, val, sizeof(a))

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

#define SC(x) scanf("%d",&x)
#define SCL(x) scanf("%lld",&x)
#define SCC(x) scanf("%c",&x)
#define SCS(x) scanf("%s",x)
#define SCU(x) scanf("%llu",&x)

#define PF printf

#define PB(x) push_back(x)
#define MP(a,b) make_pair(a,b)

using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

typedef  pair<int,int> 	         pii;
typedef  vector<int> 	         vi;

namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

LL gcd(LL a, LL b){
    if(b==0)
	return a;
    return gcd(b,a%b);
}

LL lcm(LL a, LL b){
    return (a*b)/gcd(a,b);
}

int main(){
    int t;
    cin>>t;
    REP(z,t){
        int d,n;
        cin>>d>>n;
        double tm,curr;
        int a,b;
        for(int i=0; i<n; i++){
            cin>>a>>b;
            if(i==0){
                tm=(double)(d-a)/b;
            }else{
                curr=(double)(d-a)/b;
                if(curr>tm){
                    tm=curr;
                }
            }
        }
        tm=(double)d/tm;
        cout<<"Case #"<<(z+1)<<": ";
        cout<<fixed<<setprecision(6)<<tm<<endl;
    }
    return 0;
}

//time_t t=clock();
//cout<<(double)(clock()-t)/CLOCKS_PER_SEC<<endl;
