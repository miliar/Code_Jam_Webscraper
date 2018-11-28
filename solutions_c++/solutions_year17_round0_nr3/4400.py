#include <bits/stdc++.h>
using namespace std;

vector <int> v;

void dfs(long long int n){
    if(n)v.push_back(n);
    if(n<=1) return;
    if(n%2==1){
        dfs((n-1)>>1);
        dfs((n-1)>>1);
        return;
    }
    dfs(n>>1);
    dfs((n>>1)-1);
    return;
}

int main()
{
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-small-2-attempt0.out", "w", stdout);
    int t, cs=0, n, k;
    scanf("%d", &t);
    while(t--){
        scanf("%d %d", &n, &k);
        v.clear();
        dfs(n);
        sort(v.begin(), v.end());
        int ans=v[n-k];
        int l, r;
        if(ans%2){
            l=r=(ans-1)>>1;
        }
        else{
            l=((ans)>>1);
            r=((ans)>>1)-1;
        }
        printf("Case #%d: %d %d\n", ++cs, l, r);
    }
    return 0;
}
