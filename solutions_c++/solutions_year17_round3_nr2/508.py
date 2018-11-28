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
struct node{
    int st,ed;
}A[M],B[M];
int C[M];
bool cmp(node a,node b){
    return a.st<b.st;
}
bool cmp1(node a,node b){
    return a.ed-a.st<b.ed-b.st;
}
int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        memset(C,0,sizeof(C));
        int n,m;
        scanf("%d%d",&n,&m);
        for(int j=1;j<=n;j++){
            scanf("%d%d",&A[j].st,&A[j].ed);
            for(int k=A[j].st;k<A[j].ed;k++) C[k]=2;
        }
        for(int j=1;j<=m;j++){
            scanf("%d%d",&B[j].st,&B[j].ed);
            for(int k=B[j].st;k<B[j].ed;k++) C[k]=1;
        }
        sort(A+1,A+1+n,cmp);
        sort(B+1,B+1+m,cmp);
        int anss=INF;
        for(int a=1;a<=2;a++){
            if(C[0]&&C[0]!=a) continue;
            for(int b=1;b<=2;b++){
                if(C[1439]&&C[1439]!=b) continue;
                C[0]=a;
                C[1439]=b;
                int left[]={0,720,720};
                for(int j=0;j<1440;j++){
                    if(C[j]==1) left[1]--;
                    if(C[j]==2) left[2]--;
                }
                if(left[1]<0||left[2]<0);
                else{
//                    printf("a = %d b = %d\n",a,b);
                    vector<node>E;
                    for(int j=0;j<1440;){
                        int ed=j;
                        for(int k=j;k<1440;k++){
                            if(!C[k]){
                                ed=k+1;
                            }
                            else break;
                        }
                        if(j==ed){
                            j++;
                            continue;
                        }
//                        if(a==2&&b==1) printf("j = %d ed = %d\n",j,ed);
                        E.push_back({j,ed});
                        j=ed;
                    }
                    sort(E.begin(),E.end(),cmp1);
                    int ans=0;
                    for(int j=0;j<E.size();j++){
                        int l=E[j].st-1,r=E[j].ed;
//                        if(a==2&&b==1) printf("st = %d ed = %d ans = %d\n",E[j].st,E[j].ed,ans);
                        if(C[l]!=C[r]) ans++;
                        else{
                            if(E[j].ed-E[j].st<=left[C[l]]) left[C[l]]-=E[j].ed-E[j].st;
                            else ans+=2;
                        }
//                        if(a==2&&b==1) printf("st = %d ed = %d ans = %d\n",E[j].st,E[j].ed,ans);
                    }
                    if(a!=b) ans++;
                    for(int j=0;j<1439;j++){
                        if(C[j]&&C[j+1]){
                            if(C[j]!=C[j+1]) ans++;
                        }
                    }
//                    printf("a = %d b = %d ans = %d\n",a,b,ans);
                    anss=min(anss,ans);
                }
                memset(C,0,sizeof(C));
                for(int j=1;j<=n;j++) for(int k=A[j].st;k<A[j].ed;k++) C[k]=2;
                for(int j=1;j<=m;j++) for(int k=B[j].st;k<B[j].ed;k++) C[k]=1;
            }
        }
//        if(cas==71) printf("n = %d m = %d %d %d %d %d\n",n,m,A[1].st,A[1].ed,B[1].st,B[1].ed);
        printf("Case #%d: %d\n",cas++,anss);
    }
    return 0;
}
