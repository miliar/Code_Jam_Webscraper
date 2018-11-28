#include <iostream>
#include <stdio.h>
#include <queue>
using namespace std;
#define M_PI 3.14159265358979323846  /* pi */
#define LL long long int

bool compare(const pair<int, int> &p1, const pair<int, int> &p2) {
    return p1.first < p2.first;
}

LL calcArea(priority_queue<LL> pq ) {
    LL sum = 0;
    while (!pq.empty()) {
        sum += -pq.top();
        pq.pop();
    }
    
    return sum;
}

int main() {
    int cases, n, k, r, h;
    cin >> cases;
    for (int c = 1; c <= cases; c++) {
        cin >> n >> k;
        vector<pair<int, int> > pancakes;
        for (int i = 0; i < n; i++) {
            cin >> r >> h;
            pancakes.push_back(make_pair(r, h));
        }
        sort(pancakes.begin(), pancakes.end(), compare);

        priority_queue<LL> pq;
        LL res = 0;
        for (int i = 0; i < n; i++) {
            LL r = pancakes[i].first, h = pancakes[i].second;

            if (i+1 >= k) {
                LL t = r*r + 2*r*h + calcArea(pq);;
                res = max(t, res);
            }
            pq.push(-2*r*h);
            if (pq.size() >= k) pq.pop();
        }
        printf("Case #%d: %.9f\n", c, M_PI*res);
        // cout << "Case #" << c << ": " << setprecision(9) << M_PI*res << endl;    
    }
}