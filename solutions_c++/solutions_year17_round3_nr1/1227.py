#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

int T, N, K;
pair<double, double> cake[10000];

const double pi = acos(-1);
double ans, sum;

int main() {
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        cin >> N >> K;
        for (int i = 0; i < N; i++) cin >> cake[i].first >> cake[i].second;
        sort(cake, cake + N);
        
        ans = -1, sum = 0;
        priority_queue< double > q;
        while (!q.empty()) q.pop();
        
        for (int i = 0; i < K - 1; i++) {
            q.push( -cake[i].first * cake[i].second );
            sum += cake[i].first * cake[i].second;
        }
        
        for (int i = K - 1; i < N; i++) {
            double tmpAns = (sum + cake[i].first * cake[i].second) * 2 + cake[i].first * cake[i].first;
            if (ans < tmpAns) ans = tmpAns;
            if (q.size() && cake[i].first * cake[i].second > -q.top()) {
                sum += q.top();
                sum += cake[i].first * cake[i].second;
                q.pop();
                q.push( -cake[i].first * cake[i].second );
            }
        }
        printf("Case #%d: %.8lf\n", cas, ans * pi);
    }
    return 0;
}