#include <iostream>
#include <cassert>

struct Stall {
    bool filled;
    int64_t index;
    int64_t left_used;
    int64_t right_used;
    int64_t max;
    int64_t min;

    friend std::ostream& operator<<(std::ostream& out, const Stall& s) {
        out << "("<< (s.filled ? "#" : "-") << "," << s.index << "," << s.left_used <<
            "," << s.right_used << "," << s.min << "," << s.max << ")";
        return out;
    }
};

int64_t choose(const Stall* stalls, int64_t start, int64_t count) {
    assert(count > 0);
    const Stall* s = nullptr;
    for (int64_t j = 0; j < count; ++j) {
        int64_t i = j + start;
        const Stall* t = &stalls[i];
        if (!t->filled) {
            if (!s || t->min > s->min || (t->min == s->min && t->max > s->max)) {
                s = t;
            }
        }
    }
    return s->index;
}


void init(Stall* stalls, int64_t count) {
    for (int64_t j = 0; j < count; ++j) {
        Stall& s = stalls[j];
        s.filled = false;
        s.index = j;
    }
}


void update(Stall* stalls, int64_t start, int64_t count, int64_t left, int64_t right) {
    for (int64_t j = 0; j < count; ++j) {
        int64_t i = start + j;
        Stall& s = stalls[i];
        s.left_used = left;
        s.right_used = right;
        s.max = std::max(i - left - 1, right - i - 1);
        s.min = std::min(i - left - 1, right - i - 1);
    }
}


inline void display(Stall* stalls, int64_t count) {
    for (int64_t i = 0; i < count; ++i) {
        std::cout << stalls[i] << std::endl;
    }
    std::cout << "====" << std::endl;
}

std::pair<int64_t,int64_t> solve(int64_t stall_ct, int64_t people) {
    Stall* stalls = new Stall[stall_ct];
    init(stalls, stall_ct);
    update(stalls, 0, stall_ct, -1, stall_ct);

    // display(stalls, stall_ct);
    for (int p = 0; p < people-1; ++p) {
        int64_t i = choose(stalls, 0, stall_ct);
        Stall& s = stalls[i];
        s.filled = true;
        update(stalls, s.left_used + 1, i - s.left_used - 1, s.left_used, i);
        update(stalls, i + 1, s.right_used - i - 1, i, s.right_used);
    }
    // display(stalls, stall_ct);
    int64_t i = choose(stalls, 0, stall_ct);
    Stall& s = stalls[i];
    std::pair<int64_t,int64_t> result(s.min, s.max);
    delete[] stalls;
    return result;
}

int main() {
    int testcases;
    std::cin >> testcases;
    for (int i = 0; i < testcases; ++i) {
        int64_t stalls, people;
        std::cin >> stalls >> people;
        auto result = solve(stalls, people);
        std::cout << "Case #" << (i+1) << ": " << result.second << " " << result.first << std::endl;
    }
}
