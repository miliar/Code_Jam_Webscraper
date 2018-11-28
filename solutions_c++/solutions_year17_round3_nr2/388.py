#include <cmath>
#include <iostream>
#include <vector>

typedef long double ld;
typedef unsigned long long ull;
typedef long long ll;

const ld pi = std::atan(1) * 4;

void collapse_distances(std::vector<std::pair<ull, bool>>& distances, ull& total, bool flag) {
    while (true) {
        bool has_distance = false;
        ull min_distance = 1000000000, min_distance_index;
        for (ull i = 0; i < distances.size(); ++i) {
            if (distances[i].second == flag && distances[i].first < min_distance) {
                min_distance_index = i;
                has_distance = true;
                min_distance = distances[i].first;
            }
        }
        if (has_distance && total + min_distance <= 720) {
            total += min_distance;
            distances.erase(distances.begin() + min_distance_index);
        } else {
            return;
        }
    }
}

int main() {
    ull T;
    std::cin >> T;
    std::cout.precision(9);

    for (ull t = 1; t <= T; ++t) {
        ull Ac, Aj;
        std::cin >> Ac >> Aj;
        std::vector<std::pair<std::pair<ull, ull>, bool>> activities(Ac + Aj);
        ull total_true = 0, total_false = 0;
        for (ull i = 0; i < Ac; ++i) {
            std::cin >> activities[i].first.first >> activities[i].first.second;
            activities[i].second = true;
            total_true += activities[i].first.second - activities[i].first.first;
        }
        for (ull i = Ac; i < Ac + Aj; ++i) {
            std::cin >> activities[i].first.first >> activities[i].first.second;
            activities[i].second = false;
            total_false += activities[i].first.second - activities[i].first.first;
        }
        std::sort(activities.begin(), activities.end());
        ull required = 0;
        std::vector<std::pair<ull, bool>> distances;
        for (ull i = 0; i + 1 < activities.size(); ++i) {
            if (activities[i].second == activities[i + 1].second) {
                distances.emplace_back(activities[i + 1].first.first - activities[i].first.second, activities[i].second);
            } else {
                ++required;
            }
        }
        if (activities.back().second == activities.front().second) {
            distances.emplace_back(activities.front().first.first + 1440 - activities.back().first.second, activities.back().second);
        } else {
            ++required;
        }
        collapse_distances(distances, total_true, true);
        collapse_distances(distances, total_false, false);
        std::cout << "Case #" << t << ": " << std::fixed << distances.size() * 2 + required << std::endl;
    }
    return 0;
}