#include <iostream>
#include <utility>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstdio>

typedef long long lint;
typedef std::pair<lint, lint> pancake;
const int N = 1005;
const double PI = acos(-1.0);

int T, Cas = 1, n, k;
pancake pancakes[N];
pancake copy_pancakes[N];

int cmp(pancake pa, pancake pb) {
    return pb.first < pa.first;
}

int cmpByRH(pancake pa, pancake pb) {
    return pa.first * pa.second > pb.first * pb.second;
}

void UnitCase(int CaseId) {
    std::cout << "Case #" << CaseId << ": ";
    std::cin >> n >> k;
    for (int i = 1; i <= n; i ++) {
        std::cin >> pancakes[i].first >> pancakes[i].second;
    }
    std::sort(pancakes + 1, pancakes + 1 + n, cmp);
    lint answer = 0;
    for (int i = 1; i <= n - k + 1; i ++) {
        lint base_area = pancakes[i].first * pancakes[i].first + 2 * pancakes[i].first * pancakes[i].second;
        lint other_area = 0;
        std::vector <lint> areas;
        for (int j = i + 1; j <= n; j ++) {
            areas.push_back(2 * pancakes[j].first * pancakes[j].second);
        }
        std::sort(areas.begin(), areas.end());
        std::reverse(areas.begin(), areas.end());
        for (int j = 0; j < k - 1; j ++) {
            other_area += areas[j];
        }
        lint area = base_area + other_area;
        answer = std::max(answer, area);
    }
    printf("%.12lf\n", answer * PI);
}

int main() {
    std::cin >> T;
    for (int i = 1; i <= T; i ++) {
        UnitCase(i);
    }
    return 0;
}
