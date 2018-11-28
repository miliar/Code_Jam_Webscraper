// License {{{
// Copyright © 2016 Fedor Alekseev <feodor.alexeev@gmail.com>
// This work is free. You can redistribute it and/or modify it under the
// terms of the Do What The Fuck You Want To Public License, Version 2,
// as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.
// }}}

#include <bits/stdc++.h>

#ifdef moskupols
    #define debug(...) fprintf(stderr, __VA_ARGS__)
#else
    #define debug(...) 42
#endif

#define timestamp(x) debug("["#x"]: %.3f\n", (double)clock() / CLOCKS_PER_SEC)

#define hot(x) (x)
#define sweet(value) (value)
#define faceless

#define WHOLE(v) (v).begin(),(v).end()
#define RWHOLE(v) (v).rbegin(),(v).rend()
#define UNIQUE(v) (v).erase(unique(WHOLE(v)),(v).end())

typedef long long int64;
typedef unsigned long long uint64;
typedef long double TReal;

template<class TWrapped>
class TMultiSolver {
public:
    template<typename... Args>
    explicit TMultiSolver(int testCase, Args&&... args)
        : Wrapped(std::forward<Args>(args)...)
        , TestCase(testCase)
    {
    }

    void Solve() {
        Wrapped.Solve();
    }

    void PrintAnswer(std::ostream& out) const {
        out << "Case #" << TestCase << ": ";

        std::ostringstream oss;
        Wrapped.PrintAnswer(oss);
        if (oss.str().back() != '\n') {
            oss << '\n';
        }

        out << oss.str();
    }

    TWrapped Wrapped;
    int TestCase;
};

class TSolver {
public:
    int r, c;
    std::vector<std::string> m;
    std::vector<std::string> init;

    struct TRect {
        int x1, y1;
        int x2, y2;

        TRect Expand(int dir) const {
            auto cp = *this;
            int* targets[4] = {&cp.y1, &cp.x1, &cp.y2, &cp.x2};
            int shifts[4] = {-1, -1, 1, 1};
            (*targets[dir]) += shifts[dir];
            return cp;
        }

        bool IsValid(int r, int c) const {
            return x1 >= 0 && y1 >= 0 && x2 < r && y2 < c;
        }
    };

    std::unordered_map<char, TRect> rects;

    bool tryFill(char ch, const TRect& rect) {
        if (!rect.IsValid(r, c)) {
            return false;
        }
        for (int i = rect.x1; i <= rect.x2; ++i) {
            for (int j = rect.y1; j <= rect.y2; ++j) {
                if (m[i][j] != '?' && m[i][j] != ch) {
                    return false;
                }
            }
        }
        for (int i = rect.x1; i <= rect.x2; ++i) {
            for (int j = rect.y1; j <= rect.y2; ++j) {
                m[i][j] = ch;
            }
        }
        return true;
    }

    explicit TSolver(std::istream& in) {
        in >> r >> c;
        m.resize(r);
        for (auto& s : m) {
            in >> s;
        }
    }

    bool Ok() const {
        for (const auto& s : m) {
            if (s.find('?') != std::string::npos) {
                return false;
            }
        }
        return true;
    }

    void Solve() {
        init = m;

        for (int seed = 0; seed < 1000; ++seed) {
            srand(seed);
            m = init;

            for (int i = 0; i < r; ++i) {
                for (int j = 0; j < c; ++j) {
                    if (m[i][j] != '?') {
                        rects[m[i][j]] = {i, j, i, j};
                    }
                }
            }

            for (int s = 0; s <= r * c; ++s) {
                for (auto& p : rects) {
                    char ch = p.first;
                    auto& rect = p.second;
                    auto expanded = rect.Expand(rand() % 4);
                    if (tryFill(ch, expanded)) {
                        rect = expanded;
                    }
                }
            }

            if (Ok()) break;
        }
    }

    void PrintAnswer(std::ostream& out) const {
        out << '\n';
        for (const auto& s : m) {
            out << s << '\n';
        }
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);

    int t;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        auto solver = std::make_shared<TMultiSolver<TSolver>>(i, std::cin);
        solver->Solve();
        solver->PrintAnswer(std::cout);
        debug("%d ", i);
        timestamp(multi);
    }

    timestamp(end);
    return 0;
}
