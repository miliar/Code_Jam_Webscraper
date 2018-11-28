#include<fstream>
#include<math.h>
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
struct node{
    int down;
    int up;
};
node b[100][100];
bool cmp(node x, node y){
    if(x.down == y.down) return x.up < y.up;
    return x.down < y.down;
}
int r[100];
int loc[100];
int ans = 0;
int maxx = -1;
bool flag;
bool sec;
int mark = -1;
int main(){

    int i,j,k,l,_;
    int test;
    cin>>test;
    rep(_,test){
        CL(a);
        CL(b);
        CL(r);
        CL(loc);
        ans = 0;
        cin>>n>>m;
        rep(i,n){
            cin>>r[i];
        }
        rep(i,n){
            rep(j,m){
                cin >> a[i][j];
            }
        }
        rep(i,n){
            rep(j,m){
                b[i][j].down = ceil((double(a[i][j]) / 1.1) / r[i]);
                b[i][j].up = floor((double(a[i][j]) / 0.9) / r[i]);
            }
            sort(b[i] + 1, b[i] + 1 + m, cmp);
            loc[i] = m;
        }
        flag = false;
        while(1){

            maxx = -1;
            mark = -1;
            rep(i,n){
                if(b[i][loc[i]].down > maxx){
                    maxx = b[i][loc[i]].down;
                    mark = i;
                }
            }
            if(mark == -1){
                //Clear
                rep(i,n){
                    loc[i] -= 1;
                    if(loc[i] <= 0){
                        flag = true;
                        break;
                    }
                }
            }
            else{
                sec = true;
                rep(i,n){
                    if(b[i][loc[i]].up < maxx){
                        sec = false;
                        break;
                    }
                }
                if(sec){
                    ans++;
                    //Clear
                    rep(i,n){
                        loc[i] -= 1;
                        if(loc[i] <= 0){
                            flag = true;
                            break;
                        }
                    }
                }
                else{
                    loc[mark] -= 1;
                    if(loc[mark] <= 0){
                        flag = true;
                    }
                }
            }
            if(flag){
                break;
            }
        }
        cout<<"Case #"<<_<<": "<<ans<<endl;
    }
    return 0;
}
