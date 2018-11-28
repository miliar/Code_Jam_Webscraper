#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <string.h>
#include <set>
using namespace std;

#define EPS 1e-8
#define mod 1000000007

typedef long long ll;

const double pi = acos(-1.0);

struct pancake
{
    int r, h;
    bool operator<(const pancake& b) const
    {
        return (ll)r * h < (ll)b.r * b.h;
    }
}a[1005];

bool sort_by_r(const pancake& a, const pancake& b)
{
    return a.r < b.r;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/dergach007/Desktop/FacebookHackerCup/FacebookHackerCup/A-large.in.txt", "r", stdin);
    freopen("/Users/dergach007/Desktop/FacebookHackerCup/FacebookHackerCup/A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        int n, k;
        scanf("%d %d", &n, &k);
        for(int i = 0; i < n; i++)
            scanf("%d %d", &a[i].r, &a[i].h);
        sort(a, a + n, sort_by_r);
        multiset<pancake> s;
        double maxv = 0;
        ll side = 0;
        for(int i = 0; i < n; i++)
        {
            if(s.size() == k - 1)
            {
                maxv = max(maxv, pi * a[i].r * a[i].r + 2 * pi * a[i].r * a[i].h + side * 2 * pi);
            }
            s.insert(a[i]);
            side += (ll)a[i].h * a[i].r;
            if(s.size() > k - 1)
            {
                side -= (ll)(s.begin()->r) * s.begin()->h;
                s.erase(s.begin());
            }
        }
        printf("Case #%d: %.10lf\n", t, maxv);
    }
    return 0;
}
