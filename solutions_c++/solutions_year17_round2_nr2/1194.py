#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <vector>
#include <time.h>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <iostream>
#include <assert.h>
#include <bitset>
#include <algorithm>
using namespace std;
#define MP make_pair
#define PB push_back
#define mst(a,b) memset((a),(b),sizeof(a))
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> Pii;
typedef vector<int> Vi;
typedef vector<Pii> Vii;
const int inf = 0x3f3f3f3f;
const LL INF = (1uLL << 63) - 1;
const int mod = 1e9 + 7;
const double Pi = acos(-1.0);
const int maxn = 1e5 + 5;
const int N = 2e4 + 5;
const ULL hashmod = 2908361;
const double eps = 1e-8;
int n,R,O,Y,G,B,V;
struct M{
    char a;
    int num;
    bool operator < (const M &c)const{
        return num < c.num;
    }
};
M col[11];
char ans[1111];
int main() {
#ifdef local
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("w","w",stdout);
#endif
   // ios::sync_with_stdio(false);
  //  cin.tie(0);
    int t;
    scanf("%d",&t);
    int ssss = 1;
    while(t--){
        printf("Case #%d: ",ssss++);
        col[0].a = 'R';col[1].a = 'O';col[2].a = 'Y';col[3].a = 'G';col[4].a = 'B';col[5].a = 'V';
        scanf("%d%d%d%d%d%d%d",&n,&R,&O,&Y,&G,&B,&V);
        col[0].num = R;col[1].num = O;col[2].num = Y;col[3].num = G;col[4].num = B;col[5].num = V;
        sort(col,col+6);
        if(col[5].num > col[4].num + col[3].num)printf("IMPOSSIBLE\n");
        else {
            int all = col[5].num + col[4].num + col[3].num;
            int tmp = (all + 1)/2;
            int ccc = all - tmp;
            for(int i = 0;tmp;--tmp,i+=2){
                if(col[5].num)ans[i] = col[5].a,col[5].num--;
                else ans[i] = col[3].a,col[3].num--;
            }
            for(int i = 1;ccc;ccc--,i+=2){
                if(col[3].num)ans[i] = col[3].a,col[3].num--;
                else ans[i] = col[4].a,col[4].num--;
            }
            ans[all] = '\0';
            puts(ans);
        }
    }
}
