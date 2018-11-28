#include <bits/stdc++.h>
using namespace std;

const double pi = atan2(0, -1);

inline int getint() {
    int inp; scanf("%d", &inp); return inp;
}

struct Item {
    int r, h;
    bool operator < (const Item& it) const {
        return 2 * pi * r * h > 2 * pi * it.r * it.h;
    }
};

int main() {
    int TC = getint();
    for (int tc = 1; tc <= TC; tc++) {
        printf("Case #%d: ", tc);
        int N = getint();
        int K = getint();

        vector<Item> A;
        for (int i = 0; i < N; i++) {
            Item it;
            it.r = getint();
            it.h = getint();
            A.push_back(it);
        }

        sort(A.begin(), A.end());

        double mx_area = -1.0;
        for (int i = 0; i < N; i++) {
            double area = pi * A[i].r * A[i].r + 2 * pi * A[i].r * A[i].h;
            int cnt = K - 1;
            for (int j = 0; j < N && cnt; j++) {
                if (j != i) {
                    area += 2 * pi * A[j].r * A[j].h;
                    cnt--;
                }
            }
            mx_area = max(mx_area, area);
        }

        printf("%.10f\n", mx_area);
    }
    return 0;
}
