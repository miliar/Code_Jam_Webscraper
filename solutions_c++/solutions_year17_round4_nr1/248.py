#include <iostream>
#include <utility>
#include <cstdint>
#include <algorithm>
#include <map>
#include <iterator>
#include <iomanip>
typedef std::pair<int64_t, int64_t> ii;

const int MAXN = 128;

int cnt[4];
int n, p;
int solve()
{
    int ans = 0;
    ans += cnt[0];
    if (p == 2) {
        ans += (cnt[1]+1)/2;
    }
    else if (p == 3) {
        int k = std::min(cnt[1], cnt[2]);
        ans += k;
        cnt[1] -= k;
        cnt[2] -= k;
        ans += (cnt[1]+cnt[2]+2)/3;
    }
    else {
        ans += cnt[2]/2;
        cnt[2] %= 2;
        int k = std::min(cnt[1], cnt[3]);
        ans += k;
        cnt[1] -= k;
        cnt[3] -= k;
        int rem=0;
        if (cnt[2]) {
            rem = 2;
            ans++;
        }
        int c = cnt[1]+cnt[3];
        int d = cnt[1] ? 1 : 3;
        while (c) {
            if (rem == 0) ans++;
            rem += d;
            if (rem >= p) rem -= p;
            c--;
        }

    }
    return ans;
}

int main()
{
    int t;
    std::cin >> t;
    for (int i=1; i<=t; i++)
    {
        std::cin >> n >> p;
        for (int j=0; j<p; j++) cnt[j] = 0;
        for (int j=0; j<n; j++) {
            int v;
            std::cin >> v;
            cnt[v%p]++;
        }
        std::cout << "Case #" << i << ": ";
        std::cout << solve() << "\n";
    }
}
