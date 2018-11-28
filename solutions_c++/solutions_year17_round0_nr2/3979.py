#include <iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
typedef long long ll;
using namespace std;
int Digit[25]={0};

int init(ll x)
{
    int cnt = 0;
    while(x)
    {
        Digit[++cnt] = x%10;
        x/=10;
    }
    for(int i=1;i<=cnt/2;i++)
        swap(Digit[i], Digit[cnt-i+1]);
    return cnt;
}

int main()
{
    int T, Case = 1;
    scanf("%d", &T);
    while(T--)
    {
        ll x;
        scanf("%lld", &x);
        int n = init(x);
        int flag = 0;
        for(int i=1;i<=n;i++)
        {
            if(flag == 1)
                Digit[i] = 9;
            else
            {
                if(Digit[i] < Digit[i-1])
                {
                    flag = 1;
                    Digit[i-1]--;
                    Digit[i] =9 ;
                }
            }
        }
        for(int i=n;i>0;i--)
        {
            if(Digit[i] < Digit[i-1])
            {
                Digit[i-1]--;
                Digit[i] = 9;
            }
        }
        int i = 0;
        while(Digit[i]<=0) i++;
        printf("Case #%d: ", Case++);
        while(i<=n)
        {
            printf("%d", Digit[i++]);
        }
        printf("\n");
    }
    return 0;
}

