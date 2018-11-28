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
#define MOD 1000002013
using namespace std;
ifstream cin("A.in");
ofstream cout("A.out");
typedef long long LL;
int n,m;
struct node{
    int p;
    int b;
};
node a[2000];
bool cmp1(node x, node y){
    if(x.p == y.p) return x.b < y.b;
    return x.p < y.p;
}
struct pass{
    int num;
    int cnt1;
    int cnt2;
};
bool cmp2(pass x, pass y){
    if(x.cnt1 == y.cnt1) return x.num < y.num;
    return x.cnt1 > y.cnt1;
}
pass b[2000];
int st[2000];
int cnt[10][2000];
bool is[1010][1010];
int main(){

    int i,j,k,l,_;
    int test;
    int c;
    cin>>test;
    //FILE * fp;
    //fp = fopen("A.out","w");
    rep(_,test){
        int ans = 0;
        cin>>n>>c>>m;
        int t1 = 0, t2 = 0;
        CL(cnt);
        CL(is);
        rep(i,m){
            cin>>a[i].p>>a[i].b;
            cnt[a[i].b][a[i].p]++;
            if(a[i].b == 1) t1++;
            else t2++;
        }
        if(c == 1){
            cout<<"Case #"<<_<<": "<<m<<" "<<0<<endl;
        }
        else{
            int a1 = 0;
            int ans = max(t1,t2);
            int the;
            if(t1 > t2) the = 1;
            else the = 2;
            rep(i,m){
                if(a[i].b == the){
                    is[i][a[i].p] = 1;
                }
            }
            rep(i,m){
                if(a[i].b == 3-the){

                    bool is_find = 0;
                    rep(j,m){
                        if(a[j].b == the and !is[j][a[i].p]){
                            is[j][a[i].p] = 1;
                            is_find = 1;
                            break;
                        }
                    }

                    if(!is_find){
                        if(a[i].p == 1){
                            ans++;
                        }
                        else a1++;
                    }
                }
            }
            cout<<"Case #"<<_<<": "<<ans<<" "<<a1<<endl;
        }
    }
    return 0;
}
/*
3 3 2
3 1
2 2
3 3
2 2
3 1
*/
