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

int len,arr[18];

bool isTidy(LL n){
    if((n/10)==0){
        return true;
    }
    int curr,prev=n%10;
    n/=10;
    while(n){
        curr=n%10;
        n/=10;
        if(curr>prev){
            return false;
        }
        prev=curr;
    }
    return true;
}

int calculate(LL n, int i){
    if(n==0){
        return 0;
    }
    arr[i]=n%10;
    return 1+calculate(n/10, i+1);
}

LL getLastTidy(){
    int prev=arr[0],viol=-1,index;
    FOR(i,1,len-1){
        if(arr[i]>prev || viol==arr[i]){
            viol=arr[i];
            index=i;
        }
        prev=arr[i];
    }
    if(arr[index]==1 && index==len-1){
        len--;
    }else{
        arr[index]--;
    }
    FORD(i,index-1,0){
        arr[i]=9;
    }
    LL ans=0;
    FORD(i,len-1,0){
        ans*=10;
        ans+=arr[i];
    }
    return ans;
}

int main() {
    int t;
    SC(t);
    REP(z,t){
        LL n;
        SCL(n);
        PF("Case #%d: ",(z+1));
        if(isTidy(n)){
            PF("%lld\n",n);
        }else{
            len=calculate(n,0);
            PF("%lld\n",getLastTidy());
        }
    }
    return 0;
}

//time_t t=clock();
//cout<<(double)(clock()-t)/CLOCKS_PER_SEC<<endl;
