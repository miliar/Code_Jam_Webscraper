#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

const int MAXN = 1024;
const double PI = 3.14159265359;

struct pancake {

    int h, r;

    double side_surface() const {
        return PI * 2 * (double)r * (double)h;
    }

    double top_surface() {
        return PI * (double)r * (double)r;
    }
};

bool operator<(const pancake& a, const pancake& b) {
    return a.side_surface() > b.side_surface();
}

bool operator==(const pancake& a, const pancake& b) {
    return a.h == b.h && a.r == b.r;
}

pancake p[MAXN];
pancake pc[MAXN];

void find_swap_first(int n, int firstI) {

    pancake first = pc[firstI];

    for (int i = 1; i < n; ++i) {

        if (first == p[i]) {

            swap(p[i], p[n]);
            break;
        }
    }
}

int main() {

    int t, n, k;

    scanf("%d", &t);

    for (int c = 1; c <= t; ++c) {

        scanf("%d%d", &n, &k);

        for (int i = 1; i <= n; ++i) {

            scanf("%d%d", &p[i].r, &p[i].h);
            pc[i] = p[i];
        }

        double answer = 0;

        for (int l = 1; l <= n; ++l) {

            find_swap_first(n, l);
            sort(p + 1, p + n);

            double result = p[n].top_surface() + p[n].side_surface();

            for (int i = 1; i < k; ++i) {

                result += p[i].side_surface();
            }

            answer = max(answer, result);
        }


        printf("Case #%d: %.7lf\n", c, answer);
    }
}
