#include<bits/stdc++.h>
using namespace std;
char a[30];
int main(){
    int n,k,i,j,len;
    freopen("2B.in","r",stdin);
    freopen("2B.out","w",stdout);
    scanf("%d",&n);
    for(k=0;k<n;k++){
        int ch=1;
        scanf(" %s",a);
        len = strlen(a);
        while(ch){
            ch=0;
            for(i=0;i<len-1;i++){
                if(a[i] > a[i+1]){
                    a[i]--;
                    for(j=i+1;j<len;j++){
                        a[j] = '9';
                    }
                }
            }
            //printf("%s",a);
            for(i=0;i<len-1;i++){
                if(a[i] > a[i+1]){
                    ch=1;
                    break;
                }
            }
        }
        printf("Case #%d: ",k+1);
        for(i=0;i<len;i++){
            if(a[i]!='0')
                printf("%c",a[i]);
        }
        printf("\n");
    }
    return 0;
}
/*
2
5
10
1
3
5
7
9
*/
