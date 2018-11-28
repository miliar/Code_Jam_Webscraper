#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>

#define INF 1000000007.0
#define MAXN 1010

using namespace std;

double k[MAXN], s[MAXN];
double tempo[MAXN];

int main() {
//    freopen("cruise_control_large.txt", "r", stdin);
//    freopen("cruise_control_large_out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int caso=1;
    for (caso=1; caso<=t; caso++) {
        int n;
        double d;
        scanf("%lf %d", &d, &n);
        int i;
        double maiorTempo=0;
        for (i=1; i<=n; i++) {
            scanf("%lf %lf", &k[i], &s[i]);
            tempo[i]=(d-k[i])/s[i];
           // printf("+++ %lf\n", tempo[i]);
            maiorTempo=max(maiorTempo, tempo[i]);
        }

        //printf("** %lf\n", maiorTempo);
        double v=d/maiorTempo;
        printf("Case #%d: %.16lf\n", caso, v);
    }
    return 0;
}










