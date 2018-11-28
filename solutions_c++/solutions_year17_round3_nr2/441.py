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

struct range_t {
    int start;
    int end;
    int size;
    int owner;

    range_t() = default;
    range_t(int start, int end, int owner = -1) : start(start), end(end), size(end - start), owner(owner) {
        this->start %= 24 * 60;
        this->end %= 24 * 60;
        if (this->size < 0) {
            this->size += 24 * 60;
        }
    }

    friend bool operator<(const range_t& a, const range_t& b) {
        return a.start < b.start;
    }
};

struct range_t_by_size {
    bool operator()(const range_t& a, const range_t& b) const {
        return a.size < b.size;
    }
};

struct range_t_by_size_rev {
    bool operator()(const range_t& a, const range_t& b) const {
        return b.size < a.size;
    }
};

int main() {
    auto T = read<int>();
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        // std::cerr << "---" << std::endl;
        int Ac, Aj; std::cin >> Ac >> Aj;
        std::vector<range_t> A;
        std::vector<int> O;
        for (int i = 0; i < Ac + Aj; ++i) {
            int start, end; std::cin >> start >> end;
            A.emplace_back(start, end, i < Ac ? 0 : 1);
        }
        std::sort(A.begin(), A.end());
        range_t last_range = A.back();
        std::vector<range_t> self_frees[2];
        std::vector<range_t> cross_frees;
        int need_times[2] = {12 * 60, 12 * 60};
        int switches = 0;
        for (const auto& r : A) {
            if (r.start != last_range.end) {
                // add some free time
                if (last_range.owner == r.owner) {
                    self_frees[last_range.owner].emplace_back(last_range.end, r.start, last_range.owner);
                    // std::cerr << "Got self free " << last_range.end << "-" << r.start << std::endl;
                } else {
                    cross_frees.emplace_back(last_range.end, r.start, last_range.owner);
                    // std::cerr << "Got cross free " << last_range.end << "-" << r.start << std::endl;
                }
            }
            need_times[r.owner] -= r.size;
            if (r.owner != last_range.owner) {
                ++switches;
            }
            last_range = r;
        }

        // smallest ranges last
        std::sort(self_frees[0].begin(), self_frees[0].end(), range_t_by_size_rev());
        std::sort(self_frees[1].begin(), self_frees[1].end(), range_t_by_size_rev());
        // biggest ranges last
        std::sort(cross_frees.begin(), cross_frees.end(), range_t_by_size());

        for (int owner = 0; owner <= 1; ++owner) {
            while (need_times[owner] > 0) {
                if (!self_frees[owner].empty()) {
                    // try to use as many self holes as possible
                    auto& f = self_frees[owner].back();
                    if (f.size > need_times[owner]) {
                        f.start += need_times[owner];
                        f.start %= 24 * 60;
                        f.size -= need_times[owner];
                        need_times[owner] = 0;
                    } else {
                        need_times[owner] -= f.size;
                        self_frees[owner].pop_back();
                    }
                } else if (!cross_frees.empty()) {
                    // try to use as many cross holes as possible
                    auto& f = cross_frees.back();
                    if (f.size > need_times[owner]) {
                        if (f.owner == owner) {
                            f.start += need_times[owner];
                            f.start %= 24 * 60;
                        } else {
                            f.end -= need_times[owner];
                            if (f.end < 0) {
                                f.end += 24 * 60;
                            }
                        }
                        f.size -= need_times[owner];
                        need_times[owner] = 0;
                    } else {
                        need_times[owner] -= f.size;
                        cross_frees.pop_back();
                    }
                } else {
                    // there is no free lunch left
                    break;
                }
            }
        }

        if (need_times[0] > 0 && need_times[1] > 0) {
            std::cerr << "WARNING: both people need time" << std::endl;
        }
        if (!cross_frees.empty()) {
            std::cerr << "WARNING: there is cross time left" << std::endl;
            for (const auto& r : cross_frees) {
                std::cerr << "Cross free " << r.start << "-" << r.end << " size=" << r.size << " owner=" << r.owner << std::endl;
            }
        }

        // after the above loop there should be no self or cross frees left
        // and only one of them should require extra time, just calculate how
        // much switches are required
        for (int owner = 0; owner <= 1; ++owner) {
            switches += self_frees[owner].size() * 2;
        }

        printf("Case #%d: %d\n", caseNum, switches);
    }
    return 0;
}
