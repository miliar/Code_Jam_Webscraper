#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
using namespace std;
int n,k;
int t;
int a[2000];
int cnt[2000];
int ans(int n){
    memset(cnt,0,sizeof(cnt));
    int res=0;
    int tot=0;
    for(int i=0;i+k-1<n;i++){
        if((a[i]+tot)%2!=0){
            res++;
            cnt[i]=1;
        }
        tot+=cnt[i];
        if(i-k+1>=0){
            tot-=cnt[i-k+1];
        }
    }
    for(int i=n-k+1;i<n;i++){
        if((a[i]+tot)%2!=0){
            return -1;
        }
        if(i-k+1>=0){
            tot-=cnt[i-k+1];
        }
    }
    return res;
}
int main()
{
    char input[2000];
    FILE*fin=fopen("A-large.in","r");
    FILE*fout=fopen("A-large.out","w");
    fscanf(fin,"%d",&t);
    for(int q=1;q<=t;q++){
        fscanf(fin,"%s %d",input,&k);
        n=strlen(input);
        for(int i=0;i<n;i++){
            if(input[i]=='+')
                a[i]=0;
            else
                a[i]=1;
        }
        int res=ans(n);
        fprintf(fout,"Case #%d: ",q);
        if(res==-1)
            fprintf(fout,"IMPOSSIBLE\n");
        else
            fprintf(fout,"%d\n",res);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
