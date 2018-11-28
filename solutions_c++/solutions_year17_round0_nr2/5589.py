#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;
vector<unsigned long> numbers;

unsigned long tidy(unsigned long& curr) {
    string sorted;
    do{
        ++curr;
        sorted = std::to_string(curr);
        sort(sorted.begin(), sorted.end());
    } while (std::to_string(curr) != sorted);
    return curr;
}

void GenerateNumbers(unsigned long number) {
    long ones_digit =number % 10;
    ones_digit = std::max(long(1),ones_digit);
    unsigned long base = number *10;
    for (;ones_digit < 10; ++ones_digit) {
        numbers.push_back(number * 10 + ones_digit);
    }
}

int main() {
    int iters;
    unsigned long curr = 0;
    // Collect input nums
    vector<unsigned long> inputs;
    ifstream fin;
    fin.open("input.txt");
    fin >> iters;
    ofstream fout;
    fout.open("output.txt");
    for (int i = 0; i < iters; ++i) {
        unsigned long val;
        fin >> val;
        inputs.push_back(val);
    }
    numbers.push_back(0);
    unsigned long max_val = 7000000;
    unsigned long loc = 0;
    while (numbers.size() < max_val + 1) {
        GenerateNumbers(numbers[loc]);
        loc++;
    }
    for (unsigned long i = 0; i < inputs.size(); ++i) {
        auto val = lower_bound(numbers.begin(), numbers.end(), inputs[i]);
        if (*val != inputs[i]) {
            --val;
        }
        fout << "Case #" << i+1 << ": ";
        fout << *val << endl;
        cout << inputs[i] << ": " << *val << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
