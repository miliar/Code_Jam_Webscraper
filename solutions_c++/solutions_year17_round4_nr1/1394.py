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
const int M = 1e6 + 5, INF = 0x3f3f3f3f, mod = 1e9 + 7;
const double pi=acos(-1.0);
int A[M];
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        int n,m;
        scanf("%d%d",&n,&m);
        for(int j=1;j<=n;j++){
            scanf("%d",&A[j]);
        }
        printf("Case #%d: ",cas++);
        if(m==2){
            int cnt1=0,cnt2=0;
            for(int j=1;j<=n;j++){
                if(A[j]&1) cnt1++;
                else cnt2++;
            }
            printf("%d\n",(cnt1+1)/2+cnt2);
        }
        else if(m==3){
            int cnt1=0,cnt2=0,cnt3=0;
            for(int j=1;j<=n;j++){
                if(A[j]%3==0) cnt3++;
                else if(A[j]%3==1) cnt1++;
                else cnt2++;
            }
            printf("%d\n",cnt3+min(cnt1,cnt2)+(cnt1+cnt2-2*min(cnt1,cnt2)+2)/3);
        }
        else{
            int cnt1=0,cnt2=0,cnt3=0,cnt4=0;
            for(int j=1;j<=n;j++){
                if(A[j]%4==0) cnt4++;
                else if(A[j]%4==1) cnt1++;
                else if(A[j]%4==2) cnt2++;
                else cnt3++;
            }
            int ans1=min(cnt1,cnt3);
            cnt1-=ans1;cnt3-=ans1;
            int ans2=cnt2/2;
            cnt2%=2;
            int ans3=0;
            ans3+=cnt1/4+cnt3/4;
            cnt1%=4;cnt3%=4;
//            printf("cnt1 = %d cnt3 = %d cnt2 =%d ",cnt1,cnt3,cnt2);;
            if(cnt2){
                ans3++;
                if(cnt3==3||cnt1==3) ans3++;
            }
            else{
                if(cnt3>0||cnt1>0) ans3++;
            }
            printf("%d\n",ans1+ans2+ans3+cnt4);
        }
    }
    return 0;
}
