#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <cstdlib>

using namespace std;

bool nonDecreasingOrder(string the_number) {
    size_t i;
    string previous, next;
    for(i = 1; i < the_number.size(); i++) {
        previous = the_number.substr(i - 1, 1);
        next = the_number.substr(i, 1);
        if(0 < previous.compare(next)) {
            return false;
        }
    }
    return true;
}

size_t indexOfFirstDrop(string the_number) {
    size_t i;
    for(i = 1; i < the_number.size(); i++) {
        if(the_number.at(i) < the_number.at(i - 1)) return i;
    }
    return the_number.size() - 1;
}

string nextNonDecreasingNumber(string the_number) {
    string result = "";
    size_t start_here;
    size_t i;
    start_here = indexOfFirstDrop(the_number);
    for(i = 0; i < start_here; i++) {
        result += the_number[i];
    }
    if(result.size() == the_number.size()) return result;
    for(i = start_here; i < the_number.size(); i++) {
        result += the_number[start_here - 1];
    }
    return result;
}

string oneMoreDigit(string tidy) {
    string bigger_tidy;
    size_t i;
    bigger_tidy = "";
    for(i = 0; i <= tidy.size(); i++) {
        bigger_tidy += "1";
    }
    return bigger_tidy;
}

void incrementals(size_t case_number, string tidy, string the_number, size_t a_number) {
    vector<size_t> tidy_numbers;
    string one_more_digit = "";
    size_t current;
    if('9' == tidy.at(0)) one_more_digit = oneMoreDigit(tidy);
    if(0 < one_more_digit.compare(the_number)) {
        cout << "Case #" << case_number << ": " << tidy << endl;
        return;
    }
    tidy_numbers.push_back((size_t)atoll(one_more_digit.c_str()));
    current = (size_t)atoll(one_more_digit.c_str());
    current++;

    string nonDecreasingNumber;
    ostringstream temp;
    string some_number;
    while(current <= a_number) {
        temp.str("");
        temp.clear();
        temp << current;
        some_number = temp.str();
        if(true == nonDecreasingOrder(some_number)) {
            tidy_numbers.push_back(current);
            current++;
        }
        else {
            some_number = nextNonDecreasingNumber(some_number);
            current = (size_t)atoll(some_number.c_str());
        }
    }
    cout << "Case #" << case_number << ": " << tidy_numbers[tidy_numbers.size() - 1] << endl;
}


void solve(size_t case_number, size_t a_number) {
    size_t mysize;
    string nonDecreasingNumber;
    ostringstream temp;
    string the_number;
    if(a_number < 10) {
        cout << "Case #" << case_number << ": " << a_number << endl;
        return;
    }
    temp << a_number;
    the_number = temp.str();
    mysize = the_number.size() - 1;
    for(size_t i = 0; i < mysize; i++) {
        nonDecreasingNumber += "9";
    }
    incrementals(case_number, nonDecreasingNumber, the_number, a_number);
}

int main(void) { 
    size_t total_inputs, a_number;
    cin >> total_inputs;
    for(size_t i = 0; i < total_inputs; i++) {
        cin >> a_number;
        solve(i + 1, a_number);
    }
    return 0;
}