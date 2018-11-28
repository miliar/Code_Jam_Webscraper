#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<queue>
#include<map>
using namespace std;
#define pi 3.14159265358979323846
typedef long long ll;
struct Cricle
{
    ll r;
    ll h;
    ll s;

} cricle[1010];

bool operator < (const Cricle & a, const Cricle & b)
{
    return a.s > b.s;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int cnt;
    cin >> cnt;
    for(int c = 1; c <= cnt; ++c)
    {
        int n, k;
        cin >> n >> k;
        for(int i = 0; i < n; ++i)
        {
            cin >> cricle[i].r >> cricle[i].h;
            cricle[i].s = cricle[i].r * cricle[i].h;
        }
        sort(cricle, cricle + n);
        ll rst = 0;
        for(int i = 0; i < n; ++i)
        {
            ll tmp = cricle[i].r * cricle[i].r + 2 * cricle[i].s;
            int count = 0;
            for(int j = 0; j < n && count < k - 1; ++j)
            {
                if(cricle[j].r <= cricle[i].r && j != i)
                {
                    tmp += 2 * cricle[j].s;
                    ++count;
                }
            }
            if(count == k - 1)
                rst = max(rst, tmp);
        }
        printf("Case #%d: %.9lf\n", c, rst * pi);
    }
    return 0;
}
/*
2
5 2
446112 179209
248383 321871
243179 328759
118432 675048
548998 145624
*/
