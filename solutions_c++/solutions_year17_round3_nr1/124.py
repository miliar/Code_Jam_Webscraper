#include <cstdio>
#include <queue>
#include <utility>
#include <cmath>
#include <algorithm>

using namespace std;

#define mp make_pair
#define rad first
#define hei second

const int maxN = 1111;
const double pi = 2*acos(0);

typedef pair<double, double> pdd;

int N, K;

pdd cakes[maxN];

double area, ans; int cnt;

priority_queue<double> heap;

inline double surround(const pdd& cake) {return 2*pi * cake.rad * cake.hei;}

inline double top(const pdd& cake) {return pi * cake.rad * cake.rad;}

inline double max(double a, double b) {return a < b ? b : a;}

int main() {
#ifdef RS16
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif // RS16

    int T; scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);

        scanf("%d%d", &N, &K);
        for(int i = 0; i < N; ++i) scanf("%lf%lf", &cakes[i].rad, &cakes[i].hei);
        sort(cakes, cakes+N);

        while(!heap.empty()) heap.pop();
        area = 0., cnt = 0, ans = 0.;

        for(int i = 0; i < N; ++i) {
            double s = surround(cakes[i]), t = top(cakes[i]);

            if(cnt == K-1) {
                ans = max(ans, area+s+t);
                if(cnt && -heap.top() < s) {
                    area -= -heap.top();
                    heap.pop();
                    heap.push(-s);
                    area += s;
                }
            }
            else {
                heap.push(-s);
                area += s, ++cnt;
            }
        }

        printf("%.12f\n", ans);
    }
}
