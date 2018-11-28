//
// Created by tyler on 4/7/2017.
//
/*
 * problem will be with large dataset: 1 < n < 10^18 (1 quintillion)
 * 8 quintillion: 8446744073709551615
 */

#include <iostream>
#include <sstream>

int to_int(char c) {
    return c - '0';
}

int find_untidy(std::string nstr) {
    int idx = -1;
    for (int i = 1; i < nstr.length(); ++i) {
        int prev = to_int(nstr[i - 1]);
        int curr = to_int(nstr[i]);
        if (curr < prev) {
            idx = i;
            break;
        }
    }
    return idx;
}

bool is_tidy(std::string nstr) {
    return find_untidy(nstr) < 0;
}

unsigned long long int transform(std::string nstr) {
    int idx = find_untidy(nstr);
    for (int i = idx; i < nstr.length(); ++i) {
        nstr[i] = '0';
    }
    return std::stoull(nstr) - 1;
}

void print_result(int t, unsigned long long int n) {
    std::cout << "Case #" << t << ": " << n << std::endl;
}

int main(int argc, char** args) {
    int t = 0;
    unsigned long long int n = 0;

    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        std::cin >> n;
        unsigned long long int m = n;
        std::string nstr = std::to_string(m);
        bool tidy = is_tidy(nstr);
        while (!tidy) {
            m = transform(nstr);
            nstr = std::to_string(m);
            tidy = is_tidy(nstr);
        }

        print_result(i, m);
    }

    return 0;
}

