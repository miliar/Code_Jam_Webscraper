#include <cstdio>
#include <bitset>
#include <cstring>
#include <climits>

using namespace std;

#define MAX 1005
#define MAX_C 20000

int t, k, mask, len, best, flag, counter;
char text[MAX];//, db[1 << MAX][MAX_C];

int f()
{
    /*if(counter++ == 99)
        return -1;
    /*if(db[ma][c] || c >= MAX)
        return -1;
    db[ma][c] = 1;*
    //printf("%d %d\n", ma, (1 << len) - 1);
    if(ma == (1 << len) - 1)
    {
        flag = 1;
        best = min(c, best);
        //printf("%d\n", c);
        return c;
    }*/
    /*for(int i = 0; i <= len - k; i++)
    {
        /*if(i == len - k )
            printf("%d %d %d\n", i, k, ma);*/
        /*for(int j = 0; j < k; j++)
        {
            //printf("%d\n", (1 << (i + j)));
            ma = ma ^ (1 << (i + j));
        }
        /*if(i == len - k)
            printf("%d\n",ma );*/
        /*f(c+1, ma);
        for(int j = 0; j < k; j++)
            ma = ma ^ (1 << (i + j));
    }
    return -1;*
    printf("%d %d\n", i, c);
    if(i == len-k)
    {
        int fl = 0;
        for(int j = 0; j < len; j++)
            if(text[j] == '-')
                fl = 1;
                if(!fl)
    {
        flag = 1;
        best = min(c, best);
    }
        return 0;
    }
    int fl = 0;
    for(int j = 0; j < len; j++)
        if(text[j] == '-')
            fl = 1;
    if(!fl)
    {
        flag = 1;
        best = min(c, best);
    }
    if(text[i] == '-')
    for(int j = i; j < k; j++){
        if(j == len) return -1;
        if(text[j] == '+')
            text[j] = '-';
        else
            text[j] = '+';f(i+1, c+1);}
            else
    f(i+1, c);*/
    int c = 0;
    for(int i = 0; i < len; i++)
    {
        if(text[i] == '-')
        {
            //printf("%s\n", text);
            if(i+k-1 >= len)
                return -1;
            for(int j = 0; j < k; j++)
                if(text[i+j] == '+')
                    text[i+j] = '-';
                else
                    text[i+j] = '+';
            c++;
            //printf("%s\n", text);
        }
    }
    return c;
}

int main()
{
    scanf("%d", &t);
    for(int i = 0; i < t; i++)
    {
        scanf("%s %d", text, &k);
        //mask = 0;
        len = strlen(text);
        /*for(int jj = 0; jj < MAX_C; jj++)for(int j = 0; j < 1 << len; j++)
            db[j][jj] = 0;*/
        /*for(int j = 0; j < len; j++)
            if(text[j] == '+')
                mask = mask | 1 << (len - j - 1);*/
        int count = f();
        //printf("%d %d\n", flag, best);
        if(count == -1)
            printf("Case #%d: IMPOSSIBLE\n", i+1);
        else
            printf("Case #%d: %d\n", i+1, count);
    }
}
