#include <bits/stdc++.h>

#define MIN -100000

double targets[50];

int main() {
    int T;
    scanf("%i\n", &T);
    for (int t = 0; t < T; t++) {
        //printf("Case #%i:\n", t+1);
        int N, P;
        scanf("%i %i\n", &N, &P);

        for (int i = 0; i < N; i++) {
            scanf("%lf", &targets[i]);
        }

        std::multiset<double> upl[50];

        for (int i = 0; i < N; i++) {
            double targ = targets[i];
            for (int pi = 0; pi < P; pi++) {
                double pq;
                scanf("%lf", &pq);
                pq = pq / targ;
                bool usable = (
                    ((std::floor(pq) * 1.1) >= pq && (std::floor(pq) * 0.9) <= pq)
                    || ((std::ceil(pq) * 1.1) >= pq && (std::ceil(pq) * 0.9) <= pq)
                );
                //printf("Package ingred=%i, id=%i, usable=%i, pq=%lf\n", i, pi, usable?1:0, pq);
                if (usable) {
                    upl[i].insert(pq);
                }
            }
        }

        int ans;
        if (N == 1) {
            ans = upl[0].size();
        } else if (N == 2) {
            ans = 0;
            for (auto a : upl[0]) {
                for (auto bi = upl[1].begin(); bi != upl[1].end();) {
                    double b = *bi;
                    if (b == MIN) continue;
                    double x = std::min(a, b), y = std::max(a, b);
                    double xb = x*1.1, xs=x*0.9, yb=y*1.1, ys=y*0.9;
                    if (xb >= ys) {
                        ans++;
                        //printf("Matching a=%lf, b=%lf, %lf<%lf\n", a, b, xb, ys);
                        bi = upl[1].erase(bi);
                        break;
                    } else {
                        ++bi;
                    }
                }
            }
        }
        printf("Case #%i: %i\n", t+1, ans);
    }
}
