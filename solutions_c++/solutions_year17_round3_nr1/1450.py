#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

const int maxn = 1010;
const double PI = acos(-1.0);
struct cake{
    int h, r;
} a[maxn];

bool cmp(cake a, cake b){
    return (long long)a.r * a.h > (long long) b.r * b.h;
}

int T, n, k, cas;
long long ans;

int main()
{
    scanf("%d", &T);
    while(T--) {
        scanf("%d %d", &n, &k);
        for (int i = 0; i < n; i++) {
            scanf("%d %d", &a[i].r, &a[i].h);
        }
        sort(a, a+n, cmp);
        ans = 0;
        for (int i = 0; i < n; i++) {
            long long tmp = (long long)a[i].r * a[i].r + (long long)2 * a[i].r * a[i].h;
            int cnt = 1;
            // for (int j = n-1; j >= 0; j--) {
            for (int j = 0; j < n; j++) {
                if (cnt == k) break;
                if (j != i && a[j].r <= a[i].r) {
                    cnt ++;
                    tmp += (long long)2 * a[j].r * a[j].h;
                }
            }
            if (tmp > ans) ans = tmp;
        }
        printf ("Case #%d: %.9f\n", ++cas, ans * PI);
    }
    return 0;
}
