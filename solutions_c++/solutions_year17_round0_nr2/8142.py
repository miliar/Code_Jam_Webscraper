#include <cstdio>
#include <cstring>
#include <cstdlib>

#define MAX 20

long long t, n;

long long f(long long nu)
{
    char text[MAX];
    sprintf(text, "%lld", nu);
    //printf("%s\n", text);
    int len = strlen(text);
    for(int i = len-1; i > 0; i--)
    {
        if(text[i-1] > text[i])
        {
            //printf("zeas\n");
            text[i-1]--;
            for(int j = len -1; j >= i; j--)
                text[j] = '9';
        }
    }
    /*int i = nu%10;
    while(nu > 0)
    {
        if(i < nu%10)
            return 0;
        i = nu%10;
        nu /= 10;
    }*/
    return atoll(text);
}

int main()
{
    scanf("%lld", &t);
    for(int i = 0; i < t; i++)
    {
        scanf("%lld", &n);
        printf("Case #%d: %lld\n", i+1, f(n));
        /*for(unsigned long long j = n; j > 0; j--)
            if(f(j))
            {
                printf("Case #%d: %lld\n",i+1, j);
                break;
            }*/
    }
}
