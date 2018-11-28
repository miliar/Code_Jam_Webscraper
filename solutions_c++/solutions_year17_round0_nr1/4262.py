#include <cstdio>
#include <cstring>

using namespace std;

char sir[1010];

int main()
{
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    int t,k;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        scanf("%s%d",sir+1,&k);
        int l=strlen(sir+1),sol=0;
        for(int i=1;i<=l-k+1;i++)
            if(sir[i]=='-')
            {
                sol++;
                for(int j=i;j<=i+k-1;j++)
                    if(sir[j]=='-') sir[j]='+';
                    else sir[j]='-';
            }
        int p=0;
        for(int i=1;i<=l;i++)
            if(sir[i]=='-') {p=1;break;}
        printf("Case #%d: ",test);
        if(p==1) printf("IMPOSSIBLE");
        else printf("%d",sol);
        printf("\n");
    }
    return 0;
}
