#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    freopen("codejam/B-large.in", "r", stdin);
    freopen("codejam/B-large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int nc = 1; nc <= tc; nc++)
    {
        printf("Case #%d: ", nc);
        ll t;
        cin >> t;
        vector<int> arr(20, 0);
        int i = 0;
        while (t > 0LL)
        {
            arr[i] = t % 10LL;
            t /= 10LL;
            i++;
        }
        for (int j = 0; j < i; j++)
        {
            if (arr[j] < arr[j+1])
            {
                arr[j+1]--;
                for (int k = 0; k <= j; k++)
                {
                    arr[k] = 9;
                }
            }
        }
        ll res = 0LL;
        for (i = 18; i >= 0; i--)
        {
            res = res * 10 + arr[i];
        }
        cout << res;
        printf("\n");
    }
}