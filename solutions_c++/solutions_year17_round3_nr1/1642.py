#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>
#include <functional>
using namespace std;

#define r(pair) pair.first
#define h(pair) pair.second
#define sq(x) x*x

typedef unsigned long long ull;

typedef pair<ull,ull> ii;

int t;
int n, k;
vector<ii> cakes;
priority_queue<ull,vector<ull>,greater<ull>> km1most;

int main() {
    cin >> t;
    for(int tc = 1; tc <= t; ++tc) {
        cin >> n >> k;
        cakes.resize(n);
        for(int i = 0; i < n; ++i)
            cin >> r(cakes[i]) >> h(cakes[i]);
        sort(cakes.begin(), cakes.end());
        km1most = priority_queue<ull,vector<ull>,greater<ull>>();
        ull tarea = 0;
        ull best = 0;
        for(int bottom = 0; bottom < n; ++bottom) {
            ull tradius = r(cakes[bottom]);
            ull myarea = 2*(tradius)*(h(cakes[bottom]));
            best = max(best, sq(tradius)+tarea+myarea);

            if(km1most.size() < k-1) {
                km1most.push(myarea);
                tarea += myarea;
            }
            else {
                if(km1most.size() > 0 && myarea > km1most.top()) {
                    tarea += myarea - km1most.top();
                    km1most.pop();
                    km1most.push(myarea);
                }
            }
        }
        printf("Case #%d: %lf\n", tc, M_PI*(double)best);
    }

    return 0;
}
