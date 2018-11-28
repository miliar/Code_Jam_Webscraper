#include <iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
struct element{int r,h;};
#define pi 3.141592653589793238462643383279502884197169399375105820974944592307816406286
int n, k, t;
double rez, nr[1005][1005];
element v[1005];

bool cmp(element a, element b){
    return a.r>b.r;
}

double acerc(int r){
    return pi*r*r; 
}

double acontur(int r, int h){
    return 2*pi*r*h;
}

void calculare(){
    rez=0;
    for (int poz=1;poz<=n;poz++){
        nr[poz][1]=acerc(v[poz].r)+acontur(v[poz].r,v[poz].h);
        for (int kk=2;((kk<=k)&&(kk<=poz));kk++){
            nr[poz][kk]=0;
            for (int an=1;an<poz;an++)
                nr[poz][kk]=max(nr[poz][kk],nr[an][kk-1]+acontur(v[poz].r,v[poz].h));
        }
        rez=max(rez,nr[poz][k]);
    }
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++){
        scanf("%d %d",&n,&k);
        for (int i=1;i<=n;i++)
            scanf("%d %d",&v[i].r,&v[i].h);
        sort(v+1,v+1+n,cmp);
        calculare();
        printf("Case #%d: %.10f\n",ii,rez);
    }
    return 0;
}
