#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;


const int N = 105;
int a[N], n, k;
int num[5];

int main()
{
    int T;
    scanf("%d", &T);
    for(int Case = 1; Case <= T; ++Case)
    {
        memset(num, 0, sizeof(num));
        scanf("%d%d", &n, &k);
        for(int i = 1; i <= n; ++i)
            scanf("%d", &a[i]), a[i] = a[i] % k, ++num[a[i]];
        int ans = 0;
        ans += num[0]; num[0] = 0;
        if(k == 2)
        {
            ans += num[1] / 2;
            num[1] %= 2;
            if(num[1]) ++ans;
        }
        else if(k == 3)
        {
            int tmp = min(num[1], num[2]);
            ans += tmp;
            num[1] -= tmp; num[2] -= tmp;
            ans += num[1] / 3; num[1] %= 3;
            ans += num[2] / 3; num[2] %= 3;
            if(num[1] + num[2]) ++ans;
        }
        else if(k == 4)
        {
            int tmp = min(num[1], num[3]);
            ans += num[2] / 2; num[2] %= 2;
            ans += tmp;
            num[1] -= tmp, num[3] -= tmp;
            if(num[2])
            {
                if(num[1] >= 2)
                {
                    ans += 1; num[1] -= 2; ans += num[1] / 4; num[1] %= 4;
                }
                else if(num[3] >= 2)
                {
                    ans += 1; num[3] -= 2; ans += num[3] / 4; num[3] %= 4;
                }
            }
            if(num[1] + num[2] + num[3]) ++ans;
        }
        printf("Case #%d: %d\n", Case, ans);
        
    }

    return 0;
}
