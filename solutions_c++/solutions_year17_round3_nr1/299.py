#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long ll;

#define N 1010
#define PI 3.14159265358979323846

struct Pancake {
    ll r, h, s;
} cake[N];

struct Compare {
    bool operator() (const Pancake& a, const Pancake& b) {
        return a.s > b.s;
    }
} cmp;

void solve(int case_no) {
    int n, k;
	double ans = 0.0;

    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%lld%lld", &cake[i].r, &cake[i].h);
        cake[i].s = 2LL * cake[i].r * cake[i].h;
    }

    sort(cake, cake + n, cmp);

    for (int i = 0; i < n; i++) {
        ll base_r = cake[i].r;
        ll ans_in_pi = cake[i].r * cake[i].r + cake[i].s;
        int sz = 1;
        for (int j = 0; j < n; j++) {
            if (i != j && cake[i].r >= cake[j].r && sz < k) {
                ans_in_pi += cake[j].s;
                sz++;
            }
        }
        if (sz == k)
            ans = max(ans, ans_in_pi * PI);
    }

	printf("Case #%d: %.9f\n", case_no, ans);
}

int main(int argc, char** argv) {
	int case_no, t;

	scanf("%d", &t);
	for (case_no = 1; case_no <= t; case_no++)
		solve(case_no);

	return 0;
}
