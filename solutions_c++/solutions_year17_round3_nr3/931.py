#include <bits/stdc++.h>

using namespace std;

typedef long long lint;

const long double PI=atan(1)*4;
#define pb push_back 
#define mp make_pair 
inline long double calc(pair<int, int> x) {
    return 2 * PI * (long double)x.first * x.second;
}

int main() {
    int t;
    int n, k;
    scanf("%d", &t);
    double maxio;
    for(int CASE = 1; CASE <= t; CASE++) {
        scanf("%d %d", &n, &k);
        double ul;
        int u;
        scanf("%lf", &ul);
        u = int(ul*10000 + 1e-1);
        cerr<< u <<endl;
        vector<int> svi(n);
        for(int i = 0; i < n; i++) {
            double a;
            scanf("%lf", &a);
            svi[i] = int(a*10000 + 1e-1);
        }
        sort(svi.begin(), svi.end());
        for(int i = 0; i < n; i++) {
            int sljed = 10000;
            if(i < n-1) sljed = svi[i+1];
            while(u && svi[i]<sljed) {
                for(int j = i; j >= 0 && u; j--) {
                    svi[j]++;
                    u--;
                }
            }
        }
        double maxio = 1;
        for(int i = 0; i < n; i++) {
            maxio *= svi[i]/10000.;
        }
        printf("Case #%d: %.9lf\n", CASE, maxio);
    }
    return 0;
}