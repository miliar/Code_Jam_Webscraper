#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
char a[1010];
int main()
{
    int t;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        int n,coun=0,ch=1;
        scanf(" %s %d",a,&n);
        for(int i=0;i<=strlen(a)-n;i++)
        {
            if(a[i]=='-'){
//                printf("%d\n",i);
                coun++;
                for(int j=0;j<n;j++)
                {
                    if(a[i+j]=='+') a[i+j]='-';
                    else a[i+j]='+';
                }
            }
        }
//        for(int i=0;i<=strlen(a);i++)
//            printf("%c",a[i]);
//        printf("\n");
        for(int i=strlen(a)-1;i>=strlen(a)-n+1;i--)
        {
            if(a[i]=='-')
            {
                ch=0;
                break;
            }
        }
        if(ch) printf("Case #%d: %d\n",k,coun);
        else printf("Case #%d: IMPOSSIBLE\n",k);
        memset(a,0,sizeof a);
    }
    
    return 0;
}
/*
 1
 -++++++++- 9
*/
