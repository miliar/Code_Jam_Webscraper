#include <iostream>
#include <string>

bool is_all_nine;

void make_all_nine(std::string& number, int pos) {
    int i;
    int size = number.size();
    if (!is_all_nine) {
        for (i = pos; i < size; ++i) {
            number[i] = '9';
        }
    }
}

void shift_left(std::string& number) {
    auto it = number.begin();
    while ((it+1) < number.end()) {
        *it = *(++it);
    }
    number.pop_back();
}

void decrement_number(std::string& number, int pos) {
    number[pos] -= 1;
    if (pos == 0 && number[pos] == '0') {
        shift_left(number);
    }
    else if (number[pos] < '0') {
        number[pos] = '9';
        make_all_nine(number, pos);
        is_all_nine = true;
        decrement_number(number, pos-1);
    }
}

void calculate_closest_tidy(std::string& number) {
    int num = 0;
    int i;
    for (i = 0; i < (int) number.size(); ++i) {
        if ((number[i] - '0') >= num) {
            num = (int)(number[i] - '0');
        }
        else {
            make_all_nine(number, i+1);
            decrement_number(number, i);
            i = -1;
            num = 0;
        }
    }
}

int main() {
    int testCases, currentCase;
    std::string number, inpLine;
    std::getline(std::cin, inpLine);
    testCases = stoi(inpLine);
    inpLine.clear();
    for (currentCase = 0; currentCase < testCases; ++currentCase) {
        std::getline(std::cin, number);
        calculate_closest_tidy(number);
        std::cout << "Case #" << currentCase+1 << ": ";
        std::cout << number;
        std::cout << std::endl;
        number.clear();
        is_all_nine = false;
    }
    return 0;
}