#include <cstdio>
#include <iostream>
#include <map>

using namespace std;

int main() {
    int nTest = 100;
    scanf("%d", &nTest);

    for (int test = 0; test < nTest; ++test) {
        long long n = 1000000000000000000LL;
        long long k = n;
        scanf("%lld %lld", &n, &k);

        map<long long, long long, greater<long long> > seg;
        seg[n] = 1;

        long long lastseg;
        while (1) {
            auto curr = seg.begin();

            if (curr->second >= k) {
                lastseg = curr->first;
                break;
            }

            k -= curr->second;

            if (curr->first / 2 > 0)
                seg[curr->first / 2] += curr->second;

            if ((curr->first - 1) / 2 > 0)
                seg[(curr->first - 1) / 2] += curr->second;

            seg.erase(curr);
        }

        // printf("\n%lld\n", lastseg);
        printf("Case #%d: %lld %lld\n", test + 1, lastseg / 2, (lastseg - 1) / 2);
    }


    return 0;
}
