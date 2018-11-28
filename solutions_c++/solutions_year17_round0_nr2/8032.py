#include<iostream> 
#include<stdio.h>
using namespace std;
int n,m,ans[101];
char a[101],b;
int main(){
    freopen("problemB-sample.in","r",stdin);
    freopen("problemB-sample.out","w",stdout);
    int i,j,k,s,flag;
    scanf("%d\n",&n);
    for(i=1;i<=n;i++){
        cout<<"Case #"<<i<<": ";
        for(s=1;;s++){
            scanf("%c",&b);
            //printf("%d\n", s);
            if(b!='\n')a[s]=b;
            else break;
        }
        s--;
        //printf("%d\n",s);
        while(1){
            flag=0;
            /*for(j=s;j>1;j--){
                if(a[j]=='0'){
                    while(a[j-1]=='0')a[j--]='9';
                    flag=1;
                    break;
                }
            }*/
            for(j=s;j>1;j--){
                if(a[j-1]>a[j]){
                    for(k=j;k<=s;k++)a[k]='9';
                    a[j-1]=char(int(a[j-1])-1);
                    flag=1;
                }
            }
            if(!flag)break;
        }
        for(j=1;j<=s;j++){
            if(j==1&&a[j]=='0')continue;
            printf("%c",a[j]);
            
        }
        printf("\n");
    }
    return 0;
}