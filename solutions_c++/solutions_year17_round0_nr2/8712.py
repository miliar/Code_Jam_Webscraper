#include <iostream>
#include <string>

int main() {
    int nb_items;
    std::cin >> nb_items;
    int nbcase = 0;

    while (nbcase++ < nb_items) {
        std::string str;
        std::cin >> str;

        bool done = false;
        do {
            int i = 0;
            done = true;
            // Skip 0
            while (str[i] == '0') {
                i++;
            }
            for (;i + 1 < str.size(); i++)
            {
                // Find a digit smaller than the next one
                if (str[i] > str[i + 1]) {
                    done = false;
                    str[i] -= 1;
                    // Put 9 after
                    for (int j = i + 1; j < str.size(); j++)
                        str[j] = '9';
                }
            }
        } while (!done);

        int first_idx = 0;
        while (str[first_idx] == '0' && str[first_idx + 1])
            first_idx++;

        std::cout << "Case #" << nbcase << ": "
                  << str.substr(first_idx)
                  << std::endl;
    }
    return 0;
}
