#include <bits/stdc++.h>
using namespace std;
#define MAX 50009
#define ll long long

int convert_num(ll x);
ll fn(ll x);
int is_ascending(int j);

int num[100];

int main()
{

    freopen("B-large.in", "r", stdin);
   freopen("c.out", "w", stdout);

    int tc, cases = 1;

    scanf("%d", &tc);
    while(tc--)
    {
        ll x;
        scanf("%lld", &x);
        printf("Case #%d: ", cases++);

        printf("%lld\n", fn(x));

        printf("\n");
    }

    return 0;
}

ll fn(ll x)
{
    int n = convert_num(x);
    ll tmp[100];

    if(is_ascending(n))
        return x;

    int with = 0;

    for(int i = 0; i < n; i++)
    {
        if(is_ascending(i))
        {
            ll y = 0;
            int j = 0;
            for(j = 0; j < i; j++)
                y = y * 10 + num[j];

            if(i == 0 || num[i] - 1 >= num[i - 1])
            {
                y = y * 10 + (num[i] - 1);
                j++;
                for(; j < n; j++)
                    y = y * 10 + 9;

                tmp[with++] = y;
            }
        }
    }

    sort(tmp, tmp + with);

    return tmp[with - 1];
}

int is_ascending(int j)
{
    int prev = num[0];

    for(int i = 1; i < j; i++)
    {
        if(prev > num[i])
            return 0;

        prev = num[i];
    }

    return 1;
}

int convert_num(ll x)
{
    int cnt = 0;
    ll y = x;

    if(x == 0)
    {
        num[0] = 0;
        return 1;
    }

    int tmp[100];
    while(y)
    {
        tmp[cnt++] = y % 10;
        y = y / 10;
    }

    int j = cnt - 1;
    for(int i = 0; i < cnt; i++)
        num[i] = tmp[j--];

    return cnt;
}

