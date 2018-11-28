#include <bits/stdc++.h>
#define fread(ch) freopen(ch,"r",stdin)
#define fwrite(ch) freopen(ch,"w",stdout)

using namespace std;

struct Color
{
    char ch;
    int cnt;
    bool operator <(const struct Color a)const
    {
        return cnt < a.cnt;
    }
}co[6];

int main()
{
    fread("B-small-attempt0.in");
    fwrite("out.out");
    int t,n;

    scanf("%d",&t);

    for(int z = 1; z <= t; ++z)
    {
    co[0].ch = 'R';
    co[2].ch = 'Y';
    co[4].ch = 'B';
        scanf("%d",&n);
        for(int i = 0; i < 6; ++i) scanf("%d",&co[i].cnt);
        sort(co,co+6);
        printf("Case #%d: ",z);
        if(co[5].cnt > co[4].cnt+co[3].cnt) puts("IMPOSSIBLE");
        else
        {
            for(int i = 0; i < co[5].cnt; ++i)
            {
                putchar(co[5].ch);
                if(co[4].cnt)
                {
                    putchar(co[4].ch);
                    co[4].cnt--;
                }
                if(co[5].cnt-i <= co[3].cnt)
                {
                    putchar(co[3].ch);
                    co[3].cnt--;
                }
            }
            puts("");
        }
    }

    return 0;
}
