#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

char s[100];
int a[100];

int main(){
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int T;
    int i,j,n;
    scanf("%d",&T);
    int ca=0;
    while(T--){
        ca++;
        scanf("%s",s);
        n=strlen(s);
        for(i=0;i<n;i++){
            a[i]=s[i]-'0';
        }
        int cp = -1;
        for(i=1;i<n;i++){
            if(a[i]<a[i-1]){
                cp=i;
                a[i-1]--;
                break;
            }
        }
        for(int k = 0;k<n;k++){
            for(i=cp-1;i>0;i--){
                if(a[i]<a[i-1]){
                    cp=i;
                    a[i-1]--;
                    break;
                }
            }
        }

        printf("Case #%d: ",ca);
        if(cp<0){
            for(i=0;i<n;i++){
                printf("%d",a[i]);
            }
            printf("\n");
        }
        else{
            for(i=0;i<n;i++){
                if(a[i]) break;
            }
            for(;i<cp;i++){
                printf("%d",a[i]);
            }
            for(i=cp;i<n;i++){
                printf("9");
            }
            printf("\n");
        }

    }

    return 0;
}
