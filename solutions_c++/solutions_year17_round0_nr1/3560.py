#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

char s[1005];
int a[1005];

int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T;
    int n,i,j,k;
    scanf("%d",&T);
    int ca=0;
    while(T--){
        ca++;
        scanf("%s%d",s,&k);
        n=strlen(s);
        for(i=0;i<n;i++){
            if(s[i]=='+') a[i]=1;
            else a[i]=0;
        }
        int cnt = 0;
        for(i=0;i<=n-k;i++){
            if(!a[i]){
                cnt++;
                for(j=i;j<i+k;j++){
                    a[j]=1-a[j];
                }
            }
        }
        int ok=1;
        for(i=n-k;i<n;i++){
            if(!a[i]){
                ok=0;
                break;
            }
        }
        if(ok){
            printf("Case #%d: %d\n",ca,cnt);
        }
        else{
            printf("Case #%d: IMPOSSIBLE\n",ca);
        }
    }
    return 0;
}
