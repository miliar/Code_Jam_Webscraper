#include <cstdint>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

struct problem {
    int64_t stalls;
    int64_t customers;
};


vector<problem> read_problems() {
    int n;
    cin >> n;

    vector<problem> problems;

    for (int i = 0; i < n; i++) {
        int64_t stalls;
        int64_t customers;
        cin >> stalls >> customers;

        problems.push_back({ stalls, customers });
    }

    return problems;
}

std::pair<int64_t, int64_t> solve(problem p) {
    std::map<int, int> spaces;

    spaces[p.stalls] = 1;

    for (int64_t i = 0; i < p.customers - 1; i++) {
        if (spaces.empty()) {
            break;
        }

        auto p_largest = spaces.rbegin();
        auto largest = p_largest->first;

        if (p_largest->second == 1) {
            spaces.erase(std::next(p_largest).base());
        }
        else {
            p_largest->second -= 1;
        }

        auto left = (largest - 1) / 2;
        auto right = largest / 2;

        if (left > 1) {
            auto p1 = spaces.insert(std::make_pair(left, 1));

            if (!p1.second) {
                p1.first->second += 1;
            }
        }

        if (right > 1) {
            auto p2 = spaces.insert(std::make_pair(right, 1));


            if (!p2.second) {
                p2.first->second += 1;
            }
        }
    }

    auto largest = spaces.empty() ? 0 : spaces.rbegin()->first;

    return std::make_pair(largest / 2, (largest -1 ) / 2);
}


int main(int argc, char* argv[]) {
    auto problems = read_problems();

    int n = 1;

    for (auto p : problems) {
        auto solution = solve(p);
        cout << "Case #" << n << ": " << solution.first << " " << solution.second << endl;
        n += 1;
    }

    return 0;
}