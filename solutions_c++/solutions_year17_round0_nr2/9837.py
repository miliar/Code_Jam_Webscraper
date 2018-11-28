#include <iostream>
#include <string>
#include <vector>
#include <inttypes.h>
using namespace std;


bool isSorted(long long number) {
    string stringNumber = to_string(number);
    bool sorted = true;
    for (int k = 1; k < (int)stringNumber.length() && sorted; ++k) {
        if (stringNumber[k-1] > stringNumber[k]) {
            return false;
        }
    }
    return true;
}

long long lastSortedNumber(long long number) {
    string stringNumber = to_string(number);
    for (int i = (int)(stringNumber.length()-1); i > 0; --i) {
        long long end = stoll(stringNumber.substr(i, stringNumber.length()-1))+1;
        if (isSorted(number-end)) {
            return number-end;
        }
    }
    return 0;
}


int main()
{
    int numOfCases;
    cin >> numOfCases;
    int i = 0;
    while (i < numOfCases) {
        long long lastNumber;
        std::cin >> lastNumber;
        
            if (isSorted(lastNumber)) {
                cout << "Case #" << i+1 << ": " << lastNumber << std::endl;                
            }
            else {
                cout << "Case #" << i+1 << ": " << lastSortedNumber(lastNumber) << std::endl;     
            }
        
        ++i;
    }
}
