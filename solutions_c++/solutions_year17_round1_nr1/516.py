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
int a[100][100];
int main(){

    int i,j,k,l,_;
    int test;
    char tem[100];
    cin>>test;
    rep(_,test){
        cin>>n>>m;
        CL(a);
        rep(i,n){
            cin>>tem;
            rep(j,m){
                if(tem[j-1] >= 'A' and tem[j-1] <= 'Z')  a[i][j] = tem[j-1] - 'A' + 1;
            }
        }
        bool flag = false;
        int rec;
        int last = -1;
        int first = -1;
        rep(i,n){
            flag = false;
            rec = 0;

            rep(j,m){
                if(a[i][j] != 0){
                    flag = true;
                    rec = a[i][j];
                    break;
                }
            }
            if(flag){
                rep(j,m){
                    if(a[i][j] == 0) a[i][j] = rec;
                    else rec = a[i][j];
                }
                last = i;
                if(first == -1) first = i;
            }
            else{
                if(last != -1){
                    rep(j,m){
                        a[i][j] = a[last][j];
                    }
                    if(first == -1) first = i;
                    last = i;
                }


            }

        }
            repm(i,1,first - 1){
                rep(j,m){
                    a[i][j] = a[first][j];
                }
            }
        char t;
        cout<<"Case #"<<_<<":"<<endl;
        rep(i,n){
            rep(j,m){
                t = a[i][j] + 'A' - 1;
                cout<<t;
            }
            cout<<endl;
        }
    }
    return 0;
}
