// Google Code Jam 2017 Round 1B - A
// https://code.google.com/codejam/contest/8294486/dashboard#s=p0
// 2017.04.22

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
#define md 1000000007
using namespace std;

int t;
int n, d;

int main(void){
    scanf("%d", &t);
    for(int s = 1; s <= t; s++){
        scanf("%d%d", &d, &n);
        double ans = 1e-15;
        for(int i = 0; i < n; i++){
            int c, m;
            scanf("%d%d", &c, &m);
            ans = max(ans, (double) (d - c) / m);
        }
        printf("Case #%d: %.6lf\n", s, d / ans);
    }
}
