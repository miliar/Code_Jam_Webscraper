#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
using namespace std;
#define LL long long
#define mp make_pair
#define fr first
#define sc second
#define pb push_back
#define lc (x<<1)
#define rc ((x<<1)|1)
const int N=55;
int l[N][N],r[N][N],k[N],aa[N][N],c[N];
bool cal(int n){
    int i,s=l[1][k[1]],t=r[1][k[1]];
    for (i=2;i<=n;i++) {s=max(s,l[i][k[i]]);t=min(t,r[i][k[i]]);}
    return (s<=t);
}
int main(){
   // freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int T,T0=0;cin>>T;
    while (T--){
        cout<<"Case #"<<++T0<<": ";
        int i,j,n,m,ans=0;
        scanf("%d%d",&n,&m);
        for (i=1;i<=n;i++) scanf("%d",&c[i]);
        for (i=1;i<=n;i++){
            for (j=1;j<=m;j++) scanf("%d",&aa[i][j]);
            sort(aa[i]+1,aa[i]+m+1);
        }
        for (i=1;i<=n;i++) for (j=1;j<=m;j++){
            int A=aa[i][j];
            l[i][j]=(A*10)/(11*c[i])-1,r[i][j]=(A*10)/(9*c[i])+1;
            while (l[i][j]*11*c[i]/10<A) l[i][j]++;
            while (r[i][j]*9*c[i]/10>A) r[i][j]--;
        }
        for (i=1;i<=n;i++) k[i]=1;
        while (1){
            if (cal(n)) {ans++;for (i=1;i<=n;i++) k[i]++;} else
                {
                    int mi=1;
                    for (i=1;i<=n;i++) if (r[i][k[i]]<r[mi][k[mi]]) mi=i;
                    k[mi]++; 
                }
            for (i=1;i<=n;i++) if (k[i]>m) break;
            if (i<=n) break;
        }
        printf("%d\n",ans);
    }
  //  system("pause");
    return 0;
}
