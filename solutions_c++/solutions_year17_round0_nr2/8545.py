#include <iostream>
#include <cmath>
using namespace std;
#define REPEATUP(i, a, b) for(unsigned int i = a; i < b; i++)
#define REPEATDOWN(i, a, b) for (int i = (a); i >= (b); i--)

int findLargestNonAscendingIntFrom(int input);
bool numberIsInNonAscendingOrder(int input);
int findAmountOfDigits(int input);
int *arrayFromInteger(int input);
int formIntegerFromArray(int *array, int amountOfItems);

int main() {
    int numberOfQuestions;
    cin >> numberOfQuestions;
    REPEATUP(i, 0, numberOfQuestions) {
        cout << "Case #" << i + 1 << ": ";
        int numberToProcess;
        cin >> numberToProcess;
        cout << findLargestNonAscendingIntFrom(numberToProcess) << endl;
    }
}

int findLargestNonAscendingIntFrom(int input) {
    // Check if current number is already in non-A orders
    if (numberIsInNonAscendingOrder(input)) { return input; }

    // Calculate
    int *arrayofDigits = arrayFromInteger(input);
    int amountOfDigits = findAmountOfDigits(input);
    int *testArray = new int(amountOfDigits);
    REPEATUP(i, 0, amountOfDigits) {
        testArray[i] = arrayofDigits[i];
    }

    int finalizedInt = 0;
    REPEATDOWN(i, amountOfDigits - 2, 0) {
        testArray[i] -= 1;
        REPEATUP(j, i + 1, amountOfDigits) {
            testArray[j] = 9;
        }
        int formedInt = formIntegerFromArray(testArray, amountOfDigits);
        if (numberIsInNonAscendingOrder(formedInt)) {
            finalizedInt = formedInt;
            i = 0;
        }
    }
    return finalizedInt;
}

bool numberIsInNonAscendingOrder(int input) {
    // 1. Get amount of digits
    int amountOfDigits = findAmountOfDigits(input);
    // 2. Determine
    int previousDigit = 0;
    REPEATDOWN(i, amountOfDigits - 1, 0) {
        int currentDigit = input / pow(10, i);
        if (currentDigit < previousDigit) { return false; }
        input -= currentDigit * int(pow(10, i));
        previousDigit = currentDigit;
    }
    return true;
}

int findAmountOfDigits(int input) {
    int amountOfDigits = 0;
    while (input != 0) {
        input /= 10;
        amountOfDigits++;
    }
    return amountOfDigits;
}

int *arrayFromInteger(int input) {
    int amountOfDigits = findAmountOfDigits(input);
    int *arrayofDigit = new int(amountOfDigits);
    REPEATDOWN(i, amountOfDigits - 1, 0) {
        arrayofDigit[amountOfDigits - i - 1] = input / pow(10, i);
        input -= arrayofDigit[amountOfDigits - i - 1] * int(pow(10, i));
    }
    return arrayofDigit;
}

int formIntegerFromArray(int *array, int amountOfItems) {
    int finalNumber = 0;
    REPEATUP(i, 0, amountOfItems) {
        finalNumber += array[i] * pow(10, amountOfItems - i - 1);
    }
    return finalNumber;
}