#include<fstream>
#include<algorithm>
#include<memory.h>
#include<string>
#include<vector>
#include<stdio.h>
#include<map>
#include<set>
#include<bitset>
#include<sstream>
#define rep(i,n) for(i=1;i<=n;i++)
#define repm(i,b,n) for(i=b;i<=n;i++)
#define repr(i,n) for(i=n;i>=1;i--)
#define repmr(i,n,b) for(i=n;i>=b;i--)
#define pr pair<LL,LL>
#define CL(a) memset(a,0,sizeof(a))
#define MAX_INT 2147483647
#define MOD 1000000007
using namespace std;
ifstream cin("A.in");
ofstream cout("A.out");
typedef long long LL;
int n,m;
LL a,b,c,d;
int main(){

    int i,j,k,l,_;
    int test;
    cin>>test;
    bool flag = false;
    LL sum;
    LL cnt;
    LL res;
    rep(_,test){
        cin>>a>>b;
        sum = 1;
        cnt = 0;
        while( b > sum-1){
            cnt++;
            sum *= 2;
        }
        cnt-=1;
        a = a - (1<<cnt) + 1;
        b = b - (1<<cnt) + 1;
        c = int(a/(1<<cnt));
        d = a % (1<<cnt);
        if(b <= d){
            res = c+1;
        }
        else{
            res = c;
        }
        if(res%2 == 0){
            cout<<"Case #"<<_<<": "<<res / 2<<" "<<res / 2 - 1<<endl;
        }
        else{
            cout<<"Case #"<<_<<": "<<(res - 1) / 2<<" "<<(res - 1) / 2<<endl;
        }
        //cout<<"Case #"<<_<<": "<< <<" "<< <<endl;
    }
    return 0;
}
