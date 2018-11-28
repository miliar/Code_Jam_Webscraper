#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

char t[] = "ROYGBV";
int a[6];
char x[6];

struct st
{
    int a[2];
    char x[2];
    int first;
    void print()
    {
        if( first )
        {
            for(int i=0;i<a[1];i++)
            {
                printf("%c%c", x[0], x[1]);
            }
            first = 0;
        }
        printf("%c", x[0]);
    }
};

st e[3];

bool cmp(st a, st b)
{
    if(a.a[0] - a.a[1] != b.a[0] - b.a[1])
        return a.a[0] - a.a[1] > b.a[0] - b.a[1];
    return a.a[0] > b.a[0];
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int ca=1;ca<=T;ca++)
    {
        int n;
        scanf("%d", &n);
        for(int i=0;i<6;i++)
        {
            scanf("%d", &a[i]);
            x[i] = t[i];
        }
        e[0].a[0] = a[0];
        e[0].x[0] = x[0];
        e[0].a[1] = a[3];
        e[0].x[1] = x[3];
        e[1].a[0] = a[2];
        e[1].x[0] = x[2];
        e[1].a[1] = a[5];
        e[1].x[1] = x[5];
        e[2].a[0] = a[4];
        e[2].x[0] = x[4];
        e[2].a[1] = a[1];
        e[2].x[1] = x[1];
        sort(e, e+3, cmp);
        int cnt = 0;
        bool bCan = true;
        bool bABAB = false;
        int len = 0;
        for(int i=0;i<3;i++)
        {
            e[i].first = 1;
            e[i].a[0] -= e[i].a[1];
            len += e[i].a[0];
            if( e[i].a[0] < 0 )
                bCan = false;
            else if( e[i].a[0] == 0 && e[i].a[1] > 0 )
                cnt++;
        }
        if( cnt > 1 ) bCan = false;
        if( cnt == 1 && e[1].a[0] > 0 ) bCan = false;
        if( cnt == 1 && bCan ) bABAB = true;
        if( e[0].a[0] * 2 > len ) bCan = false;
        if( !bCan )
        {
            printf("Case #%d: IMPOSSIBLE\n", ca);
        }
        else if( bABAB )
        {
            printf("Case #%d: ", ca);
            for(int i=0;i<e[0].a[1];i++)
                printf("%c%c", e[0].x[0], e[0].x[1]);
            printf("\n");
        }
        else
        {
            int i = e[0].a[0] - e[2].a[0];
            int j = e[0].a[0] - e[1].a[0];
            int k = e[0].a[0] - i - j;
            printf("Case #%d: ", ca);
            for(int p=0;p<k;p++)
            {
                e[0].print();
                e[1].print();
                e[2].print();
            }
            for(int p=0;p<i;p++)
            {
                e[0].print();
                e[1].print();
            }
            for(int p=0;p<j;p++)
            {
                e[0].print();
                e[2].print();
            }
            printf("\n");
        }
    }

    return 0;
}

