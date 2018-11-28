#include <iostream>
#include <vector>

using namespace std;

unsigned long long int pow10(int expon) {
    unsigned long long int result = 1;
    for (int i = 0; i < expon; i++) {
        result *= 10;
    }
    return result;
}

unsigned long long int lastTidy(unsigned long long int inputNum) {
    bool tidyState = false;
    int currDig = 0;
    vector<int> digVec;
    unsigned long long int result = 0;
    while(inputNum != 0) {
        digVec.push_back(inputNum % 10);
        inputNum /= 10;
    }
    while(!tidyState) {
        if (currDig == digVec.size()-1) {
            tidyState = true;
        } else if (digVec[currDig] < digVec[currDig+1]) {
            for (int i = 0; i <= currDig; i++) {
                digVec[i] = 9;
            }
            digVec[currDig+1]--;
        } else {
            currDig++;
        }
    }
    for (int i = 0; i < digVec.size(); i++) {
        result += digVec[i] * pow10(i);
    }
    return result;
}

int main()
{
    int testCase;
    unsigned long long int inputNum;
    cin >> testCase;
    for (int i = 0; i < testCase; i++) {
        cin >> inputNum;
        cout << "Case #" << i+1 << ": " << lastTidy(inputNum) << endl;
    }
    return 1;
}