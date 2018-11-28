#include <cstdio>
#include <algorithm>

using namespace std;

int v[110];

int main()
{
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    int t,n,p;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        scanf("%d%d",&n,&p);
        int sol=0;
        for(int i=1;i<=n;i++) scanf("%d",&v[i]);
        if(p==2)
        {
            int c=0;
            for(int i=1;i<=n;i++)
                if(v[i]%2==0) sol++;
                else c++;
            if(c%2==1) sol++;
            sol+=c/2;
        }
        else if(p==3)
        {
            int a=0,b=0,nr1=0,nr2=0;
            for(int i=1;i<=n;i++)
                if(v[i]%3==0) {sol++;v[i]=-1;}
                else if(v[i]%3==1) a++;
                else b++;
            for(int i=1;i<=n;i++)
                if(v[i]>-1)
                {
                    if(v[i]%3==1 && a>0) {if(b>0) {sol++;b--;a--;}
                                    else if(a>2) {sol++;a-=3;}
                                    v[i]=-1;}
                    else if(b>0)
                    {
                        if(a>0) {sol++;a--;b--;}
                        else if(b>2) {sol++;b-=3;}
                        v[i]=-1;
                    }
                }
            if(a>0 or b>0) sol++;
        }
        printf("Case #%d: %d\n",test,sol);
    }
    return 0;
}
