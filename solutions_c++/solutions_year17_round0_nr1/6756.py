#include<cstdio>
#include<cstring>
using namespace std;
char a[1001];
int mic[1001];
int main()
{
    int q,i,coun,len,k,num,j,l;
    freopen("A-large.in","r",stdin);
    freopen("1_out.txt","w",stdout);
    scanf("%d",&q);
    for(j=1;j<=q;j++)
    {
        coun=0;
        memset(mic,0,sizeof(mic));
        scanf(" %s %d",a,&k);
        len=strlen(a);
        for(i=0;i<len-k+1;i++)
        {
            if(a[i]=='-')
            {
                for(l=0;l<k;l++)
                {
                    if(a[i+l]=='-')
                        a[i+l]='+';
                    else if(a[i+l]=='+')
                        a[i+l]='-';
                }
                coun++;
            }
            //printf("%s\n",a);
        }
        num=0;
        for(;i<len;i++)
            if(a[i]=='-')
                num++;
        printf("Case #%d: ",j);
        if(num&&num!=k){
            printf("IMPOSSIBLE\n");
            continue;
        }
        printf("%d\n",coun);
    }
    return 0;
}
