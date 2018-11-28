#include <iostream>
#include <string>
#include <sstream>

bool isTidy(std::string num){
    int length = num.length();

    for (int index = 0; index < length -1; ++ index){
        if (num[index] > num[index+1]) return false;
    }

    return true;
}

// Checks if the number is 'Tidy" if not,return the
// previous Tidy
// It's tidy if the digits are in ascending order.
std::string getTidy(std::string num){
    int length = num.length();

    std::string tidy_num = "";

    for (int i = 0; i < length; ++i) {
        if (i == length - 1){
            tidy_num += num[i];
        }else if (num[i] <= num[i + 1]) {
            tidy_num += num[i];
        }else {
            char digit = num[i] - 1;
            tidy_num += digit;

            std::string rest = std::string (length-i-1,'9');

            tidy_num += rest ;
            break;
        }

    }

    if (isTidy(tidy_num)) return tidy_num;
    else return getTidy(tidy_num);

}


std::string remove_leading_zeros(std::string num){
    int length = num.length();

    for (int i = 0; i < length; ++i) {
        if (num[i] != '0') return num.substr(i);
    }

}
int main() {
    int number_of_cases = 0;
    std::cin >> number_of_cases;

    for (int case_number = 1; case_number <= number_of_cases; ++case_number){
        std::string this_case;
        std::cin>>this_case;

        std::cout << "Case #"<<case_number<<": "<<remove_leading_zeros(getTidy(this_case))<<std::endl;
    }

}