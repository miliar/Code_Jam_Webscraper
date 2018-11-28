#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N=1e6+5;

unordered_map<LL, LL> mp;
LL num[N];
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        printf("Case #%d: ", ca++);
        LL n, k;
        scanf("%I64d%I64d", &n, &k);
        mp.clear();
        int d=0, i=0;
        num[d++]=n;
        mp[n]=1;
        LL l=n, r=n;
        while(k>0)
        {
            LL m=num[i];
            k-=mp[m];
            if(m&1)
                l=r=m/2;
            else
                l=m/2-1, r=m/2;
            if(!mp[r])
                num[d++]=r;
            mp[r]+=mp[m];
            if(!mp[l])
                num[d++]=l;
            mp[l]+=mp[m];
            i++;
        }
        printf("%I64d %I64d\n", r, l);
    }
    return 0;
}
