#include <iostream>
#include <cstdio>
#define N 1005
using namespace std;
typedef long long ll;
int T,D,n,k[N],s[N];
bool check(__float128 v){
    for(int i=0;i<n;++i)
        if((__float128)D*s[i]<v*(D-k[i]))return 0;
    return 1;
}
int main(void){//__float128
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        scanf("%d%d",&D,&n);
        __float128 l=1.0,r=1e15;
        for(int i=0;i<n;++i)scanf("%d%d",&k[i],&s[i]);
        while(r-l>1e-7){
            __float128 m=(r+l)/2;
            if(check(m))l=m;
            else r=m;
        }
        printf("Case #%d: %.6lf\n",t,(double)r);
    }
}
