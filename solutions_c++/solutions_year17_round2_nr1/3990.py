#include "cstdio"
#include "algorithm"
#include "string"
#include "cstring"
#include "queue"
#include "cmath"
#include "vector"
#include "map"
#include "stdlib.h"
#include "set"
#define inf 0x3f3f3f
#define mj
#define db double
#define ll long long
using  namespace std;
const int N=1e5+5;
const int mod=1e9+7;
int k[300],s[300];
typedef struct  M
{
    int k,s;
    db x;
};
M a[1002];
int cmp(M a,M b)
{
    return a.x<b.x;
}
int main()
{
    int t;
    scanf("%d",&t);
    for(int ii=1;ii<=t;ii++)
    {
        int d,n;
        scanf("%d%d",&d,&n);
        for(int i=0;i<n;i++){
            scanf("%d%d",&k[i],&s[i]);
            a[i].k=k[i],a[i].s=s[i];
            a[i].x=(d-k[i])*1.0/s[i];
        }
        sort(a,a+n,cmp);
//        for(int i=0;i<n;i++)
//            printf("%f\n",d/a[i].x);
        printf("Case #%d: %.6f\n",ii,d/a[n-1].x);

    }
}