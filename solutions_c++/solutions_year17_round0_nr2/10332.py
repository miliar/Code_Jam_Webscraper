#include<iostream>
#include<fstream>

using namespace std;


bool isTidy(unsigned long long num);


int main() {
    fstream inFile("data\\B-small-attempt0.in");
    ofstream outFile("data\\B-small-attempt0.out");

    if (inFile.is_open() && outFile.is_open()) {
        unsigned long long cases;
        inFile >> cases;

        for (unsigned long long c = 0; c < cases; c++) {
            unsigned long long num;
            inFile >> num;

            while (!isTidy(num)) {
                num -= (num % 10) + 1;
            }

            outFile << "Case #" << c + 1 << ": " << num << endl;
        }
    } else {
        cout << "Failed to open files." << endl;
    }

    return 0;
}


bool isTidy(unsigned long long num) {
    bool tidy = true;
    unsigned long long lowestDigit = 10;

    while (num && tidy) {
        unsigned long long currDigit = num % 10;

        if (currDigit > lowestDigit) {
            tidy = false;
        } else {
            lowestDigit = currDigit;
            num /= 10;
        }
    }

    return tidy;
}