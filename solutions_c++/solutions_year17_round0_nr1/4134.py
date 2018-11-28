#include <bits/stdc++.h>

using namespace std;

int t, n, k, ans;
char ar[1005];

void solve(int y)
{
    scanf("%s %d", ar+1, &k);
    n = strlen(ar+1);
    ans = 0;
    for(int i=1;i<=n-k+1;i++){
        if(ar[i]=='-'){
            ans++;
            for(int j=i;j<i+k;j++){
                if(ar[j]=='-') ar[j] = '+';
                else ar[j] = '-';
            }
        }
    }
    for(int i=1;i<=n;i++){
        if(ar[i]=='-'){
            printf("Case #%d: IMPOSSIBLE\n", y);
            return;
        }
    }
    printf("Case #%d: %d\n", y, ans);
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A_output.txt", "w", stdout);
    scanf("%d", &t);
    for(int i=1;i<=t;i++)solve(i);
    return 0;
}
