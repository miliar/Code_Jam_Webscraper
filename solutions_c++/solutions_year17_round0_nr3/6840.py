/* Don't overcomplicate. */
/* Don't construct unnecessary objects. */
/* Stack is for everything. */

#include <bits/stdc++.h>
using namespace std;

#define MAX(T) (std::numeric_limits<T>::max())
#define wi(x) (std::cerr << (#x) << " is " << (x) << std::endl)
using i8  = int_fast8_t;
using i16 = int_fast16_t;
using i32 = int_fast32_t;
using i64 = int_fast64_t;
using u8  = uint_fast8_t;
using u16 = uint_fast16_t;
using u32 = uint_fast32_t;
using u64 = uint_fast64_t;
using st  = size_t;
const std::string nl = "\n";

// TODO define shorthands for random number generation

template<class T>
ostream& operator<<(ostream& os, const tuple<T, T>& x)
{
    os << get<0>(x) << " " << get<1>(x);
    return os;
}

int
main(int argc, char** argv)
{
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);  // disables automatic flush of std::cout before std::cin -- take care in interactive problems
    
    st T;
    cin >> T;
    using input_t = tuple<u32, u32>;
    using output_t = tuple<u32, u32>;
    vector<input_t> input(T);
    for (auto& x : input)
        cin >> get<0>(x) >> get<1>(x);
    auto solve = [](const input_t& in) -> output_t
    {
        using segment_t = output_t;
        
        auto length = [](const segment_t& s) { return get<1>(s) + 1 - get<0>(s); };
        map<u64, vector<segment_t>> seg;

        auto initial_segment = segment_t{1, get<0>(in)};
        seg[length(initial_segment)].push_back(initial_segment);
        u64 counter = 0;
        for (auto it = seg.rbegin(); true; ++it)
        {
            for (const auto& y : it->second)  // iterate over segments of the same size in coordinate-increasing order
            {
                auto l = get<0>(y);
                auto r = get<1>(y);
                auto m = l + (r - l) / 2;
                auto sl = segment_t{l, m - 1};  // left segment
                auto sr = segment_t{m + 1, r};  // right segment
                if (counter == get<1>(in) - 1)
                {
                    return {r - m, m - l};
                }
               
                seg[length(sl)].push_back(sl);
                seg[length(sr)].push_back(sr);
                // if (length(y) % 2 == 1)
                // {
                //     if (length(sl) > 0)
                //         it2->push_back(sl);
                //     if (length(sr) > 0)
                //         it2->push_back(sr);
                // }
                // else
                // {
                //     if (length(sl) > 0)
                //         it2->push_back(sl);
                //     if (length(sr) > 0)
                //         it1->push_back(sr);
                // }
                ++counter;
            }
        }
    };
    
    vector<decltype(async(solve, ref(input[0])))> pool(T);
    for (st i = 0; i < T; ++i)
        pool[i] = async(solve, ref(input[i]));
    for (st i = 0; i < T; ++i)
        cout << "Case #" << i+1 << ": " << pool[i].get() << std::endl;
}
