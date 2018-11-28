#include <bits/stdc++.h>
using namespace std;


struct cp
{
    int l, r;
    cp() {}
    cp(int _l, int _r)
    {
        l = _l;
        r = _r;
    }
    const bool operator<(const cp &a)const
    {
        if(min(l, r) != min(a.l, a.r))
            return min(l, r) < min(a.l, a.r);
        else if(max(l, r) != max(a.l, a.r))
            return max(l, r) < max(a.l, a.r);
        else
            return l < a.l;
    }
} con[1000005];
int main()
{
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-small-2-attempt0.out", "w", stdout);
    int t;
    cin >> t;
    for(int cnt = 1; cnt <= t; cnt++)
    {
        int n, k;
        cin >> n >> k;
        priority_queue <cp>q;
        n--;
        q.push(cp(n / 2, (n + 1) / 2));
        int ans1, ans2;
        while(k--)
        {
            int l = q.top().l, r = q.top().r;
            ans1 = max(l, r);
            ans2 = min(l, r);
            q.pop();
            l--;
            r--;
            q.push(cp(l / 2, (l + 1) / 2));
            q.push(cp(r / 2, (r + 1) / 2));
        }
        printf("Case #%d: %d %d\n", cnt, ans1, ans2);
    }
    return 0;
}