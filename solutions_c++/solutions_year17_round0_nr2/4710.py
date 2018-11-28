#include <bits/stdc++.h>

using namespace std;

void solve()
{
    char str[10000];
    int a[10000], m, n;
    scanf("%s", &str);
    n = strlen(str);
    for(int i=0; i<n; i++)
        a[i] = str[i] - '0';

    m = 1<<10;
    for(int i=n-1; i>0; i--)
    {
        if(a[i] < a[i-1])
        {
            a[i-1]--;a[i]=9;
            m = i;
        }
    }
    for(int i=0; i<n; i++)
    {
        if(i < m)
            (a[i] != 0)? printf("%d", a[i]) : printf("");
        else
            printf("9");
    }
    printf("\n");
}

int main()
{
    freopen("B-in.txt","r",stdin);
	freopen("B-out.txt","w",stdout);
    int T;
    scanf("%d", &T);
    for(int t=0; t<T; t++)
    {
        printf("Case #%d: ", t+1);
        solve();
    }
    return 0;
}
