#include<cstdio>
#include<string.h>
#include<stdlib.h>
main()
{
    int tt;
    scanf("%d",&tt);
    for(int ttt = 0;ttt<tt;ttt++)
    {
        char s[1001];
        int k;
        scanf("%s %d",s,&k);
        int cnt = 0;
        int ln = strlen(s);
        int flip = 0;
        int *a = (int*)calloc(sizeof(int),ln+k+1);
        bool chk = true;
        for(int i=0;i<ln;i++)
        {
            flip+=a[i];
            if(flip%2 == 0 && s[i] == '-')
            {
                if(i+k > ln)
                {
                    chk = false;
                    break;
                }
                flip++;
                cnt++;
                a[i+k] = -1;
            }
            else if(flip%2 == 1 && s[i] == '+')
            {
                if(i+k > ln)
                {
                    chk = false;
                    break;
                }
                flip++;
                cnt++;
                a[i+k] = -1;
            }
        }
        printf("Case #%d: ",ttt+1);
        if(chk)printf("%d\n",cnt);
        else printf("IMPOSSIBLE\n");
    }
}
