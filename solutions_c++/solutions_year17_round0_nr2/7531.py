#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;

int main()
{
    int t,n,j,m,l;
    char a[20],temp;
    scanf("%d",&t);
    for(n=1;n<=t;n++){
        scanf("%s",a);
        l=strlen(a);

        for(m=0;m<l/2;m++){
            temp=a[m];
            a[m]=a[l-m-1];
            a[l-m-1]=temp;
        }

        for(m=0;m<l-1;m++){
            if(a[m]<a[m+1]){
                a[m]='9';
                a[m+1]--;
                for(j=m;j>=0;j--){
                    a[j]='9';
                }
            }
            else{
                continue;
            }
        }
         for(m=0;m<l/2;m++){
            temp=a[m];
            a[m]=a[l-m-1];
            a[l-m-1]=temp;
        }
        m=0;
        while(a[m]=='0'){
            m++;
        }
        printf("Case #%d: ",n);
        for(j=m;j<l;j++){
            printf("%c",a[j]);
        }
        printf("\n");
    }
    return 0;
}
