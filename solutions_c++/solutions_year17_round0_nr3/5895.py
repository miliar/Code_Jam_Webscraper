#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int, int> ii;
////////////////////////////// BEGIN OF SEARCH ////////////////////////////// 
namespace integer_search {
    //TODO: implement fibonacci search
    template<typename Datatype, typename Function>
    Datatype first_true(Datatype l, Datatype r, const Datatype not_found, const Function& f) {
        Datatype ans = not_found;
        while (l <= r) {
            const Datatype m = l + (r-l) / 2;
            if (f(m)) {
                ans = m;
                r = m-1;
            } else {
                l = m+1;
            }
        }
        return ans;
    }

    template<typename Datatype, typename Function>
    Datatype first_false(Datatype l, Datatype r, const Datatype not_found, const Function& f) {
        Datatype ans = not_found;
        while (l <= r) {
            const Datatype m = l + (r-l) / 2;
            if (!f(m)) {
                ans = m;
                r = m-1;
            } else {
                l = m+1;
            }
        }
        return ans;
    }

    template<typename Datatype, typename Function>
    Datatype last_true(Datatype l, Datatype r, const Datatype not_found, const Function& f) {
        Datatype ans = not_found;
        while (l <= r) {
            const Datatype m = l + (r-l) / 2;
            if (f(m)) {
                ans = m;
                l = m+1;
            } else {
                r = m-1;
            }
        }
        return ans;
    }

    template<typename Datatype, typename Function>
    Datatype last_false(Datatype l, Datatype r, const Datatype not_found, const Function& f) {
        Datatype ans = not_found;
        while (l <= r) {
            const Datatype m = l + (r-l) / 2;
            if (!f(m)) {
                ans = m;
                l = m+1;
            } else {
                r = m-1;
            }
        }
        return ans;
    }

    template<typename Datatype, typename Function>
    Datatype argmax(Datatype l, Datatype r, const Function& f) {
        // f must be strictly increasing, then strictly decreasing (or just strictly monotonic)
        Datatype ans = l;
        l += 1;
        while (l <= r) {
            const Datatype m = l + (r-l) / 2;
            if (f(m) > f(m-1)) {
                ans = m;
                l = m+1;
            } else {
                r = m-1;
            }
        }
        return ans;
    }

    template<typename Datatype, typename Function>
    Datatype argmin(Datatype l, Datatype r, const Function& f) {
        // f must be strictly decreasing, then strictly increasing (or just strictly monotonic)
        Datatype ans = l;
        l += 1;
        while (l <= r) {
            const Datatype m = l + (r-l) / 2;
            if (f(m) < f(m-1)) {
                ans = m;
                l = m+1;
            } else {
                r = m-1;
            }
        }
        return ans;
    }

    template<typename Datatype, typename Function>
    auto maximum(Datatype l, Datatype r, const Function& f) -> decltype(f(l)) {
        // f must be strictly increasing, then strictly decreasing (or just strictly monotonic)
        auto ans = f(l);
        l += 1;
        while (l <= r) {
            const Datatype m = l + (r-l) / 2;
            const auto fm = f(m);
            const auto fmm1 = f(m-1);
            if (fm > fmm1) {
                ans = fm;
                l = m+1;
            } else {
                r = m-1;
            }
        }
        return ans;
    }

    template<typename Datatype, typename Function>
    auto minimum(Datatype l, Datatype r, const Function& f) -> decltype(f(l)) {
        // f must be strictly increasing, then strictly decreasing (or just strictly monotonic)
        auto ans = f(l);
        l += 1;
        while (l <= r) {
            const Datatype m = l + (r-l) / 2;
            const auto fm = f(m);
            const auto fmm1 = f(m-1);
            if (fm < fmm1) {
                ans = fm;
                l = m+1;
            } else {
                r = m-1;
            }
        }
        return ans;
    }
}

namespace floating_search {
    // Precision reference: http://codeforces.com/blog/entry/49189
    // TODO: golden-section search (and test it in some problem)
    template<typename Datatype, typename Function>
    Datatype first_true(Datatype l, Datatype r, const Datatype not_found, const int iterations, const Function& f) {
        Datatype ans = not_found;
        for (int iteration = 0; iteration < iterations; ++iteration) {
            const Datatype m = l + (r-l) / 2;
            if (f(m)) {
                ans = m;
                r = m;
            } else {
                l = m;
            }
        }
        return ans;
    }

    template<typename Datatype, typename Function>
    Datatype first_false(Datatype l, Datatype r, const Datatype not_found, const int iterations, const Function& f) {
        Datatype ans = not_found;
        for (int iteration = 0; iteration < iterations; ++iteration) {
            const Datatype m = l + (r-l) / 2;
            if (!f(m)) {
                ans = m;
                r = m;
            } else {
                l = m;
            }
        }
        return ans;
    }

