#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#define N 111111
#define ll long long
#define eps 1e-13
using namespace std;

int t;
int main(void){
    scanf("%d", &t);
    for(int s = 1; s <= t; s++){
        int n, k;
        double u, p[55];

        scanf("%d%d%lf", &n, &k, &u);
        for(int i = 0; i < n; i++) scanf("%lf", &p[i]);
        
        double lb = 0.0, ub = 1.0;
        while(ub - lb > eps){
            double md = (lb + ub) / 2;
            double s = 0;
            for(int i = 0; i < n; i++) s += max(0.0, md - p[i]);
            if(s < u) lb = md; else ub = md;
        }
        
        double ans = 1.0;
        for(int i = 0; i < n; i++) ans *= max(lb, p[i]);

        printf("Case #%d: %.9lf\n", s, ans);
    }
}
