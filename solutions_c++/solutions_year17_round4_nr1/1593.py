#include<stdio.h>

int d[105][105][105];
int c[105];

int max(int a, int b)
{
    if(a<b)return b;
    return a;
}
int min(int a, int b)
{
    if(a>b)return b;
    return a;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T,lt,n,w,x,i,j,k,res,t;
    for(i=0;i<=100;i++){
        for(j=0;j<=100;j++){
            for(k=0;k<=100;k++){
                if(i>=4)d[i][j][k]=max(d[i][j][k],d[i-4][j][k]+1);
                else if(j>=2)d[i][j][k]=max(d[i][j][k],d[i][j-2][k]+1);
                else if(k>=4)d[i][j][k]=max(d[i][j][k],d[i][j][k-4]+1);
                else if(i>=2&&j>=1)d[i][j][k]=max(d[i][j][k],d[i-2][j-1][k]+1);
                else if(i>=1&&k>=1)d[i][j][k]=max(d[i][j][k],d[i-1][j][k-1]+1);
                else if(j>=1&&k>=2)d[i][j][k]=max(d[i][j][k],d[i][j-1][k-2]+1);
                else if(i|j|k)d[i][j][k]=1;
            }
        }
    }
    scanf("%d", &T);
    for(lt=1;lt<=T;lt++)
    {
        scanf("%d %d", &n, &w);
        for(i=0;i<4;i++)c[i]=0;
        for(i=1;i<=n;i++){
            scanf("%d", &x);
            c[x%w]++;
        }
        if(w==2)res=c[0]+(c[1]+1)/2;
        if(w==3){
            t=min(c[1],c[2]);
            res=c[0]+t+(c[1]+c[2]-2*t+2)/3;
        }
        if(w==4)res=c[0]+d[c[1]][c[2]][c[3]];
        printf("Case #%d: %d\n", lt, res);
    }
    return 0;
}
