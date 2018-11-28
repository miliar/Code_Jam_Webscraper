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

int
main(int argc, char** argv)
{
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(nullptr);  // disables automatic flush of std::cout before std::cin -- take care in interactive problems
    //std::ifstream   cin("TASKNAME.in");
    //std::ofstream  cout("TASKNAME.out");
    //std::cin.rdbuf(cin.rdbuf());
    //std::cout.rdbuf(cout.rdbuf());
    //std::cerr << "file i/o is used" << nl;
    
    st T;
    cin >> T;
    vector<tuple<string, st>> input(T);
    for (auto& x : input)
        cin >> get<0>(x) >> get<1>(x);
    
    auto solve = [](const tuple<string, st>& in) -> u64
    {
        const auto m = get<0>(in).length() - get<1>(in) + 1;
        vector<bool> bs(m);
        for (st i = 0; i <= m; ++i)
        {
            fill(bs.begin(), bs.end() - i, 0);
            fill(bs.end() - i, bs.end(), 1);
            do
            {
                auto s = get<0>(in);
                for (st j = 0; j < bs.size(); ++j)
                    if (bs[j])
                        for (auto it = s.begin() + j; it != s.begin() + j + get<1>(in); ++it)
                            *it = (*it == '+' ? '-' : '+');
                if (find(s.begin(), s.end(), '-') == s.end())
                    return i;
            }
            while (next_permutation(bs.begin(), bs.end()));
        }
        return -1;
    };

    vector<decltype(async(solve, ref(input[0])))> pool(T);
    for (st i = 0; i < T; ++i)
        pool[i] = async(solve, ref(input[i]));
    for (st i = 0; i < T; ++i)
    {
        auto g = pool[i].get();
        cout << "Case #" << i+1 << ": " << (g != -1 ? to_string(g) : "IMPOSSIBLE") << nl;
    }
}
