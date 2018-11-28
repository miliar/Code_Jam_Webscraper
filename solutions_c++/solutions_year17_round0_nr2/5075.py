#include <iostream>
#include <climits>
#include <cmath>

#define MAX_NUM_DIGITS 19

using namespace std;

long answer();
void process(int numArr[], int power, int currentPower);
long calcArrValue(int numArr[]);

int main() {
    int numCases;
    cin >> numCases;
    for(int currentCase = 1; currentCase <= numCases; currentCase++) {
        cout << "Case #" << currentCase << ": " << answer() << endl;
    }
    return 0;
}

long answer() {
    long number;
    int power = 0;
    int numArr[MAX_NUM_DIGITS] = {0};

    cin >> number;

    // Acquire to what power this number is.
    while(true) {
        if(number / (long)(pow(10, power)) < 10) {
            break;
        }
        ++power;
    }
    if(power > 18) {
        cerr << "Power improperly handled" << endl;
        exit(1);
    }
    int tmpPower = 0; 
    long tmpNum = number;

    while(tmpPower <= power) {
        numArr[tmpPower] = tmpNum % 10;
        // cout << numArr[tmpPower] << endl;
        ++tmpPower;
        tmpNum /= 10;
    }

    for(int currentPower = power; currentPower > 0; currentPower--) {
        process(numArr, power, currentPower);
    }
    return calcArrValue(numArr);
}

void process(int numArr[], int power, int currentPower) {
    if(currentPower > power) {
        return;
    }
    if(numArr[currentPower] > numArr[currentPower - 1]) {
        --numArr[currentPower];
        for(int count = currentPower - 1; count >= 0; count--) {
            numArr[count] = 9;
        }
        while(currentPower + 1 <= power && 
            numArr[currentPower] < numArr[currentPower + 1]) {
            numArr[currentPower] = 9;
            --numArr[currentPower + 1];
            ++currentPower;
        }
    }
}

long calcArrValue(int numArr[]) {
    long totalValue = 0;
    for(int count = 0; count < MAX_NUM_DIGITS; count++) {
        totalValue += (long)(numArr[count]) * (long)pow(10, count);
    }
    return totalValue;
} 