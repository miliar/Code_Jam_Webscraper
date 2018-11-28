#include <iostream>
#include<stdio.h>
using namespace std;
#define nmax 1005 
long long n, poz[nmax], dist[nmax], e[nmax], s[nmax], t, q, x;
double tmin[nmax], tac; 
void rezolvare(){
    tmin[1]=0;
    for (int i=2;i<=n;i++){
        tmin[i]=-1;
        for (int j=1;j<i;j++)
            if (poz[i]-poz[j]<=e[j]){
                tac=tmin[j]+1.0*(poz[i]-poz[j])/s[j];
                if ((tac<tmin[i]) || (tmin[i]==-1))
                    tmin[i]=tac;
            }
    }
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++){
        scanf("%lld %lld",&n,&q);
        for (int i=1;i<=n;i++)
            scanf("%lld %lld",&e[i],&s[i]);
        for (int i=1;i<=n;i++){
            bool gasit=0;
            for (int j=1;j<=n;j++){
                scanf("%lld",&x);
                if (x!=-1){
                    dist[i+1]=x;
                    gasit=1;
                }
            }
            if ((!gasit)&&(i<n))
                printf("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
        }
        for (int i=1;i<=n;i++)
            poz[i]=poz[i-1]+dist[i];
        scanf("%lld %lld",&x,&x);
        rezolvare();
        printf("Case #%d: %.7f\n",ii,tmin[n]);
    }
    return 0;
}
