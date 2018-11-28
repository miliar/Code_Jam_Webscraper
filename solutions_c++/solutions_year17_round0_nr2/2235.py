#include<bits/stdc++.h>
using namespace std;
char num[25];
int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t, k, n, i, j, p, q, x, y;
    scanf("%d", &t);
    for(k = 1; k <= t; k++)
    {
        scanf("%s", num);
        n = strlen(num);
        for(i = 0; i < n-1; i++)
        {
            if(num[i] > num[i+1])
            {
                while(i && num[i] == num[i-1])
                    i--;
                num[i]--;
                for(j = i+1; j < n; j++)
                    num[j] = '9';
                break;
            }
        }
        printf("Case #%d: %lld\n", k, atoll(num));
    }
    return 0;
}
