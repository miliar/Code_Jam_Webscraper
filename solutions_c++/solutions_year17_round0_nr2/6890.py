#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
char a[30];
int main()
{
    int t;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        scanf(" %s",a);
        while(1)
        {
            int ch=1;
            for(int i=0;i<strlen(a)-1;i++)
            {
                if(a[i]>a[i+1])
                {
                    ch=0;
                    a[i]--;
                    for(int k=i+1;k<strlen(a);k++)
                        a[k]='9';
                }
            }
            if(ch) break;
        }
        printf("Case #%d: ",k);
        for(int i=0;i<strlen(a);i++)
        {
            if(i==0&a[i]=='0')
                continue;
            printf("%c",a[i]);
        }
        printf("\n");
    }
    
    return 0;
}
