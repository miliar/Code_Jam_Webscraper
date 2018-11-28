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

int main() {
    int t;
    SC(t);
    REP(z,t){
        LL n,k;
        SCL(n);
        SCL(k);
        PF("Case #%d: ",(z+1));
        if(k==1){
            PF("%lld %lld\n",(n/2LL),(n-(n/2LL)-1));
            continue;
        }
        LL ansmx,ansmn,powe=1LL,sum=0,a,b,num=n;
        while(k>powe && num>2){
            k-=powe;
            sum+=powe;
            powe*=2LL;
            num=(n-sum)/powe;
        }
        a=((num+1)*powe)-(n-sum);
        b=powe-a;
        if(num<=2 && k>powe){
            PF("0 0\n");
            continue;
        }
        if(k<=b){
            num++;
        }
        ansmx=num/2LL;
        ansmn=num-ansmx-1;
        PF("%lld %lld\n",ansmx,ansmn);
    }
    return 0;
}

//time_t t=clock();
//cout<<(double)(clock()-t)/CLOCKS_PER_SEC<<endl;
