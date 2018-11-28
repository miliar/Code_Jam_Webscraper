#include <iostream>
#include <fstream>
using namespace std;

bool is_same_digit(long long number, long long cur) {
    long long next_digit = (number / (cur * 10)) % 10;
    long long cur_digit = (number / cur) % 10;
    return next_digit == cur_digit;
}

bool is_larger_digit(long long number, long long cur) {
    long long next_digit = (number / (cur * 10)) % 10;
    long long cur_digit = (number / cur) % 10;
    return next_digit > cur_digit;
}

long long solve(long long number) {
    long long cur_offset = 1;
    long long smallest_offset = cur_offset;

    while(cur_offset <= number){
        if (number / (cur_offset * 10) == 0) break;
        if (is_same_digit(number, cur_offset)) cur_offset *= 10;
        else if (is_larger_digit(number, cur_offset))
        {
            number -= (smallest_offset / 10) == 0 ? 1 : (smallest_offset / 10);
            cur_offset = smallest_offset = 1;
        }else {
            cur_offset *= 10; smallest_offset = cur_offset;
        }
    ///    cout << number << endl << cur_offset << endl << smallest_offset << endl << endl;
    }
    return number;
}

int main () {
    int T;
    int testcase = 1;

    ifstream input;
    input.open("input.txt");
    std::ofstream outfile;
    outfile.open("out.txt", std::ios_base::app); 


    input >> T;
    while(testcase <= T) {
        long long num;
        input >> num;
        long long result = solve(num);
        outfile << "Case #" << testcase << ": " << result << endl;
        cout << "Case #" << testcase << ": " << result << endl;
        testcase++;
    }
}
