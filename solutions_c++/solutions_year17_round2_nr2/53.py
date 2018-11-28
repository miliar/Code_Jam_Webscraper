#pragma warning(disable:4996)

#include <stdio.h>
#include <memory.h>
#include <algorithm>

int n;
int type[6];
int cnt[6];

int alen;
int ans[1000];

char t2char(int x)
{
    if (x==0) return 'R';
    if (x==1) return 'O';
    if (x==2) return 'Y';
    if (x==3) return 'G';
    if (x==4) return 'B';
    return 'V';
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t, tt=0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        for (int i=0; i<6; i++)
            scanf("%d", &type[i]);

        printf("Case #%d: ", ++tt);

        alen = 0;

        if (type[0] == type[3] && type[0]+type[3] == n ||
            type[2] == type[5] && type[2]+type[5] == n ||
            type[4] == type[1] && type[4]+type[1] == n)
        {
            for (int i=0; i<type[0]; i++)
                ans[alen++] = 0, ans[alen++] = 3;
            for (int i=0; i<type[2]; i++)
                ans[alen++] = 2, ans[alen++] = 5;
            for (int i=0; i<type[4]; i++)
                ans[alen++] = 4, ans[alen++] = 1;
        }

        else
        {
            type[0] -= type[3];
            type[2] -= type[5];
            type[4] -= type[1];

            if (type[0] >= 0 && type[2] >= 0 && type[4] >= 0)
            {
                int midx = -1;
                for (int i=0; i<6; i+=2)
                    if (type[i] > 0 && (midx==-1 || type[midx] < type[i]))
                        midx = i;

                int moidx = midx;

                if (midx != -1)
                {
                    while (type[midx] > 0)
                    {
                        for (int j=0; j<type[(midx+3)%6]; j++)
                        {
                            ans[alen++] = midx;
                            ans[alen++] = (midx+3)%6;
                        }
                        ans[alen++] = midx;
                        type[(midx+3)%6] = 0;
                        type[midx]--;
                        
                        if (alen == n && midx == moidx)
                            alen = 0;

                        int midx0 = (midx+2)%6;
                        int midx1 = (midx+4)%6;

                        if (type[midx0] > type[midx1] || (type[midx0] == type[midx1] && midx == moidx))
                            midx = midx0;
                        else midx = midx1;
                    }
                }
            }
        }

        if (alen == n)
        {
            for (int i=0; i<n; i++)
                printf("%c", t2char(ans[i]));
            printf("\n");
        }
        else printf("IMPOSSIBLE\n");
    }

    return 0;
}