    template<typename Datatype, typename Function>
    Datatype last_true(Datatype l, Datatype r, const Datatype not_found, const int iterations, const Function& f) {
        Datatype ans = not_found;
        for (int iteration = 0; iteration < iterations; ++iteration) {
            const Datatype m = l + (r-l) / 2;
            if (f(m)) {
                ans = m;
                l = m;
            } else {
                r = m;
            }
        }
        return ans;
    }

    template<typename Datatype, typename Function>
    Datatype last_false(Datatype l, Datatype r, const Datatype not_found, const int iterations, const Function& f) {
        Datatype ans = not_found;
        for (int iteration = 0; iteration < iterations; ++iteration) {
            const Datatype m = l + (r-l) / 2;
            if (!f(m)) {
                ans = m;
                l = m;
            } else {
                r = m;
            }
        }
        return ans;
    }


#if 0
    template<typename Datatype, typename Function>
    Datatype argmax(Datatype l, Datatype r, const int iterations, const Function& f) {
        for (int iteration = 0; iteration < iterations; ++iteration) {
            // f must be strictly increasing, then strictly decreasing (or just strictly monotonic)
            const Datatype third = (r-l) / 3;
            const Datatype m1 = l + third;
            const Datatype m2 = m1 + third;
            if (f(m1) > f(m2)) {
                r = m2;
            } else {
                l = m1;
            }
        }
        return (l+r)/2;
    }

    template<typename Datatype, typename Function>
    Datatype argmin(Datatype l, Datatype r, const int iterations, const Function& f) {
        for (int iteration = 0; iteration < iterations; ++iteration) {
            // f must be strictly decreasing, then strictly increasing (or just strictly monotonic)
            const Datatype third = (r-l) / 3;
            const Datatype m1 = l + third;
            const Datatype m2 = m1 + third;
            if (f(m1) < f(m2)) {
                r = m2;
            } else {
                l = m1;
            }
        }
        return (l+r)/2;
    }

    template<typename Datatype, typename Function>
    auto maximum(Datatype l, Datatype r, int iterations, const Function& f) -> decltype(f(l)) {
        // f must be strictly increasing, then strictly decreasing (or just strictly monotonic)
        while (iterations--) {
            const Datatype third = (r-l) / 3;
            const Datatype m1 = l + third;
            const Datatype m2 = m1 + third;
            const auto fm1 = f(m1);
            const auto fm2 = f(m2);
            if (fm1 > fm2) {
                if (iterations == 0)
                    return fm1;
                else
                    r = m2;
            } else {
                if (iterations == 0)
                    return fm2;
                else
                    l = m1;
            }
        }
        throw std::runtime_error("no warning");
    }

    template<typename Datatype, typename Function>
    auto minimum(Datatype l, Datatype r, int iterations, const Function& f) -> decltype(f(l)) {
        // f must be strictly decreasing, then strictly increasing (or just strictly monotonic)
        while (iterations--) {
            const Datatype third = (r-l) / 3;
            const Datatype m1 = l + third;
            const Datatype m2 = m1 + third;
            const auto fm1 = f(m1);
            const auto fm2 = f(m2);
            if (fm1 < fm2) {
                if (iterations == 0)
                    return fm1;
                else
                    r = m2;
            } else {
                if (iterations == 0)
                    return fm2;
                else
                    l = m1;
            }
        }
        throw std::runtime_error("no warning");
    }
#endif

    template<typename Datatype, typename Function>
    Datatype argmax(Datatype l, Datatype r, const int iterations, const Function& f) {
        // f must be strictly increasing, then strictly decreasing (or just strictly monotonic)
        // rule of thumb: this function converges (slightly) faster than ternary search
        const Datatype golden_ratio = (1 + std::sqrt((Datatype) 5)) / 2;
        Datatype m1 = r - (r-l) / golden_ratio;
        Datatype m2 = l + (r-l) / golden_ratio;
        auto fm1 = f(m1);
        auto fm2 = f(m2);
        for (int iteration = 0; iteration < iterations; ++iteration) {
            if (fm1 > fm2) {
                r = m2;
                m2 = m1;
                fm2 = fm1;
                m1 = r - (r-l) / golden_ratio;
                fm1 = f(m1);
            } else {
                l = m1;
                m1 = m2;
                fm1 = fm2;
                m2 = l + (r-l) / golden_ratio;
                fm2 = f(m2);
            }
        }
        return (l+r)/2;
    }

