#include <cstdio>
#include <cstring>
int t;
char ch[30],rez[30];
int ordered(long long x)
{
    long long lastdig=x%10;
    x/=10;
    while(x!=0)
    {
        long long ldig2=x%10;
        x/=10;
        if(ldig2>lastdig) return 0;
        lastdig=ldig2;
    }
    return 1;
}
long long brut(long long nr1)
{
    for(long long i=nr1;i>=1;--i)
    {
        if(ordered(i)) return i;
    }
}
int main()
{
    freopen ("in.in","r",stdin);
    freopen ("out.out","w",stdout);
    scanf("%d",&t);
    for(int xyz=1;xyz<=t;xyz++)
    {
        printf("Case #%d: ",xyz);
        scanf("%s",ch);
        int mar=strlen(ch);
        int as=0;
        long long nr1=0,nr2=0;
        for(int i=0;i<mar;i++)
        {
            nr1=nr1*10+(ch[i]-'0');
            nr2=nr2*10+1;
        }
     //   long long v=brut(nr1);
      //  printf("%lld ",v);
        if(nr1<nr2)
        {
            //printf("A");
            for(int i=0;i<mar-1;i++) printf("9");
            printf("\n");
            continue;
        }
        rez[0]=ch[0];
    //    if(xyz==44) printf("%s ",ch);
        for(int i=1;i<mar;i++)
        {
            if(as==1)
            {
                rez[i]='9';
                continue;
            }
            rez[i]=ch[i];
            if(rez[i]<rez[i-1])
            {
                //if(xyz==44) printf("%c %c ",rez[i],rez[i-1]);
                rez[i-1]=ch[i-1]-1;
                as=1;
                rez[i]='9';
            }
        }
        as=0;
        for(int i=1;i<mar;i++)
        {
            if(rez[i]<rez[i-1])
            {
                as=1;
                break;
            }
        }
        if(as==1)
        {
            rez[0]=ch[0]-1;
            for(int i=1;i<mar;i++) rez[i]='9';
        }
        for(int i=0;i<mar;i++) printf("%c",rez[i]);
        printf("\n");
    }
}
