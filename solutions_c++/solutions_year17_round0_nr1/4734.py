#include <bits/stdc++.h>

using namespace std;

void solve()
{
    char str[1010];
    int k, n, cnt=0;
    bool chk = false, a[1010];
    scanf("%s %d", &str, &k);
    n = strlen(str);
    for(int i=0; i<n; i++)
        a[i] = (str[i] == '+') ? true:false;

    for(int i=0; i<n-k+1; i++)
    {
        if(!a[i])
        {
            for(int j=0; j<k && i+j<n; j++)
                a[i+j] = !a[i+j];
            cnt++;
        }
    }
    for(int i=0; i<n; i++)
        if(a[i] == false) chk = true;

    if(chk)
        printf("IMPOSSIBLE\n");
    else
        printf("%d\n", cnt);
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int t=0; t<T; t++)
    {
        printf("Case #%d: ", t+1);
        solve();
    }
    return 0;
}
