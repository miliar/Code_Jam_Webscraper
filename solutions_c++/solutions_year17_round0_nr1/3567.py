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
char s[1010];
int a[1010];
int main(){

    int i,j,k,l,_;
    int test;
    int tem;
    cin>>test;
    rep(_,test){
        cin>>s>>k;
        CL(a);
        int len = strlen(s);
        repm(i,0,len-1){
            if(s[i] == '+'){
                a[i+1] = 1;
            }
            else{
                a[i+1] = -1;
            }
        }
        int cnt = 0;
        bool flag = false;
        rep(i,len){
            if(a[i] == -1){
                if(len-i+1 < k){
                    flag = true;
                    break;
                }
                repm(j,i,i+k-1){
                    a[j] = 0 - a[j];
                }
                cnt += 1;
            }

        }
        if(flag){
            cout<<"Case #"<<_<<": "<<"IMPOSSIBLE"<<endl;
        }
        else{
            cout<<"Case #"<<_<<": "<<cnt<<endl;
        }
    }
    return 0;
}
