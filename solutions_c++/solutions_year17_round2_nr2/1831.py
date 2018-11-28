#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, i;
    scanf("%d", &t);
    for(i=1; i<=t; i++)
    {
        int a, b, c, d, e, f, g;
        scanf("%d %d %d %d %d %d %d", &a, &b, &c, &d, &e, &f, &g);
        if( (b+d>=f) && (b+f>=d) && (d+f>=b))
        {
            printf("Case #%d: ", i);

            char pre = 'x';
            char first='x', fg=1;
            while(b+d+f)
            {
                int flag = 1;
                int mx = max(d, max(b, f));
                int mn = min(d, min(b, f));
                int mid = (b+d+f) - (mx+mn);
                if(f==1 && d==1 && b==1 && first != 'x')
                {
                    if(first=='Y')
                    {
                        if(pre != 'B')
                        {
                            printf("B");
                            pre = 'B';
                            f--;
                        }
                        else if(pre != 'R')
                        {
                            printf("R");
                            pre = 'R';
                            b--;
                        }
                        else if(pre != 'Y')
                        {
                            printf("Y");
                            pre = 'Y';
                            d--;
                        }
                        if(d) printf("Y");
                        if(b) printf("R");
                        if(f) printf("B");
                        break;


                    }
                    else if(first=='R')
                    {

                        if(pre != 'B')
                        {
                            printf("B");
                            pre = 'B';
                            f--;
                        }
                        else if(pre != 'Y')
                        {
                            printf("Y");
                            pre = 'Y';
                            d--;
                        }
                        else if(pre != 'R')
                        {
                            printf("R");
                            pre = 'R';
                            b--;
                        }
                        if(b) printf("R");
                        if(d) printf("Y");
                        if(f) printf("B");
                        break;
                    }
                    else if(first == 'B')
                    {

                        if(pre != 'R')
                        {
                            printf("R");
                            pre = 'R';
                            b--;
                        }
                        else if(pre != 'Y')
                        {
                            printf("Y");
                            pre = 'Y';
                            d--;
                        }
                        else if(pre != 'B')
                        {
                            printf("B");
                            pre = 'B';
                            f--;
                        }
                        if(f) printf("B");
                        if(d) printf("Y");
                        if(b) printf("R");
                        break;
                    }


                }
                if(f==mx && pre != 'B' && f)
                {
                    printf("B");
                    f--;
                    pre = 'B';
                    flag = 0;
                    if(fg)
                    {
                        first = 'B';
                        fg = 0;
                    }
                }
                else if(b==mx && pre != 'R' && b)
                {
                    printf("R");
                    b--;
                    pre = 'R';
                    flag = 0;
                    if(fg)
                    {
                        first = 'R';
                        fg = 0;
                    }
                }
                else if(d==mx && pre != 'Y' && d)
                {
                    printf("Y");
                    d--;
                    pre = 'Y';
                    flag = 0;
                    if(fg)
                    {
                        first = 'Y';
                        fg = 0;
                    }
                }
                if(f==mid && pre != 'B' && flag && f)
                {
                    printf("B");
                    f--;
                    pre = 'B';
                }
                else if(b==mid && pre != 'R' && flag && b)
                {
                    printf("R");
                    b--;
                    pre = 'R';
                    flag = 0;
                }
                else if(d==mid && pre != 'Y' && flag && d)
                {
                    printf("Y");
                    d--;
                    pre = 'Y';
                    flag = 0;
                }
            }
            printf("\n");
        }
        else printf("Case #%d: IMPOSSIBLE\n", i);
    }
    return 0;
}
