#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <deque>
#include <vector>

#define PI 3.14159265358979323846

using namespace std;

struct pancakes {
    long long height;
    long long base;
    
    friend bool operator < (pancakes a, pancakes b) {
        if (a.height != b.height)
            return a.height > b.height;
        return a.base > b.base;
    }
};

pancakes pancake[1000];

int main() {
    int TT, T;
    scanf("%d", &TT);
    
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        int n, k;
        scanf("%d%d", &n, &k);
        
        int i, j;;
        for (i = 0; i < n; i++) {
            long long r, h;
            scanf("%lld%lld", &r, &h);
            pancake[i].height = 2*r*h;
            pancake[i].base = r*r;
        }
        sort(pancake, pancake+n);
        long long ans = 0;
        for (i = 0; i < n; i++) {
            long long tot = 0;
            int seen = 1;
            tot += pancake[i].base + pancake[i].height;
            for (j = 0; j < n && seen < k; j++) {
                if (j == i)
                    continue;
                if (pancake[j].base <= pancake[i].base) {
                    tot+=pancake[j].height;
                    seen++;
                }
            }
            ans = max(tot, ans);
        }
        
        printf("%.7lf\n", PI*ans);


    }
}
        