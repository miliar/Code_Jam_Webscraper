#include <cstdio>
#include <iostream>

using namespace std;

struct seg {
    int l, r;

    bool bigger(const seg& other) const {
        return l > other.l;
    }

    int length() {
        return r - l;
    }
};

int inner_dist(const seg& s1, const seg& s2) {
    if (s1.bigger(s2))
        return inner_dist(s2, s1);

    return s2.l - s1.r;
}

int outer_dist(const seg& s1, const seg& s2) {
    if (s1.bigger(s2))
        return outer_dist(s2, s1);

    return s1.l + 24 * 60 - s2.r;
}

seg a[100], b[100];
int n, m;

int main() {

    int nTest;
    cin >> nTest;

    for (int test = 1; test <= nTest; ++test) {
        cin >> n >> m;
        for (int i = 0; i < n; i++) {
            cin >> a[i].l >> a[i].r;
        }
        for (int i = 0; i < m; i++) {
            cin >> b[i].l >> b[i].r;
        }

        int res = 0;
        int HALF_A_DAY = 24 * 60 / 2;

        if (m == 1 || n == 1) {
            res = 2;
            goto answer;
        }


        if (n == 2) {
            int length = a[0].length() + a[1].length() + min(inner_dist(a[0], a[1]), outer_dist(a[0], a[1]));
            if (length <= HALF_A_DAY) res = 2;
            else res = 4;

            goto answer;
        }

        if (m == 2) {
            int length = b[0].length() + b[1].length() + min(inner_dist(b[0], b[1]), outer_dist(b[0], b[1]));
            if (length <= HALF_A_DAY) res = 2;
            else res = 4;

            goto answer;
        }

        answer:

        cout << "Case #" << test << ": " << res << endl;
    }

    return 0;
}
