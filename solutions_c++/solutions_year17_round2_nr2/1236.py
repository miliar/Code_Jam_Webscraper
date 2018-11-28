#include <iostream>
#include<stdio.h>
using namespace std;
#define nmax 1005


int n, pr, ant, t, v[10], rez[nmax], maxim, dif, poz, v1[10];
bool ok, gasit;
char cul[10];

bool conflict(int a, int b){
    dif=a-b;
    return (dif*dif<=1) || ((a==1)&&(b==6)) || ((a==6)&&(b==1));
}

void incep(int x){
    for (int i=1;i<=6;i++)
        v1[i]=v[i];
    pr=ant=x;   
    v[x]--;
    ok=1;
    rez[1]=x;
    for (int i=2;i<=n;i++){
        maxim=-1;
        for (int j=1;j<=6;j++)
            if (!conflict(ant,j))
                if ((v[j]>maxim) || ((v[j]==maxim)&&(conflict(pr,j)))){
                    maxim=v[j];
                    poz=j;
                }
        rez[i]=poz;
        if (maxim>0){
            v[poz]--;
            ant=poz;
        }else{
            ok=0;
            break;
        }
    }
    if (conflict(ant,pr))
        ok=0;
    
    for (int i=1;i<=6;i++)
        v[i]=v1[i];
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cul[1]='R';
    cul[2]='O';
    cul[3]='Y';
    cul[4]='G';
    cul[5]='B';
    cul[6]='V';
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++){
        scanf("%d",&n);
        
        for (int i=1;i<=6;i++){
            scanf("%d",&v[i]);
            
        }
        gasit=0;
        for (int i=1;i<=6;i++)
            if (v[i]>0){
            incep(i);
            if (ok){
                gasit=1;
                break;
            }
        }
        printf("Case #%d: ",ii);
        if (gasit){
            for (int i=1;i<=n;i++){
                printf("%c",cul[rez[i]]);
            }
        }else
            printf("IMPOSSIBLE");
        printf("\n");
    }
    return 0;
}
