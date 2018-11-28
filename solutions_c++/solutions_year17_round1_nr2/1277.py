#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

int compar(const void *a, const void *b)
{
    if(*(int *)a < *(int *)b)
        return -1;
    else if(*(int *)a > *(int *)b)
        return 1;
    else
        return 0;
}
void caser(int casen)
{
    int n, p;

    scanf("%d %d", &n, &p);

    int req[n];
    int opts[n][p];
    for(int i = 0; i < n; i++)
        scanf("%d", &req[i]);
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < p; j++)
            scanf("%d", &opts[i][j]);
        qsort(&opts[i][0], p, sizeof(int), compar);
    }

    int pos[n], servs = 0;
    for(int i = 0; i < n; i++)
        pos[i] = 0;

int count = 0;
    while(true)
    {
        for(int i = 0; i < n; i++)
        {
//            int d = ceil(opts[i][pos[i]] / (req[i] * 1.1));
            if(servs * req[i] * 1.1 < opts[i][pos[i]])
            {
                servs = ceil(opts[i][pos[i]] / (req[i] * 1.1));
                i = -1;
            }
            else if(servs > opts[i][pos[i]] / (req[i] * 0.9))
            {
                if(++pos[i] == p)
                {
                    printf("Case #%d: %d\n", casen, count);
                    return;
                }
                i--;
            }
        }
        count++;
        for(int i = 0; i < n; i++)
        {
             if(++pos[i] == p)
                {
                    printf("Case #%d: %d\n", casen, count);
                    return;
                }
        }
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++)
        caser(i);
    return 0;
}