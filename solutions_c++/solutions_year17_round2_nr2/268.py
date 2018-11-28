#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;

#define LL long long

int n,m,t,a[50],ans[2050];
char ch[]={'0','R','B','Y','G','O','V'};
string s;

int f[5];

void work()
{
    int tc; scanf("%d",&tc);
    int T_T=0;
    while(tc--)
    {
        printf("Case #%d: ",++T_T);
        s="";
        scanf("%d",&n); m=0;
        cin >>a[1] >>a[5] >>a[3] >>a[4] >>a[2] >>a[6];

        if(a[1]==a[4] && a[2]+a[3]+a[5]+a[6]==0)
        {
            for(int i=1;i<=a[1];i++) printf("%c%c",ch[1],ch[4]);
            puts("");
            continue;
        }
        if(a[2]==a[5] && a[1]+a[3]+a[4]+a[6]==0)
        {
            for(int i=1;i<=a[2];i++) printf("%c%c",ch[2],ch[5]);
            puts("");
            continue;
        }
        if(a[3]==a[6] && a[1]+a[2]+a[4]+a[5]==0)
        {
            for(int i=1;i<=a[3];i++) printf("%c%c",ch[3],ch[6]);
            puts("");
            continue;
        }
        if((a[4] && a[4]>=a[1]) || (a[5] && a[5]>=a[2]) || (a[6] && a[6]>=a[3]))
        {
            puts("IMPOSSIBLE");
            continue;
        }

        a[1]-=a[4];
        a[2]-=a[5];
        a[3]-=a[6];

        f[1]=!!a[4], f[2]=!!a[5], f[3]=!!a[6];

        m=0;
        if(a[1]>0)
        {
            ans[++m]=ch[1], a[1]--, t=1, s+=ch[1];
            if(f[1])
            {
                f[1]=0;
                for(int i=0;i<a[4];i++) s+=ch[4], s+=ch[1];
            }
        }
        else if(a[2]>0)
        {
            ans[++m]=ch[2], a[2]--, t=2, s+=ch[2];
            if(f[2])
            {
                f[2]=0;
                for(int i=0;i<a[5];i++) s+=ch[5], s+=ch[2];
            }
        }
        else
        {
            ans[++m]=ch[3], a[3]--, t=3, s+=ch[3];
            if(f[3])
            {
                f[3]=0;
                for(int i=0;i<a[6];i++) s+=ch[6], s+=ch[3];
            }
        }

        int check=1;
        while(a[1]>0 || a[2]>0 || a[3]>0)
        {
            int x=t+1, y=t-1;
            if(x>3) x=1;
            if(y==0) y=3;
            if(a[x]==0 && a[y]==0) {check=0; break;}
            if(a[x]>a[y] || a[x]==a[y] && ch[x]==ch[1])
            {
                ans[++m]=ch[x], a[x]--, t=x, s+=ch[x];
                if(f[x])
                {
                    f[x]=0;
                    for(int i=0;i<a[x+3];i++) s+=ch[x+3], s+=ch[x];
                }
            }
            else
            {
                ans[++m]=ch[y], a[y]--, t=y, s+=ch[y];
                if(f[y])
                {
                    f[y]=0;
                    for(int i=0;i<a[y+3];i++) s+=ch[y+3], s+=ch[y];
                }
            }

        }

        if(ans[1]==ans[m]) check=0;

        if(!check) puts("IMPOSSIBLE");
        else cout <<s <<endl;

    }
}

int main()
{
#ifdef yukihana0416
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
#endif // yukihana0416
    work();
    return 0;
}
