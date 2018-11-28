#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
    int i,j,n,t,k,z,c,flag;
    char a[1001];
    scanf("%d",&t);

    for(z=0;z<t;++z)
    {
        scanf("%s%d",a,&k);
        n=strlen(a);
        c=0;
        flag=1;
        printf("Case #%d: ",z+1);

        for(i=0;a[i]!='\0';++i)
            if(a[i]=='-')
                if(n-k>=i)
                {
                    for(j=0;j<k;++j)
                        if(a[i+j]=='+')
                            a[i+j]='-';
                        else
                            a[i+j]='+';
                    ++c;
                }
                else
                {
                    flag=0;
                    break;
                }
        if(flag)
            printf("%d\n",c);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}
