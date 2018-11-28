#include<bits/stdc++.h>
using namespace std;

int A[20];
typedef long long LL;


int main()
{
    freopen("./B-large.in","r",stdin);
    freopen("./out.txt","w",stdout);
    int kase;
    scanf("%d",&kase);
    for(int z = 1;z <= kase;++z)
    {
        LL n;
        scanf("%lld",&n);
        int cur = 0;
        while(n)
        {
            A[cur++] = n%10;
            n /= 10;
        }

        for(int i = cur-1;i > 0;--i)
        {
            if(A[i] <= A[i-1]) continue;
            A[i]--;
            for(int j = i-1;j >= 0;--j) A[j] = 9;

            for(int j = i;j < cur-1;++j)
                if(A[j] < 0 || A[j+1] > A[j])
                {
                    A[j] = 9;
                    A[j+1]--;
                }
            break;
        }

        printf("Case #%d: ",z);
        int t = cur-1;
        while(t >= 0 && A[t] == 0)
            t--;
        for(int i = t;i >= 0;--i)
            putchar(A[i]+'0');
        putchar('\n');
    }

    return 0;
}
