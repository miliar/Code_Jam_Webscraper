#include <iostream>
#include <vector>
#include <map>

struct package {
    int min;
    int max;

    bool operator< (const package& other) const
    {
        if (min < other.min)
            return true;
        if (min > other.min)
            return false;
        if (max < other.max)
            return true;
        return false;
    }
};

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        int N, P;
        std::cin >> N >> P;

        std::vector<int> recipe;
        for (int n = 0; n < N; ++n) {
            int R;
            std::cin >> R;
            recipe.push_back(R);
        }

        std::vector<std::map<package, int>> quantity(N);
        for (int n = 0; n < N; ++n) {
            int R = recipe[n];
            for (int p = 0; p < P; ++p) {
                int Q;
                std::cin >> Q;
                package pck;
                pck.min = (10 * Q + 11 * R - 1) / (11 * R);
                pck.max = (10 * Q) / (9 * R);
                auto i = quantity[n].find(pck);
                if (i == quantity[n].end()) {
                    quantity[n][pck] = 1;
                } else {
                    i->second += 1;
                }
            }
        }

        int y = 0;
        bool done = false;
        for (; ; ) {
            int min = -1;
            int max = -1;
            int max_index = -1;
            int count = -1;
            for (int n = 0; n < N; ++n) {
                if (quantity[n].empty()) {
                    done = true;
                    break;
                }
                int mn = quantity[n].begin()->first.min;
                if (min == -1 || mn <= min) {
                    min = mn;
                    int mx = quantity[n].begin()->first.max;
                    if (max == -1 || mx < max) {
                        max = mx;
                        max_index = n;
                    }
                }
                int ct = quantity[n].begin()->second;
                if (count == -1 || ct < count) {
                    count = ct;
                }
            }

            if (done) {
                break;
            }

            bool to_continue = false;
            for (int n = 0; n < N; ++n) {
                if (quantity[n].begin()->first.min > max) {
                    quantity[max_index].erase(quantity[max_index].begin());
                    to_continue = true;
                    break;
                }
            }
            if (to_continue) {
                continue;
            }

            for (int n = 0; n < N; ++n) {
                if (quantity[n].begin()->second == count) {
                    quantity[n].erase(quantity[n].begin());
                } else {
                    quantity[n].begin()->second -= count;
                }
            }

            y += count;
        }

        std::cout << "Case #" << t << ": " << y << std::endl;
    }
}
