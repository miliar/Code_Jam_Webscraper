#include <cstdio>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

const double pi = 3.14159265359;

int T;

int N, K;

struct cake {
    int r, h;
    bool operator <(const cake & that) const {
        return (r < that.r);
    }
} cakes[1000];

int main() {
    freopen("1a.in", "r", stdin);
    
    scanf("%d\n", &T);
    
    for (int test = 1; test <= T; test++) {
        scanf("%d %d\n", &N, &K);
        
        for (int i = 0; i < N; i++) {
            scanf("%d %d\n", &cakes[i].r, &cakes[i].h);
        }
        sort(cakes, cakes + N);
        
        priority_queue<double, std::vector<double>, std::greater<double>> pq;
        double side = 0.0;
        for (int i = 0; i < K-1; i++) {
            double r = cakes[i].r;
            
            double curr = 2 * pi * r * cakes[i].h;
            pq.push(curr);
            side += curr;
        }
        
        double maxSize = 0.0;
        for (int i = K-1; i < N; i++) {
            double r = (double)cakes[i].r;
            double curr = 2 * pi * r * cakes[i].h;
            
            side += curr;
            maxSize = max(maxSize, side + pi * r * r);
            
            pq.push(curr);
            side -= pq.top();
            pq.pop();
        }
        
        printf("Case #%d: %f\n", test, maxSize);
    }
}
