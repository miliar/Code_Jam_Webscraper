#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
const int N = 2000;

long long n;

void init()
{
    scanf("%I64d",&n);
}

bool check(long long x)
{
    long long pre = 10;
    while(x > 0)
    {
        long long now = x % 10;
        x /= 10;
        if(pre < now) return false;
        pre = now;
    }
    return true;
}

void work()
{
    if(check(n))
    {
        printf("%I64d\n",n);
        return;
    }

    long long base = 1;
    for(int i = 1;i <= 18;i++)
    {
        base *= 10;
        long long now = n / base * base - 1;
        if(check(now))
        {
            printf("%I64d\n",now);
            return;
        }
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i = 1;i <= T;i++)
    {
        printf("Case #%d: ",i);
        init();
        work();
    }

    return 0;
}
