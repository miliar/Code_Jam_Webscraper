#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

#define LOCAL
void deal(int n)
{
    int ret = -1;


    char ch[1001];
    int num;
    scanf("%s %d", ch, &num);

    int len = strlen(ch);
    int time=0;
    for (int i = 0; i < len; ++i)
    {
        //printf("%c", ch[i]);
        if(ch[i]=='+')continue;

        if(i+num>len)continue;

        for(int j=i,k=0; k<num; ++j,++k)
        {
            if(ch[j]=='+')ch[j]='-';
            else ch[j]='+';
        }
        time++;
    }



    ret=time;
    for(int i=0; i<len; ++i)
    {
        if(ch[i]=='-')
        {
            ret=-1;
            break;
        }



    }
    printf("Case #%d: ", n);

    if (ret == -1)
    {
        printf("IMPOSSIBLE\n");
    }
    else
    {
        printf("%d\n", ret);
    }
}

int main()
{
#ifdef LOCAL
    freopen ("A-large.in", "r", stdin);
    freopen ("b.out", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i)
    {
        deal(i);
    }


    return 0;
}
