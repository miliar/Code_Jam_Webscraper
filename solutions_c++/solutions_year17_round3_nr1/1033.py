#include <bits/stdc++.h>
using namespace std;
typedef std::pair<int, int> ii;
const long double pi = acos((long double) -1);

void preprocess() {
}

struct Pancake {
    long long r, h;
};
bool operator<(Pancake l, Pancake r) {
    return l.r > r.r;
}

void process_testcase(const int testcase, const int should_run) {
    int n, k;
    cin>>n>>k;
    Pancake p[n];
    for (int i = 0; i < n; ++i)
        cin>>p[i].r>>p[i].h;
    sort(p, p+n);
    if (should_run) {
        long double ans = 0;
        for (int i = 0; i < n && i+k-1 < n; ++i) {
            long double sum = pi*p[i].r*p[i].r + 2*pi*p[i].r*p[i].h;
            //printf("i = %d => sum = %.9lf (%lld %lld)\n", i, (double) sum, p[i].r, p[i].h);
            vector<long long> vec;
            for (int j = i+1; j < n; ++j)
                vec.push_back(p[j].r * p[j].h);
            sort(vec.begin(), vec.end(), greater<long long>());
            for (int j = 1; j < k; ++j) {
                sum += 2*pi*vec[j-1];
            }
            ans = max(ans, sum);
        }
        printf("Case #%d: %.12lf\n", testcase, (double) ans);
    }
}
