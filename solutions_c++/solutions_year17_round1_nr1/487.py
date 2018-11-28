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
const int N=105;
int a[N][N],b[N];
char s[N];
int main(){
  //  freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int T,T0=0;cin>>T;
    while (T--){
        cout<<"Case #"<<++T0<<":"<<endl;
        int i,ii,j,k,n,m;
        scanf("%d%d",&n,&m);
        for (i=1;i<=n;i++){
            scanf("%s",s+1);
            for (j=1;j<=m;j++) if (s[j]=='?') a[i][j]=0; else a[i][j]=s[j]-'A'+1;
        }
        for (i=1;i<=n;i++){
            for (j=1;j<=m;j++) if (a[i][j]) break;
            if (j<=m) b[i]=0; else b[i]=1;
        }
        for (i=1;i<=n;i++) if (!b[i]) break;ii=i;
        for (i=ii;i<=n;i++)
         if (b[i]) for (j=1;j<=m;j++) a[i][j]=a[i-1][j]; else
            {
                for (j=1,k=1;j<=m;j++) if (a[i][j]) for (;k<=j;k++) a[i][k]=a[i][j];
                for (j=--k;j<=m;j++) a[i][j]=a[i][k];
            } 
        for (i=1;i<ii;i++) for (j=1;j<=m;j++) a[i][j]=a[ii][j];
        for (i=1;i<=n;i++){
            for (j=1;j<=m;j++) putchar('A'+a[i][j]-1);
            puts("");
        }
    }
  //  system("pause");
    return 0;
}
