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

bool
is_tidy(u64 x)
{
    if (x < 10)
        return true;
    auto sx = to_string(x);
    char prev = sx.c_str()[0];
    for (auto& x : sx)
    {
        if (x < prev)
            return false;
        prev = x;
    }
    return true;
}

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
    u64 x;
    for (st i = 0; i < T; ++i)
    {
        cin >> x;
        while (!is_tidy(x))
            x -= 1;
        cout << "Case #" << i + 1 << ": " << x << nl;
    }
}
