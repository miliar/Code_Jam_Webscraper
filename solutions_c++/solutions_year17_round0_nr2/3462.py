#pragma comment(linker, "/STACK:102400000,102400000")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <complex>
#define LL long long
#define ULL long long
#define ls(x) tree[x].ls
#define rs(x) tree[x].rs
#define maxx(x) tree[x].maxx
#define len(p) (p.R-p.L+1)
#define keytree ch[ch[root][1]][0]
#define dis(x) dis[x.x1][x.y1][x.x2][x.y2][x.dir1][x.dir2]
using namespace std;
const int M = 2e5 + 5, INF = 0x3f3f3f3f, mod = 1e9 + 7;
char s[M];
int sum[M];
int main() {
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        scanf("%s",s+1);
        int n=strlen(s+1);
        int st=-1;
        int ok=1;
        for(int j=2;j<=n;j++){
            if(s[j]<s[j-1]){
                ok=0;
                break;
            }
            if(s[j]>s[j-1]&&st==-1) st=j;
        }
        printf("Case #%d: ",cas++);
        if(!ok&&st==-1){
            if(s[1]=='1'){
                for(int j=1;j<=n-1;j++) printf("9");
                printf("\n");
            }
            else{
                printf("%c",s[1]-1);
                for(int j=1;j<=n-1;j++) printf("9");
                printf("\n");
            }
        }
        if(!ok&&~st){
            for(int j=1;j<st;j++) printf("%c",s[j]);
            printf("%c",s[st]-1);
            for(int j=st+1;j<=n;j++) printf("9");
            printf("\n");
        }
        if(ok) printf("%s\n",s+1);
    }
    return 0;
}
