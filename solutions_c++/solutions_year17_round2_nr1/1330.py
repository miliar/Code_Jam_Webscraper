#include <iostream>
#include<stdio.h>
#include<cmath>
#define eps 0.000001
#define nmax 1005

using namespace std;

bool ok;
double st, dr, mjc, mom, iesire;
int s[nmax], k[nmax], d, n, maxs, t;


void verificare(){
    ok=true;
    mom=1.0*d/mjc;
    for (int i=1;i<=n;i++)
        if (s[i]<mjc){
            iesire=1.0*(d-k[i])/s[i];
            if (iesire>mom){
                ok=false;
                break;
            }
        }
}

void cautare(){
    st=0;   
    //dr=100000000000000000; //??
    dr=1000000000000000000; //??
    double difant=10;
    while (st<=dr){
        if (abs(st-dr)<=eps)
            break;
        if (abs(difant-(st-dr))<=eps)
            break;
        difant=st-dr;
        mjc=(st+dr)/2;
        verificare();
        if (ok)
            st=mjc+eps;
        else
            dr=mjc-eps;
    }
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++){
        scanf("%d %d",&d,&n);
        maxs=1;
        for (int i=1;i<=n;i++){
            scanf("%d %d",&k[i],&s[i]);
            maxs=max(maxs,s[i]);
        }
        cautare();
        printf("Case #%d: %.7f\n",ii,st);
    }
    return 0;
}
