#include<bits/stdc++.h>
using namespace std;
char a[1100];
int main(){
    int n,i,q,j,coun=0,s,k,len;
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    scanf("%d",&q);
    for(i=0;i<q;i++){
        coun=0;
        int ch=0;
        scanf(" %s %d",a,&k);
        len = strlen(a);
        for(j=0;j<=len-k;j++){
            if(a[j]=='-'){
                for(s=j;s<=j+k-1;s++){
                    if(a[s]=='-'){
                        a[s]='+';
                    }else{
                        a[s]='-';
                    }
                }
                coun++;
            }
        }
        for(s=len-1;s>len-k;s--){
            if(a[s]=='-'){
                ch=1;
                break;
            }
        }
        if(ch)
            printf("Case #%d: IMPOSSIBLE\n",i+1);
        else
            printf("Case #%d: %d\n",i+1,coun);
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
