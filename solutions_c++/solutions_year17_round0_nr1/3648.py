#include <iostream>

int solve(std::string pancakes, int k)
{
    int ans = 0;
    for (size_t i = 0; i + k <= pancakes.size(); i++)
    {
        if (pancakes[i] == '-')
        {
            ans++;
            for (int j = 0; j < k; j++)
            {
                pancakes[i + j] = (pancakes[i + j] == '+') ? '-' : '+';
            }
        }
    }
    for (size_t j = pancakes.size() - k; j < pancakes.size(); j++)
    {
        if (pancakes[j] == '-') return -1;
    }
    return ans;
}

int main()
{
    int t;
    std::cin >> t;
    for (int i=1; i<=t; i++)
    {
        std::string pancakes;
        int k;
        std::cin >> pancakes >> k;
        int ans = solve(pancakes, k);
        std::cout << "Case #" << i << ": ";
        if (ans < 0)
            std::cout << "IMPOSSIBLE\n";
        else
            std::cout << ans << "\n";
    }
}
