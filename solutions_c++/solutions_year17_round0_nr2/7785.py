#include <fstream>
#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>
#include <cassert>

int get_first_broken_idx(const std::vector<uint8_t>& input_number) {
    for (size_t i = 0; i < input_number.size() - 1; ++i) {
        if (input_number[i] > input_number[i + 1]) {
            return (int) i;
        }
    }
    return -1;
}

std::string number_vector_to_str(const std::vector<uint8_t>& input_number) {
    std::string num_str;
    auto it = input_number.begin();
    while (*it == 0) {
        ++it;
    }
    std::transform(it, input_number.end(), std::back_inserter(num_str), [](uint8_t c) {
        return (char) c + '0';
    });
    return num_str;
}

std::string solve_one_case(const std::vector<uint8_t>& input_number) {
    std::vector<uint8_t> last_tidy_number(input_number);
    while (true) {
        auto idx = get_first_broken_idx(last_tidy_number);
        if (idx < 0) {
            break;
        }
        assert(last_tidy_number[idx] != 0);
        last_tidy_number[idx] = static_cast<uint8_t>(last_tidy_number[idx] - 1);
        for (size_t i = (size_t) (idx + 1); i < last_tidy_number.size(); ++i) {
            last_tidy_number[i] = 9;
        }
    }
    return number_vector_to_str(last_tidy_number);
}


int main() {
    auto in = std::ifstream("B-large.in");
    auto out = std::ofstream("B-large.out");

    if (!in || !out) {
        std::cout << "Can't open files" << std::endl;
        return 1;
    }

    size_t test_num;

    in >> test_num;

    std::vector<uint8_t> input_number;
    input_number.reserve(20);
    for (int case_idx = 1; case_idx <= test_num; ++case_idx) {
        input_number.clear();

        std::string input_number_str;
        in >> input_number_str;
        std::transform(input_number_str.begin(), input_number_str.end(), std::back_inserter(input_number), [](char c) {
            return static_cast<uint8_t>(c - '0');
        });
        auto result = solve_one_case(input_number);
        out << "Case #" << case_idx << ": " << result << std::endl;
    }


    return 0;
}