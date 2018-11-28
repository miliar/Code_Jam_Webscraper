#include <bits/stdc++.h>
using namespace std;
int T,i,r,o,y,g,b,v,n,a[3];
char c[100];
//f,s,t=1st,2nd,3rd
void p(int x)
{
    printf("%c",c[x]);
}
int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
	freopen("out.out", "w", stdout);
    for(scanf("%d",&T);i<T;i++)
    {
        printf("Case #%d: ",i+1);
        scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
        if(r>=y)
        {
            if(y>=b)
            {
                c[0]='R';c[1]='Y';c[2]='B';
                a[0]=r;a[1]=y;a[2]=b;
            }
            else if(r>=b)
            {
                c[0]='R';c[1]='B';c[2]='Y';
                a[0]=r;a[1]=b;a[2]=y;
            }
            else
            {
                c[0]='B';c[1]='R';c[2]='Y';
                a[0]=b;a[1]=r;a[2]=y;
            }
        }
        else
        {
            if(b>=y)
            {
                c[0]='B';c[1]='Y';c[2]='R';
                a[0]=b;a[1]=y;a[2]=r;
            }
            else if(r>=b)
            {
                c[0]='Y';c[1]='R';c[2]='B';
                a[0]=y;a[1]=r;a[2]=b;
            }
            else
            {
                c[0]='Y';c[1]='B';c[2]='R';
                a[0]=y;a[1]=b;a[2]=r;
            }
        }
        if(2*a[0]>n && n!=1)
            printf("IMPOSSIBLE");
        else
        {
            //o=left c
            for(o=a[1]+a[2]-a[0];a[0]>0;a[0]--)
            {
                p(0);
                if(a[1]>0)
                {
                    a[1]--;
                    p(1);
                    if(o>0)
                    {
                        o--;
                        a[2]--;
                        p(2);
                    }
                }
                else if(a[2]>0)
                    p(2);
            }
        }
        printf("\n");
    }
}