    template<typename Datatype, typename Function>
    Datatype argmin(Datatype l, Datatype r, const int iterations, const Function& f) {
        // f must be strictly decreasing, then strictly increasing (or just strictly monotonic)
        // rule of thumb: this function converges (slightly) faster than ternary search
        const Datatype golden_ratio = (1 + std::sqrt((Datatype) 5)) / 2;
        Datatype m1 = r - (r-l) / golden_ratio;
        Datatype m2 = l + (r-l) / golden_ratio;
        auto fm1 = f(m1);
        auto fm2 = f(m2);
        for (int iteration = 0; iteration < iterations; ++iteration) {
            if (fm1 < fm2) {
                r = m2;
                m2 = m1;
                fm2 = fm1;
                m1 = r - (r-l) / golden_ratio;
                fm1 = f(m1);
            } else {
                l = m1;
                m1 = m2;
                fm1 = fm2;
                m2 = l + (r-l) / golden_ratio;
                fm2 = f(m2);
            }
        }
        return (l+r)/2;
    }

    template<typename Datatype, typename Function>
    auto maximum(Datatype l, Datatype r, int iterations, const Function& f) -> decltype(f(l)) {
        // f must be strictly increasing, then strictly decreasing (or just strictly monotonic)
        // rule of thumb: this function converges (slightly) faster than ternary search
        const Datatype golden_ratio = (1 + std::sqrt((Datatype) 5)) / 2;
        Datatype m1 = r - (r-l) / golden_ratio;
        Datatype m2 = l + (r-l) / golden_ratio;
        auto fm1 = f(m1);
        auto fm2 = f(m2);
        while (iterations--) {
            if (fm1 > fm2) {
                if (iterations == 0)
                    return fm1;
                r = m2;
                m2 = m1;
                fm2 = fm1;
                m1 = r - (r-l) / golden_ratio;
                fm1 = f(m1);
            } else {
                if (iterations == 0)
                    return fm2;
                l = m1;
                m1 = m2;
                fm1 = fm2;
                m2 = l + (r-l) / golden_ratio;
                fm2 = f(m2);
            }
        }
        throw std::runtime_error("no warning");
    }

    template<typename Datatype, typename Function>
    auto minimum(Datatype l, Datatype r, int iterations, const Function& f) -> decltype(f(l)) {
        // f must be strictly decreasing, then strictly increasing (or just strictly monotonic)
        // rule of thumb: this function converges (slightly) faster than ternary search
        const Datatype golden_ratio = (1 + std::sqrt((Datatype) 5)) / 2;
        Datatype m1 = r - (r-l) / golden_ratio;
        Datatype m2 = l + (r-l) / golden_ratio;
        auto fm1 = f(m1);
        auto fm2 = f(m2);
        while (iterations--) {
            if (fm1 < fm2) {
                if (iterations == 0)
                    return fm1;
                r = m2;
                m2 = m1;
                fm2 = fm1;
                m1 = r - (r-l) / golden_ratio;
                fm1 = f(m1);
            } else {
                if (iterations == 0)
                    return fm2;
                l = m1;
                m1 = m2;
                fm1 = fm2;
                m2 = l + (r-l) / golden_ratio;
                fm2 = f(m2);
            }
        }
        throw std::runtime_error("no warning");
    }
}
////////////////////////////// END OF SEARCH //////////////////////////////
/////////////////////////////////////////////////// BEGIN OF SEGMENT TREE ///////////////////////////////////////////////////
// Commutativity is not required: operations are always executed from left to right
// TODO: implement range-update and push (http://codeforces.com/blog/entry/18051)
// TODO: consider implementing upper_bound/lower_bound (for use with min/max comparators)
template<typename Data>
class SegmentTree {
public:
    SegmentTree(int left, int right, std::function<Data(Data, Data)> combine, Data initial_value=Data());
    SegmentTree(int left, int right, std::function<Data(Data, Data)> combine, std::function<Data(int)> from_position);
    SegmentTree(const std::vector<Data>& vec, std::function<Data(Data, Data)> combine);
    ~SegmentTree();

    Data query(int i, int j);
    inline Data query(int i);
    void update(int i, std::function<Data(Data)> v);
    inline void update_set(int i, Data v);
    inline void update_combine(int i, Data v);
private:
    const int m_delta, m_size;
    const std::function<Data(Data, Data)> m_combine;
    Data *const m_data;
};

template<typename Data>
SegmentTree<Data>::SegmentTree(const int left, const int right, const std::function<Data(Data, Data)> combine, const Data initial_value)
    : m_delta(left)
    , m_size(right-left+1)
    , m_combine(combine)
    , m_data(new Data[2*m_size])
{
    fill(m_data+m_size, m_data+2*m_size, initial_value);
    for (int i = m_size-1; i > 0; --i)
        m_data[i] = m_combine(m_data[i<<1], m_data[i<<1|1]);
}

