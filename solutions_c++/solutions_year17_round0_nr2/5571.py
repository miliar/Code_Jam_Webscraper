
#include <iostream>
#include <string>

using namespace std;

string setRightToNine(string number, long index) {
    string numberCopy(number);
    
    for (long i = index + 1; i < numberCopy.size(); i++) {
        numberCopy[i] = '9';
    }
    
    return numberCopy;
}

string subOneFromLeft(string number, long index) {
    string numberCopy(number);
    
    long i = index;
    while (numberCopy[i] == '0') {
        numberCopy[i] = '9';
        
        i--;
    }
    
    int current = numberCopy[i] - '0';
    current--;
    numberCopy[i] = current + '0';
    
    return numberCopy;
}

string diffString(string number) {
    string numberCopy(number);
    
    for (long i = number.size() - 2; i >= 0; i--) {
        char current = numberCopy[i];
        char righter = numberCopy[i+1];
        
        if (current > righter) {
            numberCopy = setRightToNine(numberCopy, i);
            numberCopy = subOneFromLeft(numberCopy, i);
        }
    }
    
    return numberCopy;
}

string removeLeadingZeroes(string number) {
    long i = 0;
    
    while(number[i] == '0') {
        i++;
    }
    
    return number.substr(i);
}

string solveString(string numberStr) {
    string result = diffString(numberStr);
    
    return removeLeadingZeroes(result);
}

int main(int argc, const char * argv[]) {
    
    int t;
    cin >> t;
    cin.ignore();
    
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        
        string numberStr;
        
        getline(cin, numberStr);
        
        cout << solveString(numberStr) << endl;
    }
    
    return 0;
}
