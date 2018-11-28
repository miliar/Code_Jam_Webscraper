#include <iostream>
#include <vector>

void eachDigit(unsigned long x, std::vector<int> *digits);
int isMono(std::vector<int> digits);
void changeNum(int x, std::vector<int> *digits);
unsigned long toLong(std::vector<int> *digits);

int main() {
    int T = 0;

    std::cin >> T;

    std::vector<unsigned long> N((unsigned long)T);

    for (int i = 0; i < T; ++i) {
        std::cin >> N[i];
    }

    std::cout << std::endl;



    std::vector<int> digits;
    unsigned long x = 0;

    for (int i = 0; i < T; ++i) {
        eachDigit(N[i], &digits);

        for (int j = isMono(digits); j != -1; j = isMono(digits)) {
            changeNum(j, &digits);
        }

        x = toLong(&digits);

        std::cout << "Case #" << (i+1) << ": " << x << std::endl;
    }

    return 0;
}

void eachDigit(unsigned long x, std::vector<int> *digits)
{
    if(x >= 10)
        eachDigit(x / 10, digits);

    int digit = (int)(x % 10);

    digits->push_back(digit);
}

int isMono(std::vector<int> digits){

    for (int i = 0; i < (digits.size() - 1); ++i) {
        if (digits[i] > digits[i + 1]){
            return i;
        }
    }

    return -1;
}

void changeNum(int x, std::vector<int> *digits){
    digits->at((unsigned long)x)--;
    for (int i = x + 1; i < digits->size(); i++){
        digits->at((unsigned long)i) = 9;
    }

}

unsigned long toLong(std::vector<int> *digits){
    unsigned long converted = 0;
    for (int i = (int)digits->size()-1, step = 1; i >= 0; --i, step *= 10) {
        converted += digits->at((unsigned long)i) * step;
    }
    digits->clear();
    return converted;
}