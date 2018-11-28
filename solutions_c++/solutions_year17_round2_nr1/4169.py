#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<vector>
#include<algorithm>
#define FOR(i,l,n) for(int i=l;i<n;i++)
using namespace std;
int same (double a, double b) {
    return ((a - b) > -0.0000001 && (a - b) < 0.0000001);
}
struct horse {
    int k,s;
};
int main() {
    int t;
    scanf("%d", &t);
    FOR(i, 0, t) {
        int d, n;
        scanf("%d", &d);
        scanf("%d", &n);
        int K[n], S[n];
        double k[n], s[n];
        map<int, horse> horse_map;
        FOR(j, 0, n) {
            scanf("%d %d", &K[j], &S[j]);
            horse h;
            h.k = (double)K[j];
            h.s = (double)S[j];
            horse_map[K[j]] = h;
        }
        int x=0;
        for(map<int, horse>::iterator it=horse_map.begin(); it!=horse_map.end(); ++it) {
            k[x] = it->second.k;
            s[x] = it->second.s;
            x++;
        }
        double D= d * 1.0000000;
        double time = 0.0000000;
        int remaining = n;
        while (remaining != 0) {
            double curr_min = 1000000001.0000000;
            FOR(j, 0, n) {
                double curr_time = curr_min;
                if (j<n-1) {
                    if (s[j] > s[j+1])
                        if (!same(k[j], k[j+1]))
                            curr_time = (k[j+1] - k[j]) / (s[j] - s[j+1]);
                        else {
                            continue;
                        }
                    else
                        continue;
                }
                if ( j == n-1)
                    curr_time = (D - k[j]) / s[j];
                //cout << curr_time <<"--"<< D <<"--"<< k[j] <<"--"<< s[j] << endl;
                curr_min = min(curr_time, curr_min);
            }
            FOR(j, 0, n) {
                k[j] += s[j]*curr_min;
                //cout << j << "--" << k[j] << endl;
                if (same(k[j], D) || k[j] - D >0.0000001) {
                    remaining--;
                }
            }
            n = remaining;
            time += curr_min;
        }
        //cout << fixed << setprecision(7) << time << endl;
        //cout << fixed << setprecision(7) << D << endl;
        double ans = D/ time;
        printf("Case #%d: %.6f\n", i+1, ans);
    }
    return 0;
}
