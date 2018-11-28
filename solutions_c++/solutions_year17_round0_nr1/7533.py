#include <iostream>
#include <cstdio>
#include <string.h>

using namespace std;

int main()
{
    int t,f,l,count,j,n;
    char a[1000];
    scanf("%d",&t);
    for(int p=1;p<=t;p++){
        scanf("%s",a);
        scanf("%d",&f);
        count=0;
        l=strlen(a);

        for(j=l-1;j>=f-1;j--){
            if(a[j]=='-'){
                a[j]='+';
                int m=j-1;
                for(n=1;n<f;n++){
                    if(a[m]=='-'){
                        a[m]='+';
                    }
                    else{
                        a[m]='-';
                    }
                    m--;
                }
                count++;
            }
            else{
                continue;
            }
        }
        for(n=0;n<=j+1;n++){
            if(a[n]=='+'){
                continue;
            }
            else
                break;
        }
        if(n-1==j+1){
            printf("Case #%d: %d\n",p,count);
        }
        else{
            printf("Case #%d: IMPOSSIBLE\n",p);
        }
    }
    return 0;
}
