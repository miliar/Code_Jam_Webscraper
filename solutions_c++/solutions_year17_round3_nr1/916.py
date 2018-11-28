#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
typedef long long LL;
const double PI = acos(-1);
LL T, n, k;

struct Node
{
    LL r, h;
} p[1002];

bool cmp(Node a, Node b)
{
    if(a.r == b.r) (LL)a.r*(LL)a.h > (LL)b.r*(LL)b.h;
    return a.r > b.r;
}

bool cmp1(Node a, Node b)
{
    return (LL)a.r*(LL)a.h > (LL)b.r*(LL)b.h;
}

int main()
{
    
    freopen("/Users/RUSH_D_CAT/Desktop/in.txt", "r", stdin);
    freopen("/Users/RUSH_D_CAT/Desktop/out.txt", "w", stdout);
    
    cin >> T;
    int cas = 0;
    while(T--)
    {
        cin >> n >> k;
        for(int i=1;i<=n;i++) cin >> p[i].r >> p[i].h;
        sort(p+1, p+1+n, cmp);
        double ans = 0;
        for(int i=1;i<=n;i++)
        {
            sort(p+i+1, p+1+n, cmp1);
            double sum = PI*(LL)p[i].r*(LL)p[i].r + 2*PI*(LL)p[i].r*(LL)p[i].h;
            if(i+k > n+1) break;
            for(int j=i+1;j<i+k;j++)
            {
                sum += 2*PI*(LL)p[j].h*(LL)p[j].r;
            }
            sort(p+1, p+1+n, cmp);
            ans = max(sum, ans);
        }

        printf("Case #%d: %.12f\n", ++cas, ans);
    }
}