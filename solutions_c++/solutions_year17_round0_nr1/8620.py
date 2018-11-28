#include <string>
#include <iostream>
#include <vector>

#define NB_MAX 99999

int nb = NB_MAX;

void flip_act(int range, std::string &str, int size, int pivot) {
    if (pivot + range > size)
        return;

    for (int j = 0; j < range; j++) {
        if (str[j + pivot] == '-')
            str[j + pivot] = '+';
        else
            str[j + pivot] = '-';
    }
}

bool is_valid(std::string &str) {
    int i = 0;
    while (str[i] == '+')
        i++;
    return i == str.size();
}

void flipper(int range, std::string &str, int size, int nb_act,
             std::vector<bool> &mark, int start = 0) {
    // We already have a better solution
    if (nb_act >= nb)
        return;
    // We found a solution
    if (is_valid(str))
    {
        nb = nb_act;
    }
    // Looking for a solution
    else
    {
        // Ooops
        if (start >= size)
            return;

        // Without flip
        flipper(range, str, size, nb_act, mark, start + 1);
        // With flip
        flip_act(range, str, size, start);
//        std::cout << str << std::endl;
        flipper(range, str, size, nb_act + 1, mark, start + 1);
        flip_act(range, str, size, start);
    }
}

int main() {

    int t; // testcases
    std::cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        nb = NB_MAX;
        std::string pancakes;
        std::cin >> pancakes;
        int size = pancakes.size();
        int range;
        std::cin >> range;
        auto flip_list = std::vector<bool>(size, false);

        flipper(range, pancakes, size, 0, flip_list);

        std::cout << "Case #" << tc << ": ";
        if (nb == NB_MAX)
            std::cout << "IMPOSSIBLE" << std::endl;
        else
            std::cout << nb << std::endl;
    }
    return 0;
}
