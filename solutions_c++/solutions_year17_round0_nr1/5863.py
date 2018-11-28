#include <bits/stdc++.h>
using namespace std;
#define MAX 50009
#define ll long long

int fn();

int arr[MAX], n, k;
char input[MAX];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("c.out", "w", stdout);

    int tc, cases = 1;

    scanf("%d", &tc);
    while(tc--)
    {
        scanf("%s %d", input, &k);
        n = strlen(input);

        for(int i = 0; i < n; i++)
            arr[i] = input[i] == '+' ? 1 : 0;

        int ans = fn();

        printf("Case #%d: ", cases++);
        if(ans == -1)
            printf("IMPOSSIBLE");
        else
            printf("%d", ans);
        printf("\n");
    }

    return 0;
}

int fn()
{
    int ret = 0;

    for(int i = 0; i < n; i++)
    {
        if(arr[i] == 0)
        {
            if(i + k > n)
                return -1;

            for(int j = i; j < i + k; j++)
                arr[j] = !arr[j];
            ret++;
        }
    }

    return ret;
}
