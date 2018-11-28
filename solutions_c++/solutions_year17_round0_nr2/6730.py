#include<cstdio>
#include<cstring>
using namespace std;
char a[20];
int main()
{
    int q,i,t,len,ch;
    freopen("B-large.in","r",stdin);
    freopen("B_out.txt","w",stdout);
    scanf("%d",&q);
    for(t=1;t<=q;t++)
    {
        scanf(" %s",a);
        len=strlen(a);
        ch=1;
        while(ch)
        {
            ch=0;
            for(i=0;i<len-1;i++)
            {
                if(a[i]>a[i+1])
                {
                    a[i]--;
                    ch=1;
                    i++;
                    for(;i<len;i++)
                        a[i]='9';
                }
            }
        }
        i=0;
        while(a[i]=='0')
            i++;
        printf("Case #%d: %s\n",t,a+i);
    }
}
