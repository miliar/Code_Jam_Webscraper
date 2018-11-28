#include<cstdio>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
using namespace std;

char arr[20];

int main(void){
    int t;scanf("%d",&t);
    for(int T=1;T<=t;T++){
        scanf("%s",arr);
        int suc=0;
        while(!suc){
            int len=(int)strlen(arr);
            for(int i=0;i<len-1;i++)
                if(arr[i]>arr[i+1]){
                    arr[i]=arr[i]-1;
                    for(int j=i+1;j<len;j++)
                        arr[j]='9';
                }
            int temp=0;
            for(int i=0;i<len-1;i++)
                if(arr[i]>arr[i+1]){
                    temp=1;
                    break;
                }
            if(temp==0)
                suc=1;
        }
        printf("Case #%d: ",T);
        int l=(int)strlen(arr),j;
        for(int i=0;i<l;i++)
            if(arr[i]!='0'){
                j=i;break;
            }
        for(int i=j;i<l;i++)
            printf("%c",arr[i]);
        printf("\n");
    }
    return 0;
}
