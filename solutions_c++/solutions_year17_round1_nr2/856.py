#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

template<class T>
inline T read() {
    T value;
    std::cin >> value;
    return value;
}

int div_floor(int a, int b) {
    return a / b;
}

int div_ceil(int a, int b) {
    return (a + b - 1) / b;
}

bool possible(int r, int q, int s) {
    return div_ceil(s * r * 9, 10) <= q && q <= div_floor(s * r * 11, 10);
}

struct Value {
    int smin, smax;

    Value(int smin, int smax) : smin(smin), smax(smax) {}

    bool valid() const {
        return smin <= smax;
    }

    friend bool operator<(const Value& a, const Value& b) {
        if (b.smax != a.smax) {
            return b.smax < a.smax;
        }
        return b.smin < a.smin;
    }

    Value& operator&=(const Value& b) {
        smin = std::max(smin, b.smin);
        smax = std::min(smax, b.smax);
        return *this;
    }

    friend Value operator&(const Value& a, const Value& b) {
        return Value(std::max(a.smin, b.smin), std::min(a.smax, b.smax));
    }
};

struct Iterator {
    size_t index = 0;
    std::vector<Value> v;

    Value next() {
        return v[index++];
    }

    Value current() {
        return v[index];
    }

    bool finished() {
        return index >= v.size();
    }
};

int main() {
    auto T = read<int>();
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        // std::cerr << "--- Case " << caseNum << std::endl;
        auto N = read<int>();
        auto P = read<int>();
        std::vector<int> R(N);
        for (auto& Ri : R) {
            std::cin >> Ri;
        }
        std::vector<Iterator> S(N);
        for (int i = 0; i < N; ++i) {
            // for each ingredient
            int r = R[i];
            for (int j = 0; j < P; ++j) {
                int q = read<int>();
                int smin = div_ceil(q * 10, r * 11);
                while (smin > 1 && possible(r, q, smin - 1)) {
                    --smin;
                }
                int smax = div_floor(q * 10, r * 9);
                while (possible(r, q, smax + 1)) {
                    ++smax;
                }
                if (smin > 0 && smax > 0 && smin <= smax && possible(r, q, smin) && possible(r, q, smax)) {
                    S[i].v.emplace_back(smin, smax);
                }
            }
            std::sort(S[i].v.begin(), S[i].v.end());
            // std::cerr << "Ingredient " << i << ":";
            // for (const auto& v : S[i].v) {
            //     std::cerr << " " << v.smin << "-" << v.smax;
            // }
            // std::cerr << " servings of " << r << "g" << std::endl;
        }
        int kits = 0;
        while (!S[0].finished()) {
            Value v = S[0].current();
            for (int i = 1; i < N; ++i) {
                if (S[i].finished()) {
                    goto finished;
                }
                v &= S[i].current();
            }
            if (v.valid()) {
                ++kits;
                for (int i = 0; i < N; ++i) {
                    S[i].next();
                    if (S[i].finished()) {
                        goto finished;
                    }
                }
                continue;
            }
            v = S[0].current();
            int imax = 0;
            for (int i = 1; i < N; ++i) {
                if (S[i].current() < v) {
                    v = S[i].current();
                    imax = i;
                }
            }
            S[imax].next(); // remove the worst value
            if (S[imax].finished()) {
                break;
            }
        }
    finished:
        // std::cerr << "Answer: " << kits << std::endl;
        printf("Case #%d: %d\n", caseNum, kits);
    }
    return 0;
}
