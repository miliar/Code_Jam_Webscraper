#include <bits/stdc++.h>

using std::pair;
using std::make_pair;
typedef pair<int, int> Pair;

const int N = 1000 + 10;
const double PI = acos(-1);

Pair data[N];
int n, k;

int main() {
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; ++ t) {
        scanf("%d%d", &n, &k);
        for (int i = 1; i <= n; ++ i) {
            int x, y;
            scanf("%d%d", &x, &y);
            data[i] = make_pair(x, y);
        }
        std::sort(data + 1, data + n + 1);

        double answer = 0;
        for (int max_id = k; max_id <= n; ++ max_id) {
            double temp = PI * data[max_id].first * data[max_id].first + 2 * PI * data[max_id].first * data[max_id].second;
            std::priority_queue<double> heap;
            for (int i = 1; i < max_id; ++ i) {
                heap.push((double)data[i].first * data[i].second);
            }
            for (int i = 1; i < k; ++ i) {
                double x = heap.top();
                heap.pop();
                temp += 2 * PI * x;
            }
            answer = std::max(answer, temp);
        }
        printf("Case #%d: %.7f\n", t, answer);
    }
    return 0;
}