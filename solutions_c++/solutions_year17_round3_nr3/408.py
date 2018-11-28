#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#define pb push_back
#define mp make_pair
#define eps 1e-9
#define zero(x) (fabs(x)<eps)
#define pi acos(-1.0)
#define f1 first
#define f2 second
#define CLR(x,y) memset(x,y,sizeof(x))
using namespace std;
typedef long long LL;
typedef pair <int, int> PII;
template<typename X> inline bool minimize(X&p,X q){if(p<=q)return 0;p=q;return 1;}
template<typename X> inline bool maximize(X&p,X q){if(p>=q)return 0;p=q;return 1;}
#define fr(i,x,y) for(int i=x;i<=y;i++)
double b[55];
int a[55],n[55];
int k,m,p;
int  doit(){
    scanf("%d%d",&m,&p);

    double x;
    scanf("%lf", &x);
    k=int((x + eps) * 10000);
    fr(i,1,m) {
        scanf("%lf", &x);
        b[i] = x;
        a[i] = int((x + eps) * 10000);
    }
    sort(a+1,a+m+1);
    sort(b+1,b+1+m);


        a[m+1]=10000;

    int j,i=1;
    while (i<=m){
        j=i;
        while (a[j]==a[i]&&j<=m)j++;
        fr(z,i,j-1) n[z]=j;
        i=j;
    }



       //int
     i=1;
    while (i<=m)
     {
            int j=n[i];
            if (k==0) break;
            if ((a[n[i]]-a[i])*(j-1)<=k) {
                //printf("%d %d %d %d\n",ge,a[n[i]]-1,i,k);
                fr(z, 1, j - 1)b[z] += (a[n[i]] - a[i]) / 10000.;
                k-=(a[n[i]]-a[i])*(j-1);
            }
            else{
                fr(z, 1, j - 1)b[z] += k / 10000./(j-1);
                break;
            }
            i=j;
        }
  //  if (xxx)fr(i,1,m)printf("~~~~`%lf\n",b[i]);
    double an=1;
      fr(i,1,m)  an*=b[i];
    printf("%lf\n",an);
}
int main() {
   freopen("C-small-1-attempt1 (1).in","r",stdin);
    freopen("C-small-1-attempt1 (1).out","w",stdout);

    int cas,i=0;
    scanf("%d",&cas);
    while (cas--)
    {
        printf("Case #%d: ",++i);
        doit();

    }
}
/*
 4
4 4
1.3000
0.5000 0.7000 0.8000 0.6000
 */