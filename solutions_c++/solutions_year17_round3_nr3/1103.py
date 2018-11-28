#include <iostream>
#include<cstdio>
#include<algorithm>
#define N 300

using namespace std;

int n,t;

double pi[N];

bool sort_cmp(double x, double y){
    return x<y;
}


int main()
{
    int i,j,x,y,k;
    double u,tt,avg,arg;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);

    for(i=1;i<=t;i++){
        scanf("%d %d",&n,&k);
        scanf("%lf",&u);

        for(j=0;j<n;j++){
            scanf("%lf",&pi[j]);
        }

        sort(pi,pi+n,sort_cmp);

        tt=u;
        for(j=0;j<n;j++){
            u +=pi[j];
            avg=u/(j+1);
            if(j==n-1 || avg<=pi[j+1]) break;
        }
        u=1;
        for(x=j+1;x<n;x++) u *=pi[x];
        for(x=j;x>=0;x--)  u *=avg;
        printf("Case #%d: %lf\n",i,u);



    }



    return 0;
}
