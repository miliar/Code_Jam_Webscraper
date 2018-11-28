#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <vector>
#include <queue>

const int N = 1000;
const double PI = acos(-1.0);

struct Cake
{
    int r, h;
};

bool operator < (const Cake& a, const Cake& b)
{
    if (a.r != b.r) {
        return a.r < b.r;
    }
    return (long long)a.r * a.h < (long long)b.r * b.h;
}

Cake cake[N];

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++ t) {
        int n, k;
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; ++ i) {
            scanf("%d%d", &cake[i].r, &cake[i].h);
        }
        std::sort(cake, cake + n);
        long long sum = 0, result = 0;
        std::priority_queue<long long, std::vector<long long>, std::greater<long long>> queue;
        for (int i = 0; i < n; ++ i) {
            if ((int)queue.size() == k - 1) {
                result = std::max(result, (long long)cake[i].r * cake[i].r + 2 * ((long long)cake[i].r * cake[i].h + sum));
            }
            auto v = (long long)cake[i].r * cake[i].h;
            sum += v;
            queue.push(v);
            while ((int)queue.size() > k - 1) {
                sum -= queue.top();
                queue.pop();
            }
        }
        printf("Case #%d: %.8f\n", t, PI * result);
    }
}