template<typename Data>
SegmentTree<Data>::SegmentTree(const int left, const int right, const std::function<Data(Data, Data)> combine, std::function<Data(int)> from_position)
    : m_delta(left)
    , m_size(right-left+1)
    , m_combine(combine)
    , m_data(new Data[2*m_size])
{
    for (int i = 0; i < m_size; ++i)
        m_data[i+m_size] = from_position(i+m_delta);
    for (int i = m_size-1; i > 0; --i)
        m_data[i] = m_combine(m_data[i<<1], m_data[i<<1|1]);
}

template<typename Data>
SegmentTree<Data>::SegmentTree(const std::vector<Data>& vec, const std::function<Data(Data, Data)> combine)
    : m_delta(0)
    , m_size(vec.size())
    , m_combine(combine)
    , m_data(new Data[2*m_size])
{
    for (int i = 0; i < m_size; ++i)
        m_data[i+m_size] = vec[i];
    for (int i = m_size-1; i > 0; --i)
        m_data[i] = m_combine(m_data[i<<1], m_data[i<<1|1]);
}

template<typename Data>
SegmentTree<Data>::~SegmentTree() {
    delete[] m_data;
}

template<typename Data>
Data SegmentTree<Data>::query(int l, int r) {
    l -= m_delta;
    r -= m_delta;
    l += m_size;
    r += m_size;
    if (l == r)
        return m_data[l];
    Data ansl = m_data[l];
    Data ansr = m_data[r];
    l += 1;
    while (l < r) {
        if (l&1)
            ansl = m_combine(ansl, m_data[l++]);
        if (r&1)
            ansr = m_combine(m_data[--r], ansr);
        l >>= 1;
        r >>= 1;
    }
    return m_combine(ansl, ansr);
}

template<typename Data>
inline Data SegmentTree<Data>::query(const int i) {
    return query(i, i);
}

template<typename Data>
void SegmentTree<Data>::update(int i, const std::function<Data(Data)> f) {
    i -= m_delta;
    i += m_size;
    m_data[i] = f(m_data[i]);
    while (i /= 2)
        m_data[i] = m_combine(m_data[i<<1], m_data[i<<1|1]);
}

template<typename Data>
void SegmentTree<Data>::update_set(int i, const Data v) {
    // TODO: hand-optimize other segtree codes as well
    i -= m_delta;
    i += m_size;
    m_data[i] = v;
    while (i /= 2)
        m_data[i] = m_combine(m_data[i<<1], m_data[i<<1|1]);
}

template<typename Data>
void SegmentTree<Data>::update_combine(int i, const Data v) {
    // TODO: hand-optimize other segtree codes as well
    i -= m_delta;
    i += m_size;
    m_data[i] = m_combine(m_data[i], v);
    while (i /= 2)
        m_data[i] = m_combine(m_data[i<<1], m_data[i<<1|1]);
}
/////////////////////////////////////////////////// END OF SEGMENT TREE ///////////////////////////////////////////////////

void run(const int testcase) {
    int n, k;
    cin>>n>>k;
    auto combine = [](int x, int y) {
        return max(x, y);
    };
    SegmentTree<int> segtree(1, n, combine, 0);
    int best_pos, best_v1, best_v2;
    for (int i = 0; i < k; ++i) {
        best_pos = -1;
        best_v1 = -1e9;
        best_v2 = -1e9;
        for (int j = 1; j <= n; ++j) {
            if (segtree.query(j, j) == 0) {
                int left = integer_search::last_true(1, j-1, 0, [&](int p) { return segtree.query(p, j) == 1; });
                int right = integer_search::first_true(j+1, n, n+1, [&](int p) { return segtree.query(j, p) == 1; });
                const int vleft = j-left-1;
                const int vright = right-j-1;
                const int v1 = min(vleft, vright);
                const int v2 = max(vleft, vright);
                //printf("j = %d => vleft = %d, vright =%d\n", j, vleft, vright);
                if (v1 > best_v1 || (v1 == best_v1 && v2 > best_v2)) {
                    best_pos = j;
                    best_v1 = v1;
                    best_v2 = v2;
                }
            }
        }
        //printf("i = %d => pos = %d, v1 = %d, v2 = %d\n", i, best_pos, best_v1, best_v2);
        segtree.update_set(best_pos, 1);
    }
    printf("Case #%d: %d %d\n", testcase, best_v2, best_v1);
    //if (testcase==3)exit(0);
}

int32_t main() {
    int testcases;
    cin>>testcases;
    for (int testcase = 1; testcase <= testcases; ++testcase) {
        run(testcase);
    }
}
