#include <stdio.h>
int n,r,o,y,g,b,v,x,l;
bool rr,yy,bb;
char ans[1001];
void pr()
{
    while(r--)
    {
        if(x >= l) x = 1;
        ans[x] = 'R';
        x += 2;
    }
}
void py()
{
    while(y--)
    {
        if(x >= l) x = 1;
        ans[x] = 'Y';
        x += 2;
    }
}
void pb()
{
    while(b--)
    {
        if(x >= l) x = 1;
        ans[x] = 'B';
        x += 2;
    }
}
main()
{
    freopen("B-large.in","r",stdin);
    freopen("Bl.txt","w",stdout);
    int t; scanf("%d",&t);
    for(int tt = 1;tt <= t;tt++)
    {
        scanf("%d %d %d %d %d %d %d",&n,&r,&o,&y,&g,&b,&v);
        printf("Case #%d: ",tt);
        if(r == g && o == 0 && y == 0 && b == 0 && v == 0)
        {
            while(r--) printf("RG");
            printf("\n"); continue;
        }
        if(o == b && r == 0 && y == 0 && g == 0 && v == 0)
        {
            while(o--) printf("OB");
            printf("\n"); continue;
        }
        if(y == v && o == 0 && r == 0 && b == 0 && g == 0)
        {
            while(y--) printf("YV");
            printf("\n"); continue;
        }
        if((g >= r && g != 0) || (v >= y && v != 0) || (o >= b && o != 0))
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        else
        {
            r -= g; y -= v; b -= o;
            rr = yy = bb = false;
            l = r+y+b;
            if(2*r > l || 2*y > l || 2*b > l)
            {
                printf("IMPOSSIBLE\n");
                continue;
            }
            ans[l] = '\0';
            x = 0;
            if(r >= y && y >= b)
            {
                pr(); pb(); py();
            }
            else if(r >= b && b >= y)
            {
                pr(); py(); pb();
            }
            else if(y >= b && b >= r)
            {
                py(); pr(); pb();
            }
            else if(y >= r && r >= b)
            {
                py(); pb(); pr();
            }
            else if(b >= r && r >= y)
            {
                pb(); py(); pr();
            }
            else
            {
                pb(); pr(); py();
            }
            for(int i = 0;i < l;i++)
            {
                printf("%c",ans[i]);
                if(ans[i] == 'R' && !rr)
                {
                    for(int j = 0;j < g;j++)
                        printf("GR");
                    rr = true;
                }
                else if(ans[i] == 'Y' && !yy)
                {
                    for(int j = 0;j < v;j++)
                        printf("VY");
                    yy = true;
                }
                else if(ans[i] == 'B' && !bb)
                {
                    for(int j = 0;j < o;j++)
                        printf("OB");
                    bb = true;
                }
            }
            printf("\n");
        }
    }
}
