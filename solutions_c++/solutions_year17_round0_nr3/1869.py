#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

#define eps 0.0000001
#define pi  3.14159265359
#define inf 2000000000

typedef long long lld;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

const int MAXN = 1e6 + 5;

bool places[MAXN];

int find_pos(int n) {
    int ret = -1, dmin = 0, dmax = 0;
    for (int i = 1; i <= n; i++) {
        int pos = i, posL = i, posR = i;
        if (places[pos]) {
            continue;
        }
        while (!places[posL - 1]) {
            posL--;
        }
        while (!places[posR + 1]) {
            posR++;
        }
        if (ret == -1 || dmin < min(pos - posL, posR - pos) ||
            (dmin == min(pos - posL, posR - pos)
            && dmax < max(pos - posL, posR - pos))) {
                ret = pos;
                dmin = min(pos - posL, posR - pos);
                dmax = max(pos - posL, posR - pos);
            }
    }
    return ret;
}

void solve_by_simulation(int n, int k, int solMax, int solMin) {
    for (int i = 1; i <= n; i++) {
        places[i] = false;
    }
    places[0] = places[n + 1] = true;
    int pos;
    for (int i = 1; i <= k; i++) {
        pos = find_pos(n);
        places[pos] = true;
    }
    int posL = pos, posR = pos;
    while (!places[posL - 1]) {
        posL--;
    }
    while (!places[posR + 1]) {
        posR++;
    }
    if (solMax != max(pos - posL, posR - pos) ||
        solMin != min(pos - posL, posR - pos)) {
            printf("Error n = %d k = %d: %d %d\n", n, k, max(pos - posL, posR - pos), min(pos - posL, posR - pos));
        }
}

void test() {
    queue<int> q;
    q.push(1000);
    for (int i = 0; i < 500; i++) {
        int x = q.front();
        q.pop();
        printf("%d - %d %d | ", (i + 1), x / 2, (x - 1) / 2);
        q.push(x / 2);
        q.push((x - 1) / 2);
    }
}

lld sum[100], add[100], val[100], c1[100], c2[100];

int main() {
    int tt;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
        lld n, k;
        scanf("%lld %lld", &n, &k);

        lld lvl = 1;
        sum[lvl] = 1;
        val[lvl] = n / 2;
        if (n % 2 == 0) {
            c1[lvl] = 1;
            c2[lvl] = 1;
        } else {
            c1[lvl] = 2;
            c2[lvl] = 0;
        }
        while (sum[lvl] < k) {
            val[lvl + 1] = val[lvl] / 2;
            if (val[lvl] % 2 == 0) {
                c1[lvl + 1] = c1[lvl];
                c2[lvl + 1] = c1[lvl] + 2 * c2[lvl];
            } else {
                c1[lvl + 1] = 2 * c1[lvl] + c2[lvl];
                c2[lvl + 1] = c2[lvl];
            }
            sum[lvl + 1] = sum[lvl] + c1[lvl] + c2[lvl];
            lvl++;
        }

        lld maxD, minD;

        if (k == 1) {
            maxD = n / 2;
            minD = (n - 1) / 2;
        } else {
            if (sum[lvl - 1] + c1[lvl - 1] >= k) {
                maxD = val[lvl - 1] / 2;
                minD = (val[lvl - 1] - 1) / 2;
            } else {
                maxD = (val[lvl - 1] - 1) / 2;
                minD = max(0LL, (val[lvl - 1] - 2) / 2);
            }
        }

        printf("Case #%d: %lld %lld\n", t, maxD, minD);
        //solve_by_simulation(n, k, maxD, minD);
    }
    return 0;
}
