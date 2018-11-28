#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>

template<class T>
inline T read() {
    T value;
    std::cin >> value;
    return value;
}

struct pancake_t {
    int r;
    int h;
    double side;
    bool used = false;
};

struct compare_by_r {
    bool operator()(const pancake_t& a, const pancake_t& b) const {
        return b.r < a.r;
    }
};

struct compare_by_side {
    bool operator()(const pancake_t* a, const pancake_t* b) const {
        return b->side < a->side;
    }
};

int main() {
    auto T = read<int>();
    double pi = std::acos(-1.0);
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        int N, K; std::cin >> N >> K;
        std::vector<pancake_t> p(N);
        for (int i = 0; i < N; ++i) {
            std::cin >> p[i].r >> p[i].h;
            p[i].side = 2.0 * pi * p[i].r * p[i].h;
        }
        std::sort(p.begin(), p.end(), compare_by_r());
        std::vector<pancake_t*> pp(N);
        for (int i = 0; i < N; ++i) {
            pp[i] = &p[i];
        }
        std::sort(pp.begin(), pp.end(), compare_by_side());
        double max_area = 0.0;
        for (int i = 0; i < N; ++i) {
            double area = pi * p[i].r * p[i].r + p[i].side;
            p[i].used = true;
            int k = 1;
            // collect the maximum height of pancakes
            for (int j = 0; j < N && k < K; ++j) {
                if (!pp[j]->used) {
                    area += pp[j]->side;
                    ++k;
                }
            }
            if (k < K) {
                break; // impossible
            }
            if (max_area < area) {
                max_area = area;
            }
        }
        printf("Case #%d: %.9lf\n", caseNum, max_area);
    }
    return 0;
}
