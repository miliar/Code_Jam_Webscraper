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
int main(){

    int i,j,k,l,_;
    int test;
    int tem;
    cin>>test;
    bool flag = false;
    rep(_,test){
        cin>>s;
        int len = strlen(s);

        repm(i,0,len-1){
            flag = false;
            repm(j,i+1,len-1){
                if(s[j] < s[i]){
                    flag = true;
                    break;
                }
                else if(s[j] > s[i]){
                    flag = false;
                    break;
                }
            }
            if(flag == true){
                if(s[i] == '0'){
                    cout<<"error"<<endl;
                }
                else{
                    s[i]-=1;
                    repm(j,i+1,len-1){
                        s[j] = '9';
                    }
                }
                break;
            }
        }
        cout<<"Case #"<<_<<": ";
        flag = false;
        repm(i,0,len-1){
            if(s[i] != '0' and !flag){
                flag = true;
            }
            if(flag){
                cout<<s[i];
            }
        }
        cout<<endl;
    }
    return 0;
}
