#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#define rep(i,a,b) for (int i = (a); i <= (b); ++i)
#define rep(i,a,b) for (int i = (a); i <= (b); ++i)
typedef long long ll;
using namespace std;
const int N = 1010;
int k, n, m, x, y;
double ans, f[N][N];
struct node{
    int x, y;
}a[N];
string s;
bool cmp(node a,node b){
    return (a.x > b.x || (a.x == b.x && a.y > b.y));
}
int main() {
    freopen("/users/Mr.ZY/Documents/Program/GCJ2017-1C-A/1.txt","r",stdin);
    freopen("/users/Mr.ZY/Documents/Program/GCJ2017-1C-A/A.txt","w",stdout);
     //printf("pi=%f,e=%f\n",M_PI,M_E);
    int ttt;
    cin >> ttt;
    rep (sss,1,ttt){
        memset(f,0,sizeof(f));
        memset(a,0,sizeof(a));
        cin >> n >> m;
        ans = 0;
        rep (i,1,n){
            cin >> x >> y;
            a[i].x = x;
            a[i].y = y;
        }
        sort(a+1,a+n+1,cmp);
        rep (i,1,n){
            rep (j,1,i){
                f[i][j] = f[i-1][j];
                if (j == 1){
                    f[i][j] = max(f[i][j],1.0*M_PI*a[i].x*(1.0*a[i].x+2.0*a[i].y));
                }else{
                    f[i][j] = max(f[i][j],f[i-1][j-1]+2.0*M_PI*a[i].x*a[i].y);
                }
                
            }
        }
        rep (i,1,n){
            rep (j,1,m){
                ans = max(ans,f[i][j]);
            }
        }
        //cout << ans << endl;
        printf("Case #%d: %.10lf\n",sss,ans);
    }
    return 0;
}
