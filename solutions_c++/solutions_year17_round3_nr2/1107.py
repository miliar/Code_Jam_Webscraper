#include <cstdio>
#include <algorithm>
#include <vector>
#include <functional>

using namespace std;

#define AMAX 100

struct Interval {
    int b;
    int e;
};

bool cmp(const Interval &x, const Interval &y)
{
    return x.b < y.b;
}

int main()
{
    int t;
    static Interval intc[AMAX], intj[AMAX];

    scanf("%d", &t);
    for (int tc = 1; tc <= t; ++tc) {
        int ac, aj;
        vector<int> freec, freej;

        scanf("%d %d", &ac, &aj);
        for (int i = 0; i < ac; ++i) {
            scanf("%d %d", &intc[i].b, &intc[i].e);
        }
        for (int i = 0; i < aj; ++i) {
            scanf("%d %d", &intj[i].b, &intj[i].e);
        }

        sort(intc, intc+ac, cmp);
        sort(intj, intj+aj, cmp);

        for (int i = 1; i < ac; ++i) {
            freec.push_back(intc[i].b-intc[i-1].e);
        }
        freec.push_back(1440+intc[0].b-intc[ac-1].e);

        for (int i = 1; i < aj; ++i) {
            freej.push_back(intj[i].b-intj[i-1].e);
        }
        freej.push_back(1440+intj[0].b-intj[aj-1].e);

        sort(freec.begin(), freec.end(), greater<int>());
        sort(freej.begin(), freej.end(), greater<int>());

        int cc = 1, cj = 1;
        int sumc = 0, sumj = 0;

        for (auto it = freec.begin(); (it != freec.end()) && (*it != 0); ++it) {
            sumc += *it;
            if (sumc < 720) {
                ++cc;
            }
        }
        for (auto it = freej.begin(); (it != freej.end()) && (*it != 0); ++it) {
            sumj += *it;
            if (sumj < 720) {
                ++cj;
            }
        }

        printf("Case #%d: %d\n", tc, 2*max(cc, cj));
    }
}
