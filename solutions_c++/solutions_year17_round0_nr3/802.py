#include <cstdio>
#include <utility>
#include <algorithm>
using namespace std;
pair<long long, long long> solve(long long n, long long k)
{
    long long l,r;
    n--;
    l=r=n/2;
    if(n&1)r++;
    if(k==1) return make_pair(r,l);
    if(k&1)return solve(l,k/2);
    return solve(r,k/2);
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out", "w", stdout);
    int T;
    scanf("%d",&T);
    for(int cases=1; cases<=T; cases++)
    {
        long long n,k;
        scanf("%I64d%I64d",&n,&k);
        pair<long long,long long> ans=solve(n,k);
        printf("Case #%d: %I64d %I64d\n", cases, ans.first, ans.second);
    }
    return 0;
}
