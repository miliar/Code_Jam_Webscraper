#pragma warning(disable:4996)

#include <stdio.h>
#include <algorithm>

int n, m;
int c[4];

int f1(int a, int b)
{
    int m = std::min(a, b);
    a-=m;
    b-=m;
    int x=m;
    x += (a+3)/4 + (b+3)/4;
    return x;
}

int f2(int a, int b)
{
    int m = std::min(a, b);
    a-=m;
    b-=m;
    int x=m;
    x += (a+3)/4 + (b+3)/4;
    if (a%4==0 && b%4==0)
        x++;
    return x;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int t, tt=0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &n, &m);
        for (int i=0; i<4; i++)
            c[i] = 0;
        for (int i=0; i<n; i++)
        {
            int x;
            scanf("%d", &x);
            c[x%m]++;
        }

        int ans = c[0];

        if (m==2)
            ans += (c[1]+1) / 2;

        else if (m==3)
        {
            int m1 = std::min(c[1], c[2]);
            c[1] -= m1;
            c[2] -= m1;
            ans += m1;
            ans += (c[1]+2)/3 + (c[2]+2)/3;
        }

        else if (m==4)
        {
            ans += c[2] / 2;
            c[2] %= 2;

            if (c[2] == 1)
            {
                int ans1 = 0;
                int ans2 = 0;
                int ans3 = 0;
                if (c[1] >= 2)
                    ans1 = 1 + f1(c[1]-2, c[3]);
                if (c[2] >= 2)
                    ans2 = 1 + f1(c[1], c[3]-2);
                ans3 = f2(c[1], c[3]);
                ans += std::max(std::max(ans1, ans2), ans3);
            }
            else
                ans += f1(c[1], c[3]);
        }

        printf("Case #%d: %d\n", ++tt, ans);
    }

    return 0;
}
