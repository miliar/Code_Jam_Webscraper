#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>

void flip(std::vector<bool>& state, int flipper_size, int pos)
{
    assert(pos < ((int)state.size() - flipper_size + 1));
    for (int i = pos; i < pos + flipper_size; ++i)
    {
        state[i] = !state[i];
    }
}

int first_blank(const std::vector<bool>& state)
{
    for (int i = 0; i < (int)state.size(); ++i)
    {
        if (!state[i])
        {
            return i;
        }
    }
    return state.size();
}

int minimum_flipps(std::vector<bool> state, int flipper_size)
{
    int num_flips = 0;
    int blank_pos = first_blank(state);
    while (blank_pos < (int)state.size() - flipper_size + 1)
    {
        flip(state, flipper_size, blank_pos);
        ++num_flips;
        blank_pos = first_blank(state);
    }
    if (blank_pos == (int)state.size())
    {
        return num_flips;
    }
    else
    {
       return -1; 
    }
}

int main()
{
    int test_cases = 0;
    std::cin >> test_cases;

    for (int i = 1; i <= test_cases; ++i)
    {
        std::string state_str;
        std::cin >> state_str;
        std::vector<bool> state;
        state.reserve(state_str.size());
        std::transform(state_str.begin(), state_str.end(), std::back_inserter(state), [](char pancake){ return pancake == '+'; });

        int flipper_size = 0;
        std::cin >> flipper_size;

        int num_flips = minimum_flipps(std::move(state), flipper_size);
        std::cout << "Case #" << i << ": " << (num_flips == -1 ? "IMPOSSIBLE" : std::to_string(num_flips)) << '\n';
    }
}
