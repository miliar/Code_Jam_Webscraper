#include <iostream>
#include <utility>
#include <cstdint>
#include <algorithm>
#include <map>
#include <iterator>

typedef std::pair<int64_t, int64_t> ii;

ii solve(int64_t N, int64_t k)
{
    ii ans;
    std::map<int64_t, int64_t> space;
    space[N] = 1; 
    while (k > 0)
    {
        int64_t v = space.rbegin()->first, n=space.rbegin()->second; 
        space.erase(v);
        int64_t left = (v-1)/2;
        int64_t right = v/2;
        if (k > n)
        {
            k -= n;
            space[left] += n;
            space[right] += n;
        }
        else
        {
            k = 0;
            ans = {right, left};
        }
    }

    return ans;
}

int main()
{
    int t;
    std::cin >> t;
    for (int i=1; i<=t; i++)
    {
        int64_t n, k;
        std::cin >> n >> k;
        ii ans = solve(n, k);
        std::cout << "Case #" << i << ": " << ans.first << " " << ans.second << "\n";
    }
}
