#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <queue>
using namespace std;
const int maxn=1000+5;
int n,k;
int t;
int cake[maxn]; //0:happy 1:blank
int f[maxn]; //the count of reverse operation
int solve(int k,int n){
    memset(f,0,sizeof(f));
    int res=0;
    int sum=0; //the sum of f
    for(int i=0;i+k<=n;i++){
        if((cake[i]+sum)%2!=0){
            res++;
            f[i]=1;
        }
        sum+=f[i];
        if(i-k+1>=0){
            sum-=f[i-k+1];
        }
    }
    for(int i=n-k+1;i<n;i++){
        if((cake[i]+sum)%2!=0){
            return -1;
        }
        if(i-k+1>=0){
            sum-=f[i-k+1];
        }
    }
    return res;
}
int main()
{
    char str[maxn];
    FILE*f1=fopen("A-large.in","r");
    FILE*f2=fopen("A-large.out","w");
    fscanf(f1,"%d",&t);
    for(int tt=1;tt<=t;tt++){
        fscanf(f1,"%s %d",str,&k);
        n=strlen(str);
        for(int i=0;i<n;i++){
            if(str[i]=='-')
                cake[i]=1;
            else
                cake[i]=0;
        }
        int ans=solve(k,n);
        fprintf(f2,"Case #%d: ",tt);
        if(ans==-1)
            fprintf(f2,"IMPOSSIBLE\n");
        else
            fprintf(f2,"%d\n",ans);
    }
    fclose(f1);
    fclose(f2);
    return 0;
}
